Imports System
Imports System.Threading
Imports SwabianInstruments.TimeTagger

Module Program
    Sub Main(args As String())
        ' Simplified global exception handler for a console application.
        ' It may Or may Not be be needed, depending on your project error handling policy.
        AddHandler AppDomain.CurrentDomain.UnhandledException,
            Sub(sender, eventArgs)
                WriteColoredLine(ConsoleColor.Red, CType(eventArgs.ExceptionObject, Exception).Message)
                Environment.Exit(1)
            End Sub

        Console.WriteLine("Hello TimeTagger!" & vbCrLf)

        If Not Environment.Is64BitProcess Then
            Console.WriteLine(
                "The process is running in the 32-bit mode." & vbCrLf &
                "For improved performance, please change the project settings such that it is running in the 64-bit mode." & vbCrLf
            )
        End If

        ' set custom logging
        TT.setLogger(
            Sub(level As Integer, message As String)
                If level >= LogLevel.LOGGER_WARNING Then
                    WriteColoredLine(ConsoleColor.Magenta, message)
                End If
            End Sub)

        Using tt As TimeTagger = SwabianInstruments.TimeTagger.TT.createTimeTagger()
            Console.WriteLine($"My serial number is: {tt.getSerial()}")

            WriteColoredLine(ConsoleColor.DarkGreen,
                "++++ Example 1:  Correlation class" & vbCrLf &
                "The internal test signal will be used to determine the jitter of the Time Tagger." & vbCrLf &
                "The distribution returned is not around x=0 because the internal test signal" & vbCrLf &
                "has a different delay than the external signal inputs." & vbCrLf
            )

            tt.setTestSignal(1, True)
            tt.setTestSignal(2, True)
            ' please note that
            ' channel_1 Is the parameter for the stop And
            ' channel_2 Is the parameter for the start
            Using correlation As Correlation = New Correlation(tt, channel_1:=2, channel_2:=1, binwidth:=50, n_bins:=1000)
                ' start measurement For one second (10E12 picoseconds) And wait till it finishes
                correlation.startFor(1_000_000_000_000)
                While correlation.isRunning()
                    Thread.Sleep(100)
                End While

                ' read the data collected within one second [t0, t0 + 1 second) time interval,
                ' where t0 Is the time when startFor was called (plus a very short USB delay)
                Dim data As Integer() = correlation.getData()
                Dim x As Long() = correlation.getIndex()

                Dim indexOfMax As Integer = 0
                For i As Integer = 1 To data.Length - 1
                    If data(i) > data(indexOfMax) Then
                        indexOfMax = i
                    End If
                Next

                Console.WriteLine("Correlation Measurement Data:")
                For i As Integer = Math.Max(0, indexOfMax - 10) To Math.Min(data.Length, indexOfMax + 11) - 1
                    Console.WriteLine("{0,6:D} ps:  {1,8:D} counts", x(i), data(i))
                Next
            End Using

            WriteColoredLine(ConsoleColor.DarkGreen,
                vbCrLf &
                "Finally we check whether all data was received via USB or data had to be discarded," & vbCrLf &
                "e.g., because the USB bandwidth was exceeded." & vbCrLf &
                "Because the test signal count rate is below the maximum USB transfer rate and the CPU effort" & vbCrLf &
                "for the analysis here is low, no overflows occur." & vbCrLf
            )

            Dim overflows As Long = tt.getOverflows()
            Console.WriteLine($"Number of buffer overflows: {overflows}." & vbCrLf)
            If overflows = 0 Then
                WriteColoredLine(ConsoleColor.Green, "All data has been processed.")
            Else
                WriteColoredLine(ConsoleColor.Red, "WARNING: Some data was discarded!")
                Environment.ExitCode = 1
            End If
        End Using
    End Sub

    Sub WriteColoredLine(color As ConsoleColor, value As String)
        Dim oldColor As ConsoleColor = Console.ForegroundColor
        Console.ForegroundColor = color
        Console.WriteLine(value)
        Console.ForegroundColor = oldColor
    End Sub
End Module
