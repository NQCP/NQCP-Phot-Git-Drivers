/*
This file is part of Time Tagger software defined digital data acquisition.
*/

#include "CustomDelayedChannel.h"
#include "CustomStartStop.h"

#include <Iterators.h>
#include <TimeTagger.h>

#include <array>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <thread>

class ScopeExitFreeTimeTagger {
public:
  ScopeExitFreeTimeTagger(TimeTagger *t) : t(t) {}
  ~ScopeExitFreeTimeTagger() { freeTimeTagger(t); }

private:
  TimeTagger *t;
};

int main_inner();

int main() {
  // Simplified global exception handler.
  // It may or may not be be needed, depending on your project error handling policy.
  try {
    return main_inner();
  } catch (std::exception &x) {
    std::cout << "Exception occurred.\n" << x.what() << std::endl;
    return 1;
  }
}

int main_inner() {
  std::cout << "Welcome to the Time Tagger API Demo" << std::endl;

#ifdef _DEBUG
  std::cout << "You are using the DEBUG version of the C++ runtime (/MDd). "
               "Please switch to the RELEASE version (/MD) for superior performance."
            << std::endl;
#endif

  if (sizeof(void *) == 4) {
    std::cout << "You are using the 32bit version of the Time Tagger. "
                 "Please switch to the 64bit version for superior performance."
              << std::endl;
  }

  std::vector<std::string> taggers = scanTimeTagger();
  if (taggers.empty()) {
    std::cout << std::endl << "No time tagger found." << std::endl << "Please attach a Time Tagger." << std::endl;
    return 1;
  }

  int res = 0;

  // connect to a time tagger
  TimeTagger *t = createTimeTagger();

  // We must free the time tagger after use. It can be done by calling freeTimeTagger(t) explicitly.
  // Alternatively, ScopeExitFreeTimeTagger can be utilized, to free time tagger when we go out of the current scope,
  // even due to an early return or exception.
  ScopeExitFreeTimeTagger guard(t);

  // turn in the test signal on the first two channels for all measurements
  for (int i = 1; i < 3; i++) {
    t->setTestSignal(i, true);
  }

  // *************************** Counterrate class example
  {
    std::cout << std::endl << "Example for the Counterrate class" << std::endl;
    std::vector<channel_t> v = {1, 2, 3, 4};
    Countrate c(t, v);

    std::this_thread::sleep_for(std::chrono::milliseconds(1000));

    // getData first allocates the memory with the provided allocator callback
    // and then copies the internal data as a snapshot
    std::vector<double> data;
    c.getData([&data](size_t size) {
      data.resize(size);
      return data.data();
    });
    std::cout << "Countrate of channel 1: " << data[0] << " (should be > 0 because the test signal is turned on)"
              << std::endl
              << "Countrate of channel 4: " << data[3] << " (should be 0 because the test signal is off)" << std::endl;

  } // The Countrate object will be destroyed here. This will stop the measurement and unregister the used channels on
    // the hardware.

  // *************************** Counter class example
  {
    std::cout << std::endl << "Example for the Counter class" << std::endl;
    std::vector<channel_t> v = {1, 2, 3, 4};
    const int bins = 10;
    Counter c(t, v, 1e8, 10); // sampling time per bin: 1e8 = 100ms, 10 bins

    std::this_thread::sleep_for(std::chrono::milliseconds(1000));

    // getData requires one linear memory with packed strides.
    // The reshape needs to be done manually.
    std::vector<int> data;
    c.getData([&data](size_t size1, size_t size2) {
      data.resize(size1 * size2);
      return data.data();
    });

    // reshape to 2d: data_reshaped[channel][bin]
    auto data_reshaped = reinterpret_cast<std::array<int, 10> *>(data.data());

    std::cout << "1st bin of channel 1: " << data_reshaped[0][0]
              << " (should be > 0 because the test signal is turned on)" << std::endl
              << "1st bin of channel 4: " << data_reshaped[3][0] << " (should be 0 because the test signal is off)"
              << std::endl;
  }

  // *************************** Custom measurement example
  {
    std::cout
        << std::endl
        << "Custom Measurement for Raw Time Tag Stream access" << std::endl
        << "There are several ways to access the raw Time Tag Stream:" << std::endl
        << "  1) dump the data via FileWriter and post-process it via FileReader;" << std::endl
        << "  2) use TimeTagStream;" << std::endl
        << "  3) use a Custom Measurement, which has the best performance for on the fly processing." << std::endl
        << std::endl
        << "We show here an example for a Custom Start Stop Measurement function." << std::endl
        << "The Custom Start Stop Measurement calculates the time difference between a given start" << std::endl
        << "to the next stop event and adds it to the histogram. The result is the very same as the" << std::endl
        << "StartStop method provided with our API." << std::endl
        << "In addition, we show how to synchronize measurements. Here we compare the Custom Start-Stop measurement"
        << std::endl
        << "with our own implemented Start-Stop measurement." << std::endl
        << "The signal of channel 2 is shifted by 2000 ps to see the full Gaussian curve and avoid cropping."
        << std::endl
        << std::endl;

    // Delay the stop channel by 2 ns to make sure it is later than the start.
    t->setInputDelay(2, 2000);

    // We first have to create a SyncrhonizedMeasurements object to synchronize several measurements.
    SynchronizedMeasurements measurementGroup(t);
    channel_t click_channel = 2, start_channel = 1;
    timestamp_t binwidth = 50; // ps
    StartStop startStop(measurementGroup.getTagger(), click_channel, start_channel, binwidth);
    CustomStartStop customStartStop(measurementGroup.getTagger(), click_channel, start_channel, binwidth);

    // This will run these measurements simultaneously.
    // Because of the asynchronous processing, they will neither start nor stop at once in real time, but they will
    // process exact the same data.
    measurementGroup.startFor(static_cast<timestamp_t>(1e12));
    measurementGroup.waitUntilFinished();

    // Fetch both vectors of data.
    std::vector<timestamp_t> data;
    startStop.getData([&data](size_t size1, size_t size2) {
      data.resize(size1 * size2);
      return data.data();
    });
    std::vector<timestamp_t> customData;
    customStartStop.getData([&customData](size_t size1, size_t size2) {
      customData.resize(size1 * size2);
      return customData.data();
    });

    std::cout << "Measurement Data: (max first 10 data points)" << std::endl
              << "StartStop                   | CustomStartStop" << std::endl;

    size_t bins = std::min<size_t>(10, std::min(data.size(), customData.size()) / 2);
    for (size_t i = 0; i < bins; i++) {
      std::cout << std::setw(6) << data[2 * i] << " ps: " << std::setw(9) << data[2 * i + 1] << " counts | "
                << std::setw(6) << customData[2 * i] << " ps: " << std::setw(9) << customData[2 * i + 1] << " counts"
                << std::endl;
    }

    if (data == customData)
      std::cout << "All " << data.size() / 2
                << " data points from the StartStop and CustomStartStop measurement are the very same." << std::endl;
    else {
      std::cout << "ERROR: results from StartStop and CustomStartStop differ!" << std::endl;
      res = 1;
    }
  }

  // *************************** Custom virtual channel example
  {
    std::cout << std::endl
              << "Custom Virtual Channel for Raw Time Tag Stream modification" << std::endl
              << "We show here an example for a Custom Delayed Channel, virtual channel implementation." << std::endl
              << "A Custom Delayed Channel takes a base channel and creates and virtual channel that represents."
              << std::endl
              << " the base channel plus a certain delay." << std::endl
              << std::endl;

    // We first have to create a SyncrhonizedMeasurements object to synchronize several measurements.
    SynchronizedMeasurements measurementGroup(t);
    channel_t base_channel = 1;
    timestamp_t delay = 1000; // ps
    CustomDelayedChannel delayed_channel(measurementGroup.getTagger(), base_channel, delay);
    StartStop startStop(measurementGroup.getTagger(), delayed_channel.getChannel(), base_channel, 1);

    // This will run these measurements simultaneously.
    // Because of the asynchronous processing, they will neither start nor stop at once in real time, but they will
    // process exact the same data.
    measurementGroup.startFor(static_cast<timestamp_t>(1e12));
    measurementGroup.waitUntilFinished();

    // Fetch both vectors of data.
    std::vector<timestamp_t> data;
    startStop.getData([&data](size_t size1, size_t size2) {
      data.resize(size1 * size2);
      return data.data();
    });

    if (data[0] == delay && data.size() == 2) {
      std::cout << "All time tags were exactly delayed as expected." << std::endl;
    } else {
      std::cout << "ERROR: Not all time tags were exactly delayed as expected!" << std::endl;
      res = 1;
    }
  }

  return res;
}
