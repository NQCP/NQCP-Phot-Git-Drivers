"""The readout-pair map: every pair of clicks between readout time bins of the SAME block, in the
same trigger period and one period later (the uncorrelated reference) - a TimeTagger
CustomMeasurement that runs where the tagger is (the LabServer), fed by the raw tag stream.

The user's specification (2026-10-17; agent_mailbox/20261017_measurement_design_readout_pair_map.md):
- a click belongs to a WINDOW (block b, flat readout-bin index u) of a table given relative to the
  trigger; clicks outside every window are ignored; no laser gate - the bins hold everything;
- per accepted period and block: same[b, u, u'] += every pair of its clicks, u <= u' (all clicks, not
  only the first; two clicks in one window go to the diagonal); next[b, u, u'] += every pair (u in
  this period, u' in the next period); single[b, u] += clicks; no pairs across blocks;
- a period is rejected (and the reference chain broken) when the trigger-to-trigger time is off the
  expected period by more than period_tolerance, or after an error / overflow / missed-events tag.

Built-in Histogram2D / HistogramND take only the FIRST stop click per axis (TimeTagger 2.21.2
docstrings) - hence this custom measurement.
"""
import numpy as np
from Swabian import TimeTagger

_TIME_TAG = 0     # TimeTagger.TagType.TimeTag; every other type (error, overflow, missed events) resets


class Readout_Pair_Counter:
    """The counting, independent of the Time Tagger (tested with hand-made tags).

    window_lo_ps, window_hi_ps: the windows [lo, hi) in ps after the trigger, sorted, non-overlapping.
    window_block, window_u: each window's block index (0..n_blocks-1) and readout-bin index (0..n_u-1).
    """

    def __init__(self, trigger_channel: int, click_channel: int, window_lo_ps, window_hi_ps,
                 window_block, window_u, n_blocks: int, n_u: int, expected_period_ps: float,
                 period_tolerance: float = 0.01):
        self.trigger_channel = int(trigger_channel)
        self.click_channel = int(click_channel)
        self.lo = np.asarray(window_lo_ps, dtype=np.int64)
        self.hi = np.asarray(window_hi_ps, dtype=np.int64)
        self.block = np.asarray(window_block, dtype=np.int64)
        self.u = np.asarray(window_u, dtype=np.int64)
        self.n_blocks = int(n_blocks)
        self.n_u = int(n_u)
        self.expected_period_ps = float(expected_period_ps)
        self.period_tolerance = float(period_tolerance)
        if self.trigger_channel == self.click_channel:
            raise ValueError("the trigger and the click channel must differ")
        if not (self.lo.shape == self.hi.shape == self.block.shape == self.u.shape) or self.lo.ndim != 1:
            raise ValueError("window_lo_ps, window_hi_ps, window_block, window_u: equal-length 1D arrays")
        if self.lo.size == 0:
            raise ValueError("no windows")
        if np.any(self.hi <= self.lo):
            raise ValueError("every window needs hi > lo")
        if np.any(self.lo[1:] < self.hi[:-1]):
            raise ValueError("the windows must be sorted and must not overlap")
        if self.lo[0] < 0 or self.hi[-1] > self.expected_period_ps:
            raise ValueError("the windows must lie inside the trigger period")
        if np.any((self.block < 0) | (self.block >= self.n_blocks) | (self.u < 0) | (self.u >= self.n_u)):
            raise ValueError("window_block / window_u out of range")
        if not 0 < self.period_tolerance < 0.5:
            raise ValueError("period_tolerance: a fraction, e.g. 0.01")
        self.clear()

    def clear(self):
        self.same = np.zeros((self.n_blocks, self.n_u, self.n_u), dtype=np.uint32)
        self.next = np.zeros((self.n_blocks, self.n_u, self.n_u), dtype=np.uint32)
        self.single = np.zeros((self.n_blocks, self.n_u), dtype=np.uint32)
        self.periods = 0
        self.periods_rejected = 0
        self.resets = 0
        self._last_trigger = None
        self._current = []          # window indices of the clicks in the open period
        self._previous = None       # {block: readout-bin indices} of the last accepted period

    def feed(self, tags):
        """Process a chunk of tags (fields type, channel, time - TimeTagger's INCOMING_TAGS_DTYPE);
        state carries over between chunks, so a period may span several calls."""
        keep = ((tags["type"] != _TIME_TAG) | (tags["channel"] == self.trigger_channel)
                | (tags["channel"] == self.click_channel))
        for kind, channel, time in zip(tags["type"][keep].tolist(), tags["channel"][keep].tolist(),
                                       tags["time"][keep].tolist()):
            if kind != _TIME_TAG:
                self._reset()
            elif channel == self.trigger_channel:
                if self._last_trigger is not None:
                    self._close_period(time - self._last_trigger)
                self._last_trigger = time
                self._current = []
            elif self._last_trigger is not None:                       # a click after a trigger
                dt = time - self._last_trigger
                i = int(np.searchsorted(self.lo, dt, side="right")) - 1
                if i >= 0 and dt < self.hi[i]:
                    self._current.append(i)

    def _reset(self):
        """Tags were lost: drop the open period, break the reference chain."""
        if self._last_trigger is not None or self._previous is not None:
            self.resets += 1
        self._last_trigger = None
        self._current = []
        self._previous = None

    def _close_period(self, length_ps):
        if abs(length_ps - self.expected_period_ps) > self.period_tolerance * self.expected_period_ps:
            self.periods_rejected += 1
            self._previous = None
            return
        self.periods += 1
        windows = np.asarray(self._current, dtype=np.int64)
        blocks, us = self.block[windows], self.u[windows]
        np.add.at(self.single, (blocks, us), 1)
        current = {}
        for b in np.unique(blocks).tolist():
            ub = us[blocks == b]
            current[b] = ub
            if ub.size > 1:
                i, j = np.triu_indices(ub.size, 1)
                np.add.at(self.same[b], (np.minimum(ub[i], ub[j]), np.maximum(ub[i], ub[j])), 1)
            if self._previous is not None and b in self._previous:
                prev = self._previous[b]
                np.add.at(self.next[b], (np.repeat(prev, ub.size), np.tile(ub, prev.size)), 1)
        self._previous = current

    def get_data(self):
        """Plain values only (they cross rpyc by value): (name, bytes, shape, dtype) per array, then
        the counters."""
        arrays = tuple((name, a.tobytes(), tuple(a.shape), a.dtype.str)
                       for name, a in (("same", self.same), ("next", self.next), ("single", self.single)))
        return arrays, int(self.periods), int(self.periods_rejected), int(self.resets)


class Readout_Pair_Map(TimeTagger.CustomMeasurement):
    """The counter fed by the tagger's raw stream. Create one per capture (like the histogram);
    start() / startFor() / stop() / isRunning() / getCaptureDuration() from the base class."""

    def __init__(self, tagger, trigger_channel: int, click_channel: int, window_lo_ps, window_hi_ps,
                 window_block, window_u, n_blocks: int, n_u: int, expected_period_ps: float,
                 period_tolerance: float = 0.01):
        TimeTagger.CustomMeasurement.__init__(self, tagger)
        self.counter = Readout_Pair_Counter(trigger_channel, click_channel, window_lo_ps, window_hi_ps,
                                            window_block, window_u, n_blocks, n_u, expected_period_ps,
                                            period_tolerance)
        self.register_channel(channel=int(trigger_channel))
        self.register_channel(channel=int(click_channel))
        self.finalize_init()

    def __del__(self):
        self.stop()          # no process() call may run during destruction (Swabian's example)

    def clear_impl(self):
        if hasattr(self, "counter"):      # the base class may clear before __init__ has made it
            self.counter.clear()

    def on_start(self):
        pass

    def on_stop(self):
        pass

    def process(self, incoming_tags, begin_time, end_time):
        self.counter.feed(incoming_tags)

    def getData(self):
        with self.mutex:
            return self.counter.get_data()
