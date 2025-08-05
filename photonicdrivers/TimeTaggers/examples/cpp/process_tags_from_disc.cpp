/*
This is a small example of how to read the raw Tag format from a dump file in
C++. For post-processing, a start-stop measurement is implemented for the
channels 1-2. An example file with 16M events can be generated with this python
code:

  from TimeTagger import *
  from time import sleep
  tt = createTimeTagger()
  tt.setTestSignal([1,2], True)
  tt.setInputDelay(2, 10000)
  fw = FileWriter(tt, 'raw_data', [1,2])
  sleep(10)
  fw.stop()

For live processing however, it is recommended to inherit the base class
IteratorBase. Such an example is shown within the CustomMeasurement example
files.
*/

#include <Iterators.h>  // FileReader
#include <TimeTagger.h> // struct Tag
#include <math.h>       // sqrt
#include <stdio.h>      // fopen, fread, fclose
#include <stdlib.h>     // malloc, calloc, free
#include <vector>

int main() {
  // allocation of the histogram
  std::vector<int> histogram(20000); // bins in ps

  { // scope for reading the file

    // opening of the raw tag file
    FileReader reader("raw_data");

    // buffer for raw Time Tags
    std::vector<Tag> buffer;

    // initial state before the processing of all tags
    timestamp_t last_start_click = 0;

    // loop over all chunks of tags
    while (reader.hasData()) {

      // read one chunk of tags into the local buffer
      reader.getDataRaw(buffer);

      // loop over all tags within this chunk
      for (Tag t : buffer) {
        if (t.type != Tag::Type::TimeTag) {
          // on overflow, invalidate the last start click
          last_start_click = 0;
        } else if (t.channel == 1) {
          // start event, keep this timestamp
          last_start_click = t.time;
        } else if (t.channel == 2) {
          // click event, increment the histogram bin (binwidth: 1 ps)
          size_t bin = t.time - last_start_click;
          if (last_start_click && bin < histogram.size()) {
            histogram[bin]++;
          }
        }
      }
    }

  } // scope for reading the file

  // Calculate the total amount of clicks within this histogram
  // Also calculate the center of gravity of the histogram
  long long total_clicks = 0;
  double offset = 0.0;
  for (size_t i = 0; i < histogram.size(); i++) {
    total_clicks += histogram[i];
    offset += histogram[i] * (double)i;
  }
  if (total_clicks == 0) {
    printf("no clicks found in histogram\n");
    return -1;
  }
  offset /= total_clicks;

  // Calculate the standard deviation of the histogram as RMS jitter
  double jitter = 0.0;
  for (size_t i = 0; i < histogram.size(); i++) {
    double shifted_offset = i - offset;
    jitter += histogram[i] * shifted_offset * shifted_offset;
  }
  jitter = sqrt(jitter / total_clicks);

  // Divide by sqrt(2) for the average jitter of the start and stop event
  jitter /= sqrt(2.0);

  // print the result on the screen
  printf("clicks: %lld, offset: %.1f ps, jitter: %.1f ps RMS\n", total_clicks, offset, jitter);

  return 0;
}
