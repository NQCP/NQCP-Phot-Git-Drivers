/*
This file is part of Time Tagger software defined digital data acquisition.
*/
#pragma once

#include "TimeTagger.h"

#include <map>
#include <vector>

/**
 *   Example to explain how to create a custom measurement class
 */
class CustomStartStop : public IteratorBase {
public:
  /**
   * CustomStartStop constructor
   *
   * \param tagger        reference to a TimeTagger
   * \param click_channel channel for stop clicks
   * \param start_channel channel for start clicks
   * \param binwidth      width of one histogram bin in ps
   */
  CustomStartStop(TimeTaggerBase *tagger, channel_t click_channel, channel_t start_channel, timestamp_t binwidth);

  ~CustomStartStop();

  /**
   * Within getData, the internal data (customData) is copied to a newly allocated allocated memory. The dimension of
   * the allocation is not known in advance, so a C++ callback is used instead.
   */
  void getData(std::function<timestamp_t *(size_t, size_t)> array_out);

protected:
  /**
   * next receives and handles the incoming tags.
   * All tags are sorted by time and comply with begin_time <= tag.time < end_time and end_time shall be the begin_time
   * of the next invocation. incoming_tags can be modified to filter or inject tags.
   * \param incoming_tags vector of incoming tags to process, might be empty
   * \param begin_time    begin timestamp of this block of tags
   * \param end_time      end timestamp of this block of tags
   * \return true if the content of this block was modified, false otherwise
   * \note This method is called with the measurement mutex locked.
   */
  bool next_impl(std::vector<Tag> &incoming_tags, timestamp_t begin_time, timestamp_t end_time) override;

  /**
   * reset measurement
   * \note This method is called with the measurement mutex locked.
   */
  void clear_impl() override;

  /**
   * callback before the measurement is started
   * \note This method is called with the measurement mutex locked.
   */
  void on_start() override;

  /**
   * callback after the measurement is stopped
   * \note This method is called with the measurement mutex locked.
   */
  void on_stop() override;

private:
  // channels used for this measurement
  const channel_t click_channel;
  const channel_t start_channel;
  const timestamp_t binwidth;

  timestamp_t last_start_tag;

  // data variable bin_index -> counts
  std::map<timestamp_t, size_t> data;
};
