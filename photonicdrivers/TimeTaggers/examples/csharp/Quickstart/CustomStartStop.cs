using System.Collections.Generic;
using System.Linq;

namespace SwabianInstruments.TimeTagger.Examples
{
    /// Example for a single-start, single-stop measurement.
    /// The class shows how to access the raw time-tag stream by
    /// inheriting from CustomMeasurements.
    /// The process() method will be called when new data is ready
    /// to be processed from the time-tag stream.
    /// This start-stop histogram measurement implementation calculates
    /// the time difference from the incoming start to the next stop event.
    /// It is implemented such that the number of bins increases (x values)
    /// automatically when a new time difference bin is required to store the counts.
    internal class CustomStartStop : CustomMeasurement
    {
        private readonly int _clickChannel;
        private readonly int _startChannel;
        private readonly long _binWidth;
        private long _last;
        private readonly Dictionary<long, uint> _data = new();

        public CustomStartStop(TimeTaggerBase tagger, int clickChannel, int startChannel, long binWidth) : base(tagger)
        {
            _startChannel = tagger.isUnusedChannel(startChannel) ? clickChannel : startChannel;
            _clickChannel = clickChannel;
            _binWidth = binWidth;

            // The method register_channel(channel) activates
            // that data from the respective channels is transferred
            // from the Time Tagger to the PC.
            register_channel(_startChannel);
            register_channel(_clickChannel);

            clear_impl();

            // At the end of a CustomMeasurement constructor,
            // we must indicate that we have finished.
            finalize_init();
        }

        protected override void Dispose(bool disposing)
        {
            // The measurement must be stopped before deconstruction to avoid
            // concurrent process() calls.
            lock (this)
            {
                stop();
                base.Dispose(disposing);
            }
        }

        // on_start() is called when a measurement starts (initialization, start(), startFor()).
        protected override void on_start()
        {
            // The lock is already acquired within the backend.
            _last = 0;
        }

        // on_stop() is called when a measurement stops (stop(), end of integration time for startFor()).
        protected override void on_stop()
        {
            // The lock is already acquired within the backend.
        }

        // The clear_impl is called when .clear() or startFor(..., true) is called.
        protected override void clear_impl()
        {
            // The lock is already acquired within the backend.
            _last = 0;
            _data.Clear();
        }

        /// <summary>Main processing method for the incoming raw time-tags.</summary>
        ///
        /// The lock is already acquired within the backend.
        ///
        /// Please make sure that the processing is fast. The incoming_tags
        /// will be only passed to the next measurement waiting for data
        /// when the process() method of this measurement finishes
        /// and the lock is released.
        ///
        /// <param name="incomingTags">The incoming raw time tag stream provided as a read-only reference.
        /// 	The storage will be deallocated after this call, so you must not store a reference to
        /// 	this object. Make a copy instead.
        /// 	Please note that the time tag stream of all channels is passed to the process method,
        /// 	not only the ones from register_channel(...).</param>
        /// <param name="beginTime">Begin timestamp of the current time-tag data block.</param>
        /// <param name="endTime">End timestamp of the current time-tag data block.</param>
        protected override void process(TagBlock incomingTags, long beginTime, long endTime)
        {
	        foreach (var tag in incomingTags)
	        {
		        // tag is not a TimeTag, so we are in an error state, e.g. overflow
		        if (tag.type != TagType.TimeTag)
		        {
			        _last = 0;
		        }
		        else if (tag.channel == _clickChannel && _last != 0)
		        {
			        // valid event and we have received an start event already
			        long slot = (tag.time - _last) / _binWidth;
			        _data.TryGetValue(slot, out uint value);
			        _data[slot] = value + 1;
			        _last = 0;
		        }
		        if (tag.channel == _startChannel)
		        {
			        _last = tag.time;
		        }
	        }
        }

        // Returns a 2d array including the x and y data of the histogram acquired.
        public long[,] GetData()
        {
            // Acquire a lock this instance to guarantee that process() is not running in parallel
            // This ensures to return consistent data.
            _lock();
            try
            {
                long[,] result = new long[_data.Count, 2];
                int i = 0;
                foreach (var kv in _data.OrderBy(x => x.Key))
                {
                    result[i, 0] = kv.Key * _binWidth;
                    result[i, 1] = kv.Value;
                    i++;
                }
                return result;
            }
            finally
            {
                // We have gathered the data, unlock, so measuring can continue.
                _unlock();
            }
        }
    }
}