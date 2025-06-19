using System;
using System.Linq;
using System.Threading;

namespace SwabianInstruments.TimeTagger.Examples
{
	internal class Program
    {
	    private static void Main()
        {
            // Simplified global exception handler for a console application.
            // It may or may not be be needed, depending on your project error handling policy.
            AppDomain.CurrentDomain.UnhandledException += (_, eventArgs) =>
            {
                WriteColoredLine(ConsoleColor.Red, ((Exception)eventArgs.ExceptionObject).Message);
                Environment.Exit(1);
            };

            Console.WriteLine("Hello TimeTagger!\n");

            if (!Environment.Is64BitProcess)
                Console.WriteLine(
                    "The process is running in the 32-bit mode.\n" +
                    "For improved performance, please change the project settings such that it is running in the 64-bit mode.\n"
                );

            // set custom logging
            TT.setLogger((level, message) =>
            {
                if (level >= (int)LogLevel.LOGGER_WARNING)
                    WriteColoredLine(ConsoleColor.Magenta, message);
            });

            // 'using' ensures that tt is disposed when we leave {}-scope
            using TimeTagger tt = TT.createTimeTagger();

            Console.WriteLine($"My serial number is: {tt.getSerial()}\n");

            // Example 1
            // all objects within {}-scope which declared with 'using'
            // will be disposed automatically when we leave the scope,
            // so there is no need to call Dispose() explicitly
            {
                WriteColoredLine(ConsoleColor.DarkGreen,
                    "++++ Example 1:  Correlation class\n" +
                    "The internal test signal will be used to determine the jitter of the Time Tagger.\n" +
                    "The distribution returned is not around x=0 because the internal test signal\n" +
                    "has a different delay than the external signal inputs.\n"
                );

                tt.setTestSignal(1, true);
                tt.setTestSignal(2, true);
                // please note that
                // channel_1 is the parameter for the stop and
                // channel_2 is the parameter for the start
                using Correlation correlation = new Correlation(tt, channel_1: 2, channel_2: 1, binwidth: 50, n_bins: 1000);

                // start measurement for one second (10e12 picoseconds) and wait till it finishes
                correlation.startFor((long)1e12);
                while (correlation.isRunning())
                    Thread.Sleep(100);

                // read the data collected within one second [t0, t0 + 1 second) time interval,
                // where t0 is the time when startFor was called (plus a very short USB delay)
                int[] data = correlation.getData();
                long[] x = correlation.getIndex();

                int indexOfMax = 0;
                for (int i = 1; i < data.Length; i++)
                    if (data[i] > data[indexOfMax])
                        indexOfMax = i;

                Console.WriteLine("Correlation Measurement Data:");
                for (int i = Math.Max(0, indexOfMax - 10); i < Math.Min(data.Length, indexOfMax + 11); i++)
                    Console.WriteLine("{0,6:D} ps:  {1,8:D} counts", x[i], data[i]);
            }

            WriteColoredLine(ConsoleColor.DarkGreen,
                "\n" +
                "++++ Example 2:  Custom Measurement for Raw Time Tag Stream access\n" +
                "There are several ways to access the raw Time Tag Stream:\n" +
                "  1) dump the data via FileWriter and post-process it via FileReader;\n" +
                "  2) use TimeTagStream;\n" +
                "  3) use a Custom Measurement, which has the best performance for on the fly processing.\n" +
                "\n" +
                "We show here an example for a Custom Start Stop Measurement function.\n" +
                "The Custom Start Stop Measurement calculates the time difference between a given start\n" +
                "to the next stop event and adds it to the histogram. The result is the very same as the\n" +
                "StartStop method provided with our API.\n" +
                "In addition, we show how to synchronize measurements. Here we compare the Custom Start-Stop measurement\n" +
                "with our own implemented Start-Stop measurement.\n" +
                "The signal of channel 2 is shifted by 2000 ps to see the full Gaussian curve and avoid cropping.\n"
            );
            // Delay the stop channel by 2 ns to make sure it is later than the start.
            tt.setInputDelay(2, 2000);

            // Example 2
            {
                using SynchronizedMeasurements measurementGroup = new(tt);

                // Instead of a real Time Tagger, we initialize the measurement with the proxy object measurementGroup.getTagger()
                // This adds the measurement to the measurementGroup. In contrast to a normal initialization of a measurement, the
                // measurement does not start immediately but waits for an explicit .start() or .startFor().
                using StartStop startStop = new StartStop(measurementGroup.getTagger(), click_channel: 2, start_channel: 1, binwidth: 50);
                using CustomStartStop customStartStop = new CustomStartStop(measurementGroup.getTagger(), clickChannel: 2, startChannel: 1, binWidth: 50);

                measurementGroup.startFor((long)1e12);
                while (measurementGroup.isRunning())
                    Thread.Sleep(100);

                long[,] data = startStop.getData();
                long[,] customData = customStartStop.GetData();

                Console.WriteLine("Measurement Data: (max first 10 data points)");
                Console.WriteLine("StartStop                   | CustomStartStop");
                int count = Math.Min(10, Math.Min(data.GetLength(0), customData.GetLength(0)));
                for (int i = 0; i < count; i++)
                    Console.WriteLine("{0,6:D} ps: {1,9:D} counts | {2,6:D} ps: {3,9:D} counts", data[i, 0], data[i, 1], customData[i, 0], customData[i, 1]);

                var equal =
                    data.Rank == customData.Rank &&
                    Enumerable.Range(0, data.Rank).All(dimension => data.GetLength(dimension) == customData.GetLength(dimension)) &&
                    data.Cast<long>().SequenceEqual(customData.Cast<long>());
                if (equal)
                    Console.WriteLine("All " + data.GetLength(0) + " data points from the StartStop and CustomStartStop measurement are the very same.");
                else
                {
                    WriteColoredLine(ConsoleColor.Red, "ERROR: results from StartStop and CustomStartStop differ!");
                    Environment.ExitCode = 1;
                }
            }

            WriteColoredLine(ConsoleColor.DarkGreen,
                "\nFinally we check whether all data was received via USB or data had to be discarded,\n" +
                "e.g., because the USB bandwidth was exceeded.\n" +
                "Because the test signal count rate is below the maximum USB transfer rate and the CPU effort\n" +
                "for the analysis here is low, no overflows occur.\n"
            );

            var overflows = tt.getOverflows();
            Console.WriteLine($"Number of buffer overflows: {overflows}.\n");
            if (overflows == 0)
                WriteColoredLine(ConsoleColor.Green, "All data has been processed.");
            else
            {
                WriteColoredLine(ConsoleColor.Red, "WARNING: Some data was discarded!");
                Environment.ExitCode = 1;
            }
        }

        private static void WriteColoredLine(ConsoleColor color, string value)
        {
            ConsoleColor oldColor = Console.ForegroundColor;
            Console.ForegroundColor = color;
            Console.WriteLine(value);
            Console.ForegroundColor = oldColor;
        }
    }
}
