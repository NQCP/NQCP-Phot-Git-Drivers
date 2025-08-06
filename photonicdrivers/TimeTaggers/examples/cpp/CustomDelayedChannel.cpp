/*
This file is part of Time Tagger software defined digital data acquisition.
*/

#include "CustomDelayedChannel.h"
#include <TimeTagger.h>

CustomDelayedChannel::CustomDelayedChannel(TimeTaggerBase *tagger, channel_t base_channel, timestamp_t delay)
    : IteratorBase(tagger), base_channel(base_channel), delay(delay) {

  if (delay < 0) {
    throw std::invalid_argument("delay must be at least 0 ps");
  }

  // We have to register at the TimeTagger hardware which channels are currently in use. Tags of channels which are not
  // used are not sent to the computer.
  registerChannel(base_channel);

  // This requests the TimeTagger Software to allocate a new virtual channel identifier for us.
  output_channel = getNewVirtualChannel();

  // This will tell the TimeTagger that the initialization is done. So from now on, the worker threads will start
  // evaluating this measurement.
  finishInitialization();
}

CustomDelayedChannel::~CustomDelayedChannel() { stop(); }

void CustomDelayedChannel::on_start() {
  // This will clear the state of this virtual channel after initialization or after restart after calling stop().
  overflow_state_on = false;
  delayed_tags.clear();
}

channel_t CustomDelayedChannel::getChannel() const {
  // Provide the allocated channel number.
  return output_channel;
}

bool CustomDelayedChannel::next_impl(std::vector<Tag> &incoming_tags, timestamp_t begin_time, timestamp_t end_time) {
  // DelayedChannels is implemented by making a 'mirror' or copy of the time tag stream.
  // In this mirror we will insert every time tag plus the time tags from a 'delay queue'.
  // Whenever we read a tag, we flush all former pending tags in the 'delay queue' before copying the input tag.
  // This ensures the order of the yielded time tags and maintain all other channels.
  // If the input tag corresponds to the 'delayed channel', we make a delayed copy of its timestamp and add it to the
  // delay queue.

  // Helper to flush all pending events before the higher_bound
  const auto flush_tags = ([this](timestamp_t higher_bound) {
    while (!delayed_tags.empty() && delayed_tags.front().time - higher_bound < 0) {
      if (overflow_state_on) {
        // We are in overflow mode. We cannot flush the events, so let's emit missed_events instead.
        Tag missed_tag = delayed_tags.front();
        missed_tag.type = Tag::Type::MissedEvents;
        missed_tag.missed_events = 1;
        mirror.push_back(missed_tag);
      } else {
        mirror.push_back(delayed_tags.front());
      }
      delayed_tags.pop_front();
    }
  });

  for (const Tag &tag : incoming_tags) {
    // flush all delayed elements which are older than the current tag
    flush_tags(tag.time);
    mirror.push_back(tag);

    if (tag.type == Tag::Type::TimeTag) {
      // if the tag belongs to the base channel, create a copy for our virtual channel and delay it.
      if (tag.channel == base_channel) {
        Tag t = tag;
        t.channel = output_channel;
        t.time += delay;
        delayed_tags.push_back(t);
        break;
      }
    } else {
      // If the tag is not a normal time tag, we must handle the special case.
      // We use an if/else first as this cases are extremely unlikely and we want to reduce comparisons.
      switch (tag.type) {
      case Tag::Type::Error:
        delayed_tags.clear();
        break;

      case Tag::Type::OverflowBegin:
        overflow_state_on = true;
        break;

      case Tag::Type::OverflowEnd:
        overflow_state_on = false;
        break;

      default:
        break;
      }
    }
  }

  // flush all delayed elements which are older than the current block
  flush_tags(end_time);

  // exchange our internal mirror with the incoming tags in order to modify the stream.
  incoming_tags.swap(mirror);

  // clear the incoming buffer to save memory.
  mirror.clear();

  // we have modified the stream, return true to notify the time tagger that we have.
  return true;
}
