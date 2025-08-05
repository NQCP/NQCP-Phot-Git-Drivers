// Swabian Instruments Time Tagger header files
#include <Iterators.h>
#include <TimeTagger.h>

// MathGL header files -- http://mathgl.sourceforge.net/
#define DRAW_MATHGL_PLOT
#ifdef DRAW_MATHGL_PLOT
#include <mgl2/mgl.h>
#endif

// C++ header files
#include <cassert>
#include <chrono>
#include <cmath>
#include <iostream>
#include <thread>
#include <vector>

int main() {
  // Connect to the Time Tagger
  TimeTagger *tagger = createTimeTagger();

  // Hard coded example configuration for the correlation
  channel_t c1 = 1;
  channel_t c2 = 2;
  timestamp_t binwidth = 10; // in ps
  int n_bins = 1000;

  // Local vectors to fetch the correlation data
  std::vector<int> counts;
  std::vector<timestamp_t> indices;

  // Enable the built-in test signal generator on two channels
  tagger->setTestSignal(c1, true);
  tagger->setTestSignal(c2, true);

  // Next step: Implementation of a correlation measurement
  {
    // Let's create the correlation measurement based on the configuration above
    Correlation corr(tagger, c2, c1, binwidth, n_bins);

    // The measurement will start immediately, but enabling the input port might
    // take a while. To achieve a fully deterministic result, we have to wait
    // till all configurations are applied.
    tagger->sync();

    // Measure for exact one second, given in ps
    timestamp_t one_sec(1e12);
    corr.startFor(one_sec);
    while (corr.isRunning()) {
      // Feel free to do whatever is needed. If this shall be embedded in a
      // bigger application, the main loop handler should be called instead of
      // sleeping.
      std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }

    // Fetch the amount of counts per correlation bin
    corr.getData([&counts, n_bins](size_t size) {
      // Some measurements have a mutable amount of bins. So we need to allocate
      // the memory within a callback. This blocks the internal processing of
      // the Time Tagger, so avoid all costly or blocking operations.
      assert(size == n_bins);
      counts.resize(size);
      return counts.data();
    });

    // Fetch the timing of every correlation bin
    corr.getIndex([&indices, n_bins](size_t size) {
      assert(size == n_bins);
      indices.resize(size);
      return indices.data();
    });

    // End of scope, so the correlation measurement instance will be destroyed.
    // This will unregister the input port to avoid needless USB bandwidth and
    // CPU utilization.
  }

  // Compute the total amount and the average offset of all events.
  double offset = 0;
  uint64_t total_counts = 0;
  for (size_t i = 0; i < n_bins; i++) {
    offset += static_cast<double>(counts[i]) * indices[i];
    total_counts += counts[i];
  }
  total_counts = std::max<uint64_t>(total_counts, 1);
  offset /= total_counts;

  // For statistical analysis, also compute the variance for the standard
  // deviation
  double variance = 0;
  for (size_t i = 0; i < n_bins; i++) {
    double time_difference = indices[i] - offset;
    variance += static_cast<double>(counts[i]) * time_difference * time_difference;
  }
  variance /= total_counts;

  // Debug outputs
  std::cout << "Total counts: " << total_counts << ", " << "offset: " << offset << "ps, "
            << "standard deviation: " << std::sqrt(variance) << "ps" << std::endl;

  // Next step: Generate the correlation plot
#ifdef DRAW_MATHGL_PLOT
  {
    // data arrays for plotting
    mglData x_data(n_bins);
    mglData y_counts(n_bins);
    mglData y_gauss(n_bins);

    // Generate x, normalized counts, and a Gaussian fit based on the standard
    // deviation. The counts are normalized based on integral(counts) == 1.
    for (size_t i = 0; i < n_bins; i++) {
      x_data.a[i] = (indices[i] - offset) * 1e-3;
      y_counts.a[i] = 1e3 * static_cast<double>(counts[i]) / total_counts / binwidth;
      if (variance > 0)
        y_gauss.a[i] = std::exp(-0.5e6 * x_data.a[i] * x_data.a[i] / variance) /
                       std::sqrt(2e-6 * 3.14159265358979323846 * variance);
      else
        y_gauss.a[i] = 0;
    }

    // And draw the plot
    mglGraph gr(0, 1920, 1080);
    gr.SetFontSize(3);
    gr.SetRanges(x_data, y_counts);
    gr.Plot(x_data, y_counts, "b", "legend 'Correlation'");
    gr.Plot(x_data, y_gauss, "r", "legend 'Gaussian fit'");
    gr.Axis();
    gr.Label('x', "time (ns)");
    gr.Label('y', "normalized counts (1/ns)");
    gr.Box();
    gr.Legend();
    gr.Title("Correlation example");
    gr.WriteFrame("correlation.png");

    std::cout << "Plot saved as 'correlation.png'." << std::endl;
  }
#endif

  // Everything is done, let's free the Time Tagger object again.
  // If this shall be embedded within a bigger application, this object shall be
  // cached.
  freeTimeTagger(tagger);

  return 0;
}
