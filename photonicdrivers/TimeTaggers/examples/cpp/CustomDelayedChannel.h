/*
This file is part of Time Tagger software defined digital data acquisition.
*/
#pragma once

#include <TimeTagger.h>

#include <deque>
#include <vector>

/**
 *   Example to explain how to create a custom virtual channel class
 */
class CustomDelayedChannel : public IteratorBase {
public:
  /**
   * CustomVirtualChannel constructor
   *
   * \param tagger        reference to a TimeTagger
   * \param base_channel  channel to be delayed
   * \param delay         amount of the delay
   */
  CustomDelayedChannel(TimeTaggerBase *tagger, channel_t base_channel, timestamp_t delay);

  ~CustomDelayedChannel();

  /**
   * Returns the channel of the internally created virtual channel.
   */
  channel_t getChannel() const;

protected:
  /**
   * next receives and handles the incoming tags. All tags are sorted by time and comply with begin_time <= tag.time <
   * end_time and end_time shall be the begin_time of the next invocation. incoming_tags can be modified to filter or
   * inject tags.
   * \param incoming_tags vector of incoming tags to process, might be empty
   * \param begin_time    begin timestamp of this block of tags
   * \param end_time      end timestamp of this block of tags
   * \return true if the content of this block was modified, false otherwise
   * \note This method is called with the measurement mutex locked.
   */
  bool next_impl(std::vector<Tag> &incoming_tags, timestamp_t begin_time, timestamp_t end_time) override;

  /**
   * callback before the measurement is started
   * \note This method is called with the measurement mutex locked.
   */
  void on_start() override;

private:
  // channels used for this measurement
  const channel_t base_channel;
  const timestamp_t delay;
  channel_t output_channel;

  std::vector<Tag> mirror;
  std::deque<Tag> delayed_tags;
  bool overflow_state_on{};
};
