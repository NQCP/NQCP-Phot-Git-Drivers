/*
This file is part of Time Tagger software defined digital data acquisition.
*/

#include "CustomStartStop.h"
#include "TimeTagger.h"

CustomStartStop::CustomStartStop(TimeTaggerBase *tagger, channel_t click_channel, channel_t start_channel,
                                 timestamp_t binwidth)
    : IteratorBase(tagger), click_channel(click_channel), start_channel(start_channel), binwidth(binwidth) {

  if (binwidth < 1) {
    throw std::invalid_argument("binwidth must be at least 1 ps");
  }

  // We have to tell the TimeTagger hardware which channels are currently in use - so register them (tags of channels
  // which are not used are not sent to the computer).
  registerChannel(click_channel);
  registerChannel(start_channel);

  clear_impl();

  // This will tell the TimeTagger that the initialization is done. So from now on, the worker threads will start
  // evaluating this measurement.
  finishInitialization();
}

CustomStartStop::~CustomStartStop() {
  // This measurement must be stopped before deconstruction. This will wait until no thread is within next_impl.
  stop();
}

// Get data copies the local data to a newly allocated memory.
void CustomStartStop::getData(std::function<timestamp_t *(size_t, size_t)> array_out) {
  // This lock object will ensure that no other thread is within next_impl.
  auto lk = getLock();

  // return an interleaved output of {timestamp : clicks, ...}
  // std::map is sorted, so just iterate over all elements
  size_t size = data.size();
  timestamp_t *arr = array_out(size, 2);
  for (auto &item : data) {
    *arr++ = item.first * binwidth; // timestamp in ps
    *arr++ = item.second;           // clicks
  }
}

void CustomStartStop::clear_impl() {
  // reset all of the internal state of this measurement
  last_start_tag = 0;
  data.clear();
}

void CustomStartStop::on_start() {
  // Reset the last start tag on restarting.
  // Else we report a wrong interval to before stopping.
  last_start_tag = 0;
}

void CustomStartStop::on_stop() {
  // optional callback
}

// Here we handle the incoming time-tags.
bool CustomStartStop::next_impl(std::vector<Tag> &incoming_tags, timestamp_t begin_time, timestamp_t end_time) {
  // iterate over all the tags received
  for (const Tag &tag : incoming_tags) {
    switch (tag.type) {
    case Tag::Type::Error:         // happens on clock switches and USB errors
    case Tag::Type::OverflowBegin: // indicates the begin of overflows
    case Tag::Type::OverflowEnd:   // indicates the end of overflows
    case Tag::Type::MissedEvents:  // reports the amount of tags in overflow
      // Here you must implement what should happen when the hardware data buffer is overflowing because of the limited
      // transfer bandwidth. Sometimes you have to restart the measurement, sometimes you're fine with the amount of
      // missed events, sometimes you don't care about overflows. In this start-stop measurement, we set the last start
      // tag to invalid when we are in an error state.
      last_start_tag = 0;
      break;

    case Tag::Type::TimeTag:
      if (tag.channel == click_channel && last_start_tag != 0) {
        // On click tag: Increase the clicks in this bin by one.
        timestamp_t slot = (tag.time - last_start_tag) / binwidth;
        data[slot]++;

        // This shall be a single-stop measurement. If you like single-start multiple-stop, drop the next line.
        last_start_tag = 0;
      }
      if (tag.channel == start_channel) {
        // Update the last start tag timestamp. If start == stop channel, this will leave this measurement in an aimed
        // status.
        last_start_tag = tag.time;
      }
      break;
    }
  }

  // return true if incoming_tags was modified. If so, please keep care about the requirements:
  // -- all tags must be sorted
  // -- begin_time <= tags < end_time
  return false;
}
