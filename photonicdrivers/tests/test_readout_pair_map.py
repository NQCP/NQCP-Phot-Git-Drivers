"""Readout_Pair_Map (2026-10-17): the counting against an independent brute-force count on random tag
streams cut into random chunks, a hand-checked case, the input checks, and the real CustomMeasurement
on a VIRTUAL tagger (no hardware). Offline; nothing is written anywhere.

    python -m pytest photonicdrivers/tests/test_readout_pair_map.py -q
"""
import itertools

import numpy as np
import pytest

from photonicdrivers.TimeTaggers.Readout_Pair_Map import Readout_Pair_Counter

TRIG, CLICK, OTHER = 8, 5, 3
PERIOD = 100_000
DTYPE = np.dtype({"names": ["type", "missed_events", "channel", "time"],
                  "formats": ["u1", "<u2", "<i4", "<i8"], "offsets": [0, 2, 4, 8], "itemsize": 16})

# Two blocks, 3 readouts x 2 bins each (n_u = 6), with gaps between readouts and between blocks.
LO, HI, BLOCK, U = [], [], [], []
for b, start in enumerate((10_000, 50_000)):
    for k in range(3):
        for j, (a, z) in enumerate(((0, 1_000), (1_000, 4_000))):
            LO.append(start + 5_000 * k + a)
            HI.append(start + 5_000 * k + z)
            BLOCK.append(b)
            U.append(2 * k + j)


def counter():
    return Readout_Pair_Counter(TRIG, CLICK, LO, HI, BLOCK, U, 2, 6, PERIOD, 0.01)


def stream(events):
    """events: (time, channel, type) -> the tag array, time-ordered."""
    events = sorted(events)
    tags = np.zeros(len(events), dtype=DTYPE)
    for i, (time, channel, kind) in enumerate(events):
        tags[i] = (kind, 0, channel, time)
    return tags


def brute(tags):
    """An independent count: periods between consecutive triggers; valid when no reset tag lies in it
    and its length is within 1 %; next-period pairs between consecutive valid periods."""
    triggers = [int(t["time"]) for t in tags if t["type"] == 0 and t["channel"] == TRIG]
    resets = [int(t["time"]) for t in tags if t["type"] != 0]
    clicks = [int(t["time"]) for t in tags if t["type"] == 0 and t["channel"] == CLICK]
    same = np.zeros((2, 6, 6), np.int64)
    nxt = np.zeros((2, 6, 6), np.int64)
    single = np.zeros((2, 6), np.int64)
    periods = rejected = 0
    previous = None
    for t0, t1 in zip(triggers, triggers[1:]):
        if any(t0 <= r <= t1 for r in resets):
            previous = None
            continue
        if abs((t1 - t0) - PERIOD) > 0.01 * PERIOD:
            rejected += 1
            previous = None
            continue
        periods += 1
        found = []
        for c in clicks:
            if t0 <= c < t1:
                for lo, hi, b, u in zip(LO, HI, BLOCK, U):
                    if lo <= c - t0 < hi:
                        found.append((b, u))
        for b, u in found:
            single[b, u] += 1
        for (b1, u1), (b2, u2) in itertools.combinations(found, 2):
            if b1 == b2:
                same[b1, min(u1, u2), max(u1, u2)] += 1
        if previous is not None:
            for (b1, u1), (b2, u2) in itertools.product(previous, found):
                if b1 == b2:
                    nxt[b1, u1, u2] += 1
        previous = found
    return same, nxt, single, periods, rejected


def unpack(data):
    arrays, periods, rejected, resets = data
    out = {name: np.frombuffer(raw, dtype=np.dtype(dt)).reshape(shape) for name, raw, shape, dt in arrays}
    return out, periods, rejected, resets


def random_stream(rng, n_periods=400):
    events, t = [], 1_000
    for n in range(n_periods):
        length = PERIOD if n != 137 else 2 * PERIOD                   # one missing trigger
        events.append((t, TRIG, 0))
        for c in rng.integers(0, length, rng.poisson(6)):              # clicks anywhere, laser bins too
            events.append((t + int(c), CLICK, 0))
        for c in rng.integers(0, length, rng.poisson(3)):              # another channel: ignored
            events.append((t + int(c), OTHER, 0))
        if n == 250:
            events.append((t + 30_000, 0, 2))                          # an overflow inside a period
        t += length + int(rng.integers(-200, 200))                     # trigger jitter < 1 %
    return stream(events)


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_matches_a_brute_force_count_in_random_chunks(seed):
    rng = np.random.default_rng(seed)
    tags = random_stream(rng)
    c = counter()
    cuts = np.sort(rng.choice(np.arange(1, tags.size), 40, replace=False))
    for chunk in np.split(tags, cuts):                                 # periods span chunk borders
        c.feed(chunk)
    got, periods, rejected, resets = unpack(c.get_data())
    same, nxt, single, b_periods, b_rejected = brute(tags)
    assert periods == b_periods and rejected == b_rejected == 1 and resets == 1
    assert np.array_equal(got["single"], single)
    assert np.array_equal(got["same"], same)
    assert np.array_equal(got["next"], nxt)
    assert got["same"].sum() > 100 and got["next"].sum() > 100         # the test exercises pairs
    assert not np.tril(got["same"][0], -1).any()                        # stored u <= u'


def test_a_hand_checked_case():
    t0 = 1_000
    events = [(t0, TRIG, 0), (t0 + PERIOD, TRIG, 0), (t0 + 2 * PERIOD, TRIG, 0)]
    # period 1: block 0 readout 0 bin 0 twice (the diagonal), readout 2 bin 1; block 1 readout 1 bin 0;
    # a click in the gap between readouts (ignored)
    for dt in (10_100, 10_200, 10_000 + 10_000 + 2_000, 50_000 + 5_000 + 500, 14_500):
        events.append((t0 + dt, CLICK, 0))
    # period 2: block 0 readout 1 bin 1; block 1 readout 1 bin 0
    for dt in (10_000 + 5_000 + 3_000, 50_000 + 5_000 + 100):
        events.append((t0 + PERIOD + dt, CLICK, 0))
    c = counter()
    c.feed(stream(events))
    got, periods, rejected, resets = unpack(c.get_data())
    assert (periods, rejected, resets) == (2, 0, 0)
    same = np.zeros((2, 6, 6), np.uint32)
    same[0, 0, 0] = 1           # the two clicks in block 0, readout 0, bin 0
    same[0, 0, 5] = 2           # each of them with readout 2 bin 1
    assert np.array_equal(got["same"], same)                           # nothing across blocks
    nxt = np.zeros((2, 6, 6), np.uint32)
    nxt[0, 0, 3] = 2            # period 1 (readout 0 bin 0, twice) -> period 2 readout 1 bin 1
    nxt[0, 5, 3] = 1
    nxt[1, 2, 2] = 1            # block 1: readout 1 bin 0 -> readout 1 bin 0
    assert np.array_equal(got["next"], nxt)
    assert got["single"][0].tolist() == [2, 0, 0, 1, 0, 1] and got["single"][1].tolist() == [0, 0, 2, 0, 0, 0]


@pytest.mark.parametrize("change, message", [
    (dict(window_hi_ps=[w - 1 for w in LO]), "hi > lo"),
    (dict(window_lo_ps=LO[::-1], window_hi_ps=HI[::-1]), "sorted"),
    (dict(window_u=[u + 6 for u in U]), "out of range"),
    (dict(expected_period_ps=40_000), "inside the trigger period"),
    (dict(click_channel=TRIG), "must differ"),
])
def test_refuses_a_bad_table(change, message):
    kwargs = dict(trigger_channel=TRIG, click_channel=CLICK, window_lo_ps=LO, window_hi_ps=HI,
                  window_block=BLOCK, window_u=U, n_blocks=2, n_u=6, expected_period_ps=PERIOD)
    kwargs.update(change)
    with pytest.raises(ValueError, match=message):
        Readout_Pair_Counter(**kwargs)


def test_the_custom_measurement_on_a_virtual_tagger():
    """The real CustomMeasurement (through the driver method) on a virtual tagger: its process()
    fed directly with a tag array; getData() returns plain values only (they cross rpyc by value)."""
    from Swabian import TimeTagger
    from photonicdrivers.TimeTaggers.Swabian_TimeTagger_Driver import Swabian_TimeTagger_Driver
    tagger = TimeTagger.createTimeTaggerVirtual()
    try:
        driver = Swabian_TimeTagger_Driver()
        driver.connection = tagger
        m = driver.initialise_readout_pair_map(TRIG, CLICK, LO, HI, BLOCK, U, 2, 6, PERIOD, 0.01)
        assert np.dtype(TimeTagger.CustomMeasurement.INCOMING_TAGS_DTYPE) == DTYPE
        tags = random_stream(np.random.default_rng(5), 100)
        m.process(tags, 0, 0)
        data = m.getData()
        assert all(isinstance(x, (str, bytes, tuple, int)) for row in data[0] for x in row)
        got, periods, _, _ = unpack(data)
        same, nxt, single, b_periods, _ = brute(tags)
        assert periods == b_periods and np.array_equal(got["same"], same) and np.array_equal(got["next"], nxt)
        m.clear()
        assert unpack(m.getData())[1] == 0
        m.stop()
        del m
    finally:
        TimeTagger.freeTimeTagger(tagger)
