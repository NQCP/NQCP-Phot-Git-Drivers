| Time | Tagger  | User    | Manual      |
| ---- | ------- | ------- | ----------- |
|      |         | Release | 2.17.4.0    |
|      | Swabian |         | Instruments |
Jul 16, 2024

CONTENTS
1 GettingStarted 1
1.1 GetfamiliarwithyourTimeTagger . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 GraphicalUserInterfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2.1 TimeTaggerLab . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2.2 WebApplication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3 Programminglanguages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3.1 Python . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3.2 LabVIEW(via.NET) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.3.3 Matlab(wrapperfor.NET) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.3.4 WolframMathematica(via.NET) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.3.5 .NET . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.3.6 C# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.3.7 C++ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2 Installationinstructions 11
2.1 Windows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.1.1 Installation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.2 Linux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.2.1 Installation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.2.2 Knownissues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.2.3 TimeTaggerwithPython . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.2.4 TimeTaggerwithC++ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3 Hardwarelicenseupgrades . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3.1 TimeTaggerLab . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.3.2 WebApplication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3 Tutorials 17
3.1 ConfocalFluorescenceMicroscope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.1.1 TimeTaggerconfiguration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.1.2 Intensityscanningmicroscope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.1.3 FluorescenceLifetimeMicroscope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.1.4 Alternativepixeltriggerformats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.2 OpticallyDetectedMagneticResonance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.2.1 Creationofopticalandmicrowavepulsepatterns . . . . . . . . . . . . . . . . . . . . . . . 25
3.2.2 Signalgenerationanddetection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.2.3 Sweepingmodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.2.4 ODMRcontrast . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.3 MeasuringCoincidences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.3.1 TimeTaggerconfiguration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.3.2 Coincidence-counting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
i

3.3.3 Delayadjustmentforcoincidencedetection . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.3.4 ExclusivecoincidencesusingCombinationsvirtualchannel . . . . . . . . . . . . . . . . . . 34
3.3.5 Coincidence-countingvsCorrelationMeasurement . . . . . . . . . . . . . . . . . . . . . . 36
3.4 RemoteTimeTaggerwithPython . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.4.1 SharingaTimeTaggerwithNetworkTimeTagger . . . . . . . . . . . . . . . . . . . . . . 37
3.4.2 RemotecontrolofaTimeTaggerwithPyro . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.4.3 Remoteprocedurecall . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.4.4 Initialsetup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.4.5 Minimalexample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.4.6 CreatingtheTimeTagger . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.4.7 Measurementsandvirtualchannels. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.4.8 Workingexample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.4.9 Whatisnext? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
4 Synchronizer 47
4.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
4.2 Keyapplications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
4.2.1 Crosstalkelimination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
4.2.2 Hightransferrate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
4.2.3 Multi-roomexperiment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
4.2.4 SynchronizerwithasingleTimeTagger . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
4.3 Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
4.4 Cableconnections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
4.4.1 Usinganexternalreferenceclock. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
4.5 Softwareandchannelnumbering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
4.5.1 Incompletecableconnections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
4.5.2 Bufferoverflows. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
4.6 Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
4.6.1 Conditionalfilter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
4.6.2 Internaltestsignal. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
4.7 StatusLEDsandtroubleshooting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
5 Hardware 53
5.1 Inputchannels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
5.1.1 Electricalcharacteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
5.1.2 Configurableinputtermination-TimeTaggerXonly . . . . . . . . . . . . . . . . . . . . . 53
5.1.3 HighResolutionMode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
5.2 Dataconnection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
5.3 LEDs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
5.3.1 TimeTaggerX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
5.3.2 TimeTaggerUltra. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
5.3.3 TimeTagger20 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
5.4 Testsignal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
5.5 Syntheticinputdelay . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
5.6 Syntheticdeadtime . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
5.7 Eventdivider . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
5.8 ConditionalFilter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
5.9 Binequilibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
5.10 Overflows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
5.11 ExternalClockInput . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
5.12 Synchronizationsignals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
5.13 FPGAlink . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
5.14 GeneralpurposeIO(GPIO) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
ii

6 SoftwareOverview 63
6.1 GraphicalUserInterfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
6.2 Precompiledlibrariesandhigh-levellanguagebindings . . . . . . . . . . . . . . . . . . . . . . . . . 63
6.3 C++API . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
7 ApplicationProgrammingInterface 65
7.1 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
7.1.1 Measuringcross-correlation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
7.1.2 Usingvirtualchannels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
7.1.3 UsingmultipleTimeTaggers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
7.1.4 UsingTimeTaggerremotely . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
7.2 TheTimeTaggerLibrary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
7.2.1 Unitsofmeasurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
7.2.2 Channelnumbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
7.2.3 Unusedchannels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
7.2.4 Constants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
7.2.5 Enumerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
7.2.6 Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
7.2.7 Helperclasses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
7.3 TimeTaggerclasses. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
7.3.1 GeneralTimeTaggerfeatures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
7.3.2 TimeTaggerhardware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
7.3.3 TheTimeTaggerVirtualclass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
7.3.4 TheTimeTaggerNetworkclass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
7.3.5 Additionalclasses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
7.4 VirtualChannels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
7.4.1 Availablevirtualchannels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
7.4.2 Commonmethods. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
7.4.3 Coincidence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
7.4.4 Coincidences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
7.4.5 Combinations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
7.4.6 Combiner . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
7.4.7 ConstantFractionDiscriminator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
7.4.8 DelayedChannel. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
7.4.9 EventGenerator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
7.4.10 FrequencyMultiplier . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
7.4.11 GatedChannel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
7.4.12 TriggerOnCountrate. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
7.5 MeasurementClasses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
7.5.1 Availablemeasurementclasses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
7.5.2 Commonmethods. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
7.5.3 Eventcounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
7.5.4 Timehistograms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
7.5.5 Fluorescence-lifetimeimaging(FLIM) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
7.5.6 Phase&frequencyanalysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
7.5.7 Time-tag-streaming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
7.5.8 Helperclasses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
7.5.9 CustomMeasurements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
8 InDepthGuides 159
8.1 ConditionalFilter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
8.1.1 Exampleconfigurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
8.1.2 Understandingthefilteringmechanism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
8.1.3 SetupoftheConditionalFilter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
iii

8.2 RawTime-Tag-Streamaccess . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
8.2.1 Dumpingandpost-processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
8.2.2 On-the-flyprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166
8.3 SynchronizationoftheTimeTaggerpipeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166
8.4 FPGAlink . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
8.4.1 GettingStartedwithSFP+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
8.4.2 UsingQSFP+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
8.4.3 Modifyingthereferencedesign . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
9 UsageStatisticsCollection 169
9.1 Contentsoftheusagestatisticsdata . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
9.2 Waysofcontrol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
9.3 TimeTaggerLabdiagnostics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
10 Legal&Safety 171
10.1 TimeTaggerX -Safetynotice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
10.1.1 Symbols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
10.1.2 Operationenvironment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
10.1.3 Electricalcharacteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
10.1.4 Electrostatic-sensitivedevice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
10.1.5 Equipmentinstallation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
10.1.6 Maintenanceandrepair . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
10.1.7 Disposalandrecycling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
10.1.8 Contact,supportandservice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
11 RevisionHistory 177
11.1 V2.17.4-17.07.2024 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177
11.2 V2.17.2-02.07.2024 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177
11.3 V2.17.0-22.04.2024 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
11.4 V2.16.2-28.06.2023 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
11.5 V2.16.0-05.06.2023 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
11.6 V2.15.0-06.03.2023 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
11.7 V2.14.0-23.12.2022 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
11.8 V2.13.2-22.11.2022 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
11.9 V2.12.4-09.11.2022 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
11.10 V2.12.2-04.10.2022 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
11.11 V2.12.0-01.09.2022 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
11.12 V2.11.0-22.04.2022 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
11.13 V2.10.6-16.03.2022 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
11.14 V2.10.4-23.02.2022 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
11.15 V2.10.2-31.12.2021 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
11.16 V2.10.0-22.12.2021 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
11.17 V2.9.0-07.06.2021 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
11.18 V2.8.4-04.05.2021 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
11.19 V2.8.2-26.04.2021 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
11.20 V2.8.0-29.03.2021 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
11.21 V2.7.6-26.04.2021 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
11.22 V2.7.4-19.04.2021 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
11.23 V2.7.2-22.12.2020 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
11.24 V2.7.0-01.10.2020 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193
11.25 V2.6.10-07.09.2020 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193
11.26 V2.6.8-21.08.2020 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194
11.27 V2.6.6-10.07.2020 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194
11.28 V2.6.4-27.05.2020 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
iv

11.29 V2.6.2-10.03.2020 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196
11.30 V2.6.0-23.12.2019 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
11.31 V2.4.4-29.07.2019 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
11.32 V2.4.2-12.05.2019 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 200
11.33 V2.4.0-10.04.2019 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 200
11.34 V2.2.4-29.01.2019 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
11.35 V2.2.2-13.11.2018 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
11.36 V2.2.0-07.11.2018 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
11.37 V2.1.6-17.05.2018 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
11.38 V2.1.4-21.03.2018 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
11.39 V2.1.2-14.03.2018 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
11.40 V2.1.0-06.03.2018 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
11.41 V2.0.4-01.02.2018 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
11.42 V2.0.2-17.01.2018 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203
11.43 V2.0.0-14.12.2017 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203
11.44 V1.0.20-24.10.2017 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203
11.45 V1.0.6-16.03.2017 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204
11.46 V1.0.4-24.11.2016 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
11.47 V1.0.2-28.07.2016 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
11.48 V1.0.0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
11.49 ChannelNumberSchema0and1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
Index 207
v

vi

CHAPTER
ONE
GETTING STARTED
ThefollowingsectiondescribeshowtogetstartedwithyourTimeTagger.
First,pleaseinstallthemostrecentdriver/software,includinggraphicaluserinterfaces,libraries,andexamplesforC++,
Python,.NET,C#,LabVIEW,Matlab,andMathematica.
TimeTaggersoftwaredownload
https://www.swabianinstruments.com/time-tagger/downloads/
Youarehighlyencouragedtoreadthesectionsbelowtogetstartedwiththegraphicaluserinterfaceand/ortheTime
Taggerprogramminglibraries.
Additionalinformationaboutthehardware,API,etc. canbefoundinthemenubarontheleftandonourmainwebsite:
https://www.swabianinstruments.com/time-tagger/.
IfyouareusingLinux,pleasetakealookattheLinuxsection.
1.1 Get familiar with your Time Tagger
TolearnmoreabouttheTimeTaggeryouareencouragedtoconsultthefollowingresources.
1. Run the Graphical User Interface, Time Tagger Lab or the Web Application, to play with your Time Tagger
interactively. The examples below will allow you to experience basic data acquisition. Play with the Time
Taggersettingstoseetheireffectsontypicalmeasurements.
2. CheckouttheApplicationProgrammingInterfacechapter. ItgivesyouadetailedoverviewofallTimeTagger
features and data processing classes. Check out the following sections to get started using the Time Tagger
softwarelibraryintheprogramminglanguageofyourchoice.
3. Studythecodeexamplesinthe.\examples\<language>\foldersofyourTimeTaggerinstallation.
1

TimeTaggerUserManual,Release2.17.4.0
1.2 Graphical User Interfaces
1.2.1 Time Tagger Lab
TimeTaggerLabistheGraphicalUserInterface(GUI)applicationforWindowsoperatingsystems. Itisdesignedto
performstandardmeasurementsquicklyandtogetaninteractiveexperiencewithyourTimeTagger.
1. DownloadandinstallthemostrecentTimeTaggersoftwarefromourdownloadssite.
2. StartTime Tagger LabfromtheWindowsstartmenu.
3. TheTimeTaggerLabwelcomescreenopensandpresentsallavailabledevices. IfyouplugorunplugaTime
Tagger,thedisplaywillupdateautomatically.
2 Chapter1. GettingStarted

TimeTaggerUserManual,Release2.17.4.0
TimeTaggerLaballowsyoutoworkwithyourTimeTaggerinteractively. WewillnowusetheTimeTagger’sinternal
testsignaltomeasureacrosscorrelationbetweentwochannelsasanexample.
1. On the welcome screen, click on the panel representing your desired device. The Home screen of your Time
Taggershowsup.
2. On the top of the Home screen, you can toggle between the basic display you are currently looking at and the
Detailed View. ActivatetheDetailed View.
3. In the upper panel of the Detailed View, you can change settings for every input. Activate the internal test
signaloninputs1and2bycheckingtheboxesontherightmostcolumn.
4. GobacktothebasicdisplaybydeactivatingDetailed view. Thecountratedisplays(cps)showatestsignal
countrateof800to900kHz,andthetriggerlevelsettingisreplacedbythelabeltest signal.
Withtheactivatedtestsignal,wecanstartourfirstmeasurement.
1. Clickon Open creator (F2)intheMeasurementspanelontheleft. Thecreatorgivesyouanoverviewof
allavailablemeasurements.
2. Pick Bidirectional histogram - Correlation. Now you can read through a detailed description and
changetheinitialsettingsofyourmeasurement.
3. SetReference channelto1andClick channelto2. ClickAdd measurement.
4. Themeasurementgraphisshowingup. Tostartthemeasurement,clickthePlaybuttonnexttothegraph.
5. AGaussianpeakshouldbedisplayed. Youcanzoominusingthecontrolsontheplot. Iftheresolutionisnot
sufficient,tryasmallerBin widthinthemeasurementsettings.
6. Thedetectionjitterofasinglechannelis √1 timesthestandarddeviationofthistwo-channelmeasurement(the
2
FWHM(Full-widthathalf-maximum)oftheGaussianpeakis2.35timesitsstandarddeviation).
Youhavejustverifiedthetimeresolution(detectionjitter)ofyourTimeTagger.
1.2. GraphicalUserInterfaces 3

TimeTaggerUserManual,Release2.17.4.0
| 1.2.2 | Web Application |     |     |     |     |     |
| ----- | --------------- | --- | --- | --- | --- | --- |
The Web Application is the traditional provided GUI (Graphical User Interface) for Windows and Linux for quick
measurements. OnWindowssystems,werecommendswitchingtoTimeTaggerLabtoday.
1. DownloadandinstallthemostrecentTimeTaggersoftwarefromourdownloadssite.
| 2. StarttheTime | Tagger | ApplicationfromtheWindowsstartmenu. |     |     |     |     |
| --------------- | ------ | ----------------------------------- | --- | --- | --- | --- |
3. TheWebApplicationshouldshowupinyourbrowser.
TheWebApplicationusestheTCPport50120asdefaultport. Ifthiscollideswithanotherapplicationyoucan
Note:
| changetheportwithpassingtheargumentTimeTaggerServer.exe |     |     |     | -p  | 50120. |     |
| ------------------------------------------------------- | --- | --- | --- | --- | ------ | --- |
The Web Application allows you to work with your Time Tagger interactively. We will now use the Time Tagger’s
internaltestsignaltomeasureacrosscorrelationbetweentwochannelsasanexample.
1. ClickAdd TimeTagger,clickInit(selectresolutionifavailable)onanyoftheavailableTimeTaggers
| 2. Click | measurement, | look | for           |           |                      | and click |
| -------- | ------------ | ---- | ------------- | --------- | -------------------- | --------- |
|          | Create       |      | Bidirectional | Histogram | (Class: Correlation) |           |
Createnexttoit.
| 3. SelectRising |      | 1forChannel1andRising |      | 2forChannel2. |     |     |
| --------------- | ---- | --------------------- | ---- | ------------- | --- | --- |
|                 | edge |                       | edge |               |     |     |
4. SetBinwidthto10psandleaveNumber of data pointsat1000,clickInitialize.
TheTimeTaggerisnowacquiringdata,butitdoesnotyethaveasignal. Wewillnowenableitsinternaltestsignal.
| 1. Onthetopleft,clickonthesettingswheelnexttoTime |     |                                 |     | Tagger. |     |     |
| ------------------------------------------------- | --- | ------------------------------- | --- | ------- | --- | --- |
| 2. Onthefarright,checkTest                        |     | signalforchannels1and2,clickOk. |     |         |     |     |
3. AGaussianpeakshouldbedisplayed. Youcanzoominusingthecontrolsontheplot.
4. Thedetectionjitterofasinglechannelis √1 timesthestandarddeviationofthistwo-channelmeasurement(the
| FWHMoftheGaussianpeakis2.35timesitsstandarddeviation). |     |     | 2   |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
Youhavejustverifiedthetimeresolution(detectionjitter)ofyourTimeTagger.
| 1.3 Programming |     | languages |     |     |     |     |
| --------------- | --- | --------- | --- | --- | --- | --- |
1.3.1 Python
1. MakesurethatyourTimeTagger deviceisconnectedtoyourcomputerandtheTimeTagger WebApplication
(especiallytheserverwindow)isclosed.
2. MakesuretheTimeTaggersoftwareandaPythondistribution(onWindowsOSwerecommendAnaconda)are
installed.
3. Openacommandshellandnavigatetothe .\examples\python\1-QuickstartfolderinyourTimeTagger
installationdirectory
| 4. Startanipythonshellwithplottingsupportbyenteringipython |     |     |             | --pylab |     |     |
| ---------------------------------------------------------- | --- | --- | ----------- | ------- | --- | --- |
| 5. Runthehello_world.pyscriptbyenteringrun                 |     |     | hello_world |         |     |     |
Thehello_worldexecutesasimpleyetusefulmeasurementthatdemonstratesmanyessentialfeaturesoftheTimeTagger
programminginterface:
1. ConnectyourTimeTagger
| 4   |     |     |     |     | Chapter1. | GettingStarted |
| --- | --- | --- | --- | --- | --------- | -------------- |

TimeTaggerUserManual,Release2.17.4.0
2. Startthebuilt-intestsignal(~0.8MHzsquarewave)andapplyittochannels1and2
3. Controlthetriggerlevelofyourinputs-althoughitisnotnecessaryhere
4. Initializeastandardmeasurement(Correlation)inordertofindthedelayofthetestsignalbetweenchannel1
and2
5. Howtocontrolthedelayofdifferentinputsprogrammatically.
Youareencouragedtoopenandreadthehello_world.pyfileinaneditortounderstandwhatitisdoing. Withthis
basicknowledge,youcanexploretheotherexamplesinthe1-Quickstartfolder:
1.3. Programminglanguages 5

TimeTaggerUserManual,Release2.17.4.0
| No. | Topic | Classes&Methods |     |     |
| --- | ----- | --------------- | --- | --- |
Basicsoftwarecontrol(folder1-basic_software_control)
| 1-A | Createamea- | createTimeTagger(),Counter.getData(), |     |     |
| --- | ----------- | ------------------------------------- | --- | --- |
|     | surement    | Counter.getIndex()                    |     |     |
|     | Count rate  |                                       |     |     |
Counter
trace
| 1-B | Start & stop | Countrate,start(),stop(),startFor() |     |     |
| --- | ------------ | ----------------------------------- | --- | --- |
measure-
ments
| 1-C | Synchronize |     |     |     |
| --- | ----------- | --- | --- | --- |
SynchronizedMeasurements
measure-
ments
|     | Use different | Correlation,Histogram,                  |     |     |
| --- | ------------- | --------------------------------------- | --- | --- |
|     | histograms    | StartStop,HistogramLogBins              |     |     |
| 1-D | Virtual Chan- | DelayedChannel,Coincidence,GatedChannel |     |     |
nels
| 1-E | Logging | setLogger() |     |     |
| --- | ------- | ----------- | --- | --- |
errors
| 1-F | (External) | TimeTaggerBase.setSoftwareClock(), |     |     |
| --- | ---------- | ---------------------------------- | --- | --- |
software
FrequencyStability
clock
Controllingthehardware(folder2-controlling-the-hardware)
| 2-A | Get hardware | scanTimeTagger(),TimeTagger.getSerial(),          |     |     |
| --- | ------------ | ------------------------------------------------- | --- | --- |
|     | information  | TimeTagger.getModel(),TimeTagger.getSensorData(), |     |     |
TimeTaggerBase.getConfiguration()
2-B The input TimeTagger.setTriggerLevel(),TimeTagger.getDACRange()
triggerlevel
| 2-C | Filter tags on | TimeTagger.setConditionalFilter(),         |     |     |
| --- | -------------- | ------------------------------------------ | --- | --- |
|     | hardware       | TimeTagger.setEventDivider()               |     |     |
| 2-D | Control input  | TimeTaggerBase.setInputDelay(),Histogram2D |     |     |
delays
| 2-E | Overflows | TimeTaggerBase.getOverflows(), |     |     |
| --- | --------- | ------------------------------ | --- | --- |
TimeTagger.setTestSignalDivider()
| 2-F | HighRes | createTimeTagger(),TimeDifferences |     |     |
| --- | ------- | ---------------------------------- | --- | --- |
mode
Dumpandre-analyzetime-tags(folder3-dump-and-reanalyze-time-tags)
| 3-A | Dumptagsby | FileWriter |     |     |
| --- | ---------- | ---------- | --- | --- |
FileWriter
| 3-B | The Time | createTimeTaggerVirtual(),TimeTaggerVirtual |     |     |
| --- | -------- | ------------------------------------------- | --- | --- |
Tagger Vir-
tual
Workingwithrawtime-tags(folder4-working-with-raw-time-tags)
| 4-A | The Fil- | FileReader,TimeTagStreamBuffer |     |     |
| --- | -------- | ------------------------------ | --- | --- |
eReader
| 4-B | Streaming | TimeTagStream |     |     |
| --- | --------- | ------------- | --- | --- |
rawtime-tags
| 4-C | Custom Mea- | CustomMeasurement |     |     |
| --- | ----------- | ----------------- | --- | --- |
surements
MoredetailsaboutthesoftwareinterfacearecoveredbytheAPIdocumentationinthesubsequentsection
| 6   |     |     | Chapter1. | GettingStarted |
| --- | --- | --- | --------- | -------------- |

TimeTaggerUserManual,Release2.17.4.0
1.3.2 LabVIEW (via .NET)
InLabVIEW,youcanaccessandprogramyourTimeTaggerthrough.NETinteroperability.
Asetofexamplesisprovidedin.\examples\LabVIEW\forLabVIEW2014andhigher(32and64bit).
1.3.3 Matlab (wrapper for .NET)
WrapperclassesareprovidedforMatlabsothatnativeMatlabvariablescanbeused.
TheTimeTaggertoolboxisautomaticallyinstalledduringthesetup. If TimeTaggerisnotavailableinyourMatlab
environmenttrytoreinstallthetoolboxfrom.\driver\Matlab\TimeTaggerMatlab.mltbx.
Thefollowingchangesinrespecttothe.NETlibraryhavebeenmade:
• staticfunctionsareavailablethroughtheTimeTaggerclass
• allclassesexceptfortheTimeTagger,TimeTaggerNetwork,andTimeTaggerVirtualclasseswillhaveaTT
prefix(e.g. TTCountrate)topreventconflictwithanyvariables/classesinyourMatlabenvironment
AnexampleofhowtousetheTimeTaggerwithMatlabcanbefoundin.\examples\Matlab\.
1.3.4 Wolfram Mathematica (via .NET)
Time Tagger functionality is provided to Mathematica via .NET interoperability interface. Please take a look at the
examplesin.\examples\Mathematica\.
1.3.5 .NET
Weprovidea.NETclasslibrary(32,64bitandCIL)fortheTimeTaggerwhichcanbeusedtoaccesstheTimeTagger
frommanyhigh-levellanguages.
Thefollowingareimportanttonote:
• Namespace: SwabianInstruments.TimeTagger
• thecorrespondinglibrary.\driver\xxx\SwabianInstruments.TimeTagger.dllisregisteredintheGlobal
AssemblyCache(GAC)
1.3. Programminglanguages 7

TimeTaggerUserManual,Release2.17.4.0
• static functions (e.g. to create an instance of a TimeTagger) are accessible via SwabianInstruments.
TimeTagger.TT
1.3.6 C#
AsampleVisualStudioC#projectprovidedinthe.\examples\csharp\Quickstartdirectorycoversthebasicsof
howtousetheTimeTagger.NETAPI.Anexampleofcreating‘custommeasurements’isalsoincluded.
Please copy the project folder to a directory within the user environment such that files can be written within the
directory.
An‘ExampleSuite’isprovidedinthe.\examples\csharp\ExampleSuitedirectory. ‘ExampleSuite’isaninter-
active application that demonstrates various measurements that can be performed with the TimeTagger. Reference
sourcecodetosetupandplot(withOxyPlot)eachmeasurementisalsoprovidedwithintheapplication. Additionally,
the application contains examples for creating and using ‘Virtual channels’, ‘Filtering’ and ‘Accessing the raw time
tags’.
Note: RunningtheExampleSuiterequires‘.NETCore3.1DesktopRuntime(v3.1.10)’.
1.3.7 C++
The provided Visual Studio C++ project can be found in .\examples\cpp\. Using the C++ interface is the most
performantwaytointeractwiththeTimeTaggerasitsupportswritingcustommeasurementclasseswithnooverhead.
Butitismoreelaboratecomparedtotheotherhigh-levellanguages. Pleasevisit .\documentation\Time Tagger
C++ API Manual.pdfformoredetailsontheC++API.
Note:
• theC++headersarestoredinthe.\driver\include\folder
• thefinalassemblymustlink.\driver\xYZ\TimeTagger.lib
• the library .\driver\xYZ\TimeTagger.dll is linked with the shared v142 or newer Visual Studio runtime
(/MD)
• useTimeTaggerD.libandTimeTaggerD.dllfortheVisualStudiodebugruntime(/MDd)
• uselibTimeTagger.dlland libTimeTagger.afortheMinGWC++ABIfortheMINGW32andUCRT64
environment.
Debugandreleasebuilds: Performanceissueswithdebugbuilds
Forthistopic,itisrequiredtobeabitmorepreciseonwhatiscalleda Debugbuild. VisualStudiodefaultcompiler
flagsforDebugare/MDd /O0 /ZiandforRelease/MD /O2 /DNDEBUG.
• /O0vs/O2
Thisisthegeneraloptimizationlevel. /O0meansnooptimization, soeveryinstructionissurroundedby
load_from_memory and store_to_memory. This is a huge waste of CPU resources, but it guarantees
thateverylocalvariablecanbeinspectedateverytime. Wesuggesttousethedefaultoptimizationlevel
/O2bydefaultandtooverwriteitonlyforrequiredmethodsusingpragmas: MSVCoptimizepragma.
8 Chapter1. GettingStarted

TimeTaggerUserManual,Release2.17.4.0
• /MDdvs/MD
Thisflagselectswhich(incompatible)runtimeC++ABIyouwanttouseforthewholeproject. Thedebug
runtimeMDdhasadditionalfieldsandchecksfore.g. betterrangechecking. Itisgoodpracticetorunyour
codewiththematleastoncebeforeeachcommit. Astheyareincompatiblewitheachother,ALLlinkedC++
librariesMUSTusethesameruntime. ThisflagistheonlydifferencebetweenourdebugTimeTaggerD.
dllandnon-debugTimeTagger.dlllibrary. WesuggesttouseMDevenfordebugbuilds,elsethedebug
runtimewilldegeneratetheoverallperformancealsointheinternalTimeTaggercode.
• /Zi
Thisflagtellsthecompilertogeneratea*.pdbsymbolfile. Thisisusedbythedebuggertomape.g. the
assemblytotheC++codeandthestacktothelocalvariable. Asthishasnoperformanceoverhead,always
usethisflagforallinternalbuilds.
• /DNDEBUG
ThemacroNDEBUGistheCwaytodisableassert(). Theyareusuallygoodatcatchingsameerrorswithout
much overhead. We also like to recommend to switch your compiler to CLANG and use its undefined
behavior sanitizer, the address sanitizerm or the thread sanitizer. Microsoft announced it a bit ago that
MSVCnowhastheaddresssanitizer,whichfindsout-of-boundsaccesses,use-after-freeandsimilarissues:
AddressSanitizer(ASan)forWindowswithMSVC.
Sointheend,itisnotaboutjustusingDebugorRelease. Itisaboutwhichsetofflagsisused. Pleaseselecteachof
themcarefullybasedonyourtarget.
1.3. Programminglanguages 9

TimeTaggerUserManual,Release2.17.4.0
| 10  | Chapter1. | GettingStarted |
| --- | --------- | -------------- |

CHAPTER
TWO
INSTALLATION INSTRUCTIONS
2.1 Windows
Time Tagger software requires Windows 10 or higher. We provide separate Windows installers for 32 and 64 bit
systems.
2.1.1 Installation
1. Downloadtheinstallerfromourdownloadssite.
2. Runtheinstallerandfollowtheinstructions.
3. ConnectyourTimeTagger.
4. MakesurethatyourcomputerisconnectedtotheinternetonceyouruntheTimeTaggersoftware. Thesoftware
needstorequestitslicensefromourserver. Oncethelicenseistransferred, nointernetconnectionisrequired
anymore.
2.2 Linux
2.2.1 Installation
Download and install the package for your Linux distribution from the Time Tagger downloads page https://www.
swabianinstruments.com/time-tagger/downloads/.
ThepackageinstallsthePythonandC++librariesforamd64systems,includingexampleprograms.
Graphicaluserinterface(WebApplication):
• Launchviatimetaggerfromtheconsoleortheapplicationlauncher.
11

TimeTaggerUserManual,Release2.17.4.0
| 2.2.2 Known | issues |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- |
• IncaseyouhaveinstalledapreviousversionoftheTimeTaggersoftware,pleaseresetthecacheofyourbrowser.
• ClosingtheWebApplicationservermaycauseanerrormessagetoappear.
| 2.2.3 Time | Tagger with | Python |     |     |     |
| ---------- | ----------- | ------ | --- | --- | --- |
• InstallNumPy(e.g. pip install numpy),whichisrequiredfortheTimeTaggerlibraries.
• ThePythonlibrariesareinstalledinyourdefaultPythonsearchpath: /usr/lib/pythonX.Y/dist-packages/
or/usr/lib64/pythonX.Y/site-packages/.
• Theexamplescanbefoundwithinthe/usr/lib/timetagger/examples/python/folder.
YoucancompileaPythonmoduleforcustomPythoninstallationsinthefollowingway:
| The source | of the Python wrapper |                 | is provided in |                                     |     |
| ---------- | --------------------- | --------------- | -------------- | ----------------------------------- | --- |
|            |                       | _TimeTagger.cxx |                | /usr/lib64/pythonX.Y/site-packages/ |     |
. For building the wrapper, the GNU C++ compiler and the development headers of Python and numpy need to be
installed. The resulting _TimeTagger.so and the high-level wrapper TimeTagger.py relay the Time Tagger C++
interfacetoPython.
| PYTHON_FLAGS="(cid:96)python3-config |     | --includes | --libs(cid:96)" |     |     |
| ------------------------------------ | --- | ---------- | --------------- | --- | --- |
NUMPY_FLAGS="-I(cid:96)python3 -c \"print(__import__('numpy').get_include())\"(cid:96)"
| TTFLAGS="-I/usr/include/timetagger |     | -lTimeTagger" |     |     |     |
| ---------------------------------- | --- | ------------- | --- | --- | --- |
CFLAGS="-std=c++17 -O2 -DNDEBUG -fPIC $PYTHON_FLAGS $NUMPY_FLAGS $TTFLAGS"
| g++ -shared | _TimeTagger.cxx | $CFLAGS | -o _TimeTagger.so |     |     |
| ----------- | --------------- | ------- | ----------------- | --- | --- |
| 2.2.4 Time  | Tagger with     | C++     |                   |     |     |
• Theexamplescanbefoundwithinthe/usr/lib/timetagger/examples/cpp/folder.
• The header files can be found within the /usr/include/timetagger/ folder (-I /usr/include/
timetagger).
• Theassemblyshallbelinkedwith/usr/lib/libTimeTagger.so(-l TimeTagger).
TheC++interfacewilllikelyalsoworkonotherdistributionsoutofthebox.
| 2.3 Hardware | license | upgrades |     |     |     |
| ------------ | ------- | -------- | --- | --- | --- |
TheTimeTaggerUltraandTimeTaggerXhaveahardwarelicensethatcanbeupgradedtoactivateadditionalchannels
and features. To upgrade your license, please get in touch with sales@swabianinstruments.com. After purchasing a
licenseupgrade,thenewlicensebecomesavailablewithinafewminutes. Youcaninstallyournewlicenseusingone
ofthegraphicaluserinterfaces. Anactiveinternetconnectionisneededoncefortheupgradeprocess.
| 12  |     |     |     | Chapter2. | Installationinstructions |
| --- | --- | --- | --- | --------- | ------------------------ |

TimeTaggerUserManual,Release2.17.4.0
2.3.1 Time Tagger Lab
1. ConnecttheTimeTaggertoyourPC
2. StartTimeTaggerLab
3. Ifanewlicenseisavailable,youwillseethefollowing:
4. Clickon“Updatethelicense”. Thenewlicensewillbeappliedimmediatelyandyouwillsee:
2.3. Hardwarelicenseupgrades 13

TimeTaggerUserManual,Release2.17.4.0
2.3.2 Web Application
1. ConnecttheTimeTaggertoyourPC
2. StarttheTimeTaggerWebApplication
3. Clickon“AddTimeTagger”inthetopleftcorner
4. You should see your connected Time Tagger and at the bottom the button “Check for License Upgrade” (the
serialnumbershouldbedifferent)
5. Clickon“CheckforLicenseUpgrade”
6. Ifanewlicenseisavailable,youwillseethefollowing:
14 Chapter2. Installationinstructions

TimeTaggerUserManual,Release2.17.4.0
7. Ifyouwanttoactivatethenewlicense,pleaseclick“FlashDevice”andwaituntiltheprocessiscomplete. You
willseethefollowingmessage:
2.3. Hardwarelicenseupgrades 15

TimeTaggerUserManual,Release2.17.4.0
| 16  | Chapter2. | Installationinstructions |
| --- | --------- | ------------------------ |

CHAPTER
THREE
TUTORIALS
3.1 Confocal Fluorescence Microscope
ThistutorialguidesyouthroughsettingupadataacquisitionforatypicalconfocalmicroscopecontrolledwithSwabian
Instruments’TimeTagger. Inthistutorial,wewilluseTimeTagger’sprogramminginterfacetodefinethedataacqui-
sition part of a scanning microscope. We will make no specific assumption of how the position scanning system is
implementedexceptthatithastoprovidesuitablesignalsdetailedinthetext.
Thebasicprincipleofconfocalmicroscopyisthatthelight,collectedfromasample,isspatiallyfilteredbyaconfocal
aperture,andonlyphotonsfromasinglespotofasamplecanreachthedetector. Comparedtoconventionalmicroscopy,
confocalmicroscopyoffersseveraladvantages,suchasincreasedimagecontrastandbetterdepthresolution,because
thepinholeeliminatesallout-of-focusphotons,includingstraylight.
Thefollowingdrawingshowsatypicalconfocalfluorescencemicroscopesetup.
Inthissetup,theobjectivefocusestheexcitationlightfromthelaseratthefluorescentsampleand,atthesametime,
collectstheresultingemission. Theemissionphotonspassthroughtheconfocalapertureandarriveatthesingle-photon
detector(SPD).Foreverydetectedphoton,theSPDproducesavoltagepulseatitsoutput,namelyaphotonpulse.
17

TimeTaggerUserManual,Release2.17.4.0
Imagefromarasterscan
Intheconfocalmicroscopy,thedetectionareaisasmalldiffraction-limitedspot. Therefore,torecordanimage,one
hastoscanthesamplesurfacepoint-by-pointandrecordthedetectorsignalateverylocation. Themajorityofscanning
microscopesemployarasterscanpaththatvisitseverypointonsamplestep-by-stepandline-by-line. Thefigurebelow
visualizesthetravelpathinatypicalrasterscan.
Inthefigureabove,thescanstartsfromthebottom-leftcornerandproceedshorizontallyinsteps. Ateachscanposition,
thescannerhastowaitforarbitraryintegrationtimetoallowsufficientphotoncollection. Thisprocessstopswhenthe
scannerreachesthetop-rightpoint.
Alongthescanpath,thepositionergeneratesapulseforeverynewsampleposition. Inthefollowingtext,wewillcall
thissignalapixelpulse.
Tomeasureaconfocalfluorescenceimage,thearrivaltimesofthefollowingthreesignalsmustberecorded: photon
pulses,laserpulses,andpixelpulses.
| 3.1.1 Time | Tagger configuration |     |     |     |     |
| ---------- | -------------------- | --- | --- | --- | --- |
TheTimeTaggerlibraryincludesseveralmeasurementclassesdesignedforconfocalmicroscopy.
Wewillstartbydefiningchannelnumbersandstoretheminvariablesforconvenience.
| PIXEL_START_CH | = 1 # Rising   | edge on input | 1   |     |     |
| -------------- | -------------- | ------------- | --- | --- | --- |
| PIXEL_END_CH   | = -1 # Falling | edge on input | 1   |     |     |
| LASER_CH =     | 2              |               |     |     |     |
| SPD_CH = 3     |                |               |     |     |     |
Nowlet’sconnecttotheTimeTagger.
| 18  |     |     |     | Chapter3. | Tutorials |
| --- | --- | --- | --- | --------- | --------- |

TimeTaggerUserManual,Release2.17.4.0
tt = createTimeTagger()
The Time Tagger hardware allows you to specify a trigger level voltage for each input channel. This trigger level,
alwaysappliesforboth,risingandfallingedgesofaninputpulse. Wheneverthesignallevelcrossesthistriggerlevel,
theTimeTaggerdetectsthisasaneventandstoresthetimestamp. Itisconvenienttosetthetriggerleveltohalfasignal
amplitude. Forexample,ifyourlasersyncoutputprovidespulsesof0.2Voltamplitude,wesetthetriggerlevelto0.1
| Vonthischannel. | Thedefaulttriggerlevelis0.5Volt. |     |     |
| --------------- | -------------------------------- | --- | --- |
tt.setTriggerLevel(PIXEL_START_CH, 0.5)
| tt.setTriggerLevel(LASER_CH, |     | 0.1) |     |
| ---------------------------- | --- | ---- | --- |
TheTimeTaggerallowsfordelaycompensationateachchannel. Suchdelaysareinevitablypresentineverymeasure-
mentsetupduetodifferentcablelengthsorinherentdelaysinthedetectorsandlasersyncsignals. Itisworthnoting
thatatypicalcoaxialcablehasasignalpropagationdelayofabout5ns/m.
Let’s suppose that we have to delay the laser pulse by 6.3 ns, if we want to align it close to the arrival time of the
fluorescencephotonpulse. UsingtheTimeTagger’sAPI(ApplicationProgrammingInterface),thiswilllooklike:
tt.setInputDelay(LASER_CH, 6300) # Delay is always specified in picoseconds
| tt.setInputDelay(SPD_CH, |     | 0) # Default value | is: 0 |
| ------------------------ | --- | ------------------ | ----- |
NowwearefinishedwithsettinguptheTimeTaggerhardwareandarereadytoproceedwithdefiningthemeasurements.
| 3.1.2 Intensity | scanning | microscope |     |
| --------------- | -------- | ---------- | --- |
Inthissection,westartfromaneasyexampleofonlycountingthenumberofphotonsperpixelandspendsometimeon
understandinghowtousethepixeltriggersignal. TheTimeTaggerlibrarycontainsthegenericCountBetweenMarkers
measurementthathasallthenecessaryfunctionalitytoimplementthedataacquisitionforascanningmicroscope.
FortheCountBetweenMarkersmeasurement,youhavetospecifyonwhichchannelsthephotonandthepixelpulses
arrive. Also,wehavetospecifythetotalnumberofpointsinthescan,whichisthenumberofpixelsinthefinalimage.
Furthermore,weassumethatthepixelpulseedgesindicatewhentostart,andwhentostopcountingphotonsandthe
pulsedurationdefinestheintegrationtime. Ifyourscanningsystemgeneratespixelpulsesofadifferentformat,takea
lookatthesectionAlternativepixeltriggerformats.
Asafirststep,wecreateameasurementobjectwithallthenecessaryparametersprovided.
| nx_pix = 300      |          |     |     |
| ----------------- | -------- | --- | --- |
| ny_pix = 200      |          |     |     |
| n_pixels = nx_pix | * ny_pix |     |     |
cbm = CountBetweenMarkers(tt, SPD_CH, PIXEL_START_CH, PIXEL_STOP_CH, n_pixels)
The measurement is now prepared and waiting for the signals to arrive. The next step is to send a command to the
piezo-positionertostartscanningandproducingthepixelpulsesforeachlocation.
scanner.scan(
| x0=0, dx=1e-5, | nx=nx_pix, |     |     |
| -------------- | ---------- | --- | --- |
| y0=0, dy=1e-5, | ny=ny_pix, |     |     |
)
Note: Thecodeaboveintroducesascanner objectwhichisnotpartoftheTimeTaggerlibrary. Itisanexampleofa
hypotheticalprogramminginterfaceforapiezo-scanner. Here,wealsoassumethatthiscallisnon-blocking,andthe
3.1. ConfocalFluorescenceMicroscope 19

TimeTaggerUserManual,Release2.17.4.0
scriptcancontinueimmediatelyafterstartingthescan.
Afterwestartedthescanner,theTimeTaggerreceivesthepixelpulses,countstheeventsateachpixel,andstoresthe
countinitsinternalbuffer. Onecanreadthebuffercontentperiodicallywithoutdisturbingtheacquisition,evenbefore
themeasurementiscompleted. Therefore,youcanseetheintermediateresultsandvisualizethescanprogress.
The resulting data from the CountBetweenMarkers measurement is a vector. We have to reorganize the elements of
thisvectoraccordingtothescanpathifwewanttodisplayitasanimage. Fortherasterscan,thisreorganizationcan
bedonebyasimplereshapingofthevectorintoa2Darray.
Thefollowingcodegivesyouanexampleofhowyoucanvisualizethescanprocess.
while scanner.isScanning():
| counts | = cbm.getData()      |         |         |     |     |
| ------ | -------------------- | ------- | ------- | --- | --- |
| img    | = np.reshape(counts, | nx_pix, | ny_pix) |     |     |
plt.imshow(img)
plt.pause(0.5)
| 3.1.3 Fluorescence | Lifetime | Microscope |     |     |     |
| ------------------ | -------- | ---------- | --- | --- | --- |
InthesectionIntensityscanningmicroscope,wecompletelydiscardedthetimeofarrivalforphotonandlaserpulses.
TheTimeTaggerallowsyoutorecordafluorescencedecayhistogramforeverypixeloftheconfocalimagebytaking
intoaccountthetimedifferencebetweenthearrivalofthephotonandlaserpulses. Thistaskcanbeachievedusing
theTimeDifferencesmeasurementfromtheTimeTaggerlibrary. Inthissubsection,wewillusetheTimeDifferences
measurement.
The TimeDifferences measurement calculates thetime differences between laserand photon pulses and accumulates
theminahistogramforeverypixel. Themeasurementclassconstructorrequiresimagingandtimingparameters, as
showninthefollowingcodesnippet.
| nx_pix = | 300 # Number          | of pixels  | along x-axis  |     |     |
| -------- | --------------------- | ---------- | ------------- | --- | --- |
| ny_pix = | 200 # Number          | of pixels  | along y-axis  |     |     |
| binwidth | = 50 # in picoseconds |            |               |     |     |
| n_bins = | 2000 # number         | of bins in | a histogram   |     |     |
| n_pixels | = nx_pix * ny_pix     | # number   | of histograms |     |     |
flim = TimeDifferences(
tt,
click_channel=SPD_CH,
start_channel=LASER_CH,
next_channel=PIXEL_START_CH,
binwidth=binwidth,
n_bins=n_bins,
n_histograms=n_pixels
)
Nowwestartthescannerandwaituntilthescaniscompleted. Duringthescan,wecanreadthecurrentdataanddisplay
itinrealtime.
while scanner.isScanning():
| counts | = flim.getData() |     |     |     |     |
| ------ | ---------------- | --- | --- | --- | --- |
img3D = np.reshape(counts, n_bins, nx_pix, ny_pix) # Fluorescence image cube
(continuesonnextpage)
| 20  |     |     |     | Chapter3. | Tutorials |
| --- | --- | --- | --- | --------- | --------- |

TimeTaggerUserManual,Release2.17.4.0
(continuedfrompreviouspage)
# User defined function that estimates fluorescence lifetime for every pixel
flimg = get_lifetime(img3D)
plt.imshow(flimg)
plt.pause(0.5)
3.1.4 Alternative pixel trigger formats
What if a piezo-scanner provides a different trigger signal compared to considered in the previous sections? In this
section,welookintoafewcommontypesoftriggersignalsandhowtoadaptourdataacquisitiontomakethemwork.
Pixelpulsewidthdefinestheintegrationtime
integration
time
pixel N pixel N+1 pixel N+2
time
Thecasewhenthepulsewidthdefinestheintegrationtimehasbeenconsideredintheprevioussubsections.
Pixelpulseindicatesthepixelstart
integration
time
pixel N pixel N+1 pixel N+2
time
When a pixel pulse has a duration different from the desired integration time, we must define the integration time
manually. Onewaywouldbetorecordalleventsuntilthenextpixelpulseandrelyonastrictlyfixedpixelpulseperiod.
Alternatively,wecancreateawell-definedtimewindowaftereachpixelpulse,sothemeasurementsystembecomes
insensitivetothevariationofthepixelpulseperiod.
OnecandefinethetimewindowusingtheDelayedChannel whichprovidesadelayedcopyoftheleadingedgefor
thepixelpulse.
integr_time = int(1e10) # Integration time of 10 ms in picoseconds
delayed_vch = DelayedChannel(tt, PIXEL_START_CH, integr_time)
PIXEL_END_CH = delayed_vch.getChannel()
cbm = CountBetweenMarkers(tt, SPD_CH, PIXEL_CH, PIXEL_END_CH, n_pixels)
3.1. ConfocalFluorescenceMicroscope 21

TimeTaggerUserManual,Release2.17.4.0
TheapproachwithusingDelayedChannelallowsforaconstantintegrationtimeperpixelevenifthepixelpulsesdo
notoccuratafixedperiod. Forinstance,inarasterscan,moretimeisrequiredtomovetothebeginningofthenext
line(fly-backtime)comparedtothepixeltime.
Warning: You have to make sure that pixel pulses do not appear before the end of the integration time for the
previouspixel.
FLIMwithnon-periodicpixeltrigger
integration
time
pixel N pixel N+1 pixel N+2
time
Insomecases,ascannergeneratesthepixelpulseswithnostrictlydefinedperiod. However,mostscanningmeasure-
mentsrequireconstantintegrationtimeforeverypixel. ComparedtoCountBetweenMarkers,theTimeDifferences
measurementdonothaveaPIXEL_ENDmarkerandaccumulatethehistogramforeverypixeluntilthenextpixelpulse
isreceived. Ifthisbehaviorisundesired,orifyourpixelpulsesarenotperiodic,youwillneedtogateyourdetectorto
guaranteeaconstantintegrationtime.
The Time Tagger library provides you with the necessary tools to enforce a fixed integration time when using the
TimeDifferencesmeasurement. GatingthedetectoreventscanbedonewiththeGatedChannel. Theexamplecode
isprovidedbelow.
integr_time = int(1e10) # Integration time of 10 ms in picoseconds
delayed_vch = DelayedChannel(tt, PIXEL_START_CH, integr_time)
PIXEL_END_CH = delayed_vch.getChannel()
gated_vch = GatedChannel(tt, SPD_CH, PIXEL_START_CH, PIXEL_END_CH)
GATED_SPD_CH = gated_vch.getChannel()
flim = TimeDifferences(tt,
click_channel=GATED_SPD_CH,
start_channel=LASER_CH,
next_channel=PIXEL_START_CH,
binwidth=binwidth,
n_bins=n_bins,
n_histograms=n_pixels
)
22 Chapter3. Tutorials

TimeTaggerUserManual,Release2.17.4.0
Linepulsebutnopixelpulses
integration
time
|     |     | pixel N |     | pixel N+1 |     | pixel N+2 |
| --- | --- | ------- | --- | --------- | --- | --------- |
time
When a scanning system only has the line-start signal and does not provide the pixel pulses, we have to define time
intervals for each pixel by other means. The pixel markers can be easily generated with EventGenerator virtual
channelwhichgenerateseventsattimesrelativetothetriggerevent. Furthermore,theEventGenerator allowsyou
togeneratenotonlypixelmarkersthatareequallyspacedbutalsopixelsthatarespacednon-uniformlyorhavetime
varying integration times. For instance, you will find the EventGenerator particularly powerful, if you work with
resonantgalvo-scannersandneedtocorrectintegrationtimeandpixelspacingaccordingtothespeedprofileofyour
scanner. TheexamplebelowshowshowtoapplyEventGeneratorforgenerationofpixelmarkers.
| nx_pix = | 300 |     | # Number | of pixels       | along | x-axis       |
| -------- | --- | --- | -------- | --------------- | ----- | ------------ |
| ny_pix = | 200 |     | # Number | of pixels/lines |       | along y-axis |
integr_time = int(3e9) # Integration time of 3 ms in picoseconds
line_duration = 1e12 # Duration of the line scan in picoseconds
| binwidth      | = 50        |          | # in picoseconds |               |        |           |
| ------------- | ----------- | -------- | ---------------- | ------------- | ------ | --------- |
| n_bins =      | 2000        |          | # number         | of bins       | in a   | histogram |
| n_pixels      | = nx_pix    | * ny_pix | # number         | of histograms |        |           |
| LINE_START_CH | =           | 3        |                  |               |        |           |
| # Pixels      | are equally | spaced   | in time          | (constant     | speed) |           |
pixel_start_times = numpy.linspace(0, line_duration, nx_pix, dtype='int64')
| # Pixel          | integration    | time                | is constant |               |     |     |
| ---------------- | -------------- | ------------------- | ----------- | ------------- | --- | --- |
| pixel_stop_times |                | = pixel_start_times |             | + integr_time |     |     |
| # Create         | EventGenerator | channels            |             |               |     |     |
pixel_start_vch = EventGenerator(tt, LINE_START_CH, pixel_start_times.tolist())
pixel_stop_vch = EventGenerator(tt, LINE_START_CH, pixel_stop_times.tolist())
| PIXEL_START_CH     | =                             | pixel_start_vch.getChannel() |              |     |     |     |
| ------------------ | ----------------------------- | ---------------------------- | ------------ | --- | --- | --- |
| PIXEL_END_CH       | = pixel_stop_vch.getChannel() |                              |              |     |     |     |
| # Use GatedChannel |                               | to gate                      | the detector |     |     |     |
gated_vch = GatedChannel(tt, SPD_CH, PIXEL_START_CH, PIXEL_END_CH)
| GATED_SPD_CH | = gated_vch.getChannel() |     |     |     |     |     |
| ------------ | ------------------------ | --- | --- | --- | --- | --- |
flim = TimeDifferences(
tt,
click_channel=GATED_SPD_CH,
start_channel=LASER_CH,
next_channel=PIXEL_START_CH,
binwidth=binwidth,
n_bins=n_bins,
(continuesonnextpage)
3.1. ConfocalFluorescenceMicroscope 23

TimeTaggerUserManual,Release2.17.4.0
(continuedfrompreviouspage)
n_histograms=n_pixels
)
Note: IntheTimeTaggersoftwarev2.7.2wehavecompletelyredesignedFlimmeasurement. Itsupporteasyinterface
similartoTimeDifferences,aswellashigh-performanceframestreaminginterfacethatallowsforreal-timevideo-
rateFLIMimaging.
3.2 Optically Detected Magnetic Resonance
OpticallyDetectedMagneticResonance(ODMR)isaspectroscopictechniqueusedtostudyelectronspinsinmaterials.
Itinvolvesapplyingsequencesofopticalandmicrowavepulsestomanipulateandprobethespinstatesofelectrons. By
analyzingtheresponseofthematerial’sphotoluminescencetothesepulses,valuableinformationaboutthespinproper-
tiesanddynamicscanbeobtained. Thistechniqueisparticularlyusefulforstudyingspin-basedquantumtechnologies
andmaterialssuchasdiamondNVcenters.
This tutorial shows how to set up a pulsed ODMR experiment using our Time Taggers and Pulse Streamer. Pulsed
ODMRoffersdistinctadvantagesovercontinuousmode,includingenhancedcontrastandreducedsensitivitytolaser
powerfluctuations. LeveragingTimeTaggersprovidesprecisetimingcontrolforaccuratedataacquisitionandanalysis,
makingitidealforprobingfastspindynamicswithhighresolution.
Laser
s
e
c
n
e
u
q
e
S
Data
24 Chapter3. Tutorials

TimeTaggerUserManual,Release2.17.4.0
| 3.2.1 Creation | of optical | and microwave |     | pulse | patterns |     |     |     |
| -------------- | ---------- | ------------- | --- | ----- | -------- | --- | --- | --- |
Inthistutorialweconsideraspin-1system. Inmostsequences,aninitialopticalpulseservestoinitializethesystem,
e.g.,preparingitinstate|𝑚 =0⟩. Followingthisinitialization,aseriesofmicrowave(MW)pulsesandfreeevolution
𝑠
periodsmanipulatethespinstate. Finally,asecondopticalpulseinterrogatesthespinstateprojectionalongthe(|𝑚 =
𝑠
0⟩,|𝑚 =+1⟩)basis,oftenviaopticalemissionorabsorptionintensity,whilealsoresettingthesystemforsubsequent
𝑠
measurements. Variouspulsesequencesarecommonlyemployedfordifferentmeasurements:
1. Inthissequence,asingleMWpulseofvariabledurationisapplied,causingthespin
RabiOscillationSequence:
tooscillatebetweenthe|𝑚 =0⟩and|𝑚 =+1⟩states. TheamplitudeoftheRabioscillationsprovidesinformation
𝑠 𝑠
about the energy splitting between the two states. From this measurement the duration of 𝜋- and 𝜋/2-pulses can be
inferredashalfandquarterperiodsoftheoscillations,respectively.
2. This sequence involves two 𝜋/2 MW pulses separated by a variable delay. The delay time
| Ramsey | Sequence: |     |     |     |     |     |     |     |
| ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
determinesthephaserelationshipbetweenthetwopulses,affectingtheinterferencepatternobservedinthespinstate.
AnalysisoftheRamseyfringesallowsforprecisemeasurementofthespincoherencetime𝑇*.
2
3. HahnEchoSequence: Inthissequence,a𝜋/2-pulseisfollowedbyadelaytimeandthena𝜋-pulse. Thesecond
pulse flips the spin state, and the delay allows for dephasing to occur. The echo signal observed after the 𝜋/2-pulse
| providesinformationaboutthespindephasingtime𝑇 |     |     | .   |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
2
|      | Rabi Oscillations |       | Ramsey Oscillations |     |     |     | Hahn Echo Oscillations |     |
| ---- | ----------------- | ----- | ------------------- | --- | --- | --- | ---------------------- | --- |
|      | LASER             | MW    |                     |     |     |     |                        |     |
|      |                   |       |                     | 2 2 |     |     | 2                      | 2   |
| 1.00 |                   | 1.000 |                     |     |     | 1   |                        |     |
).nu .bra( ytisnetnI
0.999
0.99
0
| 0.0 | 0.5   | 1.0 0.0 |     | 0.5   | 1.0 | 0   | 50      | 100 |
| --- | ----- | ------- | --- | ----- | --- | --- | ------- | --- |
|     |  ( s) |         |     |  ( s) |     |     | 2  ( s) |     |
Tocreateanyofthesesequences,wemakeuseoftheSequenceclassofourPulseStreamer8/2. Thisclassallowsto
independentlysetpulsepatternsoneachchannel. Apulsepatternisrepresentedbyatupleintheform(duration,level).
Thedurationisalwaysspecifiedinnanosecondsandtheleveliseither0or1fordigitaloutput.
Firstofall,weconnecttothePulseStreamer.
# Change the following line to use your specific Pulse Streamer IP address
ip_hostname='169.254.8.2'
| pulser | = PulseStreamer(ip_hostname) |     |     |     |     |     |     |     |
| ------ | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
Next,wedeclarethechannelsnames,andalltherelevantparametersforcreatingasequencetomeasureRabiOscilla-
tionsandquantifyingthedurationofa𝜋-pulse. Toachievethis,weneedtocreatethefollowingpatterns:
1. Apatterntodrivethelaser,enablingittoemitopticalpulsesforsysteminitializationandreadout.
2. Apatterntodriveahighisolationmicrowaveswitchforgatingthemicrowavepulses.
3. Apatternforsynchronizationpurposes.
4. Apatterntomeasuretheincomingphotonsduringthereadoutpulsefortime-gatedanalysis.
| 3.2. OpticallyDetectedMagneticResonance |     |     |     |     |     |     |     | 25  |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |

TimeTaggerUserManual,Release2.17.4.0
| # Channel  | names  |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| optical_ch |        | = 0 |     |     |     |     |     |     |     |     |
| mw_ch      | = 1    |     |     |     |     |     |     |     |     |     |
| sync_ch    | = 2    |     |     |     |     |     |     |     |     |     |
| gate_ch    | = 3    |     |     |     |     |     |     |     |     |     |
| # Digital  | levels |     |     |     |     |     |     |     |     |     |
HIGH=1
LOW=0
| # Change          | the    | values   | according |         | to your           | experiment |         |                |     |     |
| ----------------- | ------ | -------- | --------- | ------- | ----------------- | ---------- | ------- | -------------- | --- | --- |
| period            | = 8000 | # period | of        | each    | pattern           |            |         |                |     |     |
| init_pulse_dur    |        | = 2000   | #         | width   | of initialization |            |         | optical pulses |     |     |
| readout_pulse_dur |        | =        | 300       | # width | of readout        |            | optical | pulses         |     |     |
pause = 1000 # time between a readout and next initializazion pulse
We define then a set of values over which the MW pulse duration (𝜏) is swept, to ultimately build the desired pulse
patterns.
| tau = np.arange(100, |     |     | 2000, | 100) |     |     |     |     |     |     |
| -------------------- | --- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- |
# For each selected MW pulse width, the experiment is repeated multiple times
| n_loops   | = 1000  |     |     |     |     |     |     |     |     |     |
| --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # Optical | pattern |     |     |     |     |     |     |     |     |     |
optical_patt = [(init_pulse_dur, HIGH), (period-init_pulse_dur-readout_pulse_dur-pause,␣
LOW),
˓→
|     |     | (readout_pulse_dur, |     |     |     | HIGH), | (pause, | LOW)]*n_loops*len(tau) |     |     |
| --- | --- | ------------------- | --- | --- | --- | ------ | ------- | ---------------------- | --- | --- |
# MW pattern
| # Initialize |         | the MW | pulse | pattern |     |     |     |     |     |     |
| ------------ | ------- | ------ | ----- | ------- | --- | --- | --- | --- | --- | --- |
| mw_patt      | = []    |        |       |         |     |     |     |     |     |     |
| for ti       | in tau: |        |       |         |     |     |     |     |     |     |
mw_patt.extend([(init_pulse_dur, LOW), (ti, HIGH), (period-init_pulse_dur-ti,␣
LOW)]*n_loops)
˓→
| # Pulse   | pattern | that         | marks | a                   | new value | of  | a MW pulse     | duration |     |     |
| --------- | ------- | ------------ | ----- | ------------------- | --------- | --- | -------------- | -------- | --- | --- |
| sync_patt | =       | [(10, HIGH), |       | (period*n_loops-10, |           |     | LOW)]*len(tau) |          |     |     |
# Add last sync pulse to the pattern to mark the end of the acquisition
| sync_patt.extend([(10, |     |        | HIGH)])  |     |        |     |     |     |     |     |
| ---------------------- | --- | ------ | -------- | --- | ------ | --- | --- | --- | --- | --- |
| # Pattern              | for | gating | detector |     | clicks |     |     |     |     |     |
gate_patt = [(period-readout_pulse_dur-pause, LOW), (readout_pulse_dur,HIGH),
|                |     | (pause, | LOW)]*n_loops*len(tau) |          |     |     |     |     |     |     |
| -------------- | --- | ------- | ---------------------- | -------- | --- | --- | --- | --- | --- | --- |
| # Set channels |     | using   | class                  | Sequence |     |     |     |     |     |     |
seq = Sequence()
| seq.setDigital(optical_ch, |      |          |          | optical_patt) |     |     |     |     |     |     |
| -------------------------- | ---- | -------- | -------- | ------------- | --- | --- | --- | --- | --- | --- |
| seq.setDigital(mw_ch,      |      |          | mw_patt) |               |     |     |     |     |     |     |
| seq.setDigital(sync_ch,    |      |          |          | sync_patt)    |     |     |     |     |     |     |
| seq.setDigital(gate_ch,    |      |          |          | gate_patt)    |     |     |     |     |     |     |
| # Display                  | your | sequence |          |               |     |     |     |     |     |     |
(continuesonnextpage)
| 26  |     |     |     |     |     |     |     |     | Chapter3. | Tutorials |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- |

TimeTaggerUserManual,Release2.17.4.0
(continuedfrompreviouspage)
seq.plot()
| 3.2.2 Signal | generation | and detection |     |     |
| ------------ | ---------- | ------------- | --- | --- |
ToperformODMRmeasurements,weconnecttheTimeTaggeranddeclarethechannelsused. Here,wecanalsoadjust
thehardwaresettingsforeachchannel.
| tagger = createTimeTagger() |     |     |     |     |
| --------------------------- | --- | --- | --- | --- |
gate = 1
sync = 2
| detector = | 3   |     |     |     |
| ---------- | --- | --- | --- | --- |
Then,weneedtofiltertheincomingdetectorclicksrevealedbytheTimeTaggeraccordingtothegeneratedgatepattern.
ThiscanbedoneatthesoftwarelevelbyemployingthevirtualchannelGatedChannel. Therisingandfallingedgesof
thegatesignalareusedtoopenandcloseeachtimegate,respectively.
| gated_detector_vch | = GatedChannel(tagger, |     | detector, | gate, -gate) |
| ------------------ | ---------------------- | --- | --------- | ------------ |
# Get the channel number that will be used in the CBM measurement
| gated_detector | = gated_detector_vch.getChannel() |     |     |     |
| -------------- | --------------------------------- | --- | --- | --- |
Next,wesetupaCountBetweenMarkersmeasurementtocountthefilteredeventsonadetectorchannelbetweensync
events,thatheraldthechangeoftheMWpulsewidth. Thecountsareaccumulatedinanarraywhosenumberofbins
| isequaltothenumberof𝜏 | values. |     |     |     |
| --------------------- | ------- | --- | --- | --- |
cbm = CountBetweenMarkers(tagger, gated_detector, sync, CHANNEL_UNUSED, len(tau))
cbm.start()
tagger.sync()
Nowthatthemeasurementissetup,thesequencecanberunbythePulseStreamerandtheeventscountedbytheTime
Tagger. Werunthesequenceonce
| n_runs = 1                 |         |        |     |     |
| -------------------------- | ------- | ------ | --- | --- |
| final = OutputState.ZERO() |         |        |     |     |
| pulser.stream(seq,         | n_runs, | final) |     |     |
andwecollectthedata
| ready = False |     |     |     |     |
| ------------- | --- | --- | --- | --- |
# Periodically get data until the CountBetweenMarkers completes the acquisition
| while ready | is False: |     |     |     |
| ----------- | --------- | --- | --- | --- |
time.sleep(.2)
| # Check | if the measurement | is ready      |           |     |
| ------- | ------------------ | ------------- | --------- | --- |
| ready   | = cbm.ready()      |               |           |     |
| counts  | = cbm.getData()    |               |           |     |
| # You   | may add progress   | visualization | code here |     |
3.2. OpticallyDetectedMagneticResonance 27

TimeTaggerUserManual,Release2.17.4.0
| 3.2.3 | Sweeping | modes |     |     |     |     |     |     |     |
| ----- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
There are different ways to acquire and accumulate data in these pulsed ODMR experiments. We report here two
protocolstocollecteventstovisualizeRamseyoscillations.
Inthefirstmethod,theinterpulsedelay𝜏 issweptandthedataarecollectedinasingleacquisitionstepafterexecuting
thewholesequence. Theexamplecodeisanalogoustotheoneofthepreviousparagraph,exceptfortheconstruction
oftheRamseysequence.
dur_pi = 200 # Change value according to the outcome of Rabi measurement
| tau = np.arange(100, |         |     | 1500, 100) | # Interpulse | time | delay |     |     |     |
| -------------------- | ------- | --- | ---------- | ------------ | ---- | ----- | --- | --- | --- |
| mw_patt              | = []    |     |            |              |      |       |     |     |     |
| for ti               | in tau: |     |            |              |      |       |     |     |     |
mw_patt.extend([(init_pulse_dur, LOW), (dur_pi/2, HIGH), (ti, LOW),
(dur_pi/2, HIGH), (period-ti-dur_pi-init_pulse_dur, LOW)]*n_loops)
Inthesecondapproach,werepeatthesequenceforthesameinterpulsedelaymultipletimes,asusual,andaccumulate
thedatabeforechangingtheinterpulsedelay.
#The optical, the sync and gate patterns do not depend on the interpulse delay
optical_patt = [(init_pulse_dur, HIGH), (period-init_pulse_dur-readout_pulse_dur-pause,␣
LOW),
˓→
|                        |         | (readout_pulse_dur, |                     | HIGH), | (pause, | LOW)]*n_loops |     |     |     |
| ---------------------- | ------- | ------------------- | ------------------- | ------ | ------- | ------------- | --- | --- | --- |
| sync_patt              | = [(10, | HIGH),              | (period*n_loops-10, |        | LOW)]   |               |     |     |     |
| sync_patt.extend([(10, |         |                     | HIGH)])             |        |         |               |     |     |     |
gate_patt = [(period-readout_pulse_dur-pause, LOW), (readout_pulse_dur,HIGH), (pause,␣
LOW)]*n_loops
˓→
seq = Sequence()
| seq.setDigital(optical_ch, |            |      | optical_patt) |                 |          |         |     |     |     |
| -------------------------- | ---------- | ---- | ------------- | --------------- | -------- | ------- | --- | --- | --- |
| seq.setDigital(sync_ch,    |            |      | sync_patt)    |                 |          |         |     |     |     |
| seq.setDigital(gate_ch,    |            |      | gate_patt)    |                 |          |         |     |     |     |
| counts                     | = []       |      |               |                 |          |         |     |     |     |
| # For each                 | interpulse |      | delay,        | events on the   | detector | channel |     |     |     |
| # between                  | two        | sync | marker events | are accumulated |          |         |     |     |     |
cbm = CountBetweenMarkers(tagger, gated_detector, sync, CHANNEL_UNUSED, 1)
tagger.sync()
| mw_patt | = []    |                    |     |                  |     |             |       |     |     |
| ------- | ------- | ------------------ | --- | ---------------- | --- | ----------- | ----- | --- | --- |
| for ti  | in tau: |                    |     |                  |     |             |       |     |     |
| mw_patt | =       | [ (init_pulse_dur, |     | LOW), (dur_pi/2, |     | HIGH), (ti, | LOW), |     |     |
(dur_pi/2, HIGH), (period-ti-dur_pi-init_pulse_dur, LOW)]*n_loops
| seq.setDigital(mw_ch, |     |     | mw_patt) |     |     |     |     |     |     |
| --------------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
cbm.start()
| # Run              | the | sequence |         |        |     |     |     |     |     |
| ------------------ | --- | -------- | ------- | ------ | --- | --- | --- | --- | --- |
| pulser.stream(seq, |     |          | n_runs, | final) |     |     |     |     |     |
(continuesonnextpage)
| 28  |     |     |     |     |     |     |     | Chapter3. | Tutorials |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- |

TimeTaggerUserManual,Release2.17.4.0
(continuedfrompreviouspage)
| ready = False |             |     |     |     |
| ------------- | ----------- | --- | --- | --- |
| # Get data    | every while |     |     |     |
| while ready   | is False:   |     |     |     |
time.sleep(.2)
ready = cbm.ready()
data = cbm.getData()
| # Store the | total counts | for each interpulse | delay | into an array |
| ----------- | ------------ | ------------------- | ----- | ------------- |
counts.append(data)
| 3.2.4 ODMR | contrast |     |     |     |
| ---------- | -------- | --- | --- | --- |
QuantifyingtheODMRcontrast,definedasthedifferentialphotoluminescencesignalbetweenmeasurementswithand
withoutapplyingmicrowaveradiation,iscrucialforseveralreasons. Itservesasadirectindicatoroftheefficiencyof
spin manipulation and the sensitivity of the measurement setup. High contrast values typically correspond to better
signal-to-noiseratios,enablingmoreprecisedeterminationofresonancefrequenciesandspinrelaxationtimes.
Theschematicsofthismeasurementisreportedinthefigurebelow. Thistrivialsequenceisrepatedforeachdifferent
microwavefrequencyselected,toobtainintheendanODMRspectrum.
Laser
Microwave
|     | PL    |     |     | PL   |
| --- | ----- | --- | --- | ---- |
|     | MWoff |     |     | MWon |
Detector
Gate
Forthedataacquisitions,therearetwopossibleimplementations:
1. AsingleCountBetweenMarkersmeasurement: therisingandfallingedgesofthegateareusedasbegin_channel
andend_channel, respectively, and2Nasn_values, whereNisthenumberoffrequenciestomeasure. Intheoutput
array,onegets,foreachfrequency,thecountswhiletheMWisoffintheevenbins(0,2,4,6,...) andthecountswhile
theMWisonintheoddbins(1,3,5,7,...).
| cbm = CountBetweenMarkers(tagger, |     | detector, | gate, -gate, | 2N) |
| --------------------------------- | --- | --------- | ------------ | --- |
2. Two different CountBetweenMarkers measurements: one collects counts when the MW frequency is on and
onewhentheMWfrequencyisoff. InthiscaseMWindicatorpulsesareneededasmarkers. ForthefirstCountBe-
3.2. OpticallyDetectedMagneticResonance 29

TimeTaggerUserManual,Release2.17.4.0
tweenMarkerstherisingandthefallingedgesoftheMWindicatorpulseareusedasbegin_channelandend_channel,
respectively. Onthecontrary, forthesecondmeasurementthefallingedgeoftheMWindicatorpulseisusedasbe-
gin_channel and the rising edge as end_channel. The gate signal should be used to filter the detector clicks at the
softwarelevelusingthethevirtualchannelGatedChannel, asdescribedinthepreviousparagraph. Thisensuresthe
sameacquisitiontime,foreachfrequency,whenthemicrowaveofandwhenitisoff.
| mw_ind = 4 |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- |
# Create a SynchronizedMeasurements instance that allows you to process the same tags
| synchronized      | = SynchronizedMeasurements(tagger) |        |       |     |     |
| ----------------- | ---------------------------------- | ------ | ----- | --- | --- |
| sync_tagger_proxy | = synchronized.getTagger()         |        |       |     |     |
| # Accumulate      | counts when                        | the MW | is on |     |     |
cbm_mw_on = CountBetweenMarkers(sync_tagger_proxy, gated_detector, mw_ind, -mw_ind, N)
| # Accumulate | counts when | the MW | is off |     |     |
| ------------ | ----------- | ------ | ------ | --- | --- |
cbm_mw_off = CountBetweenMarkers(sync_tagger_proxy, gated_detector, -mw_ind, mw_ind, N)
| 3.3 Measuring | Coincidences |     |     |     |     |
| ------------- | ------------ | --- | --- | --- | --- |
Quantuminterferenceliesattheheartofphoton-basedtechnologies,suchasphotonicquantumcomputing,quantum
metrology, and quantum networks. One of the key requirements for high-fidelity operations in these technologies is
the indistinguishability of photons, a key property of quantum states. The level of indistinguishability between two
photonsistypicallydeterminedbymeasuringtheHong–Ou–Mandel(HOM)interferencevisibility: ifthephotonsare
identical and enter separately a balanced beam splitter, they will always exit the beam splitter together in the same
output mode. If a detector is set up on each of the outputs, then the photons cannot be separately detected by the
twodetectorssimultaneously. Thus,coincidencemeasurementsenablethedetectionandanalysisofcorrelatedevents,
notably the simultaneous detection of entangled photons. When more than two photons are involved in a multipho-
ton quantum interference experiment, the interference capability extends beyond the pairwise distinguishability, and
generalizationsoftheHOMeffecttothemany-particlecasehavebeenrecentlyproposed. Onemethodtoquantifythe
n-photonindistinguishabilityreliesonacyclicmultiportinterferometerwithN=2nopticalmodes,composedof2n
beamsplittersplacedalongtwocascadedlayers. Thequantuminterferencepattern,resultingfromtheinjectionofn
indistinguishablephotonsintothe2nports-interferometerandobtainedthroughamultiphotoncoincidencedetection,
isadirectmeasurementofthen-photonindistinguishability.
| 30  |     |     |     | Chapter3. | Tutorials |
| --- | --- | --- | --- | --------- | --------- |

TimeTaggerUserManual,Release2.17.4.0
This tutorial shows how to set up a measurement to count coincidence events between groups of input channels. In
ourexample,wecountfourth-ordercoincidencesbetweenfourphotonsinjectedintoanintegratedeight-modecyclic
interferometer.
3.3.1 Time Tagger configuration
Toperformourcoincidence-countingexperiment,wefirstconnecttheTimeTaggerandselectthechannelsused.
tagger = createTimeTagger()
input_channels = tagger.getChannelList(ChannelEdge.Rising)[:8]
TheTimeTaggerhardwareallowsyoutospecifyatriggerlevelvoltageforeachinputchannel. Thedefaulttriggerlevel
is0.5V.Inourexample,wesetthetriggerlevelto0.3Vforallthechannels.
for ch in input_channels:
tagger.setTriggerLevel(ch, 0.3)
3.3. MeasuringCoincidences 31

TimeTaggerUserManual,Release2.17.4.0
3.3.2 Coincidence-counting
Ourprotocolforcountingcoincidenceeventsisschematicallyillustratedinthefigurebelow. Forclearvisualization,
thediagramconsiderscoincidencesfortwogroupsofthreechannelsamongfourinputchannelsused. First,wedefine
atimewindowasthelargesttimedifferencebetweeneventsontheinputchannelstobeconsideredasacoincidence
(sizeofrectangularshadedcoloredareas). Next, wegeneratenewstreamsoftags, whichcorrespondtocoincidence
eventsoccurringforeachgroupofinputchannels(Coincidence[1,2,3]andCoincidence[2,3,4]). Finally,wecount
theeventsoneachchannel(bottompanel).
Stream of time-tags (coincidence window = 8 ps)
channel 1
channel 2
channel 3
channel 4
Coincidence
[1, 2, 3]
Coincidence
[2, 3, 4]
|     | 0   | 10 20 | 30 40 | 50 60 | 70  | 80  |
| --- | --- | ----- | ----- | ----- | --- | --- |
Time (ps)
Counter (binwidth = 20 ps, # bins = 4)
| channel 1 |     | 0   | 1   | 2   | 2   |     |
| --------- | --- | --- | --- | --- | --- | --- |
| channel 2 |     | 2   | 2   | 2   | 2   |     |
| channel 3 |     | 1   | 1   | 2   | 2   |     |
| channel 4 |     | 2   | 1   | 1   | 2   |     |
| [1, 2, 3] |     | 0   | 1   | 2   | 2   |     |
| [2, 3, 4] |     | 1   | 1   | 1   | 2   |     |
|           | 0   | 20  | 40  | 60  |     | 80  |
Time (ps)
Our method can be implemented by creating the virtual channel Coincidences, which detects coincidence clicks on
multiple channel groups within the given coincidenceWindow. In this regard, it is good to remember that this is a
software-defined channel; therefore, it receives time-tags from the physical input channels and generates a new data
streaminthePC.TheTimeTaggerdoesnotdetectcoincidencesonboardthehardware.
Inourexample,weconsiderfourth-ordercoincidenceeventsfromeightinputchannels.
| 32  |     |     |     |     | Chapter3. | Tutorials |
| --- | --- | --- | --- | --- | --------- | --------- |

TimeTaggerUserManual,Release2.17.4.0
| order  | = 4                                           |     |     |     |        |     |     |
| ------ | --------------------------------------------- | --- | --- | --- | ------ | --- | --- |
| groups | = list(itertools.combinations(input_channels, |     |     |     | order) |     |     |
coincidences_vchannels = Coincidences(tagger, groups, coincidenceWindow=100)
Finally,thephysicalinputchannelsandtheCoincidencesvirtualchannelarefedintotheCountermeasurementclass.
| #Generate | a list | including | input and | virtual | channels |     |     |
| --------- | ------ | --------- | --------- | ------- | -------- | --- | --- |
channels = [*input_channels, *coincidences_vchannels.getChannels()]
| counting            | = Counter(tagger, |         | channels, | 1e10, 300) |     |     |     |
| ------------------- | ----------------- | ------- | --------- | ---------- | --- | --- | --- |
| measurementDuration |                   | = 10e12 | # 10 s    |            |     |     |     |
counting.startFor(measurementDuration)
counting.waitUntilFinished()
| index  | = counting.getIndex() |     |             |           |     |     |     |
| ------ | --------------------- | --- | ----------- | --------- | --- | --- | --- |
| counts | = counting.getData()  |     |             |           |     |     |     |
| 3.3.3  | Delay adjustment      | for | coincidence | detection |     |     |     |
Whendetectingcoincidenceevents,itisessentialtohavesignalsalignedintime. Delaysbetweenchannelsinevitably
arisefromexperimentalconditions,suchasdifferentopticalpathsorcablelengths,andinherentdelaysinthedetectors.
SuchdelayscanbecompensatedintheTimeTaggerbyprovidingaproperinputdelay.
|     |            | Before delay adjustment |     |           | After delay adjustment |           |           |
| --- | ---------- | ----------------------- | --- | --------- | ---------------------- | --------- | --------- |
|     | Channe l 1 |                         |     | 0 me (ps) | Channe l 1             |           | 0 me (ps) |
|     | C hannel   |  2                      |     |           | C hannel  2            |           |           |
|     |            | C hannel 3              |     |           | C hannel 3             |           |           |
|     |            | Channel 4               |     | T i       |                        | Channel 4 | T i       |
If the signals are sufficiently correlated, the best way to quantify the time misalignment between the channels is to
performmultipleCorrelationmeasurements. ThepeakoftheCorrelationcurvebetweentwochannelsiscenteredat
therelativedelay. Thisvalueisemployedaposterioritocompensatethetimemisalignmentbetweenthetwochannels.
Inourexample,wekeepthefirstchannelasareferenceandalternativelymeasuretheCorrelationbetweenitandall
| theothers. | Finally,wealignallthesignalsintime,usingsetInputDelay()method. |     |     |     |     |     |     |
| ---------- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
3.3. MeasuringCoincidences 33

TimeTaggerUserManual,Release2.17.4.0
# Set input delays to 0, otherwise the compensation result will be incorrect.
| for ch in                | input_channels: |     |     |     |     |     |
| ------------------------ | --------------- | --- | --- | --- | --- | --- |
| tagger.setInputDelay(ch, |                 | 0)  |     |     |     |     |
# Create SynchronizedMeasurements to operate on the same time tags.
sm = SynchronizedMeasurements(tagger)
| #Create   | Correlation         | measurements |     |     |     |     |
| --------- | ------------------- | ------------ | --- | --- | --- | --- |
| corr_list | = list()            |              |     |     |     |     |
| for ch in | input_channels[1:]: |              |     |     |     |     |
corr_list.append(
Correlation(sm.getTagger(), input_channels[0], ch, binwidth=1, n_bins=5000)
)
| # Start                | measurements | and accumulate | data for | 1 second |     |     |
| ---------------------- | ------------ | -------------- | -------- | -------- | --- | --- |
| sm.startFor(int(1e12), |              | clear=True)    |          |          |     |     |
sm.waitUntilFinished()
| # Determine | delays            |     |     |     |     |     |
| ----------- | ----------------- | --- | --- | --- | --- | --- |
| delays =    | list()            |     |     |     |     |     |
| for corr    | in corr_list:     |     |     |     |     |     |
| hist_t      | = corr.getIndex() |     |     |     |     |     |
| hist_c      | = corr.getData()  |     |     |     |     |     |
#Identify the delay as the center of the histogram through a weighted average
| dt = | np.sum(hist_t | * hist_c) | / np.sum(hist_c) |     |     |     |
| ---- | ------------- | --------- | ---------------- | --- | --- | --- |
delays.append(int(dt))
| print("Delays:",         | delays)                       |          |             |     |     |     |
| ------------------------ | ----------------------------- | -------- | ----------- | --- | --- | --- |
| # Compensate             | the delays                    | to align | the signals |     |     |     |
| for ch,                  | dt in zip(input_channels[1:], |          | delays):    |     |     |     |
| tagger.setInputDelay(ch, |                               | dt)      |             |     |     |     |
YoucancheckthatthedelaysareproperlycompensatedbyrepeatingtheCorrelationmeasurementsandverifyingthat
thehistogramsarecenteredatzero.
3.3.4 Exclusive coincidences using Combinations virtual channel
The indistinguishability of the input photons in a quantum interferometry experiment results in a large number of
forbidden output configurations, among the possible many-particle states. This can be viewed as the generalization
of the original two-photon HOM effect extended to the case of multiple ports and photons. In this regard, it turns
outtobebeneficialtoconsidercoincidencemeasurementswithspecificrestrictions. Forinstance, excludingcertain
coincidencesbasedontheoccurrenceofeventshappeningrightbeforeorafterthemcanbeimportante.g.,toeliminate
theeffectofbackgroundnoise,henceforrefiningquantumstatetomographyorinterferencestudies.
ThebestapproachtoachievethisgoalistoemploythevirtualchannelCombinations. Itdetectscoincidenceclickson
allpossible(2𝑁−1)channelsubgroupsfromagivennumber(N)ofchannels,whennoadditionaleventsoccurwithin
twoguardwindows,oneprecedingthefirsteventstartingthecoincidence,theotherfollowingthelasteventconcluding
thecoincidence. WereportbelowarepresentativesketchofCombinationsvirtualchannelgiventhreeinputchannels.
Itshouldbenotedthatthecombinationofeventsonchannels1,2,3resultsinthegenerationofatimestampexclusively
onthevirtualchannelVCH andnotonVCH orVCH . Thisdistinction,however,doesnotapplytothevirtual
|     |     | {1,2,3} | {1,3} | {2} |     |     |
| --- | --- | ------- | ----- | --- | --- | --- |
channelCoincidences,asthecoincidencesbetweenchannels1,2,and3constituteasubsetofcoincidencesbetween
| 34  |     |     |     |     | Chapter3. | Tutorials |
| --- | --- | --- | --- | --- | --------- | --------- |

TimeTaggerUserManual,Release2.17.4.0
CH1
CH2
CH3
VCH{1,2,3}
VCH{1,3}
VCH{2}
This is not a combination
Guard
because the click on CH3
window
is within the guard window.
|     | 0 5 | 10  | 15 20 | 25 30 35 | 40 45 | 50  |
| --- | --- | --- | ----- | -------- | ----- | --- |
timestamp (ns)
1 and 3. Contextualizing this to the quantum interferometry experiment with four input photons and eight output
ports, coincidences of order higher than four, made possible only by dark counts, are discarded on the fourth-order
combinations. ThisistrueifalleightchannelsareinputtotheCombinationsvirtualchannel.
Inthefollowingminimalexample,wedemonstratehowtoobtainthevirtualchannelnumbersforfourth-ordercombi-
nations,thatcanbeinputtotheCountermeasurementclass. Thegoaloftheexampleistoensurethateachcombination
includesatleastonenumberfromeachofthesets{1,2},{3,6},{4,5},and{7,8}.
| # Create | the Combinations | virtual | channel |     |     |     |
| -------- | ---------------- | ------- | ------- | --- | --- | --- |
combinations_vchannels = Combinations(tagger, input_channels, window_size=100)
| #Define | sets of inclusion |     |     |     |     |     |
| ------- | ----------------- | --- | --- | --- | --- | --- |
| set1 =  | {1, 2}            |     |     |     |     |     |
| set2 =  | {3, 6}            |     |     |     |     |     |
| set3 =  | {4, 5}            |     |     |     |     |     |
| set4 =  | {7, 8}            |     |     |     |     |     |
# Filter combinations of four channels groups based on conditions
| filtered_combinations |     | = [list(comb) | for comb    | in groups         |     |     |
| --------------------- | --- | ------------- | ----------- | ----------------- | --- | --- |
|                       |     | if any(num    | in set1 for | num in comb)      |     |     |
|                       |     | and any(num   | in set2     | for num in comb)  |     |     |
|                       |     | and any(num   | in set3     | for num in comb)  |     |     |
|                       |     | and any(num   | in set4     | for num in comb)] |     |     |
# Create a list with the virtual channels monitoring the combinations
| virtualchannelsnumber |     | = [] |     |     |     |     |
| --------------------- | --- | ---- | --- | --- | --- | --- |
(continuesonnextpage)
| 3.3. MeasuringCoincidences |     |     |     |     |     | 35  |
| -------------------------- | --- | --- | --- | --- | --- | --- |

TimeTaggerUserManual,Release2.17.4.0
(continuedfrompreviouspage)
for group in filtered_combinations:
virtualchannelsnumber.append(combinations_vchannels.getChannel(group))
3.3.5 Coincidence-counting vs Correlation Measurement
Let us now assume in the following discussion to have only two channels. In this scenario, a coincidence-counting
experimentcouldbealsoperformedusingothermeasurementclasses,suchasCorrelation. Thelatterisamultistart,
multistopmeasurement,whichmeansthateverystartclickiscorrelatedwitheverystopclickasfartheyarewithinthe
Correlation time span. This implies that Correlation takes into accountboth positive and negative timedifferences.
Ontheotherhand, the“ConstantFractionDiscriminator +Counter”approachdoesnotdiscriminatetheorderofthe
clicks, as the virtual channel detects an event whenever the time tags on the two channels are separated within the
coincidenceWindow,regardlessofwhetherthistimedifferenceisnegativeorpositive.
CoincidencecountscanberetrievedbysummingupafewbinsoftheCorrelationhistogramaroundzerotimedifference,
dependingonthesizeofthedefinedcoincidencewindow. However,thereisonepointtoconsiderforgettingthecorrect
numberofcoincidincesusingCorrelationmeasurementclass. Pleaseseethefigurebelow.
stnuoC
Real signal
Time
stnuoC
Coincidence
+ Counter
Time
stnuoC
Coincidence
window
Time
Differences
Time
WhensummingthebinsoftheCorrelationtogethertogetcoincidencecounts, thebinalignmentmustbetakeninto
36 Chapter3. Tutorials

TimeTaggerUserManual,Release2.17.4.0
account,togetconsistentresultsfromthetwoanalyses. ItisindeedimportanttoproperlychoosethebinsizeinCorre-
lationsuchthattheedgesofthetwoouterbinsalignwiththecoincidenceWindow.
3.4 Remote Time Tagger with Python
TheTimeTaggerisagreatinstrumentfordataacquisitionwheneveryoudetect,count,oranalyzesinglephotons. You
canquicklysetupatimecorrelationmeasurement,coincidenceanalysis,andmuchmore. However,atsomepointin
yourproject,youmaywanttocontrolyourexperimentremotely. OneoptionistouseremotedesktopsoftwarelikeVNC,
TeamViewer,WindowsRemoteDesktop,etc. Whatifyouwanttocontrolyourremoteexperimentprogrammatically?
Areyouusingmultiplecomputersandwanttocollectdatafrommanyofthematthesametime? Thesolutionforthis
is a remote control interface. Luckily, this task is very common and many software libraries cover the challenge of
dealingwithnetworksocketsandmessagingprotocols.
In the following, we want to demonstrate two ways of connecting to a Time Tagger over a network: Network Time
TaggerandPyro5.
NetworkTimeTaggerisanidealsolutionforsharingaTimeTaggerbetweendifferentcomputers. ByusingNetwork
TimeTagger,aremotecomputerhasdirectaccesstotheTimeTagstreamandcanperformmeasurementslocally,as
if the Time Tagger was directly connected over USB. Pyro on the other hand can be used to access a Time Tagger
remotely. From a remote computer, Pyro can start measurements on the computer connected to the time tagger and
returntheresults.
3.4.1 Sharing a Time Tagger with Network Time Tagger
FromTimeTaggersoftwareversion2.10onward,TimeTaggersupportsremoteoperation‘out-of-the-box’withNetwork
TimeTagger. NetworkTimeTaggerimplementsaserveronacomputerconnectedtoaTimeTaggerandsendstheTime
Tagstreamdirectlytotheclients. Clientscanthenconnecttotheserverandrunarbitrarymeasurementsindependently
ontheirowncomputersasiftheyaredirectlyconnectedtothehardwaredevice.
TheservercanbesetupwiththeTimeTaggerGraphicalUserInterfaces(TimeTaggerLaborWebApplication)or
theTimeTaggerAPIthroughTimeTagger.startServer(). Whensettinguptheserver,thehostcandecideonthe
levelofaccessfortheclients. WithAccessMode.Control(), theclientshavefullaccesstodatafromallchannels
andcanchangethesettingsoftheTimeTagger. WithAccessMode.Listen(),thehostcandecidetoonlysharedata
fromspecificchannels.
ClientscanconnecttotheserverusingtheTimeTaggerAPIwithcreateTimeTaggerNetwork(). Onceconnected,
measurementscanbeperformeddirectlyontheclientside. Functioncallsareidenticaltotheonesusedtocontrola
TimeTaggerlocally. Therefore,programswrittenwiththeTimeTaggerAPIcanbeeasilyadaptedtorunonaremote
computer.
3.4. RemoteTimeTaggerwithPython 37

TimeTaggerUserManual,Release2.17.4.0
Note: NetworkTimeTaggercanalsobeusedtoaccessaTimeTaggerwithdifferentprogramminglanguagesatthe
sametime,bothlocallyoronaremotecomputer. WithcreateTimeTaggerNetwork(),itisforexamplepossibleto
runsimultaneousmeasurementswithMatlabandPython.
BelowisaminimalworkingexampleforsettingupaNetworkTimeTaggerserverandclientwithPython3.6.
Listing1: StartingaNetworkTimeTaggerserver
import TimeTagger
| tagger = | TimeTagger.createTimeTagger() |         |     |     |     |
| -------- | ----------------------------- | ------- | --- | --- | --- |
| #connect | to the Time Tagger            | via USB |     |     |     |
tagger.startServer(access_mode = TimeTagger.AccessMode.Control,port=41101)
# Start the Server. TimeTagger.AccessMode sets the access rights for clients. Port␣
| defines | the network port | to be used |     |     |     |
| ------- | ---------------- | ---------- | --- | --- | --- |
˓→
# The server keeps running until the command tagger.stopServer() is called or until the␣
| program | is terminated |     |     |     |     |
| ------- | ------------- | --- | --- | --- | --- |
˓→
Listing2: ConnectingtoaNetworkTimeTaggerserver
import TimeTagger
| tagger = | TimeTagger.createTimeTaggerNetwork('ip:port') |     |     |     |     |
| -------- | --------------------------------------------- | --- | --- | --- | --- |
# Connect to the Time Tagger server. 'ip' is the IP address of the server and 'port' is the␣
| port defined | by the server. | The default | port is 41101 |     |     |
| ------------ | -------------- | ----------- | ------------- | --- | --- |
˓→
correlation = TimeTagger.Correlation(tagger=tagger, channel_1=1, channel_2=2, binwidth=1,
n_bins=1000)
˓→
# tagger can be used to perform measurements as if the client was connected to the␣
TimeTagger via USB. In this case, the client starts a correlation measurement.
˓→
# After a measurement is finished, the client can disconnect with TimeTagger.
freeTimeTagger(tagger)
˓→
| 3.4.2 Remote | control | of a Time Tagger | with Pyro |     |     |
| ------------ | ------- | ---------------- | --------- | --- | --- |
Pyro5 is a Python library that allows operation of a Time Tagger from a remote computer. It is able to send API
commandstotheremoteTimeTaggerandtoobtaintheirreturnvalues. Inthefollowing,wedescribehowtousePyro5
| andachieveseamlessaccesstotheTimeTagger’sAPI |     |     | remotely. |     |     |
| -------------------------------------------- | --- | --- | --------- | --- | --- |
Listing3: Teasercode
| import matplotlib.pyplot |                                         | as plt |     |     |     |
| ------------------------ | --------------------------------------- | ------ | --- | --- | --- |
| from Pyro5.api           | import Proxy                            |        |     |     |     |
| TimeTagger               | = Proxy("PYRO:TimeTagger@server:23000") |        |     |     |     |
| tagger =                 | TimeTagger.createTimeTagger()           |        |     |     |     |
hist = TimeTagger.Correlation(tagger, 1, 2, binwidth=5, n_bins=2000)
| hist.startFor(int(10e12), |     | clear=True) |     |     |     |
| ------------------------- | --- | ----------- | --- | --- | --- |
(continuesonnextpage)
| 38  |     |     |     | Chapter3. | Tutorials |
| --- | --- | --- | --- | --------- | --------- |

TimeTaggerUserManual,Release2.17.4.0
(continuedfrompreviouspage)
x = hist.getIndex()
while hist.isRunning():
plt.pause(0.1)
| y           | = hist.getData() |           |      |     |     |
| ----------- | ---------------- | --------- | ---- | --- | --- |
| plt.plot(x, |                  | y)        |      |     |     |
| 3.4.3       | Remote           | procedure | call |     |     |
Remoteprocedurecall(RPC)isatechnologythatallowsinteractionwithremoteprogramsbycallingtheirprocedures
andreceivingtheresponses. Thisinvolvesarealcodeexecutionononecomputer(server),whiletheclientcomputer
hasonlyasubstituteobject(proxy)thatmimicstherealobjectrunningontheserver. Theproxyobjectknowshowto
sendrequestsanddatatotheserverandtheserverknowshowtointerprettheserequestsandhowtoexecutethereal
code.
Inthecaseof Pyro5,theproxyobjectandservercodeareprovidedbythelibraryandweonlyneedtotellPyro5what
wewanttobecomeavailableremotely.
| 3.4.4 | Initial | setup |     |     |     |
| ----- | ------- | ----- | --- | --- | --- |
YouwillneedtohaveaPython3.6ornewerinstalledonyourcomputer. WerecommendusingAnacondadistribution.
InstalltheTimeTaggersoftwareifyouhavenotdoneityet. ThedescriptionbelowassumesthatyouhavetheTime
TaggerhardwareandarefamiliarwiththeTimeTaggerAPI.
Thelastmissingpart,thePyro5package,youcaninstallfromPyPias
| pip install |         | Pyro5   |     |     |     |
| ----------- | ------- | ------- | --- | --- | --- |
| 3.4.5       | Minimal | example |     |     |     |
Here we start from the simplest functional example and demonstrate working remote communication. The example
consistsoftwoparts: theserverandtheclientcode. Youwillneedtorunthoseintwoseparatecommandwindows.
Servercode
We need to create an adapter class with methods that we want to access remotely and decorate it with Pyro5.api.
expose(). Thefollowingcodeisverysimple. Later,wewillextendittoexposemoreoftheTimeTagger’sfunction-
ality.
import Pyro5.api
| import | TimeTagger | as  | TT  |     |     |
| ------ | ---------- | --- | --- | --- | --- |
@Pyro5.api.expose
class TimeTaggerRPC:
| """Adapter |                       | for the | Time Tagger | Library""" |              |
| ---------- | --------------------- | ------- | ----------- | ---------- | ------------ |
| def        | scanTimeTagger(self): |         |             |            |              |
|            | """This               | method  | will become | available  | remotely.""" |
return TT.scanTimeTagger()
(continuesonnextpage)
3.4. RemoteTimeTaggerwithPython 39

TimeTaggerUserManual,Release2.17.4.0
(continuedfrompreviouspage)
'__main__':
| if __name__ |       | ==     |     |        |     |                   |     |       |     |     |     |
| ----------- | ----- | ------ | --- | ------ | --- | ----------------- | --- | ----- | --- | --- | --- |
| #           | Start | server | and | expose |     | the TimeTaggerRPC |     | class |     |     |     |
Pyro5.api.Daemon(host='localhost',
| with |     |                                  |       |        |      |           |        | port=23000)   | as daemon: |     |     |
| ---- | --- | -------------------------------- | ----- | ------ | ---- | --------- | ------ | ------------- | ---------- | --- | --- |
|      | #   | Register                         | class |        | with | Pyro      |        |               |            |     |     |
|      | uri | = daemon.register(TimeTaggerRPC, |       |        |      |           |        | 'TimeTagger') |            |     |     |
|      | #   | Print                            | the   | URI of | the  | published | object |               |            |     |     |
print(uri)
|     | #   | Start | the | server | event | loop |     |     |     |     |     |
| --- | --- | ----- | --- | ------ | ----- | ---- | --- | --- | --- | --- | --- |
daemon.requestLoop()
Clientcode
Ontheclientside,weneedtoknowtheuniqueidentifieroftheexposedobject,whichwasprintedwhenyoustartedthe
server. InPyro5,everyobjectisidentifiedbyaspecialstring(URI)thatcontainstheobjectidentitystringandtheserver
address. Asyoucanseeinthecodebelow,wedonotusetheTimeTaggersoftwaredirectlybutrathercommunicateto
theserverthathasit.
import Pyro5.api
| # Connect   |       | to the                                               | TimeTaggerRPC |         |      | object        | on the      | server        |             |     |     |
| ----------- | ----- | ---------------------------------------------------- | ------------- | ------- | ---- | ------------- | ----------- | ------------- | ----------- | --- | --- |
| # This      | line  | is                                                   | all we        | need    | to   | establish     | remote      | communication |             |     |     |
| TimeTagger  |       | = Pyro5.api.Proxy("PYRO:TimeTagger@localhost:23000") |               |         |      |               |             |               |             |     |     |
| # Now,      | we    | can call                                             | methods       |         | that | will          | be executed | on            | the server. |     |     |
| # Lets      | check | what                                                 | Time          | Taggers |      | are available |             | at the        | server      |     |     |
| timetaggers |       | = TimeTagger.scanTimeTagger()                        |               |         |      |               |             |               |             |     |     |
print(timetaggers)
| >> ['1740000ABC', |     |     | '1750000ABC'] |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Congratulations! NowyouhaveaverysimplebutfunctionalcommunicationtoyourremoteTimeTaggersoftware.
| 3.4.6 | Creating |     | the | Time | Tagger |     |     |     |     |     |     |
| ----- | -------- | --- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- |
By now, our code can communicate over a network and can only report the serial numbers of the connected Time
Taggers. Inthissection,wewillexpandtheservercodeandmakeitmoreuseful. Thenextmostimportantfeatureof
theserveristoexposethecreateTimeTagger()methodtotelltheservertoinitializetheTimeTaggerhardware.
YoumaybetemptedtoextendtheTimeTaggerRPCclassasfollows:
@Pyro5.api.expose
class TimeTaggerRPC:
| """Adapter |                       |     | for the | Time   | Tagger  | Library""" |        |           |                  |     |     |
| ---------- | --------------------- | --- | ------- | ------ | ------- | ---------- | ------ | --------- | ---------------- | --- | --- |
| def        | scanTimeTagger(self): |     |         |        |         |            |        |           |                  |     |     |
|            | """Return             |     | the     | serial | numbers |            | of the | available | Time Taggers.""" |     |     |
return TT.scanTimeTagger()
| def | createTimeTagger(self): |     |     |     |     |     |     |     |     |     |     |
| --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(continuesonnextpage)
| 40  |     |     |     |     |     |     |     |     |     | Chapter3. | Tutorials |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- |

TimeTaggerUserManual,Release2.17.4.0
(continuedfrompreviouspage)
"""Create the Time Tagger."""
return TT.createTimeTagger() # This will fail! :(
To our great disappointment, the createTimeTagger method will fail when you try to access it from the client. The
reasonisinhowtheRPCcommunicationworks. Thedataandtheprogramcodehaveacertainformatinwhichitis
storedinthecomputer’smemory,andthismemorycannotbeeasilyorsafelyaccessedfromaremotecomputer. The
RPCcommunicationovercomesthisproblemusingdataserialization,i.e.,convertingthedataintoageneralizedformat
suitableforsendingoveranetworkandunderstandablebyaclientsystem.
ThePyro5,morespecificallytheserpent serializeritemploysbydefault,knowshowtoserializethestandardPython
data types like a list of strings returned by scanTimeTagger(). However, it has no idea how to interpret the
TimeTagger object returned by the createTimeTagger(). Moreover, instead of sending the TimeTagger object
totheclient,wewanttosendaproxyobjectwhichallowstheclienttotalktotheTimeTaggerobjectontheserver.
FortheTimeTagger,wedefineanadapterclass. ThenwemodifytheTimeTaggerRPC.createTimeTaggertocreatean
instanceoftheadapterclass,registeritwithPyro,andreturnit. Pyrowillautomaticallytakecareofcreatingaproxy
objectfortheclient.
@Pyro5.api.expose
class TimeTagger:
"""Adapter for the Time Tagger object"""
def __init__(self, args, kwargs):
self._obj = TT.createTimeTagger(*args, **kwargs)
def setTestSignal(self, *args):
return self._obj.setTestSignal(*args)
def getSerial(self):
return self._obj.getSerial()
# ... Other methods of the TT.TimeTagger class are omitted here.
@Pyro5.api.expose
class TimeTaggerRPC:
"""Adapter for the Time Tagger Library"""
def scanTimeTagger(self):
"""Return the serial numbers of the available Time Taggers."""
return TT.scanTimeTagger()
def createTimeTagger(self, *args, **kwargs):
"""Create the Time Tagger."""
tagger = TimeTagger(args, kwargs)
self._pyroDaemon.register(tagger)
return tagger
# Pyro will automatically create and send a proxy object
# to the client.
def freeTimeTagger(self, tagger_proxy):
"""Free Time Tagger. """
# Client only has a proxy object.
(continuesonnextpage)
3.4. RemoteTimeTaggerwithPython 41

TimeTaggerUserManual,Release2.17.4.0
(continuedfrompreviouspage)
|     | objectId | =                                            | tagger_proxy._pyroUri.object |     |         |     |     |     |
| --- | -------- | -------------------------------------------- | ---------------------------- | --- | ------- | --- | --- | --- |
|     | # Get    | adapter                                      | object from                  | the | server. |     |     |     |
|     | tagger   | = self._pyroDaemon.objectsById.get(objectId) |                              |     |         |     |     |     |
self._pyroDaemon.unregister(tagger)
return TT.freeTimeTagger(tagger._obj)
| 3.4.7 | Measurements |     | and virtual | channels |     |     |     |     |
| ----- | ------------ | --- | ----------- | -------- | --- | --- | --- | --- |
Bynow,wecanlistavailableTimeTaggerdevicesandcreateTimeTaggerobjects. Theremainingpartistoimplement
access to the measurements and virtual channels. We will use the same approach as with the TimeTagger class and
createadapterclassesforthem.
@Pyro5.api.expose
class Correlation:
| """Adapter |                | class | for Correlation             | measurement.""" |     |                  |     |     |
| ---------- | -------------- | ----- | --------------------------- | --------------- | --- | ---------------- | --- | --- |
| def        | __init__(self, |       | tagger,                     | args, kwargs):  |     |                  |     |     |
|            | self._obj      | =     | TT.Correlation(tagger._obj, |                 |     | *args, **kwargs) |     |     |
| def        | start(self):   |       |                             |                 |     |                  |     |     |
return self._obj.start()
| def | startFor(self, |                                      | capture_duration, |     | clear): |              |     |     |
| --- | -------------- | ------------------------------------ | ----------------- | --- | ------- | ------------ | --- | --- |
|     | return         | self._obj.startFor(capture_duration, |                   |     |         | clear=clear) |     |     |
| def | stop(self):    |                                      |                   |     |         |              |     |     |
return self._obj.stop()
| def | clear(self): |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
return self._obj.clear()
| def | isRunning(self): |     |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
return self._obj.isRunning()
| def | getIndex(self): |     |     |     |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
return self._obj.getIndex().tolist()
| def | getData(self): |     |     |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
return self._obj.getData().tolist()
@Pyro5.api.expose
class DelayedChannel():
| """Adapter |                   | class | for DelayedChannel."""         |                |     |                  |     |     |
| ---------- | ----------------- | ----- | ------------------------------ | -------------- | --- | ---------------- | --- | --- |
| def        | __init__(self,    |       | tagger,                        | args, kwargs): |     |                  |     |     |
|            | self._obj         | =     | TT.DelayedChannel(tagger._obj, |                |     | *args, **kwargs) |     |     |
| def        | getChannel(self): |       |                                |                |     |                  |     |     |
return self._obj.getChannel()
(continuesonnextpage)
| 42  |     |     |     |     |     |     | Chapter3. | Tutorials |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- |

TimeTaggerUserManual,Release2.17.4.0
(continuedfrompreviouspage)
@Pyro5.api.expose
class TimeTaggerRPC:
| """Adapter            | class for                                    | the           | Time Tagger     | Library"""        |
| --------------------- | -------------------------------------------- | ------------- | --------------- | ----------------- |
| # Earlier             | code omitted                                 |               | (...)           |                   |
| def Correlation(self, |                                              | tagger_proxy, |                 | *args, **kwargs): |
| """Create             | Correlation                                  |               | measurement.""" |                   |
| objectId              | = tagger_proxy._pyroUri.object               |               |                 |                   |
| tagger                | = self._pyroDaemon.objectsById.get(objectId) |               |                 |                   |
| pyro_obj              | = Correlation(tagger,                        |               |                 | args, kwargs)     |
self._pyroDaemon.register(pyro_obj)
| return                   | pyro_obj                                     |     |               |                   |
| ------------------------ | -------------------------------------------- | --- | ------------- | ----------------- |
| def DelayedChannel(self, |                                              |     | tagger_proxy, | *args, **kwargs): |
| """Create                | DelayedChannel."""                           |     |               |                   |
| objectId                 | = tagger_proxy._pyroUri.object               |     |               |                   |
| tagger                   | = self._pyroDaemon.objectsById.get(objectId) |     |               |                   |
| pyro_obj                 | = DelayedChannel(tagger,                     |     |               | args, kwargs)     |
self._pyroDaemon.register(pyro_obj)
| return | pyro_obj |     |     |     |
| ------ | -------- | --- | --- | --- |
Note: The methods Correlation.getIndex() and Correlation.getData() return numpy.ndarray arrays.
Pyro5 does not know how to serialize numpy.ndarray, therefore for simplicity of the example, we convert them
tothePythonlists.
Moreefficientapproachwouldbetoregistercustomserializerfunctionsfornumpy.ndarrayonboth,serverandclient
sides,seeCustomizingserializationsectionofthePyro5documentation.
| 3.4.8 Working | example |     |     |     |
| ------------- | ------- | --- | --- | --- |
Downloadthecompletesourcefiles
•
simple_server.py
• simple_example.py
Starttheserverinaterminalwindow:
> python simple_server.py
Nowopenasecondterminalwindowandruntheexample:
> python simple_example.py
Let us take a look at the source code of the example (shown below). You may recognize that it is
practically the same as using the Time Tagger package directly. The only difference is that the im-
port statement import TimeTagger is replaced by the proxy object creation TimeTagger = Pyro5.api.
Proxy("PYRO:TimeTagger@localhost:23000").
3.4. RemoteTimeTaggerwithPython 43

TimeTaggerUserManual,Release2.17.4.0
|                          |       |        | Listing4: simple_example.py |     |     |
| ------------------------ | ----- | ------ | --------------------------- | --- | --- |
| import numpy             | as np |        |                             |     |     |
| import matplotlib.pyplot |       | as plt |                             |     |     |
import Pyro5.api
| TimeTagger              | = Pyro5.api.Proxy("PYRO:TimeTagger@localhost:23000") |                     |     |     |     |
| ----------------------- | ---------------------------------------------------- | ------------------- | --- | --- | --- |
| # Create                | Time Tagger                                          |                     |     |     |     |
| tagger =                | TimeTagger.createTimeTagger()                        |                     |     |     |     |
| tagger.setTestSignal(1, |                                                      | True)               |     |     |     |
| tagger.setTestSignal(2, |                                                      | True)               |     |     |     |
| print('Time             | Tagger serial:',                                     | tagger.getSerial()) |     |     |     |
hist = TimeTagger.Correlation(tagger, 1, 2, binwidth=2, n_bins=2000)
| hist.startFor(int(10e12), |                | clear=True) |     |     |     |
| ------------------------- | -------------- | ----------- | --- | --- | --- |
| fig, ax =                 | plt.subplots() |             |     |     |     |
# The time vector is fixed. No need to read it on every iteration.
x = np.array(hist.getIndex())
| line, = ax.plot(x,  | x *    | 0)  |     |     |     |
| ------------------- | ------ | --- | --- | --- | --- |
| ax.set_xlabel('Time | (ps)') |     |     |     |     |
ax.set_ylabel('Counts')
| ax.set_title('Correlation |     | histogram | via Pyro-RPC') |     |     |
| ------------------------- | --- | --------- | -------------- | --- | --- |
while hist.isRunning():
| y = hist.getData() |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- |
line.set_ydata(y)
| ax.set_ylim(np.min(y), |     | np.max(y)) |     |     |     |
| ---------------------- | --- | ---------- | --- | --- | --- |
plt.pause(0.1)
# Cleanup
TimeTagger.freeTimeTagger(tagger)
del hist
del tagger
del TimeTagger
Seealso:
The Time Tagger software installer includes more complete examples of the RPC server that includes more
measurements, virtual channels and implements custom serialization of types. You can usu-
numpy.ndarray
allyfindtheexamplefilesintheC:\Program Files\Swabian Instruments\Time Tagger\examples\python\
7-Remote-TimeTagger-with-Pyro5.
| 44  |     |     |     | Chapter3. | Tutorials |
| --- | --- | --- | --- | --------- | --------- |

TimeTaggerUserManual,Release2.17.4.0
3.4.9 What is next?
One can follow the ideas presented in this tutorial and implement a fully featured Python package. You can find an
experimental version of such package at PyPi. Instead of manually wrapping every class and function of the Time
TaggerAPI,thepackageemploysmetaprogrammingandautomaticallygeneratesadapterclasses.
LetusknowifyouhaveanyquestionsaboutRPCinterfacefortheTimeTagger.
Youcanexpandontheideaspresentedinthistutorial,andimplementremotecontrolforyourcompleteexperiment.
3.4. RemoteTimeTaggerwithPython 45

TimeTaggerUserManual,Release2.17.4.0
| 46  | Chapter3. | Tutorials |
| --- | --------- | --------- |

CHAPTER
FOUR
SYNCHRONIZER
4.1 Overview
TheSwabianInstruments’Synchronizerallowsforconnectingupto8TimeTaggerUltra/TimeTaggerX devicesto
expandthenumberofavailablechannels. TheSynchronizergeneratesaclockandsynchronizationsignaltoestablish
acommontime-baseonallconnectedTimeTaggers. TheTimeTaggersoftwareenginecreatesalayerofabstraction:
thesynchronizedTimeTaggersappearasonedevicewithacombinednumberofinputchannels.
4.2 Key applications
TheSynchronizeroffersnumerousadvantagesbeyonditscapabilitytoextendthenumberofinputchannelsupto144,
whenconnectedto8TimeTaggers,withoutintroducinganyadditionaltimejitter.
4.2.1 Crosstalk elimination
EmployingsynchronizedTimeTaggersprovidesthebenefitofeffectivelysuppressinganalogcrosstalkincomparison
tomeasurementsinvolvingasingledeviceunit. Inexperimentssuchasinterferometry,forinstance,thecrosstalkpickup
incorrelationmeasurementshinderstheidentificationofthephysicalsignalfromtheelectronicnoisearoundzero. A
commonlyadoptedsolutionconsistsondelayingsignalswithrespecttoeachotherbyusingcablesofdifferentlengths.
Nevertheless,thisapproachmightintroduceadditionalcomplexities,e.g. thelengthdifferencefluctuatesovertimedue
totemperaturevariations. Inthisregard,theSynchronizerrepresentsamorerobustsolution.
4.2.2 High transfer rate
ThedatatransferratefromasingleTimeTaggertothePCislimitedto80MTags/sbythesingle-coreCPUperformance.
UtilizingmorethanoneTimeTaggerallowstousemultipleUSBcontrollersandCPUthreads,significantlyincreasing
thetotaltransferrate(upto80MTags/sperdevice),asfarastheTimeTaggerandPCprocessingcapabilitiesarenot
overcome.
47

TimeTaggerUserManual,Release2.17.4.0
4.2.3 Multi-room experiment
Insomeexperiments, TimeTaggersneedtobeplacedfarapart. ThecablelengthbetweentheSynchronizerandthe
TimeTaggercanbeaslongas50m,withoutanyadditionaltimejittercaused. DifferentSynccablesresultonlyina
constanttimeoffsetbetweenthesignals.
4.2.4 Synchronizer with a single Time Tagger
YoucanbenefitfromtheSynchronizerwithasingleTimeTaggeratleastinthefollowingtwoapplicationscenarios:
1. Longtermclockstability
TheSynchronizercontainsahighlystableclockoscillatorwhichyoucanbenefitfromevenwhenyouhaveonly
oneTimeTagger. JustconnectanyclockoutputoftheSynchronizertotheCLKIN inputoftheTimeTaggerand
enjoytheclockstabilityprovidedbytheSynchronizer,whichmattersespeciallymeasuringlongtimedifferences.
2. Absoluteclocktimestamps
ByconnectingallsignalsfromtheSynchronizerasshowninCableconnectionsthetimestampsintheTimeTag
streamwillbereferencedtothepower-uptimeoftheSynchronizer. EvenwhenyoudisconnecttheTimeTagger
fromyourPC,e.g.,incaseofpowerdown,USBtimeout,orsoftwarerestart,thetimetagsreturnedbytheTime
TaggerwillremainreferencedtothestarttimeoftheSynchronizer. Toverifythatthisconfigurationisactive,
youwillseeawarningmessageintheconsoleoncreateTimeTagger()thatyouareusingtheSynchronizer
withonlyoneTimeTagger.
4.3 Requirements
SuccessfulsynchronizationofyourTimeTaggersrequires:
• YouhaveobtainedtheSynchronizerhardware.
• Your Time Tagger Ultra has hardware version 1.2 or higher. In case you have an older device and want to
synchronizeitwithmoreunits,pleasecontactoursupportorsalesteamwww.swabianinstruments.com/contact.
• YourPChasasufficientnumberofUSB3portsfordirectconnectionofeveryTimeTagger. TheSynchronizer
itselfdoesnotrequireaUSBconnection.
• YouhaveasufficientnumberofSMAcablesofthesamelength. YouneedthreecablesforeachTimeTagger.
Formoredetails,seeinthesectionCableconnections.
• YouhaveinstalledtheTimeTaggersoftwareversion2.6.6ornewer.
4.4 Cable connections
TheSynchronizerprovidesacommonclocksignalforeveryTimeTaggeraswellasthesynchronizationsignals. Fur-
thermore,TimeTaggershavetobeconnectedtoeachotherinaloop. Theconnectionsequenceintheloopdefinesthe
channelnumberingorder. AnadditionalfeedbacksignalisrequiredtoidentifywhichoftheTimeTaggersintheloop
isthefirst.
UsingasingleTimeTaggerwithSynchronizerisalsopossibleandyoushallconnectLOOPINandLOOPOUTtogether
onthesamedevice.
48 Chapter4. Synchronizer

TimeTaggerUserManual,Release2.17.4.0
Note: AfterthereleaseoftheSynchronizer, wehavechangedtheconnectorlabelsonthefrontpanelofTimeTag-
ger Ultra. In this section, we use the new labeling scheme, while showing the corresponding old labels in brackets:
NEW_LABEL(OLD_LABEL).
Table1: ConnectionsbetweentheSynchronizerandTimeTaggers
| Synchronizer | TimeTagger       | Description               |
| ------------ | ---------------- | ------------------------- |
| CLKOUT<N>    | CLKIN(CLK)       | 500MHzclock               |
| SYNCOUT<N>   | SYNCIN(AUXIN1)   | Synchronizationdata       |
| FDBKIN       | FDBKOUT(AUXOUT2) | FeedbackfromoneTimeTagger |
Every Time Tagger should have its LOOP OUT (AUX OUT 1) connected to the LOOP IN (AUX IN 2) of next Time
Tagger,eventuallyformingasignalloop. Thefollowingdiagramvisualizestheconnectionsrequiredforthesynchro-
nizationofthreeTimeTaggers.
Warning: Forreliablesynchronization,thecablesforCLK andSYNCsignalsshallhavealengthdifferencebelow
4cm. Werecommendusingthesamecabletypeforthesetwosignals.
Additionally, we recommend connecting every Time Tagger directly to a USB3 port on the same computer. If your
computer does not have a sufficient number of USB3 ports, avoid using USB hubs as they limit the data bandwidth
availableforeveryTimeTagger. Instead,pleaseinstallanadditionalUSBcontrollercardintoyourcomputer. While
there isa widevariety of USB3controllers, youhave to lookfor onethat can deliverfull USB3bandwidth at every
4.4. Cableconnections 49

TimeTaggerUserManual,Release2.17.4.0
USB port simultaneously. Typically, such USB controllers have an individual chip for each USB port and require a
PCIex4slotonthecomputer’smotherboard..
| 4.4.1 Using | an external | reference | clock |     |     |
| ----------- | ----------- | --------- | ----- | --- | --- |
TheSynchronizerhasabuilt-inhighaccuracyandlownoisereferenceoscillatoranddistributestheclocksignalsto
allattachedTimeTaggers. Incaseyouwanttouseyourexternalreferenceclock,youhavetoconnectittotheREFIN
connectoroftheSynchronizer. Additionally, theSynchronizercansupply10MHzreferencesignalthroughitsREF
OUT output. NotethatREFOUT isdisabledwhenanexternalreferencesignalispresentattheREFIN.
Table2: RequirementstothereferencesignalatREFIN.
| Parameter    |     |         | Value                     |     |     |
| ------------ | --- | ------- | ------------------------- | --- | --- |
| Coupling     |     |         | AC                        |     |     |
| Amplitude    |     |         | 0.3... 5.0Vpp             |     |     |
| Frequency    |     |         | 10MHz                     |     |     |
| Impedance    |     |         | 50Ohm                     |     |     |
|              |     | Table3: | SignalparametersatREFOUT. |     |     |
| Parameter    |     |         | Value                     |     |     |
| Coupling     |     |         | AC                        |     |     |
| Amplitude    |     |         | 3.3Vpp(1Vpp@50Ohm)        |     |     |
| Frequency    |     |         | 10MHz                     |     |     |
| 4.5 Software | and | channel | numbering                 |     |     |
TheTimeTaggersoftwareengineautomaticallyrecognizesifaTimeTaggerbelongstoasynchronizedgroup. Itwill
alsoautomaticallyopenaconnectiontoallotherTimeTaggersinthegroupandpresentalldevicesasasingleTime
Tagger. Thereisnospecific“master”device,andtheconnectiontothesynchronizedgroupcanbeinitiatedfromany
ofthememberTimeTaggers.
TheconnectionisopenedasusualusingcreateTimeTagger(),andoptionallyyoucanspecifytheserialnumberof
theTimeTagger.
| tagger = createTimeTagger() |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- |
Thetaggerobjectprovidesacommoninterfaceforthewholesynchronizationloop,andallprogrammingisdoneinthe
samewayasforasingleTimeTagger. Notethat,comparedtoasingleTimeTagger,thechannelnumberingschemeis
modifiedforeasyidentificationbyauser. ThechannelnumberconsistsoftheTimeTaggernumberintheloopandthe
| inputnumberonthefrontpanel. |                 | Thechannelnumberformulais |     |     |     |
| --------------------------- | --------------- | ------------------------- | --- | --- | --- |
| CHANEL_NUMBER               | = TT_NUMBER*100 | + INPUT_NUMBER            |     |     |     |
Asanexample, letusassumewehavethreeTimeTaggerUltra 18inasynchronizationloop. TheTimeTaggerthat
providesthefeedbacksignaltotheSynchronizerhassequencenumber1,anditschannelnumberswillbefrom101to
118. ThechannelsofthenextTimeTaggerwillhavenumbersfrom201to218,andsoforth.
Note: IncasethechannelnumbersonyourTimeTaggerUltrastartwith0,inthesynchronizedgroup,thechannel0
willappearasN01, whereNistheTimeTaggernumber. Seemoreaboutchannelnumberingschemeinthesection
| 50  |     |     |     | Chapter4. | Synchronizer |
| --- | --- | --- | --- | --------- | ------------ |

TimeTaggerUserManual,Release2.17.4.0
ChannelNumberSchema0and1.
YoucanrequestthecompletelistofavailablechannelswiththeTimeTagger.getChannelList()method.
| from TimeTagger |                                                  | import     | createTimeTagger, |      | TT_CHANNEL_RISING_EDGES |
| --------------- | ------------------------------------------------ | ---------- | ----------------- | ---- | ----------------------- |
| # Connect       | to                                               | any of the | synchronized      | Time | Taggers                 |
| tagger          | = createTimeTagger()                             |            |                   |      |                         |
| # Request       | a list                                           | of all     | positive          | edge | channels                |
| chan_list       | = tagger.getChannelList(TT_CHANNEL_RISING_EDGES) |            |                   |      |                         |
print(chan_list)
| >> [101, | 102,       | ... , 317, | 318]        |     |     |
| -------- | ---------- | ---------- | ----------- | --- | --- |
| 4.5.1    | Incomplete | cable      | connections |     |     |
Thesoftwareengineattemptstodetectincorrectorincompleteconnectionsofthecablesinthesynchronizationloop.
Incasesomeconnectionsaremissingorweredisconnectedduringoperation,thesoftwareenginewillshowawarning
andthedatatransmissionfromthedisconnectedTimeTaggerwillbefilteredoutuntilavalidconnectionisrestored.
IssueswiththecableconnectionsandsynchronizationstatusareindicatedusingthestatusLEDsonthefrontpanelof
theSynchronizerandtheTimeTagger. SeemoreinsectionStatusLEDsandtroubleshooting.
| 4.5.2 | Buffer | overflows |     |     |     |
| ----- | ------ | --------- | --- | --- | --- |
ThesynchronizationloopalsopropagatesthebufferoverflowstatefromanyTimeTaggertoallmembersoftheloop.
Onthesoftwareside,thebufferoverflowhasthesameeffectasforasingleTimeTagger. See,Overflows.
4.6 Limitations
| 4.6.1 | Conditional | filter |     |     |     |
| ----- | ----------- | ------ | --- | --- | --- |
Theconditionalfiltercannotbeappliedacrosssynchronizeddevices. However, itcanstillbeenabledforeachTime
Taggerindependently.
Incaseyouwanttousetheconditionalfilteracrossdevices,youhavetosendthesignaltobefiltered(forexample,your
lasersync)toeveryTimeTaggerwheretriggersignalsareconnected. Insoftware,youhavetochoosethecorresponding
inputfortimedifferencemeasurements.
| 4.6.2 | Internal | test signal |     |     |     |
| ----- | -------- | ----------- | --- | --- | --- |
Theinternaltest-signalgeneratorisafree-runningoscillatorindependentfromthesystemclock. Therefore, thetest
signalsarenotcorrelatedbetweendifferentTimeTaggers,evenifthesynchronizationloopissetupcorrectly. Ifyoutry
tomeasureacorrelationwiththeinternaltestsignalacrosstwodifferentTimeTaggers,youwillseeaflathistogram.
Ontheotherhand,performingthesamemeasurementwithtwoinputchannelsofthesameTimeTaggerwillresultin
ajitter-limitedcorrelationpeak.
4.6. Limitations 51

TimeTaggerUserManual,Release2.17.4.0
| 4.7 Status | LEDs and | troubleshooting |     |     |     |
| ---------- | -------- | --------------- | --- | --- | --- |
ThefrontpaneloftheSynchronizerhasseveralLEDsthatindicateoperationstatus.
| LED    | Color      |     | Description                                      |     |     |
| ------ | ---------- | --- | ------------------------------------------------ | --- | --- |
| Power  | dark       |     | Nopowerprovided                                  |     |     |
| –      | solidgreen |     | Poweredon                                        |     |     |
| Status | dark       |     | Warmingup                                        |     |     |
| –      | solidgreen |     | Normaloperation.                                 |     |     |
| FDBKIN | solidgreen |     | Normaloperation                                  |     |     |
| –      | solidred   |     | Invalidfeedbacksignal                            |     |     |
| REFIN  | dark       |     | Noexternalreferencesignal                        |     |     |
| –      | solidgreen |     | Valid10MHzreferencesignal                        |     |     |
| –      | solidred   |     | Invalidreferencesignal                           |     |     |
| REFOUT | dark       |     | Outputisdisabledwhenusingexternalreferencesignal |     |     |
| –      | solidgreen |     | Outputenabled                                    |     |     |
The LEDs of the Time Tagger Ultra also indicate the state of the synchronization loop. See more details in section
LEDs.
| 52  |     |     |     | Chapter4. | Synchronizer |
| --- | --- | --- | --- | --------- | ------------ |

CHAPTER
FIVE
HARDWARE
5.1 Input channels
TheTimeTaggerhas8or18inputs(SMA-connectors). Theelectricalcharacteristicsaretabulatedbelow. Eachinput
candetectboth,risingandfallingedgesofaninputpulse,andeachinputhastwochannelsassociatedwithit. Rising
edges correspond to channel numbers 1 to 18 (Time Tagger 20: 1 to 8) and falling edges correspond to respective
channel numbers -1 to -18 (Time Tagger 20: -1 to -8). Thereby, you can treat rising and falling edges in a fully
equivalentfashion.
| 5.1.1 Electrical characteristics |     |              |                 |              |
| -------------------------------- | --- | ------------ | --------------- | ------------ |
| Property                         |     | TimeTagger20 | TimeTaggerUltra | TimeTaggerX  |
| Termination                      |     | 50Ohm        | 50Ohm           | 50Ohm/High-Z |
Inputvoltagerange(recommended) 0.0to3.0V -3.0to3.0V -1.5to1.5V
| Maximuminput(nodamage) |                   | -0.3to5.0V    | -5.0to5.0V | -3.0to3.0V |
| ---------------------- | ----------------- | ------------- | ---------- | ---------- |
| Triggerlevelrange      |                   | 0.0to2.5V     | -2.5to2.5V | -1to1V     |
| Minimumsignallevel     |                   | 100mV         | 100mV      | 100mV      |
| Minimumpulsewidth      |                   | 1.0ns         | 0.5ns      | 350ps      |
| 5.1.2 Configurable     | input termination | - Time Tagger | X only     |            |
The input termination of the Time Tagger X is configurable during runtime to either 50 Ohm or High-Z (see
TimeTagger.setInputImpedanceHigh()). Usually 50 Ohm should be chosen to accomplish proper HF termi-
nation,butHigh-Zisusefulincertainusecaseswithsmallamplitudesandweakoutputdrivers.
When the Time Tagger X is unpowered or not configured (before has been
| Caution: |     |     | createTimeTagger() |     |
| -------- | --- | --- | ------------------ | --- |
called),theinputterminationisHigh-Z.ThisistoprotecttheTimeTagger’sinputstagefrompotentiallydamaging
operatingconditions(e.g. signalsintoanunpoweredinputstage). Sincesoftwareversion2.17.0,thetermination
does not switch switch to 50 Ohm upon initialization anymore. However, the channel will switch to 50 Ohm by
defaultassoonasitisregistered. Toprohibitthisswitchingbehavior, settheimpedanceexplicitlytoHigh-Zby
TimeTagger.setInputImpedanceHigh()beforethefirstusageoftherespectiveinput,e.g. inameasurement.
OneofthefollowingmeasurescanbetakenwhenconnectingsignalsourcestotheTimeTaggerXwhicharesensitive
tooperationwithouttermination:
• Thesignal sourceisonly operatedafter theTimeTagger X ispowered andconfigured properly. TheTime
Tagger’sinputterminationissetto50Ohm.
53

TimeTaggerUserManual,Release2.17.4.0
• An external 50 Ohm termination is connected between SMA cable and the Time Tagger’s input port. The
TimeTagger’sinputterminationissettoHigh-Z.
• AnHFcirculatororisolatorisconnectedtotheoutputofthesignalsourcetopreventanypotentiallydamaging
reflectionsfromgettingintotheoutput.
| 5.1.3 High | Resolution | Mode |     |     |     |     |
| ---------- | ---------- | ---- | --- | --- | --- | --- |
TheTimeTaggerUltraPerformanceandtheTimeTaggerXcanoperateindifferentHighResolution(HighRes)modes.
An increased resolution is achieved by directing the signal from a single input to multiple time-to-digital converters
(TDCs). Dependingonthemode,2,4,or8TDCsareusedperinput. Byaveragingtheresults,asingletimestampwith
lowerjitterisgenerated. Ontheotherhand,thisprocessreducesthenumberofusablesignalinputs.
Thetablesshowtheusableinputsforthedifferentmodes. Channelsavailablewiththeminimalfour-channellicense
areshownwithoutparenthesis. Whenadditionalchannelsareadded,theprioritywillbegiventotheHighResones.
|     |     |          | Table1: TimeTaggerUltraPerformance |                  |     |     |
| --- | --- | -------- | ---------------------------------- | ---------------- | --- | --- |
|     |     | Mode     | HighReschannels                    | Standardchannels |     |     |
|     |     | Standard |                                    | 1-4,(5-18)       |     |     |
|     |     | HighResA | 1,3,5,7,(10,12,14,16)              | (9,18)           |     |     |
|     |     | HighResB | 1,5,10,14                          | (9,18)           |     |     |
|     |     | HighResC | 5,14                               | 9,18             |     |     |
Table2: TimeTaggerX
|     |     | Mode     | HighReschannels | Standardchannels |     |     |
| --- | --- | -------- | --------------- | ---------------- | --- | --- |
|     |     | Standard |                 | 1-4,(5-18)       |     |     |
|     |     | HighResB | 1,5,9,13,(17)   |                  |     |     |
Note: As a result of the averaging process, the quality of the calculated timestamps is affected by relative changes
intheinternaldelaysofthecontributinginputs. Thesedelaysareespeciallyaffectedbythedevice’stemperature. It
is strongly recommended to let the device heat up for at least 10 s before starting a measurement. Constant average
countrates(averagedoverthetimescaleofhundredsofmilliseconds)willprovidethebestresults. Ifyouneedmore
informationonthistopic,pleasecontactusviasupport@swabianinstruments.com.
| 5.2 Data | connection |     |     |     |     |     |
| -------- | ---------- | --- | --- | --- | --- | --- |
TheTimeTagger20ispoweredviaaUSBconnection. Therefore,youshouldensurethattheUSBportiscapableof
providingthefullspecifiedcurrent(500mA).AUSB>=2.0dataconnectionisrequiredfortheperformancespecified
here. OperatingthedeviceviaaUSBhubisstronglydiscouraged. TheTimeTagger20canstreamabout9MTags/s.
TheTimeTaggerUltraandTimeTaggerX hasaUSB3.0interface. Thisallowstostreamupto80MTags/stothePC.
TheactualnumberhighlydependsontheperformanceoftheCPUtheTimeTaggerisconnectedtoandtheevaluation
methodsinvolved.
Inaddition,theTimeTaggerX isequippedwithbothanSFP+Port(10GbE)andaQSFP+port(40GbE)whichcan
beusedforstreamingupto300MTags/sor1200MTags/srespectively.
| 54  |     |     |     |     | Chapter5. | Hardware |
| --- | --- | --- | --- | --- | --------- | -------- |

TimeTaggerUserManual,Release2.17.4.0
5.3 LEDs
TheTimeTaggerdeviceshaveLEDsshowingstatusinformation.
5.3.1 Time Tagger X
Frontpanelandpowerbutton
Onitsfrontpanel,theTimeTaggerX hasanLEDinsidethepowerbuttonandindividualchannelstatusLEDs:
Table3: PowerbuttonLED
Color Description
blue Deviceinstandby,pressbuttontoturniton
green Devicerunning
orange Deviceisgettingready
red Anerroroccurred
Table4: ChannelLEDs
Color Description
dark Channelunavailable(accordingtoyourlicense)
blue Channelavailablebutnotusedbyameasurement
solidgreen Measurementrunningbutnodatawithinlast2s
blinkinggreen
TimetagsarestreamedtothePC.
Blinkingfrequencyindicatesdatarate
solidorange Overflow
solidred Error
Rearpanel
Table5: LEDnexttotheCLKIN input
Color Description
dark Noclocksignal
solidgreen Validreferenceorsynchronizationclock
solidred Invalidreferencefrequency
solidblue Ext. clockvalid,butnotinuse
Table6: LEDnexttotheSYNCIN input
Color Description
dark NosynchronizeronCLK input
green ValidsignalatSYNCIN
red InvalidsignalatSYNCIN
5.3. LEDs 55

TimeTaggerUserManual,Release2.17.4.0
|     | Table7: LEDnexttotheLOOPIN | input |     |     |
| --- | -------------------------- | ----- | --- | --- |
Color Description
|     | dark NosynchronizeronCLK | input |     |     |
| --- | ------------------------ | ----- | --- | --- |
green ValidsignalatLOOPIN
red InvalidsignalatLOOPIN
| 5.3.2 Time | Tagger Ultra |     |     |     |
| ---------- | ------------ | --- | --- | --- |
The“Power”LEDturnsgreenwhenthepowerissuppliedtothedevice.
Table8: StatusLED
| Color         |     | Description          |     |     |
| ------------- | --- | -------------------- | --- | --- |
| solidgreen    |     | Firmwareloaded       |     |     |
| blinkinggreen |     | Timetagsarestreaming |     |     |
solidorange
Overflowsoccurred.
LEDturnsorangefor0.3sonoverflowevents.
Solidorangeindicatescontinuousoverflows.
solidred
Deviceinitializationfailed
(checkUSBconnection)
Table9: LEDnexttotheCLK input
|     | Color                         | Description                          |          |     |
| --- | ----------------------------- | ------------------------------------ | -------- | --- |
|     | dark                          | Noclocksignal                        |          |     |
|     | solidgreen                    | Validreferenceorsynchronizationclock |          |     |
|     | solidred                      | Invalidreferencefrequency            |          |     |
|     | solidblue                     | Ext. clockvalid,butnotinuse          |          |     |
|     | fastblinkingred               | Calibrationerroronatleastonechannel  |          |     |
|     | blinkingred(hardware<v1.5)    | InvalidsignalatSYNCIN                | (AUXIN1) |     |
|     | blinkingyellow(hardware<v1.5) | InvalidsignalatLOOPIN                | (AUXIN2) |     |
|     | Table10: LEDnexttotheSYNCIN   | input(hardware>=v1.5)                |          |     |
Color Description
|     | dark NosynchronizeronCLK | input |     |     |
| --- | ------------------------ | ----- | --- | --- |
green ValidsignalatSYNCIN
red InvalidsignalatSYNCIN
| 56  |     |     | Chapter5. | Hardware |
| --- | --- | --- | --------- | -------- |

TimeTaggerUserManual,Release2.17.4.0
Table11: LEDnexttotheLOOPIN input(hardware>=v1.5)
Color Description
dark NosynchronizeronCLK input
green ValidsignalatLOOPIN
red InvalidsignalatLOOPIN
5.3.3 Time Tagger 20
The“Power”LEDturnsgreenwhenthepowerissuppliedtothedevice.
Table12: StatusLED
Color Description
solidgreen Firmwareloaded
blinkinggreen-orange Timetagsarestreaming
red
Overflowsoccurred.
LEDturnsredfor0.1soneveryoverflowevent.
Solidredindicatescontinuousoverflows.
solidblue
Deviceinitializationfailed
(checkUSBconnection)
5.4 Test signal
TheTimeTaggerhasabuilt-intestsignalgeneratorthatgeneratesasquarewavewithafrequencyintherange0.8to
1.0MHz. Youcanapplythetestsignaltoanyinputchannelinsteadofanexternalinput. Thisisespeciallyusefulfor
testing,calibratingandsettinguptheTimeTaggerinitially. TheTimeTaggerX alsoprovidestheopportunitytoput
outtwosquarewavesignalswithavariablefrequencyviatheAUXOutportsonthebackofthedevice.
5.5 Synthetic input delay
You can introduce an input delay for each channel independently. This is useful if the relative timing between two
channelsisimportant,e.g.,tocompensateforpropagationdelayincablesofunequallength. Theinputdelaycanbe
setindividuallyforrisingandforfallingedges.
5.4. Testsignal 57

TimeTaggerUserManual,Release2.17.4.0
5.6 Synthetic dead time
You can introduce a synthetic dead time for each channel independently. This is useful when you want to suppress
consecutive clicks that are closely separated, e.g., to suppress after-pulsing of avalanche photodiodes or as a simple
wayofdataratereduction. Thedeadtimecanbesetindividuallyforrisingandforfallingedgesineachchannel.
5.7 Event divider
Youcanintroduceaneventdividerforeachchannelindependently. Thisisusefultodiscardagivennumberoftime
tagsbeforethenextoneisstored,e.g.,toreducethedatatransferraterequirementatexpenseofthedataaccumulation
efficiency. Theeventdividercanbesetindividuallyforrisingandforfallingedges.
5.8 Conditional Filter
TheConditionalFilterallowsyoutodecreasethetimetagratewithoutlosingthosetimetagsthatarerelevanttoyour
application, for instance, where you have a high-frequency signal applied to at least one channel. Examples include
fluorescencelifetimemeasurementsoropticalquantuminformationandcryptography,whereyouwanttocapturesyn-
chronizationclicksfromahighrepetitionrateexcitationlaser.
To reduce the data rate, you discard all synchronization clicks, except those that follow after one of your low rate
detectorclicks,therebyformingareducedtimetagstream. Thesoftwareprocessesthereducedtimetagstreaminthe
exactsamefashionasthefulltimetagstream.
ThisfeatureisenabledbytheConditionalFilter. AsallchannelsonyourTimeTagger arefullyequivalent, youcan
specifywhichchannelsarefilteredandwhichchannelsareusedastriggersthatenablethetransmissionofasubsequent
tagonthefilteredchannels.
Note: InTimeTagger20,thesoftware-definedinputdelays,assetbythemethodsetInputDelay(),donotapplyto
theConditionalFilterlogic.
MoredetailsandexplanationscanbefoundintheInDepthGuide: ConditionalFilter.
5.9 Bin equilibration
Thediscretizationofelectricalsignalsisneverperfect. Intime-to-digitalconversion,thismanifestsassmalldifferences
(fewps)inthebinsizesinsidetheconverterthatevenvariesfromchiptochip. Thisimperfectionisinherenttoany
time-to-digitalconversionhardware. Itisusuallynotapparenttotheuser. However, whencorrelationsbetweentwo
channels are measured on short time scales, you might see this as a weak periodic ripple on top of your signal. We
√
reducetheeffectofthisinthesoftwareatthecostofadecreaseinthetimeresolutionby 2. Thisfeatureisenabled
bydefault. Ifyourapplicationrequirestimeresolutiondowntothejitterlimit,youcandisablethisfeature.
58 Chapter5. Hardware

TimeTaggerUserManual,Release2.17.4.0
5.10 Overflows
TheTimeTagger20iscapableofcontinuousstreamingofabout9MTags/s. FortheTimeTaggerUltraandTimeTagger
X,continuoustagsstreamedcanexceed80MTags/s,dependingontheCPUofthePCtheTimeTaggerisattachedto.
Higher data rates for short times are buffered internally, so that no overflow occurs. If continuous higher data rates
persist,theinternalbuffergetscompletelyfilled. Therefore,someofthetimetagsarediscardedandnottransferredto
thePC,resultingindataloss. ThehardwareallowsyoutocheckwithTimeTaggerBase.getOverflows()whether
anoverflowconditionhasoccurred. Ifnooverflowisreturned,youcanbeconfidentthateverytimetagisreceived.
Note: Whenoverflowsoccur,TimeTaggerwillstillproducevaliddatablocksanddiscardtheinvalidtagsinbetween.
Yourmeasurementdatamaystillbevalid,althoughyouracquisitiontimewilllikelyincrease.
5.11 External Clock Input
Note: An alternative and more flexible way to apply an external clock signal is the use of TimeTaggerBase.
setSoftwareClock(). Since software version 2.10, the software clock is recommended for applying an external
clock.
TimeTaggerX andTimeTaggerUltra
TheexternalclockinputcanbeusedtosynchronizedifferentTimeTaggerdevices. Theinputclockfrequencymust
be 10 or 500 MHz. The CLK input requires between 100 mVpp and 4 Vpp AC coupled into 50 Ohm, 500 mVpp
is recommended. The lock status can be read off the LED color: If the CLK LED shines green, the Time Tagger is
lockedandusestheprovidedclock. IftheLEDisblue,avalidfrequencyissupplied,however,theTimeTaggerisstill
configuredtousetheinternalclockingsource. Incaseofawrongorunstablefrequency, theLEDwillshinered. A
500MHzCLK inputwithoutaSynchronizerwillleadtoredLEDsonLOOPIN andSYNCIN.Yet,theTimeTagger
willstillworknormallyandtheLEDscanbeignoredinthiscase.
Externalclocksignalrequirements:
TheinputclocksignalmusthaveaverylowjittertoprovidethespecifiedperformanceoftheTimeTagger. Pleasenote
thatthetimingspecificationsfortheTimeTaggerUltrawithrespecttootherdevicesonthesameclockareonlymet
fromhardwareversion2.3andlater.
Caution: In order to reach the specified input jitter for the Time Tagger with an external clock, the in-
put signals must be uncorrelated to the external clock. This restriction does not exist for TimeTaggerBase.
setSoftwareClock().
5.10. Overflows 59

TimeTaggerUserManual,Release2.17.4.0
TimeTagger20
TheTimeTagger20supportssoftwareclockfeatureonly.
5.12 Synchronization signals
TimeTaggerX andTimeTaggerUltra
Upto8TimeTaggerUltraand/orTimeTaggerXunitscanbesynchronizedinsuchawaythattheybehavelikeaunified
Time Tagger. This requires additional hardware, the Swabian Synchronizer. The Synchronizer uses the additional
hardwareconnections: SYNCIN,LOOPIN,LOOPOUT andFDBKOUT (seeSynchronizer).
Warning: On Time Tagger Ultra units sold before September 2020, the synchronization signals use the ports
labeledAUXIN1,AUXIN2,AUXOUT1,AUXOUT2. AmappingofthesignalnamesisincludedintheSynchro-
nizerdocumentation(seeSynchronizer). Ifyouownoneoftheseunitsandwouldliketohaveastickertoupdate
yourlabels,pleasereachouttoSwabianInstrumentssupport.
TimeTagger20
SynchronizationofmultipleTimeTagger20devicesisnotpossible.
5.13 FPGA link
TimeTaggerX
TheEthernetbasedFPGAlinkcanbeusedforconnectingcustomer’sFPGAdesignsdirectlytotheTimeTaggerX.The
connectionisprovidedthrougheitherSFP+orQSFP+connectoronthebackpaneloftheTimeTaggerX.Eitherone
ofthemcanbeactiveandshallbeusedforconnectionofcustomer’sdesignusingeitheraDirectAttachCable(DAC)
oropticalfibertransceiver. MoredetailsandexplanationscanbefoundintheInDepthGuide: FPGAlink.
TimeTaggerUltraandTimeTagger20
TimeTaggerUltraandTimeTagger20havenosupportforFPGAlink.
5.14 General purpose IO (GPIO)
TimeTaggerUltra
StartingfromtheTimeTaggerv2.6.6,thegeneralpurposeinputsandoutputsonTimeTaggerUltraareusedforsyn-
chronizationsignals. NewTimeTaggerUltradeviceswillhaveupdatedlabelingoftheseIOports. See,Synchronizer
60 Chapter5. Hardware

TimeTaggerUserManual,Release2.17.4.0
TimeTagger20
The Time Tagger 20 is equipped with four general purpose IO ports that interface directly with the system’s FPGA.
Thesearereservedforfutureimplementations.
5.14. GeneralpurposeIO(GPIO) 61

TimeTaggerUserManual,Release2.17.4.0
| 62  | Chapter5. | Hardware |
| --- | --------- | -------- |

CHAPTER
SIX
SOFTWARE OVERVIEW
AttheheartoftheTimeTagger softwareisamulti-threadedprocessingenginethatreceivesthetimetagstreamand
feeds it to all running measurements. The measurements and the virtual channels are parallel processing units that
analyze the time tag stream each in their own way. For example, a count rate measurement analyzes all time tags
fromoneormorespecificchannelsandcalculatestheaveragenumberoftagsreceivedpersecond. Across-correlation
measurement compute the cross-correlation between two channels, typically by sorting the time tags in histograms,
andsoon. Suchapowerfularchitectureenablesyoutoperformanythinkabledigitaltimedomainmeasurementinreal
time. Youhaveseveralchoicesonhowtousethisarchitecture.
6.1 Graphical User Interfaces
The easiest way of using the Time Tagger is one of the graphical user interfaces, either Time Tagger Lab (only on
WindowsOS)ortheWebApplication. Theyallowyoutointeractwiththehardwareonyourcomputeroratablet. You
cancreatemeasurements,getliveplots,andsaveandloadtheacquireddata.
6.2 Precompiled libraries and high-level language bindings
We have implemented a set of commonly useful measurements including count rates, auto-correlation, cross-
correlation, fluorescencelifetimeimaging(FLIM(Fluorescence-lifetimeimagingmicroscopy)), etc. Formostusers,
thesemeasurementswillcoverallneeds. ThesemeasurementsareincludedintheC++APIandprovidedasprecom-
piled library files. To make using the Time Tagger even easier, we have equipped these libraries with bindings to
higher-level languages (Python, Matlab, LabVIEW, .NET) so that you can directly use the Time Tagger from these
languages. WiththisAPIyoucaneasilystartacomplexmeasurementfromahigher-levellanguagewithonlytwolines
ofcode. TouseoneoftheseAPIs,youhavetowritethecodeinthehigh-levellanguageofyourchoice. Refertothe
chaptersGettingStarted andApplicationProgrammingInterfaceifyouplantousetheTimeTaggerinthisway.
6.3 C++ API
TheunderlyingsoftwarearchitectureisprovidedbyaC++APIthatimplementstwoclasses: oneclassthatrepresents
the Time Tagger and one class that represents a base measurement. On top of that, the C++ API also provides all
predefinedmeasurementsthataremadeavailablebythewebapplicationandhigh-levellanguagebindings. Tousethis
API,youhavetowriteandcompileaC++program.
63

TimeTaggerUserManual,Release2.17.4.0
| 64  | Chapter6. | SoftwareOverview |
| --- | --------- | ---------------- |

CHAPTER
SEVEN
|     |     |     |     | APPLICATION |     | PROGRAMMING | INTERFACE |
| --- | --- | --- | --- | ----------- | --- | ----------- | --------- |
TheTimeTaggerAPIprovidesmethodstocontrolthehardwareandtocreatemeasurementsthatarehookedontothe
timetagstream. ItiswritteninC++andwealsoprovidewrapperclassesforseveralcommonhigher-levellanguages
(Python, Matlab, LabVIEW,.NET).Maintainingthistransparentequivalencebetweendifferentlanguagessimplifies
documentation and allows you to choose the most suitable language for your experiment. The API includes a set of
standardmeasurementsthatcovercommontasksrelevanttophotoncountingandtime-resolvedeventmeasurements.
Theseclasseswillmostlikelycoveryourneedsand,ofcourse,theAPIprovidesyouapossibilitytoimplementyour
owncustommeasurements. Custommeasurementscanbecreatedinoneofthefollowingways:
• SubclassingtheIteratorBaseorCustomMeasurementclass(bestperformance,butonlyavailableintheC++,
C#andPythonAPI-seeexampleintheinstallationfolder)
| • UsingtheTimeTagStream |     |     | measurementandprocessingtherawtimetagstream. |     |     |     |     |
| ----------------------- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
• Offline processing when you store time-tags into a file using FileWriter and then read the resulting file to
performdesiredanalysisofthetime-tags. Thisalsoenablestokeeparecordofthecompletechronologyofthe
eventsinyourexperiment.
7.1 Examples
OftenthefastestwaytogetanimpressionontheAPIisthroughexamples. Severalexamplesformultipleprogramming
languagesareavailableintheTimeTaggerinstallationfolder.
| 7.1.1 Measuring |     | cross-correlation |     |     |     |     |     |
| --------------- | --- | ----------------- | --- | --- | --- | --- | --- |
Thecodebelowshowsasimpleyetoperationalexampleofhowtoperformacross-correlationmeasurementwiththe
TimeTaggerAPI.Infact,suchsimplecodeisalreadysufficienttoperformreal-worldexperimentsinalab.
| # Create                   | an instance        |        | of the TimeTagger |                 |              |         |     |
| -------------------------- | ------------------ | ------ | ----------------- | --------------- | ------------ | ------- | --- |
| tagger =                   | createTimeTagger() |        |                   |                 |              |         |     |
| # Adjust                   | trigger            | level  | on channel        | 2 to 0.25       | Volt         |         |     |
| tagger.setTriggerLevel(2,  |                    |        | 0.25)             |                 |              |         |     |
| # Add time                 | delay              | of 123 | picoseconds       | on the          | channel      | 3       |     |
| tagger.setInputDelay(3,    |                    |        | 123)              |                 |              |         |     |
| # Create                   | Correlation        |        | measurement       | for events      | in channels  | 2 and 3 |     |
| corr = Correlation(tagger, |                    |        | 2,                | 3, binwidth=10, | n_bins=1000) |         |     |
(continuesonnextpage)
65

TimeTaggerUserManual,Release2.17.4.0
(continuedfrompreviouspage)
| # Run Correlation        |     | for 1 | second      | to accumulate | the data |     |
| ------------------------ | --- | ----- | ----------- | ------------- | -------- | --- |
| corr.startFor(int(1e12), |     |       | clear=True) |               |          |     |
corr.waitUntilFinished()
| # Read the | correlation |     | data |     |     |     |
| ---------- | ----------- | --- | ---- | --- | --- | --- |
data = corr.getData()
| 7.1.2 Using | virtual | channels |     |     |     |     |
| ----------- | ------- | -------- | --- | --- | --- | --- |
TimeTaggerAPIimplementson-the-flytime-tagprocessingthroughvirtualchannels. Thefollowingexampleshows
howtime-tagsfromtwodifferentrealchannelscanbecombinedintoonevirtualchannel.
| tagger = | createTimeTagger() |     |     |     |     |     |
| -------- | ------------------ | --- | --- | --- | --- | --- |
# Enable internal generator to channels 1 and 2. Frequency ~800 kHz.
| tagger.setTestSignal([1,2], |     |     |     | True) |     |     |
| --------------------------- | --- | --- | --- | ----- | --- | --- |
# Create virtual channel that combines time-tags from real inputs 1 and 2
| vc = Combiner(tagger, |     | [1, | 2]) |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- |
# Create countrate measurement at channels 1, 2 and the "combiner" channel
| rate = Countrate(tagger, |     |     | [1, | 2, vc.getChannel()]) |     |     |
| ------------------------ | --- | --- | --- | -------------------- | --- | --- |
# Run Countrate for 1 second and print the result for all three channels
| rate.startFor(int(1e12), |     |     | clear=True) |     |     |     |
| ------------------------ | --- | --- | ----------- | --- | --- | --- |
rate.waitUntilFinished()
print(rate.getData())
| >> [ 800008.81 |     | 800008.81 | 1600017.62] |     |     |     |
| -------------- | --- | --------- | ----------- | --- | --- | --- |
Fromtheresults,weseethatthecombinedeventrateisasumoftheeventratesatbothinputchannels,asexpected.
| 7.1.3 Using | multiple |     | Time | Taggers |     |     |
| ----------- | -------- | --- | ---- | ------- | --- | --- |
YoucanusemultipleTimeTaggersononecomputersimultaneously. Inthiscase,youusuallywanttoassociateyour
instance of the TimeTagger class to the Time Tagger device. This is done by specifying the serial number of the
device,anoptionalparameter,tothefactoryfunctioncreateTimeTagger().
| tagger_1 | = createTimeTagger("123456789ABC") |     |     |     |     |     |
| -------- | ---------------------------------- | --- | --- | --- | --- | --- |
| tagger_2 | = createTimeTagger("123456789XYZ") |     |     |     |     |     |
TheserialnumberofaphysicalTimeTaggerisastringofdigitsandletters(everyTimeTaggerhasauniquehardwarese-
rialnumber). ItisprintedonthelabelatthebottomoftheTimeTaggerhardware. Inaddition,thescanTimeTagger()
method shows the serial numbers of the connected but not instantiated Time Taggers. It is also possible to read the
serialnumberforaconnecteddeviceusingTimeTagger.getSerial()method.
YoucanfindmoreexamplessuppliedwiththeTimeTaggersoftware. Pleaseseetheexamples\<language>subfolder
of your Time Tagger installation. Usually, the installation folder is C:\Program Files\Swabian Instruments\
Tagger.
Time
| 66  |     |     |     |     | Chapter7. | ApplicationProgrammingInterface |
| --- | --- | --- | --- | --- | --------- | ------------------------------- |

TimeTaggerUserManual,Release2.17.4.0
| 7.1.4 Using | Time |     | Tagger | remotely |     |     |     |
| ----------- | ---- | --- | ------ | -------- | --- | --- | --- |
UsingNetworkTimeTaggeryoucanstreamthetime-tagstoaremotecomputer(s)andprocessthemindependently.
YoucaneasilyworkwithyourTimeTaggerdeviceoverthenetworkasifyourremotecomputerisconnecteddirectly
tothehardware. Thisexampleshowshowyoucanstarttheserver,connectaclienttoitandperformasimplecountrate
measurement.
YoucanstarttheserverbycallingTimeTagger.startServer()onaexistingTimeTaggerobject.
| # Connected | to                 | the hardware |      | as     | usual |                 |     |
| ----------- | ------------------ | ------------ | ---- | ------ | ----- | --------------- | --- |
| tagger =    | createTimeTagger() |              |      |        |       |                 |     |
| # Start     | the server         | with         | full | remote |       | control enabled |     |
tagger.startServer(AccessMode.Control)
| # Keep this  | process |     | running |         |        |              |     |
| ------------ | ------- | --- | ------- | ------- | ------ | ------------ | --- |
| input('Press | ENTER   | to  | exit    | the     | server | process...') |     |
| # Stop the   | server  | if  | user    | pressed | ENTER  | key          |     |
tagger.stopServer()
| # Disconnect | from | the | hardware |     |     |     |     |
| ------------ | ---- | --- | -------- | --- | --- | --- | --- |
freeTimeTagger(tagger)
Forsimplicityoftheexampleweassumethattheserverisrunningasaseparateprocessonthesamecomputer. There-
fore, we run the client code on the same computer and use localhost as a server address. You can also adjust the
serveraddressandtrytheclientcodeonanotherPC.
| # Server  | address,      | we     | assume | it  | runs | on the same computer |     |
| --------- | ------------- | ------ | ------ | --- | ---- | -------------------- | --- |
| address   | = 'localhost' |        |        |     |      |                      |     |
| # Connect | to the        | server |        |     |      |                      |     |
ttn = createTimeTaggerNetwork(address)
| # Enable             | test signal |     | on the      | remote | hardware |                    |          |
| -------------------- | ----------- | --- | ----------- | ------ | -------- | ------------------ | -------- |
| ttn.setTestSignal(1, |             |     | True)       |        |          |                    |          |
| ttn.setTestSignal(2, |             |     | True)       |        |          |                    |          |
| # Create             | `Countrate` |     | measurement |        | and      | run it for a fixed | duration |
| cr = Countrate(ttn,  |             |     | [1,2,3])    |        |          |                    |          |
cr.startFor(1e12)
cr.waitUntilFinished()
| # Print | the resulting |     | data |     |     |     |     |
| ------- | ------------- | --- | ---- | --- | --- | --- | --- |
print(cr.getData())
| # Close | the connection |     | to  | the server |     |     |     |
| ------- | -------------- | --- | --- | ---------- | --- | --- | --- |
freeTimeTagger(ttn)
7.1. Examples 67

TimeTaggerUserManual,Release2.17.4.0
7.2 The TimeTagger Library
TheTimeTaggerLibrarycontainsclassesforhardwareaccessanddataprocessing. Thissectioncoverstheunitsand
terminologydefinitionsaswellasdescribesconstantsandfunctionsdefinedatthelibrarylevel.
7.2.1 Units of measurement
Timeismeasuredandspecifiedinpicoseconds. Time-tagsindicatetimesincedevicestart-up,whichisrepresentedby
a64-bitintegernumber. Notethatthisimpliesthatthetimevariablewillrolloveronceapproximatelyevery107days.
Thiswillmostlikelynotberelevanttoyouunlessyouplantorunyoursoftwarecontinuouslyoverseveralmonths,and
youaretakingdataattheinstancewhentherolloverishappening.
AnalogvoltagelevelsarespecifiedinVolts.
7.2.2 Channel numbers
YoucanusetheTimeTaggertodetectbothrisingandfallingedges. ThroughoutthesoftwareAPI,therisingedges
arerepresentedbypositivechannelnumbersstartingfrom1andthefallingedgesarerepresentedbynegativechannel
numbers. Virtualchannelswillautomaticallyobtainnumbershigherthanthepositivechannelnumbers.
The Time Taggers delivered before mid 2018 have a different channel numbering. More details can be found in the
ChannelNumberSchema0and1section.
7.2.3 Unused channels
Theremightbetheneedtoleaveaparameterundefinedwhencallingaclassconstructor. Dependingontheprogram-
minglanguageyouareusing,youpassanundefinedchannelviathestaticconstantCHANNEL_UNUSED,whichcanbe
foundintheTTclassfor.NETandintheTimeTaggerclassinMatlab.
7.2.4 Constants
CHANNEL_UNUSED
Canbeusedinsteadofachannelnumberwhennospecificchannelisassumed. InMATLAB,useTimeTagger.
CHANNEL_UNUSED.
7.2.5 Enumerations
class AccessMode
Controls how the Time Tagger server delivers the data-blocks to the connected clients, and if the clients are
allowedtochangethehardwaresettings.
Control
ClientshavecontroloverallsettingsontheTimeTagger. Thedata-blocksaredeliveredasynchronouslyto
everyclient.
Listen
ClientscannotchangesettingsontheTimeTaggerandonlysubscribetotheexposedchannels. Thedata-
blocksaredeliveredasynchronouslytoeveryclient.
68 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
SynchronousControl
ThesameasAccessMode.Controlbutthedataisdeliveredsynchronouslytoeveryclient.
Warning: Thismodeisnotrecommendedforgeneraluse. Theserverwillattempttodeliveradata-
block to every connected client before sending the next data-block. Therefore, the data transmission
willalwaysbelimitedbytheslowestclient. Ifanyoftheclientscannothandlethedataratefastenough
comparedtothedata-rateproducedbytheTimeTaggerhardware,allconnectedclientswillbeaffected
andtheTimeTaggerhardwarebuffermayoverflow. Thiscanhappenduetothenetworkspeedlimitor
insufficientCPUspeedonanyoftheconnectedclients.
class ChannelEdge
SelectsthechannelsthatTimeTagger.getChannelList()returns.
All
RisingandfallingedgesofchannelswithHighResandStandardresolution.
Rising
RisingedgesofchannelswithHighResandStandardresolution.
Falling
FallingedgesofchannelswithHighResandStandardresolution.
HighResAll
RisingandfallingofchannelsedgeswithHighResresolution.
HighResRising
RisingedgesofchannelswithHighResresolution.
HighResFalling
FallingedgesofchannelswithHighResresolution.
StandardAll
RisingandfallingedgesofchannelswithStandardresolution.
StandardRising
RisingedgesofchannelswithStandardresolution.
StandardFalling
FallingedgesofchannelswithStandardresolution.
class CoincidenceTimestamp
DefineswhattimestamptouseforacoincidenceeventinCoincidence/Coincidences.
Last
Usethelasttime-tagtodefinethetimestampofthecoincidence.
Average
Calculate the average timestamp of all time-tags in the coincidence and use it as the timestamp of the
coincidence.
First
Usethefirsttime-tagtodefinethetimestampofthecoincidence.
ListedFirst
Use the timestamp of the channel at the first position of the list when Coincidence or a group of
Coincidencesisinstantiated.
7.2. TheTimeTaggerLibrary 69

TimeTaggerUserManual,Release2.17.4.0
class FpgaLinkInterface
DetermineswhichEthernetPortontheTimeTaggerX shouldbeusedinTimeTagger.enableFpgaLink().
SFPP_10GE
UsetheSFP+PortontheTimeTaggerX forFPGAlinkoutput.
QSFPP_40GE
UsetheQSFP+PortontheTimeTaggerX forFPGAlinkoutput.
class GatedChannelInitial
TheinitialstateofaGatedChannel.
Closed = 0
Thegateisclosedinitially.
Open = 1
Thegateisopeninitially.
class Resolution
Defines the resolution mode of the Time Tagger on connection using createTimeTagger(). Details on the
availableinputsarelistedinthehardwareoverview.
Standard
Useonetime-to-digitalconversionperchannel. Allphysicalinputscanbeused.
HighResA
√
Usetwotime-to-digitalconversionsperchannel. Theresolutionisincreasedbyafactorof≃ 2compared
totheStandardmode,butonlyareducednumberofcertaininputscanbeused. Someinputsmayremain
inStandardmodedependingonyourlicense.
HighResB
Usefourtime-to-digitalconversionsperchannel. Theresolutionisincreasedbyafactorof≃2compared
totheStandardmode,butonlyareducednumberofcertaininputscanbeused. Someinputsmayremain
inStandardmodedependingonyourlicense.
HighResC
√
Useeighttime-to-digitalconversionsperchannel. Theresolutionisincreasedbyafactorof≃ 8compared
totheStandardmode,butonlyareducednumberofcertaininputscanbeused. Someinputsmayremain
inStandardmodedependingonyourlicense.
class TagType
Thisenumerationdescribestheoverflowcondition.
TimeTag = 0
Anormaleventfromanyinputchannel,nooverflow.
Error = 1
An error in theinternal data processing, e.g. on plugging the external clock. This invalidates the global
time.
OverflowBegin = 2
Marksthebeginningofanintervalwithincompletedatabecauseoftoohighdatarates.
OverflowEnd = 3
Markstheendoftheinterval. Allevents,whichwerelostinthisinterval,havebeenhandled
70 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
MissedEvents = 4
Thisvirtualeventsignalsthenumberoflosteventsperchannelwithinanoverflowinterval. Mightbesent
repeatedlyforlargernumberoflostevents.
class UsageStatisticsStatus
Disabled = 0
Usagestatisticscollectionanduploadisdisabled.
Collecting = 1
Enable usage statistics collection local but without automatic uploading. This option might be useful to
collectusagestatisticsfordebuggingpurpose.
CollectingAndUploading = 2
Enableusagestatisticscollectionandautomaticupload
7.2.6 Functions
[ ]
createTimeTagger( serial='',resolution=Resolution.Standard )
EstablishestheconnectiontoafirstavailableTimeTaggerdeviceandcreatesaTimeTaggerobject. Optionally,
theconnectiontoaspecificdevicecanbeachievedbyspecifyingthedeviceserialnumber.
IftheHighResmodeisavailable,itcanbeselectedfromResolution. Detailsontheavailableinputsarelisted
inthehardwareoverview.
InMATLAB,thisfunctionisaccessedasTimeTagger.createTimeTagger.
Parameters
• serial(str)–Serialnumberstringofthedeviceoremptystring
• resolution (Resolution) – Select the resolution of the Time Tagger. The default is
Resolution.Standard.
Returns
TimeTaggerobject
Returntype
TimeTagger
Raises
RuntimeError–ifnoTimeTaggerdevicesareavailableoriftheserialnumberisnotcorrect.
createTimeTaggerVirtual()
CreatesavirtualTimeTaggerobject. VirtualTimeTaggerusestime-tagdumpfile(s)asadatasourceinsteadof
Timetaggerhardware. ThisallowsyoutouseallTimeTaggerlibrarymeasurementsforofflineprocessingofthe
dumpedtimetagstream. Forexample,youcanrepeattheanalysisofyourexperimentwithdifferentparameters,
likedifferentbinwidthsetc.
InMATLAB,thisfunctionisaccessedasTimeTagger.createTimeTaggerVirtual.
Returns
TimeTaggerVirtualobject
Returntype
TimeTaggerVirtual
7.2. TheTimeTaggerLibrary 71

TimeTaggerUserManual,Release2.17.4.0
[ ]
createTimeTaggerNetwork( address='localhost:41101' )
CreatesanewTimeTaggerNetworkobject. Duringcreation,theobjecttriestoopenaconnectiontothespecified
Time Tagger server that has been created by TimeTagger.startServer(). This makes the remote time-tag
streamlocallyavailable. Iftheconnectionfails,themethodwillthrowanexception.
InMATLAB,thisfunctionisaccessedasTimeTagger.createTimeTaggerNetwork.
Parameters
address(str)–IPaddress,hostname,ordomain-nameoftheserver,wheretheTimeTagger
server is running. The port number is optional and can be specified if server listens on a port
otherthandefault41101.
Returns
TimeTaggerNetworkobjectthatcanbeused,e.g.,formeasurements
Returntype
TimeTaggerNetwork
Raises
• RuntimeError–iftheconnectiontotheservercannotbemade.
• ValueError–iftheaddressstringhasaninvalidformat.
[ ]
getTimeTaggerServerInfo( address='localhost:41101' )
Returns TimeTagger configuration, exposed channels, hardware channels and virtual channels as a JSON for-
mattedstring.
Parameters
address (str) – IP address, hostname or domain-name of the server, where the Time Tagger
server is running. The port number is optional and can be specified if server listens on a port
otherthandefault41101.
Returns
Informationaboutserver,availablechannelsandexposedchannels.
Returntype
strordict
Raises
• RuntimeError–iftheconnectiontotheservercannotbemade.
• ValueError–iftheaddressstringhasaninvalidformat.
freeTimeTagger(tagger)
ReleasesallTimeTaggerresourcesandterminatestheactiveconnection.
Parameters
tagger(TimeTaggerBase)–TimeTaggerBaseobjecttodisconnect
scanTimeTagger()
ReturnsalistoftheserialnumbersoftheconnectedbutnotinstantiatedTimeTaggers.
InMATLABthisfunctionisaccessibleasTimeTagger.scanTimeTagger().
Returns
Listofserialnumbers
Returntype
list[str]
72 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
scanTimeTaggerServers()
ScansthenetworkforavailableTimeTaggerservers.
Note: TheserverdiscoveryalgorithmusesmulticastUDPmessagessenttotheaddress239.255.255.83:41102.
Thismethodisexpectedtoworkwellinmostsituations,howeverthereisapossibilitywhenitcouldfail. The
serversmaynotbediscoverableifthesystemfirewallrejectsmulticasttrafficorblocksaccesstoUDPport41102.
Additionally,multicasttrafficistypicallynotforwardedtootherIPnetworksbyrouters.
Returns
AlistofaddressesoftheTimeTaggerserversthatareavailableinthenetwork.
Returntype
list[str]
setLogger(callback)
Registersacallbackfunction,e.g. forcustomizederrorhandling. Pleaseseetheexamplesintheinstallationfolder
onhowtouseit. Callbackfunctionshallhavethefollowingsignaturecallback(level,message). Bydefault,the
logmessagesareprintedintotheconsole.
Pythonexample:
def logger_func(level, message):
print(level, message)
setLogger(logger_func)
Matlabexample:
function logger_func(level, message)
fprintf('%d : %s\n', level, message)
end
TimeTagger.setLogger(@logger_func)
setTimeTaggerChannelNumberScheme(intscheme)
Deprecatedsinceversion2.17: allvaluesofschemeexceptfor1aredeprecated
Selectswhetherthefirstphysicalchannelstartswith0or1.
This method is deprecated and will be removed soon. The only purpose of this method
is to call setTimeTaggerChannelNumberScheme(TT_CHANNEL_NUMBER_SCHEME_ONE) (with
TT_CHANNEL_NUMBER_SCHEME_ONE = 2) before createTimeTagger() for old devices (channel num-
bersstartingwith0)whichwillsuppressadeprecationwarning.
Important: ThemethodmustbecalledbeforethefirstcalltocreateTimeTagger().
getTimeTaggerChannelNumberScheme()
Deprecatedsinceversion2.17.
Returnsthecurrentlyusedchannelscheme.
Returns
Channelscheme
Returntype
int
7.2. TheTimeTaggerLibrary 73

TimeTaggerUserManual,Release2.17.4.0
mergeStreamFiles(output_filename,input_filenames,channel_offsets,time_offsets,overlap_only)
Parameters
• output_filename(str)–Filenamewheretostorethemergeresult*.ttbin.
• input_filenames(List[str])–Listofdumpfilesthatwillbemerged
• channel_offsets (List[int]) – Channelnumber offset for each *.ttbin file. Useful
wheninputfileshavethesamechannelnumbers.
• time_offsets(List[int])–Timeoffsetforeach*.ttbinfileinpicoseconds.
• overlap_only(bool)–IfTrue,thenmergeonlytheregionswherethetimeisoverlapping.
This function merges a list of time tag stream files into one file. The merged stream file can be loaded into
the TimeTaggerVirtual for processing. The file merging combines streams into one with the possibility of
specifyingaconstanttimeoffsetforeachinputstreamfile. Additionally,itispossibletospecifychannelnumber
offsetiftheinputstreamfileswererecordedfromthesamechannelnumbers,forinstance,usingtwoTimeTagger
devices. Theparametersinput_filenames,channel_offsets,andtime_offsetsshallbeofequallength.
Thisfunctionhandlesthe*.ttbinfilesthesamewayastheTimeTaggerVirtual.replay().
Seealso: FileWriter,FileReader,andTheTimeTaggerVirtualclass.
Note: When merging multiple stream files recorded at different times or from different devices, you have to
be aware of possible time base differences. This function does not rescale the data into a common time base
as this would require additional information and external synchronization signal. If you want to improve the
synchronicityofthetimebasebetweentwodevices,pleasesendthereferenceclocksignaltoanyoftheavailable
inputsofeachTimeTaggerandsetupthesoftwareclocksetSoftwareClock().
getVersion()
Returns
VersionoftheTimeTaggersoftware.
Returntype
str
Usagestatisticsdatacollection
SeealsothesectionUsageStatisticsCollection.
setUsageStatisticsStatus(status)
Parameters
status(UsageStatisticsStatus)–Newstatusoftheusagestatisticsdatacollection.
Thisfunctionallowsausertooverridethesystem-widedefaultsettingoncollectionandsubmissionoftheusage
statisticsdata. ThisfunctionoperateswithinthescopeofacurrentOSuser. Thesystem-widedefaultsettingis
givenduringtheinstallationoftheTimeTaggersoftware. Pleaseruntheinstalleragaintoallowcollectionand
uploadingortodisabletheusagestatistics.
getUsageStatisticsStatus()
Returns
Returnsthecurrentstatusoftheusagestatisticsforthecurrentuser. Thestatusisdescribedby
theUsageStatisticsStatus.
74 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
Returntype
UsageStatisticsStatus
getUsageStatisticsReport()
This function returns the current state of the usage statistics report as a JSON formatted string. If there is no
reportdataavailableoritwassubmittedjustnow,theoutputisamessage: Info: Noreportdataavailableyet. If
youhadgivenyourconsentearlierandthenrevokedit,thisfunctionwillstillreturnearlieraccumulatedreport
data.
Returns
UsagestatisticsdataencodedasJSONstring.
Returntype
str
7.2.7 Helper classes
class ChannelGate(gate_open_channel: int,gate_close_channel: int,initial: GatedChannelInitial=
GatedChannelInitial.Open)
Parameters
• gate_open_channel(int)–Numberofthechannelthatopenstheevaluationgate.
• gate_close_channel(int)–Numberofthechannelthatclosestheevaluationgate.
• initial(GatedChannelInitial)–Initialstateoftheevaluationgate.
Thisobjectdefinesanevaluationgatethatispassedtoameasurementclass. Thetime-tagstreamitselfisnotmod-
ifiedbutsectionsofthestreamcanbeexcludedfromtheevaluation. Incontrasttotime-tagstreambasedgating
(seeGatedChannel),thisconceptallowsthemeasurementclasstocalculatethecorrectdatanormalization.
7.3 TimeTagger classes
TheTimeTaggerclassesrepresentthedifferenttime-tagsourcesforyourmeasurementsandanalysis. Theseobjects
arecreatedbyfactoryfunctionsintheTimeTaggerlibrary:
TimeTaggerhardware
TheTimeTagger representsahardwaredeviceandallowsaccesstohardwaresettings. Toconnect
toahardwareTimeTaggerandtogetaTimeTaggerobject,usecreateTimeTagger().
VirtualTimeTagger
The TimeTaggerVirtual allows replaying files created with the FileWriter. To create a
TimeTaggerVirtualobject,usecreateTimeTaggerVirtual().
NetworkTimeTagger
The TimeTaggerNetwork allows the (remote) access to a Time Tagger made available
via TimeTagger.startServer(). The TimeTaggerNetwork object is created with
createTimeTaggerNetwork()whichalsoestablishesconnectiontotheserver.
7.3. TimeTaggerclasses 75

TimeTaggerUserManual,Release2.17.4.0
7.3.1 General Time Tagger features
TheTimeTaggerBaseclassdefinesmethodsandfunctionalitypresentinallTimeTaggerobjects. Thespecificclasses
below inherit from TimeTaggerBase. Every measurement and virtual channel instance requires a reference to a
TimeTaggerBaseobjecttoassociatewith.
class TimeTaggerBase
setInputDelay(channel,delay)
ConveniencemethodthatcallssetDelaySoftware()ifyouuseaTimeTagger20orthedelayis>2µs,
otherwisesetDelayHardware()iscalled.
Parameters
• channel(int)–Channelnumber
• delay(int)–Delaytimeinpicoseconds
getInputDelay(channel)
ConveniencemethodthatreturnsthesumofgetDelaySoftware()andgetDelayHardware().
Parameters
channel(int)–Channelnumber
Returns
Delaytimeinpicoseconds
Returntype
int
setDelayHardware(channel,delay)
Note: MethodisnotavailablefortheTimeTagger20.
Setanartificialdelayperchannel. Thedelaycanbepositiveornegative. Thisdelayisappliedonboardthe
TimeTaggerdirectlyafterthetime-to-digitalconversion, soitalsoaffectstheConditionalFilter. Ifyou
exceedthemaximumhardwaredelayrange,pleaseusesetDelaySoftware()instead.
Parameters
• channel(int)–Channelnumber
• delay (int) – Delay time in picoseconds, the maximum/minimum value allowed is
±2000000(±2µs)
getDelayHardware(channel)
Note: MethodisnotavailablefortheTimeTagger20.
ReturnsthevalueofthedelayappliedonboardtheTimeTaggerinpicosecondsforthespecifiedchannel.
Parameters
channel(int)–Channelnumber
Returns
Delaytimeinpicoseconds
Returntype
int
76 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
setDelaySoftware(channel,delay)
Set an artificial delay per channel. The delay can be positive or negative. This delay is applied on the
computer,soitdoesnotaffectonboardprocessessuchastheConditionalFilter.
Parameters
• channel(int)–Channelnumber
• delay(int)–Delaytimeinpicoseconds
getDelaySoftware(channel)
Returnsthevalueofthedelayappliedonthecomputerinpicosecondsforthespecifiedchannel.
Parameters
channel(int)–Channelnumber
Returns
Delaytimeinpicoseconds
Returntype
int
setDeadtime(channel,deadtime)
Setsthedeadtimeofachannelinpicoseconds. Theminimumdeadtimeisdefinedbytheinternalclock
period, which is 6 ns for the Time Tagger 20, 2 ns for the Time Tagger Ultra, and 1.333 ns for the Time
TaggerX.FortheTimeTagger20,therequesteddeadtimewillberoundedtothenearestmultipleofthe6
nsclockcycle. Theothermodelsallowforarbitrarydeadtimesgreaterthantherespectiveminimumdead
time.
As the dead time passed as an input might be altered to the rounded value, the rounded value will be
returned. Themaximumdeadtimeis393µsfortheTimeTagger20,2147µsfortheTimeTaggerUltra,
and716µsfortheTimeTaggerX.Largerdeadtimeswillresultinanexception.
Note: The specified dead time is 2.1 ns for Time Tagger Ultra and 1.5 ns for Time Tagger X. With the
defaultsettingofthehardwaredeadtimefilter,aneventarrivingbetweenthedefaulthardwaredeadtime
and the specified dead time after the last event of that channel might be dropped (e.g., an event arriving
between2nsand2.1nsafterthelasteventonthatchannelforTimeTaggerUltra).
Parameters
• channel(int)–Channelnumber
• deadtime(int)–Deadtimevalueinpicoseconds
Returns
Resultingdeadtimeinpicoseconds,thatmightberoundedtothenearestvalidvalue(mini-
mumdeadtimeormultipleoftheclockperiod).
Returntype
int
getDeadtime(channel)
Returnsthedeadtimevalueforthespecifiedchannel.
Parameters
channel(int)–Physicalchannelnumber
Returns
Deadtimevalueinpicoseconds
7.3. TimeTaggerclasses 77

TimeTaggerUserManual,Release2.17.4.0
Returntype
int
getOverflows()
Returnsthenumberofoverflows(missingblocksoftimetagsduetolimitedUSBdatarate)thatoccurred
sincestart-uporlastcalltoclearOverflows().
Returns
Numberofoverflows
Returntype
int
getOverflowsAndClear()
Returns the number of overflows that occurred since start-up and sets them to zero (see,
clearOverflows()).
Returns
Numberofoverflows
Returntype
int
clearOverflows()
Settheoverflowcountertozero.
setSoftwareClock(input_channel: int,input_frequency: float,averaging_periods: float=1000,
wait_until_locked: bool=True)
Defineinsoftwareoneoftheinputchannelsasthebaseclockforallchannels. Thisfeaturesetsupasoftware
PLL(Phase-lockedloop)andrescalesallincomingtime-tagsaccordingtothesoftwareclockdefined. The
PLLprovidesanewtimebasewith“idealclocktags”separatedbyexactlythedefinedclock_period. For
measurements,youcanuseboth,rescaledandidealclocktags.
Whilethe PLL isnotlocked, thetimebaseoftheinstrumentisinvalid. Inthiscase, thetime-tagstream
changes to the overflow mode. This means that after every call to setSoftwareClock(), you will find
overflowsbecausethePLLstartsfromanunlockedstate.
Caution: It is often useful to apply this feature in combination with TimeTagger.
setEventDivider() on the input_channel. The values of input_frequency and averaging_periods
correspondtothetransferredtime-tags,nottothephysicalfrequency. Changingthedivider indepen-
dently after setting up the software clock may lead to a failure of the locking process. Do not add
input_channeltothelistoffiltered channelsinTimeTagger.setConditionalFilter().
FortheTimeTagger20,aphaseerrorof200psneedstobeconsideredwhenusingthesoftwareclock.
Parameters
• input_channel(int)–Thephysicalchannelthatisusedassoftwareclockinput.
• input_frequency (float) – The frequency of the software clock after application of
TimeTagger.setEventDivider() (e.g. a 10 MHz clock signal with divider = 20 has
input_frequency = 500 000). The value should not deviate from the real frequency by
morethanafewpercent. Default: 10E6,for10MHz.
• averaging_periods(float)–Thenumberofcyclestoaverageover. Thesuppression
ofdiscretizationnoiseisimprovedbyahigheraveraging_periods. Ifthevalueistoolarge,
however,thiswillresultinincreasedphasejitterduetothedriftoftheinternalclockorthe
appliedsoftwareclocksignal. Default: 1000.
78 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
• wait_until_locked (bool) – Blocks the execution until the software clock is locked.
Throwsanexceptiononlockingerrors. Alllockinglogmessagesarefilteredwhilethiscall
isexecuted. Default: True
disableSoftwareClock()
Disablethesoftwareclock.
getSoftwareClockState()
Providesanobjectrepresentingthecurrentsoftwareclockstate. Thisincludestheconfigurationparameters
aswellasdynamicvaluesgeneratedbasedontheincomingsignal.
Returns
Anobjectthatcontainsthecurrentstateofthesoftwareclock.
Returntype
SoftwareClockState
getFence(alloc_fence: bool=True)
Generateanewfenceobject,whichvalidatesthecurrentconfigurationandthecurrenttime. Thisfenceis
uploadedtotheearliestpipelinestageoftheTimeTagger. Waitingonthisfenceensuresthatallhardware
settings,suchastriggerlevels,channelregistrations,etc.,havepropagatedtotheFPGAandarephysically
active. SynchronizestheTimeTaggerinternalmemorysothatalltagsarrivingafterthewaitForFence()
call were actually produced after the getFence() call. The waitForFence() function waits until all
tags,whicharepresentatthetimeofthefunctioncallwithintheinternalmemoryoftheTimeTagger,are
processed. Thiscallmightblocktolimitthenumberofactivefences.
Parameters
alloc_fence (bool) – optional, default: True. If False, a reference to the most recently
createdfencewillbereturnedinstead
Returns
Theallocatedfence
Returntype
int
waitForFence(fence,timeout: int=-1)
Waitforafenceinthedatastream. SeegetFence()formoredetails.
Parameters
• fence(int)–fenceobject,whichshallbewaitedon
• timeout (int) – (optional) Timeout in milliseconds. Negative means no timeout, zero
returnsimmediately. Default: -1.
Returns
Trueifthefencehaspassed,falseontimeout
Returntype
bool
sync(timeout: int=-1)
Ensurethatallhardwaresettings,suchastriggerlevels,channelregistrations,etc.,havepropagatedtothe
FPGAandarephysicallyactive. SynchronizestheTimeTaggerinternalmemory,sothatalltagsarriving
afterasynccallwereactuallyproducedafterthesynccall. Thesyncfunctionwaitsuntilalltags, which
arepresentatthetimeofthefunctioncallwithintheinternalmemoryoftheTimeTagger,areprocessed.
ItisequivalenttowaitForFence(getFence()).
7.3. TimeTaggerclasses 79

TimeTaggerUserManual,Release2.17.4.0
The operation of this method on the TimeTaggerNetwork depends on the server access mode. If the
TimeTaggerNetwork isconnectedtotheTimeTaggerserverstartedinAccessMode.Control,thesyn-
chronizationwillbedoneallwaythroughtheserverandthehardware. IftheTimeTaggerserverstartedin
AccessMode.Listen,theclientwillbeabletosynchronizeonlywiththeserverbutwillnotsynchronize
withtheTimeTaggerHardware. However,ifaUSBsynchronizationfencewascreatedbytheserverside,
theclientswillalsoseeit.
Seealso:
• getFence(),waitForFence(),startServer(),AccessMode
• SynchronizationoftheTimeTaggerpipeline
Parameters
timeout(int)–(optional)Timeoutinmilliseconds. Negativemeansnotimeout, zerore-
turnsimmediately. Default: -1.
Returns
Trueifthesynchronizationwassuccessful,falseontimeout
Returntype
bool
getInvertedChannel(channel)
Returnsthechannelnumberfortheinvertededgeofthechannelpassedinviathechannelparameter. In
casethegivenchannelhasnoinvertedchannel,CHANNEL_UNUSED isreturned.
Parameters
channel(int)–Channelnumber
Returns
Channelnumber
Returntype
int
isUnusedChannel(channel)
ReturnstrueifthepassedchannelnumberisCHANNEL_UNUSED.
Parameters
channel(int)–Channelnumber
Returns
True/False
Returntype
bool
getConfiguration()
ReturnsaJSONformattedstring(dictinPython)containingcompleteinformationontheTimeTagger
settings. ItalsoincludesdescriptionsofmeasurementsandvirtualchannelscreatedonthisTimeTagger
instance.
Returns
TimeTaggersettingsandcurrentlyexistingmeasurements.
Returntype
strordict
80 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
7.3.2 Time Tagger hardware
class TimeTagger
Baseclass: TimeTaggerBase
This class provides access to the hardware and exposes methods to control hardware settings, such as trigger
levels or even filters. Behind the scenes, it opens the USB connection, initializes the device and receives and
managesthetime-tag-stream.
reset()
ResettheTimeTaggertothestart-upstate.
setTriggerLevel(channel,voltage)
SetthetriggerlevelofaninputchannelinVolts.
Parameters
• channel(int)–Physicalchannelnumber
• voltage(float)–TriggerlevelinVolts
getTriggerLevel(channel)
Returnstriggerlevelforthespecifiedphysicalchannelnumber.
Parameters
channel(int)–Physicalchannelnumber
Returns
Theappliedtriggervoltagelevel,whichmightdifferfromtheinputparameterduetotheDAC
discretization.
Returntype
float
getHardwareDelayCompensation(channel)
Getthehardwareinputdelaycompensationforthegivenchannelinpicoseconds.
This compensation can be understood as an implicit part of setDelayHardware() and
setDelaySoftware(). If your device is able to set an arbitrary delay onboard, this applies to the
hardwaredelaycompensationaswell.
Parameters
channel(int)–Channelnumber
Returns
Hardwaredelaycompensationinpicoseconds
Returntype
int
setConditionalFilter(trigger,filtered,hardwareDelayCompensation=True)
Activatesordeactivatestheeventfilter. Timetagsonthefilteredchannelsarediscardedunlesstheywere
preceded by a time tag on one of the trigger channels, which reduces the data rate. More details can be
foundintheIn-DepthGuide: ConditionalFilter.
Parameters
• trigger(list[int])–Listofchannelnumbers
• filtered(list[int])–Listofchannelnumbers
7.3. TimeTaggerclasses 81

TimeTaggerUserManual,Release2.17.4.0
• hardwareDelayCompensation(bool)–optional,default: True. IfsettoFalse,thephys-
ical hardware delay will not be compensated. This is only relevant for devices without
setDelayHardware(),donotsetthisvaluetoFalseifyourdeviceiscapableofonboard
delaycompensation. Withoutonboarddelaycompensation,settingthevaluetoFalseguar-
anteesthatthetriggertagoftheconditionalfilterisalwaysinbeforethetriggeredtagwhen
theInputDelaysaresetto0.
clearConditionalFilter()
Deactivatestheeventfilter. EquivalenttosetConditionalFilter([], [], True). Enablesthephys-
icalhardwaredelaycompensationagainifitwasdeactivatedbysetConditionalFilter().
getConditionalFilterTrigger()
Returnsthecollectionoftriggerchannelsfortheconditionalfilter.
Returns
Listofchannelnumbers
Returntype
list[int]
getConditionalFilterFiltered()
Returnsthecollectionofchannelstowhichtheconditionalfilteriscurrentlyapplied.
Returns
Listofchannelnumbers
Returntype
list[int]
setEventDivider(channel,divider)
Event divider (n = 4)
t = 0 time
click skip skip skip click skip skip skip click
Applies an event divider filter with the specified factor to a channel, which reduces the data rate. Only
everyn-theventfromtheinputstreampassesthroughthefilter,asshownintheimage. Thedividerisa16
bitinteger,sothemaximumvalueis65535.
Notethatiftheconditionalfilterisalsoactive,theconditionalfilterisappliedfirst.
Parameters
• channel(int)–Physicalchannelnumber
• divider(int)–Dividerfactor,min. 1andmax. 65535
getEventDivider(channel)
Getstheeventdividerfilterfactorforthegivenchannel.
Parameters
channel(int)–Channelnumber
Returns
Dividerfactorvalue
Returntype
int
82 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
setInputImpedanceHigh(channel,state)
Note: MethodisonlyavailablefortheTimeTaggerX.
Sets the input impedance to High-Z for the specified channel. Before createTimeTagger(), after
TimeTagger.reset(), and after freeTimeTagger(), the input is in the High-Z state. If not set ex-
plicitlytoHigh-ZbysetInputImpedanceHigh(),theinputwillswitchto50Ohmbydefaultassoonas
theinputisused.
Parameters
• channel(int)–Channelnumber
• state(bool)–True/False
# Upon initialization, all inputs are in the High-Z state:
tagger = TimeTagger.createTimeTagger()
# If you want to keep a channel in High-Z, set it right after initialization:
tagger.setInputImpedanceHigh(1, True)
# The Time Tagger will now stay in High-Z on channel 1, channel 2 will switch␣
to 50 Ohm:
˓→
cr = TimeTagger.Countrate(tagger, [1, 2])
getInputImpedanceHigh(channel)
Note: MethodisonlyavailablefortheTimeTaggerX.
Returnswhethertheinputimpedanceissettohigh-Zforthespecifiedchannel.
Parameters
channel(int)–Channelnumber
Returns
stateofhighinputimpedance
Returntype
bool
setInputHysteresis(channel,value)
Note: MethodisonlyavailablefortheTimeTaggerX.
Sets the input hysteresis value for the specified channel. Oscillations of the measured signal within the
hysteresisrangearoundthetriggervalueareignoredandthereforedonottriggernewevents. Supported
valuesare1mV,20mV,70mV.Defaultinputhysteresisvalueis20mV.
Parameters
• channel(int)–Channelnumber
• value(int)–hysteresisvoltagevalueinmV(1,20,70)
7.3. TimeTaggerclasses 83

TimeTaggerUserManual,Release2.17.4.0
getInputHysteresis(channel)
Note: MethodisonlyavailablefortheTimeTaggerX.
ReturnsthevoltagevalueinmVoftheinputhysteresisforthespecifiedchannel.
Parameters
channel(int)–Channelnumber
Returns
hysteresisvoltagevalueinmV
Returntype
int
setNormalization(channels,state)
EnablesordisablesGaussiannormalizationofthedetectionjitter. Enabledbydefault.
Parameters
• channels(list[int])–Listofphysicalchannelnumbers
• state(bool)–True/False
getNormalization(channel)
ReturnsTrueifGaussiannormalizationisenabled.
Returns
True/False
Returntype
bool
setTestSignal(channels,state)
Connectordisconnectthechannelswiththeon-chipuncorrelatedsignalgenerator.
Parameters
• channels(list[int])–Listofphysicalchannelnumbers
• state(bool)–True/False
getTestSignal(channel)
Returnstrueiftheinternaltestsignalisactivatedonthespecifiedchannel.
Parameters
channel(int)–Physicalchannelnumber
Returns
True/False
Returntype
bool
getSerial()
Returnsthehardwareserialnumber.
Returns
Serialnumberstring
Returntype
str
84 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
getModel()
Returns
Modelnameasstring
Returntype
str
getPcbVersion()
ReturnsTimeTaggerPCB(Printedcircuitboard)version.
Returns
PCBversion
Returntype
str
getDACRange()
Return a vector containing the minimum and the maximum DAC (Digital-to-Analog Converter) voltage
rangeforthetriggerlevel.
Returns
MinandmaxvoltageinVolt
Returntype
(float,float)
getChannelList(type=ChannelEdge.All)
Returnsalistofchannelscorrespondingtothegiventype.
Parameters
type(ChannelEdge)–Limitsthereturnedchannelstothespecifiedchanneledgetype
Returns
Listofchannelnumbers
Returntype
list[int]
setHardwareBufferSize(size)
SetsthemaximumbuffersizewithintheTimeTagger. Thedefaultvalueis64MTags,butcanbechanged
withintherangeof32kTagsto512MTags. Pleasenotethatthisbuffercanonlybefilledwithatotaldata
rateofupto500MTags/s. Seealso,SynchronizationoftheTimeTaggerpipeline
Note: TimeTagger20usesbydefaultthewholebufferof8MTags,whichcanbefilledwithatotaldata
rateofupto40MTags/s.
Parameters
size(int)–Buffersize,mustbeapositivenumber
autoCalibration()
Runanauto-calibrationoftheTimeTaggerhardwareusingthebuilt-intestsignal.
Returns
thelistofjitterofeachinputchannelinpicosecondsbasedonthecalibrationdata.
Returntype
list[float]
7.3. TimeTaggerclasses 85

TimeTaggerUserManual,Release2.17.4.0
getDistributionCount()
Returnsthecalibrationdatarepresentedincounts.
Returns
Distributiondata
Returntype
2D_array[int]
getDistributionPSec()
Returnsthecalibrationdatainpicoseconds.
Returns
Calibrationdata
Returntype
2D_array[int]
getPsPerClock()
Returnsthedurationofaclockcycleinpicoseconds. Thisistheinverseoftheinternalclockfrequency.
Returns
Clockperiodinpicoseconds
Returntype
int
setStreamBlockSize(max_events=131072,max_latency=20)
This option controls the latency and the block size of the data stream. Depending on which of the two
parametersisexceededfirst,theblockstreamsizeisadjustedaccordingly.
Note: Theblocksizewillbereducedevenfurtherwhennonewtagarriveswithinroughly1-2µs.
Parameters
• max_events(int)–maximumnumberofeventswithinoneblock(256-32M),default:
131072events
• max_latency (int) – maximum latency in milliseconds for constant input rates (1 to
10000),default: 20ms.
setTimeTaggerNetworkStreamCompression(active)
Enables/disables the compression of TimeTags before they are streamed from the server to the clients.
Activationcanbehelpfulforslownetworkenvironments(<=100MBit/s)ifthebandwidthisthelimiting
factor. For instance, the amount of streamed data of periodic signals is reduced by about a factor of 2.
The compression, on the other hand, leads to increased CPU utilization and is not advantageous for fast
networks(>=1GBit/s).
Parameters
active(bool)–flagdefiningwhetherthecompressionisenabled(default: False).
setTestSignalDivider(divider)
Changethefrequencyoftheon-chiptestsignal.
FortheTimeTaggerX,thebasefrequencyis333.333MHzandthedefaultdivider375correspondsto~890
kCounts/s.
FortheTimeTaggerUltra,thebasefrequencyis100.800MHzandthedefaultdivider126correspondsto
~800kCounts/s.
86 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
FortheTimeTagger20, thebasefrequencyis62.5MHzandthedefaultdivider74correspondsto~850
kCounts/s.
Parameters
divider(int)–Divisionfactor
getTestSignalDivider()
Returnsthevalueoftestsignaldivisionfactor.
getDeviceLicense()
Returns a JSON formatted string (dict in Python) containing license information of the Time Tagger
device,forinstance,model,edition,andavailablechannels.
Returns
Licenseinformation
Returntype
dict
getSensorData()
PrintsaJSONformattedstring(dictinPython)containingallavailablesensordataforthegivenboard.
TheTimeTagger20hasnoonboardsensors.
Returns
Sensordata
Returntype
dict
disableLEDs(state)
Disables all channel LEDs and back LEDs. The disabling of the power button LED will follow in the
upcomingrelease.
Parameters
state(bool)–True/False
setLED(bitmask)
Manually change the state of the Time Tagger LEDs. The power LED of the Time Tagger 20 cannot be
programmedbysoftware.
Example:
# Turn off all LEDs
tagger.setLED(0x01FF0000)
# Restore normal LEDs operation
tagger.setLED(0)
0->LEDoff
1->LEDon
illuminationbits
0-2: status,rgb-allTimeTaggermodels
3-5: power,rgb-TimeTaggerUltraonly
6-8: clock,rgb-TimeTaggerUltraonly
0->normalLEDbehavior,notoverwrittenbysetLED
7.3. TimeTaggerclasses 87

TimeTaggerUserManual,Release2.17.4.0
1->LEDstateisoverwrittenbythecorrespondingbitof0-8
maskbits
16-18: status,rgb-allTimeTaggermodels
19-21: power,rgb-TimeTaggerUltraonly
22-24: clock,rgb-TimeTaggerUltraonly
Parameters
bitmask(int)–LEDbitmask.
setSoundFrequency(freq_hz)
SettheTimeTagger’sinternalbuzzertoafrequencyinHz.
Parameters
freq_hz(int)–ThesoundfrequencyinHz,use0toswitchthebuzzeroff.
enableFpgaLink(channels,destination_mac,link_interface=FpgaLinkInterface::SFPP_10GE,exclusive=
False)
EnabletheFPGAlinkoftheTimeTaggerX
Parameters
• channels(list[int])–Listofchannels,whichshallbestreamedovertheFPGAlink
• destination_mac(str)–DestinationMAC,useanemptystringforthebroadcastad-
dressof“FF:FF:FF:FF:FF:FF”
• link_interface(FpgaLinkInterface)–selectswhichinterfaceshallbeused
• exclusive(bool)–DeterminesiftimetagsshouldexclusivelybetransmittedoverEth-
ernet,increasingEthernetperformanceandavoidingUSBissues
disableFpgaLink()
DisabletheFPGAlinkoftheTimeTaggerX
startServer(access_mode,channels=[],port=41101)
StartaTimeTaggerserverthatcanbeaccessedviaTimeTaggerNetwork. Theserveraccessmodecontrols
iftheclientsareallowedtochangethehardwareparameters. Seealso: AccessMode.
Parameters
• access_mode(AccessMode)–AccessModeinwhichtheservershouldrun. Eithercon-
trolorlisten
• channels (list[int]) – Channels to be streamed. Used only when
access_mode=AccessMode.Listen
• port(int)–PortatwhichthisTimeTaggerserverwillbelisteningon.
Raises
RuntimeError–ifserverisalreadyrunning.
stopServer()
StoptheTimeTaggerserverifcurrentlyrunning,otherwisedonothing.
isServerRunning()
Returns
TrueisserverisrunningandFalseotherwise.
88 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
Returntype
bool
Note: The following xtra methods are mainly for development purposes and may be discontinued in future
softwareversionswithoutfurthernotice. Thextrasettermethodsinthisfirstsectionareonlyavailableforthe
TimeTaggerUltraandtheTimeTaggerX.
xtra_setAvgRisingFalling(channel,enable)
Configures if the rising and falling events shall be averaged. This is implemented on the device before
anyfilterlikeeventdivideranditdoesnotrequiretotransferbothevents. Theprimaryapplicationofthis
featureistheinvestigationofperiodicsignalswithdefineddutycycle.
Theyneedtobemanuallydelayedtobewithinawindowof+-500psoferror,elseeventsmightgetlost.
Thisconditionrestrictstheapplicablesignalstopulsesofconstantduration. Thismethodhasnosideeffects
onthechannelgetInvertedChannel(),youcanstillfetchtheoriginaleventsthere. Howeverifbothare
configuredtoreturntheaveragedresult,thetimestampswillbeidentical.
Parameters
• channel(int)–Thechannel,onwhichtheaveragevalueshallbereturned
• enable(bool)–Selectwhethertheaveragingfeatureisenabled
xtra_getAvgRisingFalling(channel)
Returnthestateoftheaveragingofrisingandfallingedges.
Parameters
channel(int)–Thechannelforwhichtheaveragingstateisreturned
Returns
Thecurrentenablestate
Returntype
bool
xtra_setHighPrioChannel(channel,enable)
Sets the priority state of a channel. This setting is applied on the hardware before USB transfer. If a
bufferoverflowoccurs,channelswithhigh-prioritystatewillinterrupttheoverflowmodeandbetransmit-
tedasstandardtime-tags(TagType.TimeTag). Timinginformationoflow-prioritychannelsisdismissed
inoverflowmodeandonlythenumberofcountsistransmitted(TagType.MissedEvents). Atypicalap-
plicationofthehigh-prioritychannelsisCountBetweenMarkerswithhigh-prioritymarkers. Inthiscase,
theoverflowrangewillbeideallyslicedbythemarkers.
Parameters
• channel(int)–Thechannelonwhichthehigh-prioritystateshallbeenabled
• enable(bool)–Selectwhetherhighpriorityisenabled
Caution: Interrupting the overflow mode may break the protection mechanism the overflow mode
provides. Thismayleadtoirreversiblelossofevents,notonlylossoftheirtiminginformation. High
priorityshouldonlybeassignedtolow-countratechannels,e.g. pixeltriggersorsimilarcontrolevents.
xtra_getHighPrioChannel(channel)
Gettheprioritystateofachannel.
7.3. TimeTaggerclasses 89

TimeTaggerUserManual,Release2.17.4.0
Parameters
channel(int)–Channelnumber
Returns
Thecurrentenablestateofthehigh-priorityfeatureonthischannel
Returntype
bool
Note: The following xtra methods are mainly for development purposes and may be discontinued in future
softwareversionswithoutfurthernotice. Thextrasettermethodsinthissecondsectionareonlyavailableforthe
TimeTaggerX.
xtra_setAuxOut(channel,state)
Enables/DisablestheAuxOutsignalforthespecifiedAuxchannel.
Parameters
• channel(int)–Auxchannelnumber
• state(bool)–True/False
xtra_getAuxOut(channel)
ReturnswhethertheAuxOutsignalisenabledforthespecifiedAuxchannel.
Returns
StateoftheAuxOutsignal
Returntype
bool
xtra_setAuxOutSignal(channel,divider,duty_cylce)
Setsthesignalshape,i.e.,dutycycleandfrequency,oftheAuxoutsignalforthespecifiedAuxchannel.
Parameters
• channel(int)–Auxchannelnumber
• divider(int)–DivideroftheAuxOutbasesignalfrequency(333MHz)
• duty_cycle(float)–Thedutycycleoftheauxsignal
xtra_getAuxOutSignalDivider(channel):
ReturnsthedividerforthefrequencyoftheAuxOutsignalgeneratororthespecifiedAuxchannel.
Parameters
channel(int)–Auxchannelnumber
Returns
DividerforthefrequencyoftheAuxOutsignalgenerator
Returntype
int
xtra_getAuxOutSignalDutyCycle(channel)
ReturnsthedutycycleoftheAuxOutsignalforthespecifiedAuxchannel.
Parameters
channel(int)–Auxchannelnumber
Returns
DutycycleoftheAuxOutsignalgenerator
90 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
Returntype
float
xtra_measureTriggerLevel(channel)
Measuresandreturnstheappliedvoltagethresholdofthespecifiedchannel.
Parameters
channel(int)–Channelnumber
Returns
Appliedvoltagethresholdofachannel
Returntype
float
xtra_setClockSource(source)
Specifiesthedifferentclocksources: 0-internalclock,1-externalclock10Mhz,2-externalclock500
MHz.
Parameters
source(int)–Numberoftheclocksource. Allowedvalues: 0,1,2
xtra_getClockSource()
Returnstheusedclocksource: 0-internalclock,1-externalclock10Mhz,2-externalclock500MHz.
Returns
Numberoftheclocksource
Returntype
int
xtra_setClockAutoSelect(state)
Enables/Disablestheautoclockingfunction.
Parameters
state(bool)–True/False
xtra_getClockAutoSelect()
Returnswhethertheautoclockingfunctionisenabled.
Returns
Stateofautoclocking
Returntype
bool
xtra_setClockOut(state)
Activates/Deactivatesthe10MHzclockoutput.
Parameters
state(bool)–True/False
7.3. TimeTaggerclasses 91

TimeTaggerUserManual,Release2.17.4.0
| 7.3.3 | The TimeTaggerVirtual |     | class |     |     |     |     |
| ----- | --------------------- | --- | ----- | --- | --- | --- | --- |
IntheTimeTaggersoftwareversion2.6.0,wehaveintroducedthenewTimeTaggerVirtual,whichallowsreplaying
earlierstoredtime-tagdumpfiles. UsingthevirtualTimeTagger,youcanrepeatyourexperimentdataanalysiswith
differentparametersorevenperformdifferentmeasurements.
Note: The virtual Time Tagger requires a free software license, which is automatically acquired from the Swabian
| Instruments | license server | when               |     | or                        |     | is called while | a Time |
| ----------- | -------------- | ------------------ | --- | ------------------------- | --- | --------------- | ------ |
|             |                | createTimeTagger() |     | createTimeTaggerVirtual() |     |                 |        |
Taggerisattached. Oncereceived,thelicenseispermanentlystoredonthisPCandtheVirtualTimeTaggerwillwork
withoutTimeTaggerhardwareattached.
class TimeTaggerVirtual
Baseclass:
TimeTaggerBase
replay(file,begin=0,duration=-1,queue=True)
Replay a dump file specified by its path file or add it to the replay queue. If the flag queue is false, the
currentqueuewillbediscardedandfilewillbereplayedimmediately.
Thefileparametercanspecifyaheaderfileorsinglespecificfileasshowninthefollowingexample.
|     | # Assume | we have following | the files | in the | current directory: |     |     |
| --- | -------- | ----------------- | --------- | ------ | ------------------ | --- | --- |
# filename.ttbin
# filename.1.ttbin
# filename.2.ttbin
|     | # Replay | all files | named "filename.NN.ttbin" |     | sequentially |     |     |
| --- | -------- | --------- | ------------------------- | --- | ------------ | --- | --- |
virtual_tagger.replay('filename.ttbin')
|     | # Replay | a single file | "filename.1.ttbin" |     |     |     |     |
| --- | -------- | ------------- | ------------------ | --- | --- | --- | --- |
virtual_tagger.replay('filename.1.ttbin')
Seealso: FileWriter,FileReader,andmergeStreamFiles().
Parameters
|     | •   | file(str)–thefiletobereplayed |     |     |     |     |     |
| --- | --- | ----------------------------- | --- | --- | --- | --- | --- |
• begin(int)–durationinpicosecondstoskipatthebeginningofthefile. Anegativetime
willgenerateapauseinthereplay.
• duration(int)–durationinpicosecondstobereadfromthefile. duration=-1willreplay
|     |     | everything. (default:                    | -1) |     |                 |     |     |
| --- | --- | ---------------------------------------- | --- | --- | --------------- | --- | --- |
|     | •   | queue(bool)–flagifthisfileshallbequeued. |     |     | (default: True) |     |     |
Returns
IDofthequeuedfile
Returntype
int
stop()
Thismethodstopsthecurrentfileandclearsthereplayqueue.
|     |     | [   | ]   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
ID=0,timeout=-1
| waitForCompletion( |     |     | )   |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
Blocksthecurrentthreaduntilthereplayiscompleted.
| 92  |     |     |     | Chapter7. | ApplicationProgrammingInterface |     |     |
| --- | --- | --- | --- | --------- | ------------------------------- | --- | --- |

TimeTaggerUserManual,Release2.17.4.0
Thismethodblocksthecurrentexecutionandwaitsuntilthegivenfilehasfinisheditsreplay. IfnoIDis
provided,itwaitsuntilallqueuedfilesarereplayed.
Thisfunctiondoesnotblockonazerotimeout. Negativetimeoutsareinterpretedasinfinitetimeouts.
Parameters
• ID(int)–selectswhichfiletowaitfor. (default: 0)
• timeout(int)–timeoutinmilliseconds
Returns
trueifthefileiscomplete,falseontimeout
Returntype
bool
setReplaySpeed(speed)
Configuresthespeedfactorforthevirtualtagger.
Avalueofspeed=1.0willreplayatareal-timerate. Allspeed values<0.0willreplaythedataasfastas
possiblebutstopsattheendofalldata. Thisisthedefaultvalue. Extremeslowreplayspeedbetween0.0
and0.1isnotsupported.
Parameters
speed(float)–replayspeedfactor.
getReplaySpeed()
Returnsthecurrentspeedfactor.
PleaseseealsosetReplaySpeed()formoredetails.
getConfiguration()
ReturnsaJSONformattedstring(dictinPython)containinginformationontheTimeTaggerVirtualin-
stanceandontherealTimeTaggersettingsstoredinthecurrenttimetagstreamfile.
7.3.4 The TimeTaggerNetwork class
IntheTimeTaggersoftwareversion2.10,wehaveintroducedawayofsendingthetime-tagstreamtootherapplications
andevenremotecomputersforindependentprocessing. WecallthisfeatureNetworkTimeTagger. Youcanuseitwith
any TimeTagger hardwaredevice bystarting the time-tagstream serverwith TimeTagger.startServer(). Once
theserverisrunning,theclientscanconnecttoitbycallingcreateTimeTaggerNetwork()andspecifyingtheserver
address. A client can be any computer that can access the server over the network or another process on the same
computer. Itisalsopossibletoruntheserverandclientondifferentoperatingsystemsorusedifferentprogramming
languages.
Noteonperformance
The Network Time Tagger server sends a time tag stream in a compressed format requiring about 4 bytes per time
tag. Everyclientreceivesthedataonlyfromthechannelsrequiredbytheclient. Themaximumachievabledatarate
willdependonmultiplefactors,likeserverandclientCPUperformance,operatingsystem,networkadapterused,and
networkbandwidth,aswellasthewholenetworkinfrastructure.
Ina1GbpsEthernetnetwork,itispossibletoachieveabout26MTags/secondofthetotaloutgoingdataratefromthe
server. Notethatthisbandwidthissharedamongallclientsconnected. Likewise,a10GbpsEthernetnetworkallows
reachinghigherdatarateswhilehavingmoreclients. Inourtests,wereachedupto40MTags/sperclient.
When you run the server and the client on the same computer, the speed of the network adapters installed on your
systembecomesirrelevant. Inthiscase,theoperatingsystemsendsthedatadirectlyfromtheservertotheclient.
7.3. TimeTaggerclasses 93

TimeTaggerUserManual,Release2.17.4.0
class TimeTaggerNetwork
Baseclass: TimeTaggerBase
Note: Although the TimeTaggerNetwork formally inherits from TimeTaggerBase, almost all methods of
the hardware Time Tagger TimeTagger are available on the client (except for TimeTagger.startServer()
andTimeTagger.stopServer()). Theseredundantmethodsarenotlistedinthissection. Acalltoamethod
that exists on TimeTagger will be forwarded to the server. If a method with similar functionality exists on
the TimeTaggerNetwork only, it can be distinguished by the suffix ...Client. If the server is running in
AccessMode.Listenandamethodcallforwardedtotheserverwouldcausesettingchangesontheserver-side,
thecallwillraiseanexceptionontheclient.
Thisschemeofforwardingmayleadtounexpectedbehavior:IftheserverisstartedinAccessMode.Listenwith
arestrictedsetofchannelsandyoucallTimeTagger.getChannelList()ontheclientside,notallchannels
returnedbythismethodcanbeaccessed. Youcanrequestthelistofaccessiblechannelsfromtheserverwith
getTimeTaggerServerInfo().
TheTimeTaggerNetwork representsaclient-sideoftheNetworkTimeTaggerandprovidesaccesstotheTime
Taggerserver. AservercanbecreatedonanyphysicalTimeTaggerbycallingTimeTagger.startServer().
TheTimeTaggerNetwork objectiscreatedbycallingcreateTimeTaggerNetwork().
isConnected()
CheckiftheNetworkTimeTaggeriscurrentlyconnectedtoaserver.
Returns
True/False
Return_type
bool
setDelayClient(channel,delay)
Sets an artificial software delay per channel on the client side. To specify it on the server side, see
setDelaySoftware() or setDelayHardware() (Time Tagger Ultra only). This delay will be applied
onlyonthisobjectandwillnotaffecttheserversettingsordelaysatanyotherclientsconnectedtothesame
TimeTaggerserver.
Parameters
• channel(int)–Channelnumber
• delay(int)–Delaytimeinpicoseconds
getDelayClient(channel)
Returnsthevalueofthedelayappliedontheclient-sideinpicosecondsforthespecifiedchannel.
Parameters
channel(int)–Channelnumber
Returns
inputdelayinpicoseconds
Return_type
int
clearOverflowsClient()
Clearstheoverflowcounterontheclient-side. AcalltogetOverflows()willreturntheinformationasit
isavailableontheserver. SeegetOverflowsClient()formoreinformationonclient-sideoverflows.
94 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
getOverflowsClient()
Iftheserverisnotabletosendallthetime-tagstotheclient,e.g. duetolimitednetworkbandwidth,the
time-tag stream switches to the overflow mode. This means that the client might experience additional
overfloweventsthatarenotoriginatingfromthehardware. Thiscountercountsalloverflowsoccurredon
the hardware and on the server since the client connection or last call to clearOverflowsClient() or
getOverflowsAndClearClient().
Returns
Thevalueoftheclient-sideoverflowcounter.
Return_type
int
getOverflowsAndClearClient()
| The same | as  | but also clears | the client-side | counter. | See |
| -------- | --- | --------------- | --------------- | -------- | --- |
getOverflowsClient()
getOverflowsClient()formoreinformationonclient-sideoverflows.
| 7.3.5 Additional | classes |     |     |     |     |
| ---------------- | ------- | --- | --- | --- | --- |
class SoftwareClockState
TheSoftwareClockStateobjectcontainsthecurrentconfigurationstate:
| clock_period: | int |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- |
TheroundedclockperiodmatchingtheinputfrequencysetinTimeTaggerBase.setSoftwareClock().
| input_channel: | int |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
ThephysicalinputchannelofthesoftwareclocksetinTimeTaggerBase.setSoftwareClock().
| ideal_clock_channel: | int |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- |
Avirtualchannelnumbertoreceivetheidealclocktags. Duringalockingperiod,thesetagsareseparated
byclock_period bydefinition. Toreceivetherescaledmeasuredclocktags,useclock_channel.
| averaging_periods: | float |     |     |     |     |
| ------------------ | ----- | --- | --- | --- | --- |
TheaveragingperiodssetinTimeTaggerBase.setSoftwareClock().
enabled: bool
Indicateswhetherthesoftwareclockisactiveornot.
Beyondtheconfigurationstate,theobjectprovidescurrentruntimeinformationofthesoftwareclock:
| is_locked: | bool |     |     |     |     |
| ---------- | ---- | --- | --- | --- | --- |
IndicateswhetherthePLLofthesoftwareclockwasabletolocktotheinputsignal.
| error_counter: | int |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
AmountoflockingerrorssincethelastTimeTaggerBase.setSoftwareClock()call.
last_ideal_clock_event: int
Timestampofthelastidealclockeventinpicoseconds.
| period_error: | float |     |     |     |     |
| ------------- | ----- | --- | --- | --- | --- |
Currentdeviationofthemeasuredclockperiodfromtheidealperiodgivenbyclock_period.
phase_error_estimation: float
Currentrootofthesquareddifferencesofclock_input timestampsandidealclocktimestamps. Thisvalue
includesthediscretizationnoiseoftheclock_inputchannel.
| 7.3. TimeTaggerclasses |     |     |     |     | 95  |
| ---------------------- | --- | --- | --- | --- | --- |

TimeTaggerUserManual,Release2.17.4.0
7.4 Virtual Channels
Virtualchannelsaresoftware-definedchannelsascomparedtotherealinputchannels. Virtualchannelscanbeunder-
stoodasastreamflowprocessingunits. Theyhaveaninputthroughwhichtheyreceivetime-tagsfromarealoranother
virtualchannelandoutputtowhichtheysendprocessedtime-tags.
Virtual channels are used as input channels to the measurement classes the same way as real channels. Since the
virtualchannelsarecreatedduringrun-time,thecorrespondingchannelnumber(s)areassigneddynamicallyandcan
beretrievedusinggetChannel()orgetChannels()methodsofvirtualchannelobject.
7.4.1 Available virtual channels
Note: In MATLAB, the Virtual Channel names have common prefix TT*. For example: Combiner is named as
TTCombiner. ThispreventspossiblenamecollisionswithexistingMATLABoruserfunctions.
Coincidence
Detectscoincidenceclicksontwoormorechannelswithinagivenwindow.
Coincidences
Detectscoincidenceclicksonmultiplechannelgroupswithinagivenwindow.
Combinations
Detectscoincidenceclicksonallpossiblecombinationsofgivenchannelswithinagiventimewindow,preceded
andfollowedbytwoguardwindowsofthesamewidthwithoutanyeventsonthesechannels.
Combiner
Combinestwoormorechannelsintoone.
ConstantFractionDiscriminator
Detectsrisingandfallingedgesofaninputpulseandreturnstheaveragetime.
DelayedChannel
Clonesinputchannelswhichcanbedelayed.
EventGenerator
Generatesasignalpatternforeverytriggersignal.
FrequencyMultiplier
FrequencyMultiplierforachannelwithaperiodicsignal.
GatedChannel
Transmits signals of an input_channel depending on the signals arriving at gate_start_channel and
gate_stop_channel.
TriggerOnCountrate
Generatesaneventwhenthecountrateofagivenchannelcrossesgiventhresholdvalue.
96 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
7.4.2 Common methods
VirtualChannel.getChannel()
VirtualChannel.getChannels()
Returnsthechannelnumber(s)correspondingtothevirtualchannel(s). Usethischannelnumbertheverysame
wayasthechannelnumberofphysicalchannel,forexample,asaninputtoameasurementclassoranothervirtual
channel.
Important: Virtualchannelsoperateonthetimetagsthatarriveattheirinput. Thesetimetagscanbefrom
rising or falling edges of the physical signal. However, the virtual channels themselves do not support such a
conceptasaninvertedchannel.
getConfiguration()
Returns configuration data of the virtual channel object. The configuration includes the name, values of
the current parameters and the channel numbers. Information returned by this method is also provided with
TimeTaggerBase.getConfiguration().
Returns
Configurationdataofthevirtualchannelobject.
Returntype
dict
7.4.3 Coincidence
channel A
channel B
channel C
Coincidence
0 10 20 30 40 50 60 70 80
Time (ns)
Detectscoincidenceclicksontwoormorechannelswithinagivenwindow. Thevirtualchannelistriggered,e.g.,when
channelAANDchannelBreceivedasignalwithinthegivencoincidencewindow. Thetimestampofthecoincidence
onthevirtualchannelisthetimeofthelasteventarrivingtocompletethecoincidence.
class Coincidence(tagger,channels,coincidenceWindow=1000,timestamp=CoincidenceTimestamp.Last)
Parameters
• tagger(TimeTaggerBase)–TimeTaggerobjectinstance
• channels (list[int]) – list of channels on which coincidence will be detected in the
virtualchannel
• coincidenceWindow(int)–maximumtimebetweenalleventsforacoincidence[ps]
• timestamp(CoincidenceTimestamp)–typeoftimestampforvirtualchannel
Seeallcommonmethods
7.4. VirtualChannels 97

TimeTaggerUserManual,Release2.17.4.0
7.4.4 Coincidences
CH1
CH2
CH3
CH4
VCH{1,2,3}
VCH{2,3,4}
|     | 0 10 | 20 30 | 40  | 50 60 70 | 80  |
| --- | ---- | ----- | --- | -------- | --- |
Time (ns)
Detects coincidence clicks on multiple channel groups within a given window. If several different coincidences are
required with the same window size, Coincidences provides better performance in comparison to multiple virtual
Coincidencechannels. OneobjectoftheCoincidenceclassislimitedto64uniquechannelsinthelistofchannel
groups(coincidenceGroup).
Examplecode:
from TimeTagger import Coincidence, Coincidences, CoincidenceTimestamp, createTimeTagger
| tagger | = createTimeTagger() |     |     |     |     |
| ------ | -------------------- | --- | --- | --- | --- |
coinc = Coincidences(tagger, [[1,2], [2,3,5]], coincidenceWindow=10000,␣
timestamp=CoincidenceTimestamp.ListedFirst)
˓→
| coinc_chans | = coinc.getChannels() |     |     |     |     |
| ----------- | --------------------- | --- | --- | --- | --- |
coinc1_ch = coinc_chans[0] # double coincidence in channels [1,2] with timestamp of␣
| channel | 1   |     |     |     |     |
| ------- | --- | --- | --- | --- | --- |
˓→
coinc2_ch = coinc_chans[1] # triple coincidence in channels [2,3,5] with timestamp of␣
| channel | 2   |     |     |     |     |
| ------- | --- | --- | --- | --- | --- |
˓→
| # or equivalent | but less              | performant                       |     |     |     |
| --------------- | --------------------- | -------------------------------- | --- | --- | --- |
| coinc1          | = Coincidence(tagger, | [1,2], coincidenceWindow=10000,␣ |     |     |     |
timestamp=CoincidenceTimestamp.ListedFirst)
˓→
| coinc2 | = Coincidence(tagger, | [2,3,5], coincidenceWindow=10000,␣ |     |     |     |
| ------ | --------------------- | ---------------------------------- | --- | --- | --- |
˓→ timestamp=CoincidenceTimestamp.ListedFirst)
coinc1_ch = coinc1.getChannel() # double coincidence in channels [1,2] with timestamp␣
| of channel | 1   |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- |
˓→
coinc2_ch = coinc2.getChannel() # triple coincidence in channels [2,3,5] with timestamp␣
| of channel | 2   |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- |
˓→
| 98  |     |     | Chapter7. | ApplicationProgrammingInterface |     |
| --- | --- | --- | --------- | ------------------------------- | --- |

TimeTaggerUserManual,Release2.17.4.0
Note: OnlyC++andpythonsupportjaggedarrays(arrayofarrays,likeuint[][])whicharerequiredtocombineseveral
coincidencegroupsandpassthemtotheconstructoroftheCoincidencesclass. Hence,theAPIdiffersforMatlab,which
requiresacellarrayof1Dvectorstobepassedtotheconstructor(seeMatlabexamplesprovidedwiththeinstaller).
ForLabVIEW,aCoincidencesFactory-ClassisavailabletocreateaCoincidencesobject, whichisalsoshowninthe
LabVIEWexamplesprovidedwiththeinstaller).
class Coincidences(tagger,coincidenceGroups,coincidenceWindow,timestamp)
Parameters
• tagger(TimeTaggerBase)–TimeTaggerobjectinstance
• coincidenceGroups(list[list[int]])–listofchannelgroupsonwhichcoincidence
willbedetectedinthevirtualchannel
• coincidenceWindow(int)–maximumtimebetweenalleventsforacoincidence[ps]
• timestamp(CoincidenceTimestamp)–typeoftimestampforvirtualchannel(Last,Av-
erage,First,ListedFirst)
Seeallcommonmethods
7.4.5 Combinations
CH1
CH2
CH3
VCH{1,2,3}
VCH{1,3}
VCH{2}
This is not a combination
Guard
because the click on CH3
window
is within the guard window.
0 5 10 15 20 25 30 35 40 45 50
timestamp (ns)
Acombinationisagroupofclicksonasetofchannelswithinagiventimewindow. Thistimewindowissurrounded
by two guard windows of the same width. These guard windows do not contain any events on the channels being
monitored.
7.4. VirtualChannels 99

TimeTaggerUserManual,Release2.17.4.0
Theheraldingguardwindowprecedesthefirstclickinthecombination. Thefollowingguardwindowstartsatthetime
ofthelasteventwithinthecombinationwindow. Ifthereisaclickononeofthemonitoredchannelswithintheguard
windows,nocombinationeventisgenerated. Anewcombinationwindowthenstartswiththenextclickafteranempty
guardwindow.
Everytimeacombinationisdetectedonthemonitoredchannels,Combinationsemitsatagonthecorrespondingvirtual
channel. Thetimestamponthisvirtualchannelisthetimeofthelasteventincludedinthecombination. Given𝑁 input
channelstobemonitored, therewillbe2𝑁 −1possiblecombinations, eachhavingacorrespondingvirtualchannel
number.
Inaddition,𝑁 extravirtualchannelscalled‘SumChannels’arecreated. Thismoduleemitsaclickonthe‘n-th’ofthese
channelsoneach‘n-foldcombination’, regardlessofthechannelsthatcontributedtothecombination. Forinstance,
thisisusefulforpseudo-photon-number-resolutionwithdetectorarrays.
Note: Multipleeventsonthesamechannelwithinonetimewindowarecountedasone.
class Combinations(tagger,channels,window_size)
Parameters
• tagger(TimeTaggerBase)–TimeTaggerobjectinstance
• channels(list[int])–listofchannelsonwhichthecombinationswillbedetected
• window_size(int)–maximumtimebetweenalleventstomakeacombination,minimum
timewithoutanyeventdetectedbeforeandafterthecombinationwindow[ps]
Seeallcommonmethods
getChannel(input_channels)
Returns the virtual channel number corresponding to the combination formed by the given set of input
channels.
Parameters
input_channels(list[int])–listofchannelsformingthecombinationmonitoredbythe
returnedvirtualchannel
getCombination(virtual_channel)
Returnsthesetofinputchannelsformingacombinationeventonthegivenvirtualchannelvirtual_channel.
Parameters
virtual_channel(int)–virtualchannelstoringtheclicksfromthecombinationformed
bythereturnedchannels
Returns
Listofchannelsformingthecombinationmonitoredbytheinputvirtualchannel
Returntype
list[int]
getSumChannel(n_channels)
Returns the virtual channel number on which an event is generated when any combination of exactly
n_channelsclicksisdetectedwithinthewindow_size.
Parameters
n_channels(int)–lengthofthecombinationsmonitoredbythereturnedvirtualchannel
100 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
7.4.6 Combiner
channel A
channel B
Combiner
0 10 20 30 40 50 60 70 80
Time (ns)
Combinestwoormorechannelsintoone. Thevirtualchannelistriggered,e.g.,fortwochannelswheneitherchannel
AORchannelBreceivedasignal.
class Combiner(tagger,channels=[])
Parameters
• tagger(TimeTaggerBase)–TimeTaggerobjectinstance
• channels(list[int])–Listofchannelstobecombinedintoasinglevirtualchannel
Seeallcommonmethods
7.4.7 ConstantFractionDiscriminator
input pulses trigger level
pulse edges
Constant
Fraction
Discriminator
0 10 20 30 40 50 60 70 80
Time (ns)
ConstantFractionDiscriminator(CFD)detectsrisingandfallingedgesofaninputpulseandreturnstheaveragetime
ofbothedges. Thisisusefulinsituationswhenprecisetimingofthepulsepositionisdesiredforthepulsesofvarying
durationsandamplitudes.
Forexample,thefigureaboveshowsfourinputpulsesseparatedby15nanoseconds. Thefirsttwopulseshaveequal
widthsbutdifferentamplitudes,themiddletwopulseshaveequalamplitudebutdifferentdurations,andthelastpulse
hasadurationlongerthanthesearch_windowandisthereforeskipped. Forsuchinputsignal,ifwemeasurethetime
oftherisingedgesonly,wegetanerrorinthepulsepositions,whilewithCFDthiserroriseliminatedforsymmetric
pulses.
Note: ThevirtualCFDrequiresthetimetagsoftherisingandfallingedge. Thisleadsto:
7.4. VirtualChannels 101

TimeTaggerUserManual,Release2.17.4.0
• Thetransferreddataoftheinputchannelistwicetheregularinputrate.
• Whenyoushiftthesignal,e.g.,viasetInputDelay(),youhavetoshiftbothedges.
• Whenyouusetheconditionalfilter,applythetriggerfrombothchannels.
Inaddition,youmayencounterdataratelimitationsduethecomputationalcomplexityofthisvirtualchannel. Consider
usingxtra_setAvgRisingFalling()forsimilarfunctionalitywhenthevariationbetweenpulsedurationsissmall.
There,thecomputationsareperformedontheTimeTaggerhardwareinsteadofonyourPC,andonlyhalfthedatarate
needstobetransferredforthesameresult.
class ConstantFractionDiscriminator(tagger,channels,search_window)
Parameters
• tagger(TimeTagger)–TimeTaggerobject
• channels(list[int])–listofchannelsonwhichtoperformCFD
• search_window(int)–maxpulsedurationinpicosecondstobedetected
Seeallcommonmethods
7.4.8 DelayedChannel
input
Delayed
Channel
0 10 20 30 40 50 60 70 80
Time (ns)
Clones input channels, which can be delayed by a time specified with the delay parameter in the constructor or the
setDelay()method. Anegativedelaywilldelayallotherevents.
Note: Ifyouwanttosetaglobaldelayforoneormoreinputchannels,setInputDelay()isrecommendedaslong
asthedelaysaresmall,whichmeansthatnotmorethan100eventsonallchannelsshouldarrivewithinthemaximum
delayset.
class DelayedChannel(tagger,input_channel,delay)
Parameters
• tagger(TimeTaggerBase)–TimeTaggerobject
• input_channel(int)–channeltobedelayed
• delay(int)–amountoftimetodelayinps
Seeallcommonmethods
setDelay(delay)
Allowsmodifyingthedelaytime.
102 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
Warning: Callingthismethodwithareduceddelaytimemayresultinapartiallossoftheinternally
bufferedtimetags.
Parameters
delay(int)–Delaytimeinpicoseconds
7.4.9 EventGenerator
EventGenerator (pattern=[0, 2000, 4000, 6000, 8000], trigger_divider=2)
trigger
stop
Event
Generator
0 10 20 30 40 50 60 70 80
Time (ns)
Emits an arbitrary pattern of timestamps for every trigger event. The number of trigger events can be reduced by
trigger_divider. Thestartofanewpatterndoesnotaborttheexecutionofunfinishedpatterns,sopatternsmayoverlap.
Theexecutionofallrunningpatternscanbeabortedbyaclickofthestop_channel, i.e. overlappingpatternscanbe
avoidedbysettingthestop_channeltothetrigger_channel.
class EventGenerator(tagger,trigger_channel,pattern,trigger_divider,stop_channel)
Parameters
• tagger(TimeTaggerBase)–TimeTaggerobjectinstance.
• trigger_channel(int)–Channelnumberofthetriggersignal.
• pattern (list[int]) – List of relative timestamps defining the pattern executed upon a
triggerevent.
• trigger_divider(int)–Factorbywhichthenumberoftriggereventsisreduced. (de-
fault: 1)
• divider_offset (int) – If trigger_divider > 1, the divider_offset the number of trigger
clickstobeignoredbeforeemittingthefirstpattern. (default: 0)
• stop_channel(int)–Channelnumberofthestopchannel. (optional)
Seeallcommonmethods
7.4. VirtualChannels 103

TimeTaggerUserManual,Release2.17.4.0
7.4.10 FrequencyMultiplier
channel A
Frequency
Multiplier
0 10 20 30 40 50 60 70 80
Time (ns)
FrequencyMultiplierforachannelwithaperiodicsignal.
Note: VeryhighoutputfrequenciescreateahighCPUload,eventuallyleadingtooverflows.
class FrequencyMultiplier(tagger,input_channel,multiplier)
Parameters
• tagger(TimeTaggerBase)–TimeTaggerobjectinstance
• input_channel(int)–channelonwhichtheupscalingofthefrequencyisbasedon
• multiplier(int)–frequencyupscalingfactor
Seeallcommonmethods
7.4.11 GatedChannel
input
gate start
gate stop
Gated
Channel
0 10 20 30 40 50 60 70 80
Time (ns)
Transmitsthesignalfromaninput_channeltoanewvirtualchannelbetweenanedgedetectedatthegate_start_channel
andthegate_stop_channel.
class GatedChannel(tagger,input_channel,gate_start_channel,gate_stop_channel,
initial=GatedChannelInitial.Closed)
Parameters
• tagger(TimeTaggerBase)–TimeTaggerobject
• input_channel(int)–Channelwhichisgated
104 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
• gate_start_channel(int)–Channelonwhichasignaldetectedwillstartthetransmis-
sionoftheinput_channelthroughthegate
• gate_stop_channel(int)–Channelonwhichasignaldetectedwillstopthetransmission
oftheinput_channelthroughthegate. Notethatgate_stop_channel==gate_start_channel
willresultinanexception.
• initial (GatedChannelInitial) – The initial state of the gate. If overflows occur, the
gatewillberesettothisstateaswell. Bydefault,thestateisClosed.
Seeallcommonmethods
Note: Ifyouassignthesamechanneltoinput_channelandtogate_start_channelorgate_stop_channel,respectively,
theinternalexecutionorderofthetransmissiondecisionandthegateoperation(openingorclosing)becomesimportant:
Foreachtagontheinput_channel, thedecisionismadebasedonthepreviousstate. Afterthisdecisionismadefor
itself,thetagmighttogglethegatestate.
• input_channel==gate_stop_channel:
If the gate is open prior to the arrival of the tag, the tag will pass the gate and close it afterward. All
subsequenttagswillbeeliminateduntilaneventongate_start_channelopensthegateagain. Thismeans
that after the gate has been opened, only a single tag will pass the gate, which is exactly the behavior of
theConditionalFilterwithwithgate_start_channel actingasthetriggerandinput_channel actingasthe
filteredchannel.
• input_channel==gate_start_channel:
Ifthegateisopenpriortothearrivalofthetag,thetagitselfwillbeblockedbutopensthegateafterward.
Allsubsequenttagswillpassthegateuntilaneventongate_stop_channelclosesthegateagain. Thismeans
thateveryeventongate_stop_channelwilleliminateexactlythenexteventontheinput_channel.
Thisbehaviorhasbeenchangedinsoftwareversion2.10.8.
7.4.12 TriggerOnCountrate
TriggerOnCountrate(tagger, 1, 5000000, 625e3 [Hz], 100e3 [Hz])
Channel 1
Countrate
inside
window
time_window reference_countrate
Channel hysteresis
Above range
Channel
Below
0 10 20 30 40 50 60 70 80
Time (µs)
Measuresthecountrateinsidearollingtimewindowandemitstagswhenadefinedreference_countrateiscrossed.
A TriggerOnCountrate object provides two virtual channels: The above channel is triggered when the count rate
exceedsthethreshold(transitionfrombelowtoabove). Thebelowchannelistriggeredwhenthecountratefallsbelow
thethreshold(transitionfromabovetobelow).
7.4. VirtualChannels 105

TimeTaggerUserManual,Release2.17.4.0
Toavoidtheemissionofmultipletriggertagsinthetransitionarea,thehysteresiscountratemodifiesthethresholdwith
respecttothetransitiondirection: Aneventintheabovechannelwillbetriggeredwhenthechannelisinthebelow
stateandrisestoreference_countrate+hysteresisorabove. Viceversa,thebelowchannelfireswhenthechannelisin
theabovestateandfallstothelimitofreference_countrate-hysteresisorbelow.
Thetime-tagsarealwaysinjectedattheendoftheintegrationwindow. YoucanusetheDelayedChannel toadjust
thetemporalpositionofthetriggertagswithrespecttotheintegrationtimewindow.
Theveryfirsttagofthevirtualchannelwillbeemittedtime_windowaftertheinstantiationoftheobjectandwillreflect
thecurrentstate,soeitheraboveorbelow.
class TriggerOnCountrate(tagger,input_channel,reference_countrate,hysteresis,time_window)
Parameters
• tagger(TimeTaggerBase)–TimeTaggerobjectinstance.
• input_channel(int)–Channelnumberofthechannelwhosecountratewillcontrolthe
triggerchannels.
• reference_countrate(float)–ThereferencecountrateinHzthatseparatestheabove
rangefromthebelowrange.
• hysteresis(float)–ThethresholdcountrateinHzfortransitioningtotheabovethresh-
oldstateiscountrate>=reference_countrate+hysteresis,whereasitiscountrate<=ref-
erence_countrate - hysteresis for transitioning to the below threshold state. The hysteresis
avoidstheemissionofmultipletriggertagsuponasingletransition.
• time_window (int) – Rolling time window size in ps. The count rate is analyzed within
thistimewindowandcomparedtothethresholdcountrate.
Seeallcommonmethods
getChannelAbove()
Getthechannelnumberoftheabovechannel.
getChannelBelow()
Getthechannelnumberofthebelowchannel.
getChannels()
Getbothvirtualchannelnumbers: [getChannelAbove(),getChannelBelow()]
getCurrentCountrate()
Getthecurrentcountrateaveragedwithinthetime_window.
injectCurrentState()
Emitatime-tagintotherespectivechannelaccordingtothecurrentstate. Thisisusefulifyoustartanew
measurementthatrequirestheinformation. Thefunctionreturnswhetheritwaspossibletoinjecttheevent.
TheinjectionisnotpossibleiftheTimeTaggerisinoverflowmodeorthetimewindowhasnotpassedyet.
Thefunctioncallisnon-blocking.
isAbove()
ReturnswhethertheVirtualChanneliscurrentlyintheabovestate.
isBelow()
ReturnswhethertheVirtualChanneliscurrentlyinthebelowstate.
106 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
7.5 Measurement Classes
TheTimeTaggerlibraryincludesseveralclassesthatimplementvariousmeasurements. Allmeasurementsarederived
from a base class called IteratorBase that is described further down. As the name suggests, it uses the iterator
programmingconcept.
All measurements provide a set of methods to start and stop the execution and to access the accumulated data. In a
typicalapplication,thefollowingstepsareperformed(seeexample):
1. Createaninstanceofameasurement
2. Waitforsometime
3. Retrievethedataaccumulatedbythemeasurementbycallinga.getData()method.
7.5.1 Available measurement classes
Note: In MATLAB, the Measurement names have common prefix TT*. For example: Correlation is named as
TTCorrelation. ThispreventspossiblenamecollisionswithexistingMATLABoruserfunctions.
Correlation
Auto-andCross-correlationmeasurement.
CountBetweenMarkers
Countstagsononechannelwithinbinswhicharedeterminedbytriggersononeortwootherchannels. Usesa
staticbufferoutput. Usethistoimplementagatedcounter,acountersynchronizedtoexternalsignals,etc.
Counter
Countstheclicksononeormorechannelswithafixedbinwidthandacircularbufferoutput.
Countrate
Averagetagrateononeormorechannels.
Dump
Deprecated-pleaseuseFileWriterinstead. Dumpmeasurementwritesalltime-tagsintoafile.
FileReader
Allowsyoutoreadtime-tagsfromafilewrittenbytheFileWriter.
FileWriter
Thisclasswritestime-tagsintoafilewithalosslesscompression. ItreplacestheDumpclass.
Flim
Fluorescencelifetimeimaging.
FrequencyCounter
Analyzethephaseevolutionofmultiplechannelsatperiodicsamplingpoints.
FrequencyStability
Analyzesthefrequencystabilityofperiodsignals.
Histogram
Asimplehistogramoftimedifferences. Thiscanbeusedtomeasurelifetime,forexample.
Histogram2D
A2-dimensionalhistogramofcorrelatedtimedifferences. Thiscanbeusedinmeasurementssimilarto2DNMR
spectroscopy. (Single-Start,Single-Stop)
7.5. MeasurementClasses 107

TimeTaggerUserManual,Release2.17.4.0
HistogramLogBins
Accumulatestimedifferencesintoahistogramwithlogarithmicincreasingbinsizes.
HistogramND
An-dimensionalhistogramofcorrelatedtimedifferences. (Single-Start,Single-Stop)
IteratorBase
Baseclassforimplementingcustommeasurements(onlyC++).
PulsePerSecondMonitor
Monitorsthesynchronicityof1pulsepersecond(PPS)signals.
Sampler
TheSamplerclassallowssamplingthestateofasetofchannelsviaatriggerchannel.
Scope
Detectstherisingandfallingedgesonachanneltovisualizetheincomingsignalssimilartoanultrafastlogic
analyzer.
StartStop
Accumulatesahistogramoftimedifferencesbetweenpairsoftagsontwochannels. Onlythefirststoptagafter
astarttagisconsidered. Subsequentstoptagsarediscarded. Thehistogramlengthisunlimited. Binsandcounts
arestoredinanarrayoftuples. (Single-Start,Single-Stop)
SynchronizedMeasurements
Helperclassthatallowssynchronizationofthemeasurementclasses.
TimeDifferences
Accumulatesthetimedifferencesbetweentagsontwochannelsinoneormorehistograms. Thesweepingthrough
ofhistogramsisoptionallycontrolledbyoneortwoadditionaltriggers.
TimeDifferencesND
AmultidimensionalimplementationoftheTimeDifferencesmeasurementforasynchronousnexthistogramtrig-
gers.
TimeTagStream
This class provides you with access to the time-tag stream and allows you to implement your own on-the-fly
processing. See Raw Time-Tag-Stream access to get on overview about the possibilities for the raw time-tag-
streamaccess.
7.5.2 Common methods
class IteratorBase
clear()
Discardsaccumulatedmeasurementdata,initializesthedatabufferwithzerovalues,andresetsthestateto
theinitialstate.
start()
Startsorcontinuesdataacquisition. Thismethodisimplicitlycalledwhenameasurementobjectiscreated.
[ ]
startFor(duration ,clear=True )
Startsorcontinuesthedataacquisitionforthegivenduration(inps). Afterthedurationtime,themethod
stop() is called and isRunning() will return False. Whether the accumulated data is cleared at the
beginningofstartFor()iscontrolledwiththesecondparameterclear,whichisTruebydefault.
stop()
After calling this method, the measurement will stop processing incoming tags. Use start() or
startFor()tocontinueorrestartthemeasurement.
108 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
abort()
Immediatelyabortsthemeasurement,discardsaccumulatedmeasurementdata,andresetsthestatetothe
initialstate.
Warning: Aftercallingabort(),thelastblockofdatamightbecomeirreversiblycorrupted. Please
alwaysusestop()toendameasurement.
isRunning()
ReturnsTrueifthemeasurementiscollectingthedata. ThismethodwillreturnFalseifthemeasurement
wasstoppedmanuallybycallingstop()orautomaticallyaftercallingstartFor()andthedurationhas
passed.
Note: Allmeasurementsstartaccumulatingdataimmediatelyaftertheircreation.
Returns
True/False
Returntype
bool
waitUntilFinished(timeout=-1)
Blockstheexecutionuntilthemeasurementhasfinished. CanbeusedwithstartFor().
Thisisroughlyequivalenttoapollingloopwithsleep().
measurement.waitUntilFinished(timeout=-1)
# is roughly equivalent to
while measurement.isRunning():
sleep(0.01)
Parameters
timeout (int) – timeout in milliseconds. Negative value means no timeout, zero returns
immediately.
Returns
Trueifthemeasurementhasfinished,Falseontimeout
Returntype
bool
getCaptureDuration()
Totalcapturedurationsincethemeasurementcreationorlastcalltoclear().
Returns
Capturedurationinps
Returntype
int
getConfiguration()
Returnsconfigurationdataofthemeasurementobject. Theconfigurationincludesthemeasurementname,
and the values of the current parameters. Information returned by this method is also provided with
TimeTaggerBase.getConfiguration().
7.5. MeasurementClasses 109

TimeTaggerUserManual,Release2.17.4.0
Returns
Configurationdataofthemeasurementobject.
Returntype
dict
7.5.3 Event counting
Countrate
2
1
0
0 100 200 300 400 500 600 700 800
Time (ns)
langis
Countrate
0.0 0.2 0.4 0.6 0.8 1.0
1.0
getData() = counts / time
0.5 = 7 / 800ns
= 8 750 000 counts / second
0.0
0.0 0.2 0.4 0.6 0.8 1.0
Measurestheaveragecountrateononeormorechannels. Specifically,itdeterminesthecountspersecondonthespec-
ifiedchannelsstartingfromtheveryfirsttagarrivingaftertheinstantiationorlastcalltoclear()ofthemeasurement.
TheCountrateworkscorrectlyevenwhentheUSBtransferrateorbackendprocessingcapabilitiesareexceeded.
class Countrate(tagger,channels)
Parameters
• tagger(TimeTaggerBase)–timetaggerobjectinstance
• channels(list[int])–channelsforwhichtheaveragecountrateismeasured
Seeallcommonmethods
getData()
Returns
Averagecountrateincountspersecond.
Returntype
1D_array[float]
getCountsTotal()
Returns
Thetotalnumberofeventssincetheinstantiationofthisobject.
Returntype
1D_array[int]
110 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
Counter
2
1
0
0 50 100 150 200 250
langis
Counter (n_bins=4, binwidth=50)
time (ps)
1.0
0.5
0.0
0 1 2 3
)(ataDteg
nib
rep
stnuoc
1 3 0 1 2 1 + ?
not fully
bin dropped out integrated
bin
#bin
Time trace of the count rate on one or more channels. Specifically, this measurement repeatedly counts tags within
a time interval binwidth and stores the results in a two-dimensional array of size number of channels by n_values.
Theincomingdataisfirstaccumulatedinanot-accessiblebin. Whentheintegrationtimeofthisbinhaspassed,the
accumulateddataisaddedtotheinternalbuffer,whichcanbeaccessedviathegetData... methods. Datastoredinthe
internalcircularbufferisoverwrittenwhenn_valuesareexceeded. Youcanpreventthisbyautomaticallystoppingthe
measurementintimeasfollowscounter.startFor(duration=binwidth*n_values).
[ ]
class Counter(tagger,channels ,binwidth=1e9,n_values=1 )
Parameters
• tagger(TimeTaggerBase)–timetaggerobject
• channels(list[int])–channelsusedforcountingtags
• binwidth(int)–binwidthinps(default: 1e9)
• n_values(int)–numberofbins(default: 1)
Seeallcommonmethods
[ ]
getData( rolling=True )
Returnsanarrayofaccumulatedcounterbinsforeachchannel. Theoptionalparameterrolling,controlsif
thenotintegratedbinsarepaddedbeforeoraftertheintegratedbins.
Whenrolling=True,themostrecentdataisstoredinthelastbinofthearrayandeverynewcompleted
binshiftsallotherbinsright-to-left. Whencontinuouslyplotted,thiscreatesaneffectofrollingtraceplot.
Forinstance,itisusefulforcontinuousmonitoringofcountratechangesovertime.
Whenrolling=False,themostrecentdataisstoredinthenextbinafterprevioussuchthatthearrayis
filled up left-to-right. When array becomes full and the Counter is still running, the array index will be
reset to zero and the array will be filled again overwriting previous values. This operation is sometimes
called“sweepplotting”.
Parameters
rolling(bool)–Controlshowthecounterarrayisfilled.
Returns
Anarrayofsize‘numberofchannels’byn_valuescontainingthecountsineachfullyinte-
gratedbin.
7.5. MeasurementClasses 111

TimeTaggerUserManual,Release2.17.4.0
Returntype
2D_array[int]
getIndex()
Returnstherelativetimeofthebinsinps. Thefirstentryofthereturnedvectorisalways0.
Returns
Avectorofsizen_valuescontainingthetimebinsinps.
Returntype
1D_array[int]
[ ]
getDataNormalized( rolling=True )
DoesthesameasgetData()butreturnsthecountrateinHzasafloat. Notintegratedbinsandbinsin
overflowmodearemarkedasNaN.
Returntype
2D_array[float]
getDataTotalCounts()
Returnstotalnumberofeventsperchannelsincethelastcalltoclear(),includingthecurrentlyintegrating
bin. ThismethodworkscorrectlyevenwhentheUSBtransferrateorbackendprocessingcapabilitiesare
exceeded.
Returns
Numberofeventsperchannel.
Returntype
1D_array[int]
getDataObject(remove=False)
Returns CounterData objectcontainingasnapshot ofthedataaccumulatedinthe Counter atthetime
thismethodiscalled.
Parameters
remove(bool)–Controlsifthereturneddatashallberemovedfromtheinternalbuffer.
Returns
Anobjectprovidingaccesstoasnapshotdata.
Returntype
CounterData
class CounterData
Objects of this class are created and returned by Counter.getDataObject(), and contain a snapshot of the
dataaccumulatedbytheCountermeasurement.
size: int
Numberofreturnedbins.
dropped_bins: int
Numberofbinswhichhavebeendroppedbecausen_valuesoftheCounterhasbeenexceeded.
overflow: bool
Statusflagforwhetheranyofthereturnedbinshavebeeninoverflowmode.
getIndex()
Returnstherelativetimeofthebinsinps. Thefirstentryofthereturnedvectorisalways0forsize>0.
Returns
Avectorofsizesizecontainingtherelativetimebinsinps.
112 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
Returntype
1D_array[int]
getData()
Returns
Anarrayofsize‘numberofchannels’bysizecontainingonlyfullyintegratedbins.
Returntype
2D_array[int]
getDataNormalized()
DoesthesameasgetData()butreturnsthecountrateincounts/second. Binsinoverflowmodearemarked
asNaN.
Returntype
2D_array[float]
getFrequency(time_scale: int=1_000_000_000_000)
Returnsthecountsnormalizedtothespecifiedtimescale. BinsinoverflowmodearemarkedasNaN.
Parameters
time_scale–Scalesthereturnvaluetothistimeinterval. Defaultis1s,sothereturnvalue
isinHz. Fornegativevalues,thetimescaleissettobinwidth.
Returntype
2D_array[float]
getDataTotalCounts()
Returns the total number of events per channel since the last call to clear(), excluding the counts of
theinternalbinwheredataiscurrentlyintegratedinto. ThismethodworkscorrectlyevenwhentheUSB
transferrateorbackendprocessingcapabilitiesareexceeded.
Returns
Numberofeventsperchannel.
Returntype
1D_array[int]
getTime()
ThisissimilartogetIndex()butitreturnstheabsolutetimestampsofthebins. Forsubsequentcallsto
getDataObject(),thesearrayscanbeconcatenatedtoobtainafullindexarray.
Returns
AvectorofsizesizecontainingthetimecorrespondingtothereturnvalueofCounterData.
getData()inps.
Returntype
1D_array[int]
getOverflowMask()
Arrayofvaluesforeachbinthatindicateifanoverflowoccurredduringaccumulationoftherespectivebin.
Returns
Anarrayofsizesizecontainingoverflowmask.
Returntype
1D_array[int]
7.5. MeasurementClasses 113

TimeTaggerUserManual,Release2.17.4.0
CountBetweenMarkers
Count Between Markers
t = 0 time
begin click click click begin click click click click begin
getData() data[0] = 3 Gated Counter data[1] = 4
t = 0 time
begin click click end click begin click click end click click begin
getData() data[0] = 2 data[1] = 2
Counts events on a single channel within the time indicated by a “start” and “stop” signals. The bin edges between
whichcountsareaccumulatedaredeterminedbyoneormorehardwaretriggers. Specifically,themeasurementrecords
dataintoavectoroflengthn_values(initiallyfilledwithzeros). Itwaitsfortagsonthebegin_channel. Whenatag
is detected on the begin_channel it starts counting tags on the click_channel. When the next tag is detected on the
begin_channel it stores the current counter value as the next entry in the data vector, resets the counter to zero and
startsaccumulatingcountsagain. Ifanend_channelisspecified,themeasurementstoresthecurrentcountervalueand
resetsthecounterwhenatagisdetectedontheend_channelratherthanthebegin_channel. Youcanusethis,e.g.,to
accumulatecountswithinagatebyusingrisingedgesononechannelasthebegin_channel andfallingedgesonthe
samechannelastheend_channel. TheaccumulationtimeforeachvaluecanbeaccessedviagetBinWidths(). The
measurementstopswhenallentriesinthedatavectorarefilled.
[
class CountBetweenMarkers(tagger,click_channel,begin_channel ,end_channel=CHANNEL_UNUSED,
]
n_values=1000 )
Parameters
• tagger(TimeTaggerBase)–timetaggerobject
• click_channel(int)–channelonwhichclicksarereceived,gatedbybegin_channeland
end_channel
• begin_channel(int)–channelthattriggersthebeginningofcountingandsteppingtothe
nextvalue
• end_channel (int) – channel that triggers the end of counting (optional, default:
CHANNEL_UNUSED)
• n_values(int)–numberofvaluesstored(databuffersize)(default: 1000)
Seeallcommonmethods
getData()
Returns
Arrayofsizen_valuescontainingtheacquiredcountervalues.
Returntype
1D_array[int]
114 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
getIndex()
Returns
Vectorofsizen_valuescontainingthetimeinpsofeachstartclickinrespecttotheveryfirst
startclick.
Returntype
1D_array[int]
getBinWidths()
Returns
Vectorofsizen_valuescontainingthetimedifferencesof‘start->(nextstartorstop)’forthe
acquiredcountervalues.
Returntype
1D_array[int]
ready()
Returns
Truewhentheentirearrayisfilled.
Returntype
bool
7.5.4 Time histograms
Thissectiondescribesvariousmeasurementsthatcalculatetimedifferencesbetweeneventsandaccumulatetheresults
intoahistogram.
StartStop
0 100 200 300 400 500
time (ps)
langis
StartStop
start start click click start click
dt dt
60
40
20
0
0 50 100 150 200 250
)(ataDteg
getData()
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 #bin
Asimplestart-stopmeasurement. Thisclassperformsastart-stopmeasurementbetweentwochannelsandstoresthe
timedifferencesinahistogram. Thehistogramresolutionisspecifiedbeforehand(binwidth)butthehistogramrange
7.5. MeasurementClasses 115

TimeTaggerUserManual,Release2.17.4.0
(numberofbins)isunlimited. Itisadaptedtothelargesttimedifferencethatwasdetected. Thus,allpairsofsubsequent
| clicksareregistered. | Onlynon-emptybinsarerecorded. |     |     |     |     |     |     |
| -------------------- | ----------------------------- | --- | --- | --- | --- | --- | --- |
StartStop(tagger,click_channel [ ,start_channel=CHANNEL_UNUSED,binwidth=1000 ]
| class |     |     |     |     |     | )   |     |
| ----- | --- | --- | --- | --- | --- | --- | --- |
Parameters
• tagger(TimeTaggerBase)–timetaggerobjectinstance
• click_channel(int)–channelonwhichstopclicksarereceived
• (int) – channel on which start clicks are received (default:
start_channel
CHANNEL_UNUSED)
|     | • binwidth(int)–binwidthinps(default: |     |     | 1000) |     |     |     |
| --- | ------------------------------------- | --- | --- | ----- | --- | --- | --- |
Seeallcommonmethods
getData()
Returns
Anarrayoftuples(arrayofshapeNx2)containingthetimes(inps)andcountsofeachbin.
Onlynon-emptybinsarereturned.
Returntype
2D_array[int]
Histogram
Histogram
| langis start | click | start | start |     | click click |     |     |
| ------------ | ----- | ----- | ----- | --- | ----------- | --- | --- |
|              | dt1   |       |       | dt2 |             |     |     |
dt3
dt4
dt5
| 0   | 100 | 200 |     | 300 | 400 | 500 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
time (ps)
)(ataDteg
| 0   | 50    | 100   |        | 150      | 200      | 250      | getIndex() |
| --- | ----- | ----- | ------ | -------- | -------- | -------- | ---------- |
| 0 1 | 2 3 4 | 5 6 7 | 8 9 10 | 11 12 13 | 14 15 16 | 17 18 19 | #bin       |
Accumulatetimedifferencesintoahistogram. Thisisasimplemultiplestart, multiplestopmeasurement. Thisisa
specialcaseofthemoregeneralTimeDifferencesmeasurement. Specifically,themeasurementwaitsforclicksonthe
start_channel,andforeachstartclick,itmeasuresthetimedifferencebetweenthestartclicksandallsubsequentclicks
ontheclick_channelandstorestheminahistogram. Thehistogramrangeandresolutionarespecifiedbythenumber
ofbinsandthebinwidthspecifiedinps. Clicksthatfalloutsidethehistogramrangeareignored. Dataaccumulation
isperformedindependentlyforallstartclicks. Thistypeofmeasurementisfrequentlyreferredtoasa‘multiplestart,
multiplestop’measurementandcorrespondstoafullauto-orcross-correlationmeasurement.
| 116 |     |     |     | Chapter7. | ApplicationProgrammingInterface |     |     |
| --- | --- | --- | --- | --------- | ------------------------------- | --- | --- |

TimeTaggerUserManual,Release2.17.4.0
[ ]
class Histogram(tagger,click_channel ,start_channel=CHANNEL_UNUSED,binwidth=1000,n_bins=1000 )
Parameters
• tagger(TimeTaggerBase)–timetaggerobjectinstance
• click_channel(int)–channelonwhichclicksarereceived
• start_channel (int) – channel on which start clicks are received (default:
CHANNEL_UNUSED)
• binwidth(int)–binwidthinps(default: 1000)
• n_bins(int)–thenumberofbinsinthehistogram(default: 1000)
Seeallcommonmethods
getData()
Returns
Aone-dimensionalarrayofsizen_binscontainingthehistogram.
Returntype
1D_array[int]
getIndex()
Returns
Avectorofsizen_binscontainingthetimebinsinps.
Returntype
1D_array[int]
7.5. MeasurementClasses 117

TimeTaggerUserManual,Release2.17.4.0
HistogramLogBins
Uniformly distributed time differences
2
0
|     | 101 |     | 102 |     | 103 |     |     | 104 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Counts per bin
)(ataDteg 1000
500
0
|     | 101 |     | 102 |     | 103 |     |     | 104getBinEdges() |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- |
Counts per bin / binwidth
)(dezilamroNataDteg
0.6
0.4
0.2
0.0
|     | 101 |       | 102   |        | 103      |          |          | 104getBinEdges() |
| --- | --- | ----- | ----- | ------ | -------- | -------- | -------- | ---------------- |
|     | 0 1 | 2 3 4 | 5 6 7 | 8 9 10 | 11 12 13 | 14 15 16 | 17 18 19 | 20 #bin          |
TheHistogramLogBinsmeasurementissimilartoHistogrambutthebinedgesarespacedlogarithmically. Asthebins
donothaveahomogeneousbinwidth,apropernormalizationisrequiredtointerprettherawdata.
For excluding time ranges from the histogram evaluation while maintaining a proper normalization,
HistogramLogBins optionally takes two gating arguments of type ChannelGate. This can, e.g., be used to
pause the acquisition during erroneous ranges that have to be identified by virtual channels. The same mechanism
automaticallyappliestooverflowranges.
Theacquiredhistogram𝐻(𝑡)isnormalizedby
|     |     |     | 𝐻̃︀(𝜏)=𝐼(𝜏)·𝐶 |       | ·𝐶    |     |     |     |
| --- | --- | --- | ------------- | ----- | ----- | --- | --- | --- |
|     |     |     |               | click | start |     |     |     |
with an estimation of counts and the click and start channel count rates, and
|     |                   | 𝐼(𝜏)                                |     |     |     | 𝐶 click = | 𝑁 click /𝑡 click | 𝐶 start = |
| --- | ----------------- | ----------------------------------- | --- | --- | --- | --------- | ---------------- | --------- |
| 𝑁   | /𝑡 ,respectively. | Typically,thiswillbeusedtocalculate |     |     |     |           |                  |           |
start start
𝐻(𝜏)
𝑔(2)(𝜏)=
𝐻̃︀(𝜏)
10exp_stopsandwithoutinterruptions,
For𝑡 ≫ 𝐼(𝜏)/𝑡willapproachthebinwidthoftherespectivebin. Duringthe
earlyacquisitionandincaseofinterruptions,𝐼(𝜏)canbesignificantlysmaller,whichcompensatesforcountsthatare
excludedfrom𝐻(𝜏).
class HistogramLogBins(tagger,click_channel,start_channel,exp_start,ex_stop,n_bins,click_gate=None,
start_gate=None)
| 118 |     |     |     |     | Chapter7. | ApplicationProgrammingInterface |     |     |
| --- | --- | --- | --- | --- | --------- | ------------------------------- | --- | --- |

TimeTaggerUserManual,Release2.17.4.0
Parameters
• tagger(TimeTaggerBase)–timetaggerobjectinstance
• click_channel(int)–channelonwhichclicksarereceived
• start_channel(int)–channelonwhichstartclicksarereceived
• exp_start(float)–exponent10^exp_startinsecondswheretheveryfirstbinbegins
• exp_stop(float)–exponent10^exp_stopinsecondswheretheverylastbinends
• n_bins(int)–thenumberofbinsinthehistogram
• click_gate(ChannelGate)–optionalevaluationgatefortheclick_channel
• start_gate(ChannelGate)–optionalevaluationgateforthestart_channel
Seeallcommonmethods
getDataObject()
Returns
Adataobjectcontainingrawandnormalizationdata.
Returntype
HistogramLogBinsData
getBinEdges()
Returns
Avectorofsizen_bins+1containingthebinedgesinpicoseconds.
Returntype
1D_array[int]
getData()
Deprecated since version 2.17.0: please use HistogramLogBins.getDataObject() and
HistogramLogBinsData.getCounts()instead.
Returns
Aone-dimensionalarrayofsizen_binscontainingthehistogram.
Returntype
1D_array[int]
getDataNormalizedCountsPerPs()
Deprecatedsinceversion2.17.0.
Returns
Thecountsnormalizedbythebinwidthofeachbin.
Returntype
1D_array[float]
getDataNormalizedG2()
Deprecatedsinceversion2.17.0: pleaseusegetDataObject()andHistogramLogBinsData.getG2()
instead.
Returns
Thecountsnormalizedbythebinwidthofeachbinandtheaveragecountrate.
Returntype
1D_array[float]
7.5. MeasurementClasses 119

TimeTaggerUserManual,Release2.17.4.0
class HistogramLogBinsData
Containsthehistogramcounts𝐻(𝜏)andthecorrespondingnormalizationfunction𝐻̃︀(𝜏).
getG2()
Returns
Aone-dimensionalarrayofsizen_binscontainingthenormalizedhistogram𝐻(𝜏)/𝐻̃︀(𝜏).
Returntype
1D_array[float]
getCounts()
Returns
Aone-dimensionalarrayofsizen_binscontainingtherawhistogram𝐻(𝜏).
Returntype
1D_array[int]
getG2Normalization()
Returns
Aone-dimensionalarrayofsizen_binscontainingthenormalization𝐻̃︀(𝜏).
Returntype
1D_array[float]
Histogram2D
Signal
250
start start
200
start
150
click click
stop 1
100
click click
50
stop 2
0
0 100 200 300 400 0 50 100 150 200 250
time (ps) getIndex_1()
)(2_xednIteg
Histogram 2D
+1
+1
Thismeasurementisa2-dimensionalversionoftheHistogrammeasurement. Themeasurementaccumulatesatwo-
dimensionalhistogramwherestopsignalsfromtwoseparatechannelsdefinethebincoordinate. Forinstance,thiskind
ofmeasurementissimilar tothatoftypical2DNMRspectroscopy. Thedatawithinthehistogramisacquiredvia a
single-start,single-stopanalysisforeachaxis. Thefirststopclickofeachaxisistakenafterthestartclicktoevaluate
thehistogramcounts.
120 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
class Histogram2D(tagger,start_channel,stop_channel_1,stop_channel_2,binwidth_1,binwidth_2,n_bins_1,
n_bins_2)
Parameters
• tagger(TimeTaggerBase)–timetaggerobject
• start_channel(int)–channelonwhichstartclicksarereceived
• stop_channel_1(int)–channelonwhichstopclicksforthetimeaxis1arereceived
• stop_channel_2(int)–channelonwhichstopclicksforthetimeaxis2arereceived
• binwidth_1(int)–binwidthinpsforthetimeaxis1
• binwidth_2(int)–binwidthinpsforthetimeaxis2
• n_bins_1(int)–thenumberofbinsalongthetimeaxis1
• n_bins_2(int)–thenumberofbinsalongthetimeaxis2
Seeallcommonmethods
getData()
Returns
Atwo-dimensionalarrayofsizen_bins_1byn_bins_2containingthe2Dhistogram.
Returntype
2D_array[int]
getIndex()
Returns a 3D array containing two coordinate matrices (meshgrid) for time bins in ps for the time axes
1and2. Fordetailsonmeshgrid pleasetakealookattherespectivedocumentationeitherforMatlabor
PythonNumPy.
Returns
Athree-dimensionalarrayofsizen_bins_1xn_bins_2x2
Returntype
3D_array[int]
getIndex_1()
Returns
Avectorofsizen_bins_1containingthebinlocationsinpsforthetimeaxis1.
Returntype
1D_array[int]
getIndex_2()
Returns
Avectorofsizen_bins_2containingthebinlocationsinpsforthetimeaxis2.
Returntype
1D_array[int]
7.5. MeasurementClasses 121

TimeTaggerUserManual,Release2.17.4.0
HistogramND
ThismeasurementisthegeneralizationofHistogram2D toanarbitrarynumberofdimensions. Thedatawithinthe
histogramisacquiredviaasingle-start,single-stopanalysisforeachaxis. Thefirststopclickofeachaxisistakenafter
thestartclicktoevaluatethehistogramcounts.
HistogramND canbeusedasa1DHistogram withsingle-startsingle-stopbehavior.
class HistogramND(tagger,start_channel,stop_channels,binwidths,n_bins)
Parameters
• tagger(TimeTagger)–timetaggerobject
• start_channel(int)–channelonwhichstartclicksarereceived
• stop_channels(list[int])–channellistonwhichstopclicksarereceiveddefiningthe
timeaxes
• binwidths(list[int])–binwidthinpsforthecorrespondingtimeaxis
• n_bins(list[int])–thenumberofbinsalongthecorrespondingtimeaxis
Seeallcommonmethods
getData()
Returnsaone-dimensionalarrayofthesizeoftheproductofn_binscontainingthehistogramdata. The
arrayorderisinrow-major. Forexample,withstop_channels=[ch1, ch2]andn_bins=[2, 2],the
1D array would represent 2D bin indices in the order [(0,0), (0,1), (1,0), (1,1)], with (index
of ch1, index of ch2). Please reshape the 1D array to get the N-dimensional array. The following code
demonstrateshowtoreshapethereturned1DarrayintomultidimensionalarrayusingNumPy.
channels = [2, 3, 4, 5]
n_bins = [5, 3, 4, 6]
binwidths = [100, 100, 100, 50]
histogram_nd = HistogramND(tagger, 1, channels, binwidths, n_bins)
sleep(1) # Wait to accumulate the data
data = histogram_nd.getData()
multidim_array = numpy.reshape(data, n_bins)
Returns
Flattenedarrayofhistogrambins.
Returntype
1D_array[int]
getIndex(dim)
Returns
Returnsavectorofsizen_bins[dim]containingthebinlocationsinpsforthecorresponding
timeaxis.
Returntype
1D_array[int]
122 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
Correlation
Correlation
langis
|     | ch 1ch 1 | ch 2 |     |     | ch 2 | ch 1 |     |
| --- | -------- | ---- | --- | --- | ---- | ---- | --- |
|     |          | dt   |     |     | dt   |      |     |
dt
| 0   |     |     |     |     |     |     | time |
| --- | --- | --- | --- | --- | --- | --- | ---- |
2000
1500
)(ataDteg
1000
500
0
| 100 | 75    | 50 25   | 0         | 25    | 50       | 75    | 100 getIndex() |
| --- | ----- | ------- | --------- | ----- | -------- | ----- | -------------- |
| 0   | 1 2 3 | 4 5 6 7 | 8 9 10 11 | 12 13 | 14 15 16 | 17 18 | 19 20 #bin     |
Accumulatestimedifferencesbetweenclicksontwochannelsintoahistogram,whereallticksareconsideredbothas
“start”and“stop”clicksandbothpositiveandnegativetimedifferencesareconsidered.
[ ]
class Correlation(tagger,channel_1 ,channel_2=CHANNEL_UNUSED,binwidth=1000,n_bins=1000 )
Parameters
• tagger(TimeTaggerBase)–timetaggerobject
• channel_1(int)–channelonwhich(stop)clicksarereceived
• channel_2(int)–channelonwhichreferenceclicks(start)arereceived(whenleftempty
orsettoCHANNEL_UNUSED ->anauto-correlationmeasurementisperformed,whichisthe
|     | sameassettingchannel_1=channel_2)(default:                    |     |     |       | CHANNEL_UNUSED) |     |       |
| --- | ------------------------------------------------------------- | --- | --- | ----- | --------------- | --- | ----- |
|     | • binwidth(int)–binwidthinps(default:                         |     |     | 1000) |                 |     |       |
|     | • n_bins(int)–thenumberofbinsintheresultinghistogram(default: |     |     |       |                 |     | 1000) |
Seeallcommonmethods
getData()
Returns
Aone-dimensionalarrayofsizen_binscontainingthehistogram.
Returntype
1D_array[int]
getDataNormalized()
Returnthedatanormalizedas:
∆𝑡
𝑔(2)(𝜏)=
·ℎ𝑖𝑠𝑡𝑜𝑔𝑟𝑎𝑚(𝜏)
|     |     |     | 𝑏𝑖𝑛𝑤𝑖𝑑𝑡ℎ·𝑁 | ·𝑁  |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- |
1 2
| where∆𝑡isthecaptureduration,𝑁 |     |     | and𝑁 arenumberofeventsineachchannel. |     |     |     |     |
| ----------------------------- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
1 2
Returns
Datanormalizedbythebinwidthandtheaveragecountrate.
7.5. MeasurementClasses 123

TimeTaggerUserManual,Release2.17.4.0
Returntype
1D_array[float]
getIndex()
Returns
Avectorofsizen_binscontainingthetimebinsinps.
Returntype
1D_array[int]
TimeDifferences
TimeDifferences
langis
|     | nextstartstart |     | clickstart |     |     | clicknextstart | click | start |     | clickclick |      |     |
| --- | -------------- | --- | ---------- | --- | --- | -------------- | ----- | ----- | --- | ---------- | ---- | --- |
|     |                |     | dt         |     |     |                |       |       | dt  |            |      |     |
|     |                | dt  |            |     | dt  |                | dt    |       | dt  |            |      |     |
|     | 0              |     |            | 250 |     | 500            |       | 750   |     |            | 1000 |     |
time (ps)
|     | 100 |     |     |     |     | 100 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 80  |     |     |     |     | 80  |     |     |     |     |     |     |
)(ataDteg
|     | 60  |     |     |     |     | 60  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 40  |     |     |     |     | 40  |     |     |     |     |     |     |
|     | 20  |     |     |     |     | 20  |     |     |     |     |     |     |
|     | 0   |     |     |     |     |     | 0   |     |     |     |     |     |
getIndex()
|     | 0 50 | 100 |     | 150 | 200   | 250 | 0 50 | 100 |     | 150 | 200   | 250        |
| --- | ---- | --- | --- | --- | ----- | --- | ---- | --- | --- | --- | ----- | ---------- |
|     | 0 1  | 2 3 | 4   | 5 6 | 7 8 9 |     | 0 1  | 2 3 | 4   | 5 6 | 7 8 9 | #bin       |
|     |      |     | 0   |     |       |     |      |     | 1   |     |       | #histogram |
Aone-dimensionalarrayoftime-differencehistogramswiththeoptiontoincludeuptotwoadditionalchannelsthat
control how to step through the indices of the histogram array. This is a very powerful and generic measurement.
Youcanuseittorecordconsecutivecross-correlation,lifetimemeasurements,fluorescencelifetimeimagingandmany
more measurements based on pulsed excitation. Specifically, the measurement waits for a tag on the start_channel,
thenmeasuresthetimedifferencebetweenthestarttagandallsubsequenttagsontheclick_channel andstoresthem
inahistogram. Ifnostart_channel isspecified,theclick_channel isusedasstart_channel correspondingtoanauto-
correlationmeasurement. Thehistogramhasanumbern_binsofbinsofbinwidthbinwidth. Clicksthatfalloutside
the histogram range are discarded. Data accumulation is performed independently for all start tags. This type of
measurementisfrequentlyreferredtoas‘multiplestart,multiplestop’measurementandcorrespondstoafullauto-or
cross-correlationmeasurement.
Thetime-differencedatacanbeaccumulatedintoasinglehistogramorintomultiplesubsequenthistograms. Inthis
way,youcanrecordasequenceoftime-differencehistograms. Toswitchfromonehistogramtothenextoneyouhave
tospecifyachannelthatprovideswitchmarkers(next_channel parameter). Alsoyouneedtospecifythenumberof
histogramswiththeparametern_histograms. Aftereachtagonthenext_channel,thehistogramindexisincrementedby
oneandresettozeroafterreachingthelastvalidindex. Themeasurementstartswiththefirsttagonthenext_channel.
You can also provide a synchronization marker that resets the histogram index by specifying a sync_channel. The
measurementstartswhenatagonthesync_channel arriveswithasubsequenttagonnext_channel. Whenarollover
occurs,theaccumulationisstoppeduntilthenextsyncandsubsequentnextsignal. Asyncsignalbeforearolloverwill
stoptheaccumulation,resetthehistogramindexandasubsequentsignalonthenext_channelstartstheaccumulation
again.
| 124 |     |     |     |     |     |     | Chapter7. |     | ApplicationProgrammingInterface |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------------------------- | --- | --- | --- |

TimeTaggerUserManual,Release2.17.4.0
Typically,youwillrunthemeasurementindefinitelyuntilstoppedbytheuser. However,itisalsopossibletospecify
the maximum number of rollovers of the histogram index. In this case, the measurement stops when the number of
rollovershasreachedthespecifiedvalue.
class TimeDifferences(tagger,click_channel,start_channel=CHANNEL_UNUSED,
next_channel=CHANNEL_UNUSED,sync_channel=CHANNEL_UNUSED,
binwidth=1000,n_bins=1000,n_histograms=1)
Parameters
• tagger(TimeTaggerBase)–timetaggerobjectinstance
• click_channel(int)–channelonwhichstopclicksarereceived
• start_channel (int) – channel that sets start times relative to which clicks on the click
channelaremeasured
• next_channel(int)–channelthatincrementsthehistogramindex
• sync_channel(int)–channelthatresetsthehistogramindextozero
• binwidth(int)–binwidthinpicoseconds
• n_bins(int)–numberofbinsineachhistogram
• n_histograms(int)–numberofhistograms
Note: A rollover occurs on a next_channel event while the histogram index is already in the last histogram.
If sync_channel is defined, the measurement will pause at a rollover until a sync_channel event occurs and
continuesatthenextnext_channelevent. Withundefinedsync_channel,themeasurementwillcontinuewithout
interruptionathistogramindex0.
Seeallcommonmethods
getData()
Returns
Atwo-dimensionalarrayofsizen_binsbyn_histogramscontainingthehistograms.
Returntype
2D_array[int]
getIndex()
Returns
Avectorofsizen_binscontainingthetimebinsinps.
Returntype
1D_array[int]
setMaxCounts()
Sets the number of rollovers at which the measurement stops integrating. To integrate infinitely, set the
valueto0,whichisthedefaultvalue.
getHistogramIndex()
Returns
The index of the currently processed histogram or the waiting state. Possible return values
are:
• -2: Waitingforaneventonsync_channel(onlyifsync_channelisdefined)
7.5. MeasurementClasses 125

TimeTaggerUserManual,Release2.17.4.0
• -1: Waitingforaneventonnext_channel(onlyifnext_channelisdefined)
|     | • 0... | (n_histograms-1): |     | Indexofthecurrentlyprocessedhistogram |     |     |     |     |     |     |
| --- | ------ | ----------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
Returntype
int
getCounts()
Returns
Thenumberofrollovers(histogramindexresets).
Returntype
int
ready()
Returns
TruewhentherequirednumberofrolloverssetbysetMaxCounts()hasbeenreached.
Returntype
bool
TimeDifferencesND
TimeDifferencesND
sync trigger #0
| next trigger #0 |     | ?   | 0   | 1   | 2   |     | 0   | 1   |     | 2   |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sync trigger #1
| next trigger #1  |     | 0   |     |     | 1   |     |     |     | 0   |                |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- |
| active histogram |     |     | 0   | 1   | 4   | 5   |     | 3 4 | 1   | 2              |
|                  | 0   | 200 |     | 400 |     | 600 |     | 800 |     | 1000 time (us) |
Timeline of active histograms
1# xedni margotsih
|     |     |     |     | 3   |     | 4   | 5   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     |     |     | 0   |     | 1   | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
start
|     |     |     |     | 0   |     | 1   | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
histogram index #0
ThisisanimplementationoftheTimeDifferencesmeasurementclassthatextendshistogramindexingintomultiple
dimensions.
PleasereadthedocumentationofTimeDifferencesfirst. Itcapturesmanymultiplestart-multiplestophistograms,
butwithmanyasynchronousnext_channel triggers. Aftereachtagoneachnext_channel,thehistogramindexofthe
associateddimensionisincrementedbyoneandresettozeroafterreachingthelastvalidindex. Theelementsofthe
| 126 |     |     |     |     |     | Chapter7. | ApplicationProgrammingInterface |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | ------------------------------- | --- | --- | --- |

TimeTaggerUserManual,Release2.17.4.0
parametern_histogramsspecifythenumberofhistogramsperdimension. Theaccumulationstartswhennext_channel
hasbeentriggeredonalldimensions.
Youshouldprovideasynchronizationtriggerbyspecifyingasync_channelperdimension. Itwillstoptheaccumulation
whenanassociatedhistogramindexrolloveroccurs. Asynceventwillalsostoptheaccumulation,resetthehistogram
indexoftheassociateddimension,andasubsequenteventonthecorrespondingnext_channelstartstheaccumulation
again. Thesynchronizationisdoneasynchronous,soaneventonthenext_channelincreasesthehistogramindexeven
iftheaccumulationisstopped. Theaccumulationstartswhenatagonthesync_channelarriveswithasubsequenttag
onnext_channelforalldimensions.
Please use TimeTaggerBase.setInputDelay() to adjust the latency of all channels. In general, the order of the
providedtriggersincludingmaximumjittershouldbe:
oldstarttrigger–>allsynctriggers–>allnexttriggers–>newstarttrigger
class TimeDifferencesND(tagger,click_channel,start_channel,next_channels,sync_channels,n_histograms,
binwidth,n_bins)
Parameters
• tagger(TimeTaggerBase)–timetaggerobjectinstance
• click_channel(int)–channelonwhichstopclicksarereceived
• start_channel (int) – channel that sets start times relative to which clicks on the click
channelaremeasured
• next_channels(list[int])–vectorofchannelsthatincrementsthehistogramindex
• sync_channels(list[int])–vectorofchannelsthatresetsthehistogramindextozero
• n_histograms(int)–vectorofnumbersofhistogramsperdimension
• binwidth(int)–widthofonehistogrambininps
• n_bins(int)–numberofbinsineachhistogram
Seeallcommonmethods
SeemethodsofTimeDifferencesclass.
7.5.5 Fluorescence-lifetime imaging (FLIM)
ThissectiondescribestheFLIMrelatedmeasurementsclassesoftheTimeTaggerAPI.
Flim
Changedinversion2.7.2.
Note: The Flim (beta) implementation is not final yet. It has a very advanced functionality, but details are subject
tochange. Pleasegiveusfeedback(support@swabianinstruments.com)whenyouencounterissuesorwhenyouhave
ideasforadditionalfunctionality.
7.5. MeasurementClasses 127

TimeTaggerUserManual,Release2.17.4.0
0 250 500 750 1000
time (ps)
langis
Flim
begin start clickstart click nextstart click start clickclick
dt
dt dt dt dt
100
80
60
40
20
0
0 50 100 150 200 250
)(ytisnetnIemarFtnerruCteg
100
80
60
40
20
0
0 50 100 150 200 250 getIndex()
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 #bin
0 1 #pixel
Fluorescence-lifetimeimagingmicroscopy(FLIM)isanimagingtechniqueforproducinganimagebasedonthedif-
ferencesintheexponentialdecayrateofthefluorescencefromasample.
Fluorescence lifetimes can be determined in the time domain by using a pulsed source. When a population of fluo-
rophoresisexcitedbyanultrashortordelta-peakpulseoflight,thetime-resolvedfluorescencewilldecayexponentially.
This measurement implements a line scan in a FLIM image that consists of a sequence of pixels. This could either
representasinglelineoftheimage,or-iftheimageisrepresentedasasinglemeanderingline-thiscouldrepresent
theentireimage.
Weprovidetwodifferentclassesthatsupport FLIMmeasurements: Flim andFlimBase. Flim providesaversatile
high-levelAPI.FlimBaseinsteadprovidestheessentialfunctionalitywithnooverheadtoperformFlimmeasurements.
FlimBaseisbasedonacallbackapproach.
PleasevisitthePythonexamplefolderforareferenceimplementation.
Note: Uptoversion2.7.0, theFlim implementationwasverylimitedandhasbeenfullyrewritteninversion2.7.2.
Youcanusethefollowing1to1replacementtogettheoldFlimbehavior:
# FLIM before version 2.7.0:
Flim(tagger, click_channel=1, start_channel=2, next_channel=3,
binwidth=100, n_bins=1000, n_pixels=320*240)
# FLIM 2.7.0 replacement using TimeDifferences
TimeDifferences(tagger, click_channel=1, start_channel=2,
next_channel=3, sync_channel=CHANNEL_UNUSED,
binwidth=100, n_bins=1000, n_histograms=320*240)
[
class Flim(tagger,start_channel,click_channel,pixel_begin_channel,n_pixels,n_bins,binwidth ,
pixel_end_channel=CHANNEL_UNUSED,frame_begin_channel=CHANNEL_UNUSED,
]
finish_after_outputframe=0,n_frame_average=1,pre_initialize=True )
High-LevelclassforimplementingFLIMmeasurements. TheFlimclassincludesbufferingofimagesandseveral
analysismethods.
128 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
ThisclasssupportsexpansionoffunctionalitywithcustomFLIMframeprocessingbyoverridingvirtual/abstract
frameReady() callback. If you need custom implementation with minimal overhead and highest performance,
consideroverridingFlimBaseclassinstead.
Warning: When overriding this class, you must set pre_initialize=False and then call initialize() at
theendofyourcustomconstructorcode. Otherwise,youmayexperienceunstableorerraticbehaviorofyour
program,asthecallbackframeReady()maybecalledbeforeconstructionofthesubclasscompleted.
Thedataquerymethodsareorganizedintoafewgroups.
ThemethodsgetCurrentFrame...()relatetotheactiveframewhichiscurrentlybeingacquired.
ThemethodsgetReadyFrame...()relatetothelastcompletelyacquiredframe.
ThemethodsgetSummedFrames...()operatetoallframeswhichhavebeenacquiredsofar. Optionalparam-
eteronly_ready_framesselectsifthecurrentincompleteframeshallbeincludedorexcludedfromcalculation.
Themethodsget...ExinsteadofanarrayreturnaFlimFrameInfoobjectcontainingframedatawithadditional
informationcollectedatthesametimeinstance.
Parameters
• tagger(TimeTaggerBase)–timetaggerobjectinstance
• start_channel(int)–channelonwhichclicksarereceivedforthetimedifferenceshis-
togramming
• click_channel(int)–channelonwhichstartclicksarereceivedforthetimedifferences
histogramming
• pixel_begin_channel(int)–startmarkerofapixel(histogram)
• n_pixels(int)–numberofpixels(histograms)ofoneframe
• n_bins(int)–numberofhistogrambinsforeachpixel
• binwidth(int)–binsizeinpicoseconds
• pixel_end_channel(int)–endmarkerofapixel-incomingclicksontheclick_channel
willbeignoredafterward. (optional)
• frame_begin_channel(int)–starttheframe,orresetthepixelindex. (optional)
• finish_after_outputframe (int) – sets the number of frames stored within the mea-
surementclass. Afterreachingthenumber,themeasurementwillstop. Ifthenumberis0,
oneframeisstoredandthemeasurementrunscontinuously. (optional,default: 0)
• n_frame_average(int)–averagemultipleinputframesintooneoutputframe,(optional,
default: 1)
• pre_initialize (bool) – initializes the measurement on constructing. (optional, de-
fault=True). Onsubclassing,youmustsetthisparametertoFalse,andthencall.initialize()
attheendofyourcustomconstructormethod.
Seeallcommonmethods
getCurrentFrame()
Returns
Thehistogramsforallpixelsofthecurrentlyactiveframe,2Darraywithdimensions[n_bins,
n_pixels].
7.5. MeasurementClasses 129

TimeTaggerUserManual,Release2.17.4.0
Returntype
2D_array[int]
getCurrentFrameEx()
Returns
Thecurrentlyactiveframedatawithadditionalinformationcollectedatthesameinstanceof
time.
Returntype
FlimFrameInfo
getCurrentFrameIntensity()
Returns
Theintensitiesofallpixelsofthecurrentlyactiveframe. Thepixelintensityisdefinedbythe
numberofcountsacquiredwithinthepixeldividedbytherespectiveintegrationtime.
Returntype
1D_array[float]
getFramesAcquired()
Returns
Thenumberofframesthathavebeencompletedsofar,sincethecreationorlastclearofthe
object.
Returntype
int
getIndex()
Returns
Avectorofsizen_binscontainingthetimebinsinps.
Returntype
1D_array[int]
[ ]
getReadyFrame( index=-1 )
Parameters
index(int)–Indexoftheframetobeobtained. If-1,thelastframewhichhasbeencom-
pletedisreturned. (optional)
Returns
The histograms for all pixels according to the frame index given. If the index is -1, it will
return the last frame, which has been completed. When stop_after_outputframe is 0, the
index value must be -1. If index >= stop_after_outputframe, it will throw an error.
2Darraywithdimensions[n_bins,n_pixels]
Returntype
2D_array[int]
[ ]
getReadyFrameEx( index=-1 )
Parameters
index (int) – Index of the frame to be obtained. If -1, the latest frame which has been
completedisreturned. (optional)
Returns
The frame according to the index given. If the index is -1, it will return the latest
130 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
|     | completed frame. | When stop_after_outputframe | is 0, index must | be -1. If |
| --- | ---------------- | --------------------------- | ---------------- | --------- |
index >=
stop_after_outputframe,itwillthrowanerror.
Returntype
FlimFrameInfo
[ ]
index=-1
| getReadyFrameIntensity( |     | )   |     |     |
| ----------------------- | --- | --- | --- | --- |
Parameters
index(int)–Indexoftheframetobeobtained. If-1,thelastframewhichhasbeencom-
|     | pletedisreturned. | (optional) |     |     |
| --- | ----------------- | ---------- | --- | --- |
Returns
Theintensitiesaccordingtotheframeindexgiven. Iftheindexis-1,itwillreturntheintensity
of the last frame, which has been completed. When stop_after_outputframe is 0, the index
value must be -1. If index >= stop_after_outputframe, it will throw an error. The
pixel intensity is defined by the number of counts acquired within the pixel divided by the
respectiveintegrationtime.
Returntype
1D_array[float]
|                  | [ only_ready_frames=True,clear_summed=False |     | ]   |     |
| ---------------- | ------------------------------------------- | --- | --- | --- |
| getSummedFrames( |                                             |     | )   |     |
Parameters
• only_ready_frames–Iftrue,onlythefinishedframesareadded. Onfalse,thecurrently
|     | activeframeisaggregated.                                  | (optional) |     |            |
| --- | --------------------------------------------------------- | ---------- | --- | ---------- |
|     | • clear_summed–Iftrue,thesummedframesmemorywillbecleared. |            |     | (optional) |
Returns
Thehistogramsforallpixels. Thecountswithinthehistogramsareintegratedsincethestart
orthelastclearofthemeasurement.
Returntype
2D_array[int]
|                    | [                                         |     | ]   |     |
| ------------------ | ----------------------------------------- | --- | --- | --- |
| getSummedFramesEx( | only_ready_frames=True,clear_summed=False |     | )   |     |
Parameters
• only_ready_frames(bool)–Iftrue,onlythefinishedframesareadded. Onfalse,the
currentlyactiveframeisaggregated. (optional)
• clear_summed(bool)–IfTrue,thesummedframesmemorywillbecleared. (optional)
Returns
A sum of all acquired frames with additional information collected at the same instance of
time.
Returntype
FlimFrameInfo
|     |     | [   |     | ]   |
| --- | --- | --- | --- | --- |
getSummedFramesIntensity( only_ready_frames=True,clear_summed=False )
Parameters
• only_ready_frames(bool)–Iftrue,onlythefinishedframesareadded. Onfalse,the
currentlyactiveframeisaggregated. (optional)
• clear_summed(bool)–Iftrue,thesummedframesmemorywillbecleared. (optional)
7.5. MeasurementClasses 131

TimeTaggerUserManual,Release2.17.4.0
Returns
Theintensitiesofallpixelssummedoverallacquiredframes. Thepixelintensityisthenum-
berofcountswithinthepixeldividedbytheintegrationtime.
Returntype
1D_array[float]
isAcquiring()
Tellsiftheclassisstillacquiringdata. Itcanonlyreachthefalsestateif stop_after_outputframe >
0. ThismethodisdifferentfromisRunning()andindicatesifthespecifiednumberofframesisacquired.
Afteracquisitioncompleted,itcan’tbestartedagain.
Returns
True/False
Returntype
bool
frameReady(frame_number,data,pixel_begin_times,pixel_end_times,frame_begin_time,frame_end_time)
Parameters
• frame_number(int)–currentframenumber
• data (1D_array[int]) – 1D array containing the raw histogram data, with the data of
pixeliandtimebinjatindexi * n_bins + j
• pixel_begin_times(list[int])–starttimeforeachpixel
• pixel_end_times(list[int])–endtimeforeachpixel
• frame_begin_time(int)–starttimeoftheframe
• frame_end_time(int)–endtimeoftheframe
ThemethodiscalledautomaticallybytheTimeTaggerengineforeachcompletelyacquiredframe. Inits
parameters,itprovidesFLIMframedataandrelatedinformation. Youhavetooverridethismethodwith
yourownimplementation.
Warning: Thecodeofoverridemustbefast,asitisexecutedincontextofTimeTaggerprocessing
threadandblockstheprocessingpipeline. Slowoverridecodemayleadtothebufferoverflows.
initialize()
This function initialized the Flim object and starts execution. It does nothing if constructor parameter
pre_initialize==True.
FlimFrameInfo
ThisisasimpleclassthatcontainsFLIMframedataandprovidesconvenienceaccessormethods.
Note: Objects of this class are returned by the methods of the FLIM classes. Normally user will not construct
FlimFrameInfoobjectsthemselves.
class FlimFrameInfo
132 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
pixels: int
numberofpixelsintheframe
bins: int
numberofbinsofeachhistogram
frame_number: int
currentframenumber
pixel_position: int
currentpixelposition
getFrameNumber()
Returns
Theframenumber,startingfrom0fortheveryfirstframeacquired. Iftheindexis-1,itisan
invalidframewhichisreturnedonerror.
Returntype
int
isValid()
Returns
Abooleanwhichtellsifthisframeisvalidornot. Invalidframesarepossibleonerrors,such
asrequestingthelastcompletedframewhennoframehasbeencompletedsofar.
Returntype
bool
getPixelPosition()
Returns
Avaluewhichtellshowmanypixelswereprocessedforthisframe.
Returntype
int
getHistograms()
Returns
Allhistogramsoftheframe,2Darraywithdimensions[n_bins,n_pixels].
Returntype
2D_array[int]
getIntensities()
Returns
Thesummedcountsofeachhistogramdividedbytheintegrationtime.
Returntype
1D_array[float]
getSummedCounts()
Returns
Thesummedcountsofeachhistogram.
Returntype
1D_array[int]
7.5. MeasurementClasses 133

TimeTaggerUserManual,Release2.17.4.0
getPixelBegins()
Returns
Anarrayofthestarttimestampsofeachpixel.
Returntype
1D_array[int]
getPixelEnds()
Returns
Anarrayoftheendtimestampsofeachpixel.
Returntype
1D_array[int]
FlimBase
TheFlimBaseprovidesonlythemostessentialfunctionalityforFLIMtasks. Thebenefitfromthereducedfunctionality
isthatitisverymemoryandCPUefficient. TheclassprovidestheframeReady()callback, whichmustbeusedto
analyzethedata.
[
class FlimBase(tagger,start_channel,click_channel,pixel_begin_channel,n_pixels,n_bins,binwidth ,
pixel_end_channel=CHANNEL_UNUSED,frame_begin_channel=CHANNEL_UNUSED,
]
finish_after_outputframe=0,n_frame_average=1,pre_initialize=True )
ThisisaminimalclassthatacquiresaFLIMframeandcallsvirtual/abstractframeReady()callbackmethodwith
theframedataasparameters. ThisclassisintendedforcustomimplementationsoffastFLIMframeprocessing
withminimaloverhead. Youcanreachframeacquisitionratessuitableforrealtimevideoobservation.
If you need custom FLIM frame processing implementation while retaining functionality present in the Flim
class,considersubclassingFlim instead.
Warning: When overriding this class, you must set pre_initialize=False and then call initialize() at
theendofyourcustomconstructorcode. Otherwise,youmayexperienceunstableorerraticbehaviorofyour
program,asthecallbackframeReady()maybecalledbeforeconstructionofthesubclasscompleted.
Parameters
• tagger(TimeTaggerBase)–timetaggerobjectinstance
• start_channel(int)–channelonwhichclicksarereceivedforthetimedifferenceshis-
togramming
• click_channel(int)–channelonwhichstartclicksarereceivedforthetimedifferences
histogramming
• pixel_begin_channel(int)–startmarkerofapixel(histogram)
• n_pixels(int)–numberofpixels(histograms)ofoneframe
• n_bins(int)–numberofhistogrambinsforeachpixel
• binwidth(int)–binsizeinpicoseconds
• pixel_end_channel(int)–endmarkerofapixel-incomingclicksontheclick_channel
willbeignoredafterward. (optional,default: CHANNEL_UNUSED)
• frame_begin_channel(int)–starttheframe,orresetthepixelindex. (optional,default:
CHANNEL_UNUSED)
134 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
• finish_after_outputframe (int) – sets the number of frames stored within the mea-
surementclass. Afterreachingthenumber,themeasurementwillstop. Ifthenumberis0,
oneframeisstoredandthemeasurementrunscontinuously. (optional,default: 0)
• n_frame_average(int)–averagemultipleinputframesintooneoutputframe. (optional,
default: 1)
• pre_initialize(bool)–initializesthemeasurementonconstructing. (optional,default:
True). Onsubclassing,youmustsetthisparametertoFalse,andthencall.initialize()atthe
endofyourcustomconstructormethod.
Seeallcommonmethods
isAcquiring()
Returns
Abooleanwhichtellstheuseriftheclassisstillacquiringdata. Itcanonlyreachthefalsestate
forstop_after_outputframe > 0. ThisisdifferentfromisRunning()asonceframe(s)
acquisitionisdone,itcan’tbestartedagain.
Returntype
bool
frameReady(frame_number,data,pixel_begin_times,pixel_end_times,frame_begin_time,frame_end_time)
Parameters
• frame_number(int)–currentFramenumber
• data (1D_array[int]) – 1D array containing the raw histogram data, with the data of
pixeliandtimebinjatindexi * n_bins + j
• pixel_begin_times(list[int])–starttimeforeachpixel
• pixel_end_times(list[int])–endtimeforeachpixel
• frame_begin_time(int)–starttimeoftheframe
• frame_end_time(int)–endtimeoftheframe
ThemethodiscalledautomaticallybytheTimeTaggerengineforeachcompletelyacquiredframe. Inits
parameters,itprovidesFLIMframedataandrelatedinformation. Youhavetooverridethismethodwith
yourimplementation.
Warning: Thecodeofoverridemustbefast,asitisexecutedincontextofTimeTaggerprocessing
threadandblockstheprocessingpipeline. Slowoverridecodemayleadtothebufferoverflows.
initialize()
This function initialized the Flim object and starts execution. It does nothing if constructor parameter
pre_initialize==True.
7.5. MeasurementClasses 135

TimeTaggerUserManual,Release2.17.4.0
| 7.5.6 | Phase | &   | frequency | analysis |     |     |     |     |     |     |     |     |
| ----- | ----- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Thissectiondescribesmeasurementsthatexpectperiodicsignals,e.g.,oscillatoroutputs.
FrequencyStability
FrequencyStability(tagger, channel=1, steps=[1, 3, ...], average=4)
Channel 1
|     | Internally |     |  0  |  1  |  2  3 |     |  4  |  5  |  6  |  7  |  8  |  9  |
| --- | ---------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
averaged
|               |          |     | E (1)  | E (1) | ...     |     |     | ... | E (1) | E (1) |     | ... |
| ------------- | -------- | --- | ------ | ----- | ------- | --- | --- | --- | ----- | ----- | --- | --- |
|               | ADEV for |     | 0      | 1     |         |     |     |     | 6     | 7     |     |     |
| step size n=1 |          |     |        | ×1    | ×-2 ×1  |     |     |     |       | ×1    | ×-2 | ×1  |
|               |          |     | ×1 ×-2 |       | ×1      |     |     |     | ×1    | ×-2   | ×1  |     |
|               |          |     | E (3)  | E (3) | ...     |     |     |     |       |       |     |     |
|               | ADEV for |     | 0      | 1     |         |     |     |     |       |       |     |     |
| step size n=3 |          |     |        | ×1    |         |     | ×-2 |     |       | ×1    |     |     |
|               |          |     | ×1     |       | ×-2     |     |     |     | ×1    |       |     |     |
|               |          | 0.0 | 0.5    |       | 1.0 1.5 |     | 2.0 | 2.5 |       | 3.0   | 3.5 | 4.0 |
Time (µs)
Step size n
|     |     | 100 |     |     | 102 | 103 |          |                    |     |        | 106         |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------------ | --- | ------ | ----------- | --- |
|     |     |     |     | 101 |     |     |          | 104                | 105 |        |             | 107 |
|     |     |     |     |     |     |     |          | fn (E (n))2 with E |     | (n)=ti | 2ti+n+ti+2n |     |
|     | 10  | 5   |     |     |     |     | ADEVn =  | i                  |     | i      |             |     |
i
noitaiveD nallA
log-log slope 1:
Frequency drift
6
10
log-log slope -1:
log-log slope 0:
Phase noise, esp.
Flicker period noise
7 discretization noise
10
|     |     |     | 10 6 | 10  | 5 10 | 4   | 10 3 | 10  | 2   | 10 1 | 100 |     |
| --- | --- | --- | ---- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- |
 (s)
Frequency Stability Analysis is used to characterize periodic signals and to identify sources of deviations from the
perfectperiodicity. Itcanbeemployedtoevaluatethefrequencystabilityofoscillators,forexample. Asetofestablished
metricsprovidesinsightsintotheoscillatorcharacteristicsondifferenttimescales. Themostprominentmetricisthe
AllanDeviation(ADEV).TheFrequencyStability classexecutesthecalculationofoftenusedmetricsinparallel
andconformstotheIEEE1139standard. Formoreinformation,werecommendtheHandbookofFrequencyStability
Analysis.
√︂
|     |     |     |     |     |     |     | (︁  | )︁2 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thecalculateddeviationsaretheroot-mean-square 𝑓 ∑︀ 𝐸(𝑛) ofaspecificsetoferrorsamples𝐸(𝑛) witha
𝑛 𝑖 𝑖
normalizationfactor𝑓 . Thestepsize𝑛togetherwiththeoscillatorperiod𝑇 definesthetimespan𝜏 thatis
|     |     |     | 𝑛   |     |     |     |     |     |     |     |     | 𝑛 = 𝑛𝑇 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
investigatedbythesample. Theerrorsamples𝐸(𝑛) arecalculatedfromthephasesamples𝑡thataregeneratedbythe
FrequencyStability classbyaveragingoverthetimestampsofaconfigurablenumberoftime-tags. Toinvestigate
theaveragedphasesamplesdirectly,atraceofconfigurablelengthisstoredtodisplaythecurrentevolutionoffrequency
andphaseerrors.
Eachoftheavailabledeviationshasitsspecificsample𝐸(𝑛). Forexample,theAllanDeviationinvestigatesthesecond
derivativeofthephase𝑡usingthesample𝐸(𝑛) =𝑡 −2𝑡 +𝑡 . ThefullformulaoftheAllandeviationforaset
|     |     |     |     |     | 𝑖   | 𝑖   | 𝑖+𝑛 𝑖+2𝑛  |     |                                 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------------------------- | --- | --- | --- |
| 136 |     |     |     |     |     |     | Chapter7. |     | ApplicationProgrammingInterface |     |     |     |

TimeTaggerUserManual,Release2.17.4.0
of𝑁 averagedtimestampsis
⎯
⎸ 𝑁−2𝑛
ADEV(𝜏 )= ⎸ ⎷ 1 ∑︁ (𝑡 −2𝑡 +𝑡 )2.
𝑛 2(𝑁 −2𝑛)𝜏2 𝑖 𝑖+𝑛 𝑖+2𝑛
𝑛 𝑖=1
ThedeviationscanbedisplayedintheAllandomainorinthetimedomain. Forthetimedomain, theAllandomain
dataismultipliedbyafactorproportionalto𝜏. Thismeansthatinalog-logplot,allslopesofthetimedomaincurves
√
areincreasedby+1comparedtotheAllanones. Thefactor 3forADEV(Allandeviation)/MDEV(ModifiedAllan
deviation)and√︀ 10/3for HDEV(Hadamarddeviation),respectively,isusedsothatthescaleddeviationsofawhite
phase noise distortion correspond to the standard deviation of the averaged timestamps 𝑡. In some cases, there are
differentestablishednamesfortherepresentations. TheFrequencyStability classprovidesnumerousmetricsfor
bothdomains:
Allandomain Timedomain
StandardDeviation(STDD)
AllanDeviation(ADEV) ADEVScaled= √𝜏 ADEV
3
ModifiedAllanDeviation(MDEV) TimeDeviationTDEV= √𝜏 MDEV
3
HadamardDeviation(HDEV) HDEVScaled= √𝜏 HDEV
10/3
class FrequencyStability(tagger,channel,steps,average,trace_len)
Parameters
• channel(int)–Theinputchannelnumber.
• steps(list[int])–Thestepsizestoconsiderinthecalculation. Thelengthofthelistde-
terminesthemaximumnumberofdatapoints. Becausetheoscillatorfrequencyisunknown,
itisnotpossibletodefine𝜏 directly.
• average(int)–Thenumberoftime-tagstoaverageinternally. Thisdownsamplingallows
forareductionofnoiseandmemoryrequirements. Defaultis1000.
• trace_len(int)–Numberofdatapointsinthephaseandfrequencyerrortraces,calculated
fromaverageddata. Thetracealwayscontainsthelatestdata. Defaultis1000.
Note: UseaverageandTimeTagger.setEventDivider()withcare: Theeventdividercanbeusedtosave
USBbandwidth. Ifpossible,transfermoredataviaUSBanduseaveragetoimproveyourresults.
Seeallcommonmethods
getDataObject()
Returns
Anobjectthatallowsaccesstothecurrentmetrics
Returntype
FrequencyStabilityData
class FrequencyStabilityData
getTau()
The 𝜏 axis for all deviations. This is the product of the steps parameter of the FrequencyStability
measurementandthemeasuredaverageperiodofthesignal.
7.5. MeasurementClasses 137

TimeTaggerUserManual,Release2.17.4.0
Returns
The𝜏 values.
Returntype
1D_array[float]
getADEV()
TheoverlappingAllandeviation,themostcommonanalysisframework. Inalog-logplot,theslopeallows
onetoidentifythetypeofnoise:
• -1: whiteorflickerphasenoiselikediscretizationoranalognoisydelay
• -0.5: whiteperiodnoise
• 0: flickerperiodnoiselikeelectricnoisyoscillator
• 0.5: integratedwhiteperiodnoise(randomwalkperiod)
• 1: frequencydrift,e.g.,inducedthermally
Sample
𝐸(𝑛) =𝑡 −2𝑡 +𝑡
𝑖 𝑖 𝑖+𝑛 𝑖+2𝑛
Domain
Allandomain
Returns
TheoverlappingAllanDeviation.
Returntype
1D_array[float]
getMDEV()
Modified overlapping Allan deviation. It averages the second derivate before calculating the RMS. This
splitstheslopeofwhiteandflickerphasenoise:
• -1.5: whitephasenoise,likediscretization
• -1.0: flickerphasenoise,likeanelectricnoisydelay
Themetricismorecommonlyusedinthetimedomain,seegetTDEV().
Sample
𝐸(𝑛) = 1 ∑︀𝑛−1(𝑡 −2𝑡 +𝑡 )
𝑖 𝑛 𝑗=0 𝑖+𝑗 𝑖+𝑗+𝑛 𝑖+𝑗+2𝑛
Domain
Allandomain
Returns
TheoverlappingMDEV.
Returntype
1D_array[float]
getHDEV()
The overlapping Hadamard deviation uses the third derivate of the phase. This cancels the effect of a
constantphasedriftandconvergesformoredivergentnoisesourcesathigherslopes:
• 1: integratedflickerperiodnoise(flickerwalkperiod)
• 1.5: doubleintegratedwhiteperiodnoise(randomrunperiod)
ItisscaledtomatchtheADEVforwhiteperiodnoise.
138 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
Sample
𝐸(𝑛) =𝑡 −3𝑡 +3𝑡 −𝑡
𝑖 𝑖 𝑖+𝑛 𝑖+2𝑛 𝑖+3𝑛
Domain
Allandomain
Returns
TheoverlappingHadamardDeviation.
Returntype
1D_array[float]
getSTDD()
Caution: Thestandarddeviationisnotrecommendedasameasureoffrequencystabilitybecauseit
isnon-convergentforsometypesofnoisecommonlyfoundinfrequencysources,mostnoticeablethe
frequencydrift.
Standarddeviationoftheperiods.
Sample
𝐸(𝑛) =𝑡 −𝑡 −mean (𝑡 −𝑡 )
𝑖 𝑖 𝑖+𝑛 𝑘 𝑘 𝑘+𝑛
Domain
Timedomain
Returns
Thestandarddeviation.
Returntype
1D_array[float]
getADEVScaled()
Domain
Timedomain
Returns
ThescaledversionoftheoverlappingAllanDeviation,equivalenttogetADEV()*getTau()
√
/ 3.
Returntype
1D_array[float]
getTDEV()
The Time Deviation (TDEV) is the common representation of the Modified overlapping Allan deviation
getMDEV(). Takingthelog-logslope+1andthesplittingoftheslopeofwhiteandflickerphasenoiseinto
account,itallowsaneasyidentificationofthetwocontributions:
• -0.5: whitephasenoise,likediscretization
• 0: flickerphasenoise,likeanelectricnoisydelay
Domain
Timedomain
Returns
√
TheoverlappingTimeDeviation,equivalenttogetMDEV()*getTau()/ 3.
7.5. MeasurementClasses 139

TimeTaggerUserManual,Release2.17.4.0
Returntype
1D_array[float]
getHDEVScaled()
Caution: While HDEV is scaled to match ADEV for white period noise, this function is scaled to
matchtheTDEV(Timedeviation)forwhitephasenoise. Thedifferenceofperiodvsphasematching
isroughly5%andeasytooverlook.
Domain
Timedomain
Returns
The scaled version of the overlapping Hadamard Deviation, equivalent to getHDEV() *
getTau()/√︀ 10/3.
Returntype
1D_array[float]
getTraceIndex()
ThetimeaxisforgetTracePhase()andgetTraceFrequency().
Returns
Thetimeindexinsecondsofthephaseandfrequencyerrortrace.
Returntype
1D_array[float]
getTracePhase()
Providesthetimeoffsetoftheaveragedtimestampsfromalinearfitoverthelasttrace_lenaveragedtimes-
tamps.
Returns
Atraceofthelasttrace_lenphasesamplesinseconds.
Returntype
1D_array[float]
getTraceFrequency()
Provides the relative frequency offset from the average frequency during the last trace_len + 1 averaged
timestamps.
Returns
Atraceofthelasttrace_lennormalizedfrequencyerrordatapointsinpp1.
Returntype
1D_array[float]
getTraceFrequencyAbsolute(input_frequency: float=0.0)
Providestheabsolutefrequencyoffsetfromagiveninput_frequencyduringthelasttrace_len+1averaged
timestamps.
Parameters
input_frequency(float)–Nominalfrequencyoftheperiodicsignal. Defaultis0Hz.
Returns
Atraceofthelasttrace_lenfrequencydatapointsinHz.
140 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
Returntype
1D_array[float]
FrequencyCounter
Time (ns)
0 500 1000 1500 2000 2500 3000 3500 4000
SoftwareClock.
ideal_clock
_channel
Channel 1,
10 MHz with
phase noise
7
6
5
4
3
2
1
0
getPeriods
Count()
getPeriods
Fraction()
getPhase(1e7)
get
Frequency()
getFrequency
Instantaneous()
0 1 2 3
getIndex()
doirep
evitaleR
FrequencyCounter(tagger, channels=[1], sampling_interval=1e6, fitting_window=800e3)
[0] [9] [19] [30]
[0.1494] [0.9958] [0.9959] [0.0697]
[0.1494] [-0.0042] [-0.0041] [0.0697]
[NaN] [9.85e6] [10.00e6] [10.07e6]
[10.29e6] [10.24e6] [9.99e6] [9.98e6]
Thismeasurementcalculatesthephaseofaperiodicsignalatevenlyspacedsamplingtimes. IftheSoftwareClock is
active,thesamplingtimeswillautomaticallyalignwiththeSoftwareClockState.ideal_clock_channel. Multi-
plechannelscanbeanalyzedinparalleltocomparethephaseevolutionintime. Aroundeverysamplingtime,thetime
tagswithinanadjustablefitting_windowareusedtofitthephase.
class FrequencyCounter(tagger,channels: list[int],sampling_interval: int,fitting_window: int,n_values: int=
0)
Parameters
• tagger(TimeTaggerBase)–TimeTaggerobjectinstance
• channels(list[int])–Listofchannelstoanalyze
• sampling_interval (int) – The sampling interval in picoseconds. If the Software-
Clock is active, it is recommended to set this value to an integer multiple of the
SoftwareClockState.clock_period.
• fitting_window(int)–Timetagswithinthisrangearoundasamplingpointarefittedfor
phasecalculation
7.5. MeasurementClasses 141

TimeTaggerUserManual,Release2.17.4.0
• n_values(int)–Maximumnumberofsamplingpointstostore
Seeallcommonmethods
getDataObject(event_divider: int=1,remove: bool=False)
Returns a FrequencyCounterData object containing a snapshot of the data accumulated in the
FrequencyCounter atthetimethismethodiscalled. Theevent_divider argumentcanbeusedtoscale
theresultsaccordingtothecurrentsettingofTimeTagger.setEventDivider(). Theremoveargument
allowsyoutocontrolwhetherthedatashouldberemovedfromtheinternalbufferornot.
Parameters
• event_divider(int)–CompensatefortheEventDivider. Default: 1.
• remove(bool)–Controlifdataisremovedfromtheinternalbuffer. Default: True.
Returns
Anobjectprovidingaccesstoasnapshotdata.
Returntype
FrequencyCounterData
class FrequencyCounterData
size: int
Numberofsamplingpointsrepresentedbytheobject.
overflow_samples: int
Numberofsamplingpointsaffectedbyanoverflowrangesincethestartofthemeasurement.
align_to_reference: bool
IndicatesifthesamplinggridhasbeenalignedtotheSoftwareClock.
sampling_interval: int
Thesamplingintervalinpicoseconds.
sample_offset: int
Indexoffsetofthefirstsamplingpointintheobject.
getIndex()
Indexofthesamples. Thereferencesamplewouldhaveindex0,countingstartswith1atthefirstsampling
point.
Returns
Theindexofthesamples
Returntype
1D_array[int]
getTime()
Arrayoftimestampsofthesamplingpoints.
Returns
Thetimestampsofthesamplingpoints
Returntype
1D_array[int]
getPeriodsCount()
Theintegerpartofthephase,i.e. fullperiodsoftheoscillation.
142 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
Returns
Fullcyclesperchannelandsamplingpoint.
Returntype
2D_array[int]
getPeriodsFraction()
Thefractionofthecurrentperiodatthesamplingtime.
Warning: BecarefulwithaddinggetPeriodsCount()andgetPeriodsFraction()astherequired
precisioncanoverflowa64bitdoubleprecisionwithinminutes. Indoubt,pleaseusegetPhase()with
theexpectedfrequencyinstead.
Returns
Afractionalvalueinrange[0,1)perchannelandsamplingpoint.
Returntype
2D_array[float]
getPhase(reference_frequency: float=0.0)
Therelativephasewithrespecttoanumericalreferencesignal, typicallyattheexpectedfrequency. The
reference signal starts at phase 0 at index 0, so the return value of this method is identical to that of
getPeriodsFraction()forindex0.
Parameters
reference_frequency–ThereferencefrequencyinHztosubtract. Default: 0.0Hz.
Returns
Relativephasevaluesperchannelandsamplingpoint.
Returntype
2D_array[float]
getFrequency(time_scale: int=1_000_000_000_000)
The frequency with respect to the phase difference to the last sampling interval. At index 0, there is no
previousphasevaluetocomparewith,sothemethodreturnsanundefinedvalueNaN bydefinition.
Parameters
time_scale–Scalesthereturnvaluetothistimeinterval. Defaultis1s,sothereturnvalue
isinHz. Fornegativevalues,thetimescaleissettosampling_interval.
Returns
Afrequencyvalueperchannelandsamplingpoint.
Returntype
2D_array[float]
getFrequencyInstantaneous()
Theinstantaneousfrequencywithrespecttothecurrentfittingwindow. Thisvaluecorrespondstotheslope
ofthelinearfit.
Returns
Aninstantaneousfrequencyvalueperchannelandsamplingpoint.
Returntype
2D_array[float]
7.5. MeasurementClasses 143

TimeTaggerUserManual,Release2.17.4.0
getOverflowMask()
Ifanoverflowrangeoverlapswithafittingwindow,thevaluesareinvalid. Thismaskarrayindicatesinvalid
elementsandcanbeusedtofiltertheresultsoftheothergetters.
Returns
1indicatesthatthesamplingpointwasaffectedbyanoverflowrange,0indicatesvaliddata.
Returntype
2D_array[int]
PulsePerSecondMonitor
PulsePerSecondMonitor(tagger, reference_channel=1, signal_channels=[2, 3])
Time (s)
0 1 2 3 4 5
Reference
Channel
Channel 2
(stable)
Channel 3
(unstable)
getReference
0.e+0 -2.1e-3 3.7e-4 2.8e-3 -9.9e-4
Offsets()
getSignal
[-1.5e-3, -4.2e-2] [1.4e-2, -1.3e-3] [-6.6e-2, 1.7e-1] [-1.5e-2, nan] [-1.2e-1, 8.6e-3]
Offsets()
getStatus() True True True False True
0 1 2 3 4
Reference Index
Note: PulsePerSecondMonitor()andPulsePerSecondDataarepartoftheExperimentalnamespace,andtheir
propertiesmaychangeinfuturesoftwareversionswithoutfurthernotice. Theycanbeaccessedas:
TimeTagger.Experimental.PulsePerSecondMonitor(tagger, reference_channel=1, signal_
channels=[2,3],
˓→
filename="output", period=1E12)
Thismeasurementallowstheusertomonitorthesynchronicityofdifferentsourcesof1pulsepersecond(PPS)signals
withrespecttoareferencesource. ForeachsignalfromthereferencePPSsource,comparativeoffsetsarecalculatedfor
theothersignalchannels. Uponprocessing,aUTCtimestampfromthesystemtimeisassociatedwitheachreference
pulse.
Themonitoringstartsonthefirstsignalfromthereferencesourceandwillrununinterrupteduntilthemeasurement
is stopped. If a signal from a channel is not detected within one and a half periods, its respective offset will not be
calculatedbutthemeasurementwillcontinuenonetheless.
Byspecifyinganoutputfilename, themonitoringdatacanbecontinuouslywrittentoacomma-separatedvaluefile
(.csv).
144 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
class PulsePerSecondMonitor(tagger,reference_channel: int,signal_channels: list[int],filename: str='',
period: int=1E12)
Parameters
• tagger(TimeTaggerBase)–TimeTaggerobjectinstance.
• reference_channel (int) – the channel number corresponding to the PPS reference
source.
• signal_channels(list[int])–alistofchannelnumberswithPPSsignalstobecom-
paredtothereference.
• filename(str)–thenameofthe.csvfiletostoremeasurementdata. Bydefault,nodata
iswrittentofile.
• period(int)–theassumedperiodofthereferencesource,typicallyonesecond,inpicosec-
onds.
Seeallcommonmethods
getDataObject(boolremove=False)
Returns a PulsePerSecondData object containing a snapshot of the data accumulated in the
PulsePerSecondMonitoratthetimethismethodiscalled. Toremovethedatafromtheinternalmemory
aftereachcall,setremovetoTrue.
Parameters
remove(bool)–Controlsifthereturneddatashallberemovedfromtheinternalbuffer.
Returns
Anobjectprovidingaccesstoasnapshotdata.
Returntype
PulsePerSecondData
class PulsePerSecondData
size: int
NumberofreferencepulsescontainedinthePulsePerSecondData object.
getIndices()
The indices of each reference pulse in the PulsePerSecondData object. The first reference pulse will
have index 0, each subsequent pulse from the reference source increments the index by one. In case of
overflowsinthereferencechannel,thisindexwillbeincrementedbythenumberofmissedpulses.
Returns
Alistofindicesforeachpulsefromthereferencesource.
Returntype
1D_array[int]
getReferenceOffsets()
Alistofoffsetsofeachreferencepulsewithrespectivetoitspredecessor,withtheperiodsubtracted. For
aperfectPPSsource,thisoffsetwouldalwaysbezero.
Theoffsetofthefirstpulseisalwaysdefinedtobezero. Ifareferencesignalismissing,itsoffsetisdefined
tobeNaN.
Returns
Alistoftheoffsetsofeachreferencewithrespecttotheprevious.
Returntype
1D_array[float]
7.5. MeasurementClasses 145

TimeTaggerUserManual,Release2.17.4.0
getSignalOffsets()
ForeachreferencecontainedinthePulsePerSecondData objectalistofoffsetsforeachsignalchannel
isgiven,inthechannelordergivenbysignal_channels.
Ifanysignalismissing,itsoffsetisdefinedtobeNaN.
Returns
Alistoflistsofoffsetsforeachsignal_channelforgivenreferencepulses.
Returntype
2D_array[float]
getUtcSeconds()
ThenumberofelapsedsecondsfromthebeginningoftheUnixepoch(1stofJanuary1970)tothetimeat
whicheachreferencepulseisprocessed,asafloatingpointnumber.
Returns
A list of the number of seconds since the Unix epoch to the time of processing, for each
referencepulse.
Returntype
1D_array[float]
getUtcDates()
TheUTCtimestampsforthesystemtimeatwhicheachreferencepulseisprocessed,asastringwithISO
8601formatting(YYYY-MM-DD hh:mm:ss.ssssss).
Returns
AlistoftheUTCtimestampatprocessingtime,foreachreferencepulse.
Returntype
1D_array[str]
getStatus()
Alistofbooleansvaluesdescribingwhetherallsignals,includingfromthereferencesource,weredetected.
Truecorrespondstoacompletecollectionofsignals,Falseotherwise.
Returns
Alistofboolsdescribingthesignalintegrityforeachreferencepulse.
Returntype
1D_array[bool]
7.5.7 Time-tag-streaming
Measurement classes described in this section provide direct access to the time tag stream with minimal or no pre-
processing.
146 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
Timetagformat
Thetimetagcontainessentialinformationaboutthedetectedeventandhavethefollowingformat:
| Size  | Type        | Description                |
| ----- | ----------- | -------------------------- |
| 8bit  | enumTagType | overflowtype               |
| 8bit  | –           | reserved                   |
| 16bit | uint16      | numberofmissedevents       |
| 32bit | int32       | channelnumber              |
| 64bit | int64       | timeinpsfromdevicestart-up |
TimeTagStream
Allowsusertoaccessacopyofthetimetagstream. Itallocatesamemorybufferofthesizemax_tagswhichisfilled
withtheincomingtimetagsthatarrivefromthespecifiedchannels. UsershallcallgetData()methodperiodically
toobtainthecurrentbuffercontainingtimetagscollected. Thisactionwillreturnthecurrentbufferobjectandcreate
anotheremptybuffertobefilleduntilthenextcalltogetData().
TimeTagStream(tagger,n_max_events,channels)
class
Parameters
• tagger(TimeTaggerBase)–timetaggerobjectinstance
• n_max_events(int)–buffersizeforstoringtimetags
• channels(list[int])–non-emptylistofchannelstobecaptured.
Seeallcommonmethods
getData()
ReturnsaTimeTagStreamBuffer objectandclearstheinternalbufferoftheTimeTagStream measure-
ment. Clearing the internal buffer on each call to getData() guarantees that consecutive calls to this
methodwillreturneverytime-tagonlyonce. DatalossmayoccurifgetData()isnotcalledfrequently
enoughwithrespectton_max_events.
Returns
bufferobjectcontainingtimetagscollected.
Returntype
TimeTagStreamBuffer
class TimeTagStreamBuffer
| size: int |     |     |
| --------- | --- | --- |
Number of events stored in the buffer. If the size equals the maximum size of the buffer set in
vian_max_events,eventshavelikelybeendiscarded.
TimeTagStream
| hasOverflows: | bool |     |
| ------------- | ---- | --- |
ReturnsTrueifastreamoverflowwasdetectedinanyofthetagsreceived. Note: thisisindependentofan
overflowoftheinternalbufferofTimeTagStream.
| tStart: int |     |     |
| ----------- | --- | --- |
Returnthedata-streamtimepositionwhentheTimeTagStream orFileWriterstarteddataacquisition.
| tGetData: | int |     |
| --------- | --- | --- |
Returnthedata-streamtimepositionofthecallto.getData()methodthatcreatedthisobject.
7.5. MeasurementClasses 147

TimeTaggerUserManual,Release2.17.4.0
getTimestamps()
Returnsanarrayoftimestamps.
Returns
Eventtimestampsinpicosecondsforallchosenchannels.
Returntype
list[int]
getChannels()
Returnsanarrayofchannelnumbersforeverytimestamp.
Returns
Channelnumberforeachdetectedevent.
Returntype
list[int]
getOverflows()
Deprecatedsinceversion2.5.0: pleaseusegetEventTypes()instead.
getEventTypes()
Returns an array of event type for every timestamp. See, Time tag format. The method returns plain
integers,butyoucanuseTagTypetocomparethevalues.
Returns
Eventtypevalueforeachdetectedevent.
Returntype
1D_array[int]
getMissedEvents()
Returnsanarrayofmissedeventcountsduringanstreamoverflowsituation.
Returns
Missedeventsvalueforeachdetectedevent.
Returntype
1D_array[int]
FileWriter
Writes the time-tag-stream into a file in a structured binary format with a lossless compression. The estimated file
sizerequirementsare2-4Bytespertimetag, notincludingthecontainerthedataisstoredin. Thecontinuousback-
grounddatarateforthecontainercanbemodifiedviaTimeTagger.setStreamBlockSize(). Dataisprocessedin
blocks and each block header has a size of 160 Bytes. The default processing latency is 20 ms, which means that a
blockiswrittenevery20msresultinginabackgrounddatarateof8kB/s. Byincreasingtheprocessinglatencyvia
setStreamBlockSize(max_events=524288, max_latency=1000)to1s,theresultingdatarateforthecontainer
isreducedtoone160B/s. ThefilescreatedwithFileWritermeasurementcanbereadusingFileReaderorloaded
intotheVirtualTimeTagger.
Note: YoucanusetheDump fordumpingintoasimpleuncompressedbinaryformat. However,youwillnotbeable
tousethisfilewithVirtualTimeTaggerorFileReader.
TheFileWriterisabletosplitthedataintomultiplefilesseamlesslywhenthefilesizereachesamaximalsize. For
thefilesplittingtoworkproperly,thefilenamespecifiedbytheuserwillbeextendedwithasuffixcontainingsequential
counter,sothefilenameswilllooklikeinthefollowingexample
148 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
fw = FileWriter(tagger, 'filename.ttbin', [1,2,3]) # Store tags from channels 1,2,3
# When splitting occurs the files with following names will be created
# filename.ttbin # the sequence header file with no data blocks
# filename.1.ttbin # the first file with data blocks
# filename.2.ttbin
# filename.3.ttbin
# ...
Inaddition,theFileWriterwillqueryandstoretheconfigurationoftheTimeTaggerinthesameformatasreturned
bytheTimeTaggerBase.getConfiguration()method. Theconfigurationisalwayswrittenintoeveryfile.
Seealso: FileReader,TheTimeTaggerVirtualclass,andmergeStreamFiles().
class FileWriter(tagger,filename,channels)
Parameters
• tagger(TimeTaggerBase)–timetaggerobject
• filename(str)–nameofthefiletostoreto
• channels(list[int])–non-emptylistofrealorvirtualchannels
Classconstructor. Aswithallothermeasurements,thedatarecordingstartsimmediatelyaftertheclassinstan-
tiationunlessyouinitializetheFileWriterwithaSynchronizedMeasurements.
Note: ComparedtotheDumpmeasurement,theFileWriterrequiresexplicitspecificationofthechannels. If
youwanttostoretimetagsfromallinputchannels,youcanquerythelistofallinputchannelswithTimeTagger.
getChannelList().
Seeallcommonmethods
[ ]
split( new_filename="" )
Closethecurrentfileandcreateanewone. Ifthenew_filenameisprovided,thedatawritingwillcontinue
intothefilewiththenewfilenameandthesequencecounterwillberesettozero.
Youcanforcethefilesplittingwhenyoucallthismethodwithoutparameterorwhenthenew_filenameis
anemptystring.
Parameters
new_filename(str)–filenameofthenewfile.
setMaxFileSize(max_file_size)
Setthemaximumfilesizeondisk. Whenthissizeisexceededanewfilewillbeautomaticallycreatedto
continuerecording. Theactualfilesizemightbelargerbyoneblock. (default: ~1GByte)
getMaxFileSize()
Returns
Themaximalfilesize. SeealsoFileWriter.setMaxFileSize().
Returntype
int
getTotalEvents()
Returns
Thetotalnumberofeventswrittenintothefile(s).
7.5. MeasurementClasses 149

TimeTaggerUserManual,Release2.17.4.0
Returntype
int
getTotalSize()
Returns
Thetotalnumberofbyteswrittenintothefile(s).
Returntype
int
FileReader
ThisclassallowsyoutoreaddatafilesstorewithFileReader. TheFileReader readsadatablockofthespecified
size into a TimeTagStreamBuffer object and returns this object. The returned data object is exactly the same as
returnedbytheTimeTagStream measurementandallowsyoutocreateacustomdataprocessingalgorithmsthatwill
workboth,forreadingfromafileandfortheon-the-flyprocessing.
TheFileReaderwillautomaticallyrecognizeifthefilesweresplitandreadthemtooonebyone.
Example:
# Lets assume we have following files created with the FileWriter
# measurement.ttbin # sequence header file with no data blocks
# measurement.1.ttbin # the first file with data blocks
# measurement.2.ttbin
# measurement.3.ttbin
# measurement.4.ttbin
# another_meas.ttbin
# another_meas.1.ttbin
# Read all files in the sequence 'measurement'
fr = FileReader("measurement.ttbin")
# Read only the first data file
fr = FileReader("measurement.1.ttbin")
# Read only the first two files
fr = FileReader(["measurement.1.ttbin", "measurement.2.ttbin"])
# Read the sequence 'measurement' and then the sequence 'another_meas'
fr = FileReader(["measurement.ttbin", "another_meas.ttbin"])
Seealso: FileWriter,TheTimeTaggerVirtualclass,andmergeStreamFiles().
class FileReader(filenames)
This is the class constructor. The FileReader automatically continues to read files that were split by the
FileWriter.
Parameters
filenames(list[str])–filename(s)ofthefilestoread.
getData(size_tn_events)
Readsthenextn_eventsandreturnsthebufferobjectwiththespecifiednumberoftimetags. TheFileReader
storesthecurrentlocationinthedatafileandguaranteesthateverytimetagisreturnedonce. Iflessthan
n_elementsarereturned,thereaderhasreachedtheendofthelastfileinthefile-listfilenames. Tocheckif
moredataisavailableforreading,itismoreconvenienttousehasData().
150 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
Parameters
n_events(int)–Numberoftimetagstoreadfromthefile.
Returns
Abufferofsizen_events.
Returntype
TimeTagStreamBuffer
hasData()
Returns
True if more data is available for reading, False if all data has been read from all the files
specifiedintheclassconstructor.
Returntype
bool
getConfiguration()
Returns
AJSONformattedstring(dictinPython)thatcontainstheTimeTaggerconfigurationatthe
timeoffilecreation.
Returntype
strordict
getChannelList()
Returns
allchannelsavailablewithintheinputfile
Returntype
list[int]
Dump
Deprecatedsinceversion2.6.0: pleaseuseFileWriterinstead.
Warning: ThefilescreatedwiththisclassarenotreadablebyTimeTaggerVirtualandFileReader.
Writesthetimetagstreamintoafileinasimpleuncompressedbinaryformatthatstoretimetagsas128bitrecords,see
Timetagformat.
Pleasevisittheprogrammingexamplesprovidedintheinstallationfolderofhowtodumpandloaddata.
class Dump(tagger,filename,max_tags,channels)
Parameters
• tagger(TimeTaggerBase)–timetaggerobjectinstance
• filename(str)–nameofthefiletodumpto
• max_tags (int) – stop after this number of tags has been dumped. Negative values will
dumpforever
• channels(list[int])–listofrealorvirtualchannelswhicharedumpedtothefile(when
emptyornotpassedallactivechannelsaredumped)
7.5. MeasurementClasses 151

TimeTaggerUserManual,Release2.17.4.0
clear()
Deletecurrentdatainthefileandrestartdatastorage.
stop()
Stopsdatarecordingandclosesdatafile.
Scope
trigger
window_size
rising edge
falling edge
trace
0 10 20 30 40 50 60 70 80
Time (ns)
TheScopeclassallowstovisualizetimetagsforrisingandfallingedgesinatimetracediagramsimilarlytoanultrafast
logicanalyzer. Thetracerecordingissynchronizedtoatriggersignalwhichcanbeanyphysicalorvirtualchannel.
However, only physical channels can be specified to the event_channels parameter. Additionally, one has to specify
the time window_size which is the timetrace duration to be recorded, the number of traces to be recorded and the
maximumnumberofeventstobedetected. If n_traces < 1thenretriggeringwilloccurinfinitely,whichissimilar
tothe“normal”modeofanoscilloscope.
Note: Scopeclassimplicitlyenablesthedetectionofpositiveandnegativeedgesforeveryphysicalchannelspecified
inevent_channels. Thisaccordinglydoublesthedataraterequirementperinput.
class Scope(tagger,event_channels=[],trigger_channel,window_size,n_traces,n_max_events)
Parameters
• tagger(TimeTagger)–TimeTaggerobject
• event_channels(list[int])–Listofchannels
• trigger_channel(int)–Channelnumberofthetriggersignal
• window_size(int)–Timewindowinpicoseconds
• n_traces(int)–Numberoftriggereventstobedetected
• n_max_events(int)–Maxnumberofeventstobedetected
Seeallcommonmethods
getData()
Returns a tuple of the size equal to the number of event_channels multiplied by n_traces, where each
elementisatupleofEvent.
152 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
Returns
Eventlistforeachtrace.
Returntype
tuple[tuple[Event]]
ready()
Returns
Returns whether the acquisition is complete which means that all traces (n_traces) are ac-
quired.
Returntype
bool
triggered()
Returns
Returnsnumberoftriggereventshavebeencapturedsofar.
Returntype
int
class Event
Pairofthetimestampandthenewstate.
time
Type
int
state
Type
State
class State
Currentinputstate. Canbeunknownbecausenoedgehasbeendetectedonthegivenchannelafterinitialization
oranoverflow.
UNKNOWN
HIGH
LOW
7.5. MeasurementClasses 153

TimeTaggerUserManual,Release2.17.4.0
Sampler
trigger in overflow
channel[0]
channel[1]
getData [ [11, 0, 2], [24, 0, 0], [36, 0, 1], not captured [71, 1, 2] ]
getDataAsMask [ [11, 0b1...00], [24, 0b00], [36, 0b10], in overflow [71, 0b1...01]]
0 10 20 30 40 50 60 70 80
Time (ns)
TheSamplerclassallowssamplingthestateofasetofchannelsviaatriggerchannel.
Foreveryeventonthetriggerinput,thecurrentstate(low: 0,high: 1,unknown: 2)willbewrittentoaninternalbuffer.
Fetchingthedataoftheinternalbufferwillclearitsinternalbuffer,soeveryeventwillbereturnedonlyonce.
TimeTaggerdetectspulseedgesandthereforeachannelwillbeintheunknownstateuntilanedgedetectioneventwas
receivedonthatchannelfromthestartofthemeasurementorafteranoverflow. Theinternalprocessingassumesthat
noeventcouldbereceivedwithinthechannel’sdeadtimeotherwiseinvaliddatawillbereporteduntilthenextevent
onthisinputchannel.
Themaximumnumberofchannelsislimitedto63foroneSamplerinstance.
class Sampler(tagger,trigger,channels,max_trigger)
Parameters
• tagger(TimeTagger)–TimeTaggerobject
• trigger(int)–Channelnumberofthetriggersignal
• channels(list[int])–Listofchannelstobesampled
• max_trigger(int)–Thenumberoftriggersandtheirrespectivesampleddata, whichis
storedwithinthemeasurementclass.
Seeallcommonmethods
getData()
Returnsandremovesthestoreddataasa2Darray(n_triggersx(1+n_channels)):
[
[timestamp of first trigger, state of channel 0, state of channel 1, ...],
[timestamp of second trigger, state of channel 0, state of channel 1, ...],
...
]
Wherestatemeans:
154 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
0: low
1: high
2: undefined (after overflow)
Returns
sampleddata
Returntype
2D_array[int]
getDataAsMask()
Returnsandremovesthestoreddataasa2Darray(n_triggersx2):
[
[timestamp of first trigger, (state of channel 0) << 0 | (state of channel␣
1) << 1 | ... | any_undefined << 63],
˓→
[timestamp of second trigger, (state of channel 0) << 0 | (state of channel␣
1) << 1 | ... | any_undefined << 63],
˓→
...
]
Wherestatemeans:
0: low or undefined (after overflow)
1: high
Ifthehighestbit(data[63])ismarked,oneofthechannelshasbeeninanundefinedstate.
Returns
sampleddata
Returntype
2D_array[int]
7.5.8 Helper classes
SynchronizedMeasurements
TheSynchronizedMeasurementsclassallowsforsynchronizingmultiplemeasurementclassesinawaythatensuresall
thesemeasurementstostart,stopsimultaneouslyandoperateonexactlythesametimetags. YoucanpassaTimeTagger
proxy-objectreturnedbySynchronizedMeasurements.getTagger()toeverymeasurementyoucreate. Thiswill
simultaneouslydisabletheirautostartandregisterforsynchronization.
class SynchronizedMeasurements(tagger)
Parameters
tagger(TimeTaggerBase)–TimeTaggerobject
registerMeasurement(measurement)
Registersthemeasurementobjectintoapoolofthesynchronizedmeasurements.
Note: Registration of the measurement classes with this method does not synchronize them.
In order to start/stop/clear these measurements synchronously, call these functions on the
7.5. MeasurementClasses 155

TimeTaggerUserManual,Release2.17.4.0
SynchronizedMeasurements object after registering the measurement objects, which should be
synchronized.
Parameters
measurement–Anymeasurement(IteratorBase)object.
unregisterMeasurement(measurement)
Unregistersthemeasurementobjectoutofthepoolofthesynchronizedmeasurements.
Note: Thismethoddoesnothingiftheprovidedmeasurementisnotcurrentlyregistered.
Parameters
measurement–Anymeasurement(IteratorBase)object.
start()
Callsstart()foreveryregisteredmeasurementinasynchronizedway.
[ ]
startFor(duration ,clear=True )
CallsstartFor()foreveryregisteredmeasurementinasynchronizedway.
stop()
Callsstop()foreveryregisteredmeasurementinasynchronizedway.
clear()
Callsclear()foreveryregisteredmeasurementinasynchronizedway.
isRunning()
CallsisRunning()foreveryregisteredmeasurementandreturnstrueifanymeasurementisrunning.
getTagger()
Returnsaproxytaggerobjectwhichcanbepassedtotheconstructorofameasurementclasstoregisterthe
measurementsatinitializationtothesynchronizedmeasurementobject. Thosemeasurementswillnotstart
automatically.
Note: The proxy tagger object returned by getTagger() is not identical with the TimeTagger object
createdbycreateTimeTagger(). Youcancreatesynchronizedmeasurementswiththeproxyobjectthe
followingway:
tagger = TimeTagger.createTimeTagger()
syncMeas = TimeTagger.SynchronizedMeasurements(tagger)
taggerSync = syncMeas.getTagger()
counter = TimeTagger.Counter(taggerSync, [1, 2])
countrate = TimeTagger.Countrate(taggerSync, [3, 4])
Passingtaggerasaconstructorparameterwouldleadtothenotsynchronizedbehavior.
156 Chapter7. ApplicationProgrammingInterface

TimeTaggerUserManual,Release2.17.4.0
7.5.9 Custom Measurements
The class CustomMeasurement allows you to access the raw time tag stream with very little overhead. By
inheriting from CustomMeasurement, you can implement your fully customized measurement class. The
CustomMeasurement.process()methodofthisclasswillbeinvokedassoonasnewdataisavailable.
Note: This functionality is only available for C++, C# and Python. You can find examples of how to use the
CustomMeasurementinyourexamplesfolder.
class CustomMeasurement(tagger)
Parameters
tagger(TimeTaggerBase)–TimeTaggerobject
TheconstructoroftheCustomMeasurement classitselftakesonlytheparametertagger. Whenyousub-class
yourownmeasurement,youcanaddtoyourconstructoranyparametersthatarenecessaryforyourmeasurement.
Youcanfinddetailedexamplesinyourexamplefolder.
Seeallcommonmethods
process(incoming_tags,begin_time,end_time)
Parameters
• incoming_tags–Tag[][struct{type,missed_events,channel,time}],thechunkoftime-
tagstobeprocessedinthiscallofprocess(). Thisisanexternalreferencethatisshared
withothermeasurementsandmightbeoverwrittenforthenextcall. Soifyouneedtostore
tags,createacopy.
• begin_time(int)–Thebegintimeofthedatachunk.
• end_time(int)–Theendtimeofthedatachunk
Overridetheprocess()methodtoincludeyourdataprocessing. ThemethodwillbecalledbytheTime
Tagger backend when a new chunk of time-tags is available. You are free to execute any code you like,
butbeawarethatthisisthecriticalpartwhenitcomestoperformance. InPython, itisadvisabletouse
numpy.array()forcalculationorevenpre-compiledcodewithNumbaifanexplicititerationofthetagsis
necessary. Checktheexamplesinyourexamplesfoldercarefullyonhowtodesigntheprocess()method.
Note: InPython,theincoming_tagsareastructuredNumpyarray. Youcanaccesssingletagsaswellas
arraysoftagentriesdirectly:
first_tag = incoming_tags[0]
all_timestamps = incoming_tags['time']
mutex
Contextmanagerobject(seeContextManagerTypes)thatlocksthemutexwhenusedandautomatically
unlocksitwhenthecodeblockexits. Forexample,itisintendedforusewithPython’s“with”keywordas
class MyMeasurement(CustomMeasurement):
def getData(self):
# Acquire a lock for this instance to guarantee that
# self.data is not modified in other parallel threads.
# This ensures to return a consistent data.
(continuesonnextpage)
7.5. MeasurementClasses 157

TimeTaggerUserManual,Release2.17.4.0
(continuedfrompreviouspage)
with self.mutex:
return self.data.copy()
| 158 | Chapter7. | ApplicationProgrammingInterface |
| --- | --------- | ------------------------------- |

CHAPTER
EIGHT
IN DEPTH GUIDES
ThissectioncontainsarticlesthatprovideindepthdetailsontheTimeTaggerhardwareandsoftware.
8.1 Conditional Filter
TheConditionalFilterisahardwarefeaturethatallowsyoutoremoveirrelevanttimetagscarryingnoinformation. In
a typical use case, you have a high-frequency signal applied to at least one channel. Examples include fluorescence
lifetimemeasurementsoropticalquantuminformationandcryptographywhereyouwanttocapturesynchronization
clicksfromahighrepetitionrateexcitationlaser.
TheConditionalFilterdistinguishesbetweentrigger channelsandfiltered channels. AllinputchannelsofyourTime
Taggerarefullyequivalentandcanbeusedasboth,triggerorfilteredchannels. Thedatarateofthefilteredchannels
willbereduced. Thereductioniscontrolledbythetriggerchannels: Everytriggeropensthegateforaneventofthe
filteredchannel. AllothereventsinthefilteredchannelswillbediscardedontheTimeTaggeranddonotneedtobe
transferredviatheUSBconnection.
Beingahardwarefeature,theConditionalFilterisnotcontrolledonthelevelofindividualmeasurements. Itisenabled
onthelevelofyourphysicaldevicewithatypicalPythoncodelookinglike
import TimeTagger
tagger = TimeTagger.createTimeTagger()
tagger.setConditionalFilter(trigger=[1], filtered=[8])
ThedetailswillbeexplainedintheSetupoftheConditionalFiltersection.
8.1.1 Example configurations
Onetriggerandonefilteredchannel
Themostfundamentalcaseinvolvesonefiltered-channelandonetrigger-channel:
tagger.setConditionalFilter(trigger=[1], filtered=[8])
TheConditionalFilterdiscardsbydefaultallsignalsofthefiltered-channel. Onlytheverynexteventistransmitted
afteraneventonthetrigger-channel. Intheexample,click2opensthegateforclick3. Whenclick3passes,itcloses
thegateandthesubsequenteventswillbediscardeduntilanotherevent(click8)occursinthetriggerchannel.
159

TimeTaggerUserManual,Release2.17.4.0
| Trigger #1  |     |  2  |     |     |     |     |     |  8  |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filtered #8 |  1  |  3  |     |  4  |  5  |  6  |     |  7  |  9  |  10 |  11 |  12 |  13 |
|             | 0   | 10  | 20  | 30  | 40  | 50  | 60  | 70  | 80  |     |     |     |     |
Time (ns)
Multipletrigger-channels
Thereistheoptiontodefinemorethanonetrigger-channelfortheConditionalFilter. Asaconsequence,thenextevent
onthefiltered-channelistransmittedwhentherewasaeventatanyofthetrigger-channels:
| tagger.setConditionalFilter(trigger=[1, |     |     |     | 2], | filtered=[8]) |     |     |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Trigger #1                              |     |  2  |     |     |               |     |     |  9  |     |     |     |     |     |
| Trigger #2                              |     |     |     |     |  6            |     |     |     |     |     |     |     |     |
|                                         |  1  |  3  |     |  4  |  5            |  7  |     |  8  |  10 |  11 |  12 |  13 |  14 |
Filtered #8
|     | 0   | 10  | 20  | 30  | 40  | 50  | 60  | 70  | 80  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time (ns)
Thisisthetypicalusecasewhenyoudetectphotonswithmultipledetectorsandwanttocorrelatebothwiththecommon
excitationlaser.
Multiplefilteredchannels
ItisalsopossibletousetheConditionalFilterwithonetrigger-channelandseveralfiltered-channels:
| tagger.setConditionalFilter(trigger=[1], |     |     |     | filtered=[7, |     | 8]) |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Trigger #1                               |     |  3  |     |              |     |     |     |  11 |     |     |     |     |     |
| Filtered #7                              |     |  2  |     |  6           |     |  8  |     |  12 |     |  14 |     |     |     |
|                                          |  1  |  4  |     |  5           |  7  |  9  |     |  10 |  13 |  15 |  16 |  17 |  18 |
Filtered #8
|     | 0   | 10  | 20  | 30  | 40  | 50  | 60  | 70  | 80  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time (ns)
| 160 |     |     |     |     |     |     | Chapter8. | InDepthGuides |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | --- | --- | --- | --- |

TimeTaggerUserManual,Release2.17.4.0
Multipletriggerandfilteredchannels
Ingeneral,youcanalsocombinemultipletrigger-channelsandmultiplefiltered-channels:
| tagger.setConditionalFilter(trigger=[1, |     |     |     | 2], | filtered=[7, | 8]) |     |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|                                         |     |  3  |     |     |              |     |     |  12 |     |     |     |     |     |
Trigger #1
| Trigger #2  |     |     |     |     |  8  |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filtered #7 |     |  2  |     |  6  |     |  9  |     |  13 |     |  15 |     |     |     |
| Filtered #8 |  1  |  4  |     |  5  |  7  |  10 |  11 |     |  14 |  16 |  17 |  18 |  19 |
|             | 0   | 10  | 20  | 30  | 40  | 50  | 60  | 70  | 80  |     |     |     |     |
Time (ns)
Thisschemeshowstwodifferenthigh-frequencysignalsonchannels#7and#8. Suchcasescanoccurwhenyouwant
toruntwocompletelyindependentexperimentsonasingleTimeTagger. Forinstance,channels#1/#7and#2/#8may
representthetwoexperiments. ItisnotpossibletosetuptwoindependentConditionalFiltersforthesegroups. The
schemeshownistheonlywaytoapplytheConditionalFilterinthiscase-withthedrawbackthatchannel#1(#2)may
alsotriggerchannel#8(#7),makingthefilteringlessefficient.
| 8.1.2 Understanding |     | the | filtering | mechanism |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The Conditional Filter is a hardware feature that is embedded in a sequence of processing stages. It is important to
understandtheorderofthesestages. Someunexpectedresultscanoccurwhenyouarenotawareofthesemechanisms,
soreadthefollowingsectionwithcare.
Terms
Inputtimestamp
Thisisthetimestampyouareinterestedin: Itreferstothetimewhentheinputsignaltransitsthetriggerlevelat
theinputconnector.
TDCtimestamp
ThisisthetimestamptheTimeTaggerisinterestedin: Itistheraw64bitintegertheFPGAattributestoapulse
edge.
Hardwaredelay
ThesignalenteringtheinputconnectorisroutedthroughtheTimeTaggerintotheFPGAwherethetimetodigital
conversionisperformed. Thisroutediffersfromchanneltochannelandsodoestheaccumulateddelay. Because
ofthis,weneedtodistinguishbetweenInputtimestampandTDCtimestamp. Thehardwaredelaycannotbe
controlledbytheuser,itisdefinedbythedesignoftheTimeTaggerhardwareandtheFPGAconfiguration(this
canvaryfromsoftwarereleasetosoftwarerelease). Butdon’tworry,theTimeTaggeriscalibratedtocompensate
forthisdelay. ThiscompensationisdoneonthedeviceincaseoftheTimeTaggerUltraandtheTimeTagger
X. The Time Tagger 20 can only apply the delay in software (see details below). Except for the purpose of
understandingtheConditionalFilter,youdonotneedtocareaboutthedifference.
| 8.1. ConditionalFilter |     |     |     |     |     |     |     |     | 161 |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

TimeTaggerUserManual,Release2.17.4.0
Externaldelay
AnydelayintroducedbeforetheTimeTagger,e.g. bycablelengthsoropticalpathways.
Processingstages
1. PulseenterstheTimeTagger: Uptotheinputconnector,theuserisinchargeoftheexternaldelays. Theycan
becontrolledbychangingcablelengthsoropticalpathways. ThetimetaggeneratedbytheTimeTaggershould
thereforerepresentthetemporalorderattheinputconnectors. Thisistheinputtimestamp.
2. Timetodigitalconversion: ThepulsespropagatethroughtheTimeTagger. Theyarecomparedtothetrigger
leveloftheinputstage. Thisresultsinahighorlowlogiclevel. Thisisstillanaloginformationthatpropagates
totheFPGA.Here,theTDCtimestampisattributedtothepulseedge. Thepropagationlengthuptothistime
todigitalconversion(TDC)differsfromchanneltochannel. Itcanbecompensatedinoneofthelaterstages.
3. Adjustablehardwaredelay(TTUltraandTTXonly!): Fromsoftwareversion2.8.0on,theTimeTaggerUltra
isabletobufferandreorderthetagsbeforetheConditionalFilter. ForTimeTaggerX,thisfeatureisavailable
fromsoftwareversion2.12.0on. YoucansetanindividualdelayforeveryinputstagebyTimeTaggerBase.
setDelayHardware(). Thisbehaveslikeanadjustablehardwaredelayandiscalibratedbydefaulttocompen-
sateforthephysicalhardwaredelay. ItchangesthebehavioroftheConditionalFiltertremendously,asyouwill
seeinthenextstages.
4. Adjustabledeadtime: Asafirstfilterstage,theadjustabledeadtimeisapplied. Itactsonlyonthechannelitself,
consideringrisingandfallingedgesastwoseparatechannels. Afteraneventinoneofthechannelsoccurred,
noothereventcanappearinthesamechannelforthedefineddeadtime. OntheTimeTagger20,thedeadtime
canonlybesetinintegermultiplesoftheFPGAclockcycleof6nswithatechnicallyrequiredminimumofone
cycle. Conversely, ontheTimeTaggerUltra andTimeTaggerX,thedeadtimecanbesettoanyintegervalue
greaterthanthedurationofoneFPGAclockcycle,whichis2000psand1333ps,respectively.
5. Conditional Filter: As a second filter stage, the Conditional Filter is applied. The time tags of trigger chan-
nels and filtered channels are compared. If your device is able to introduce Adjustable hardware delay, this
happens based on the timestamp including the Hardware delay compensation and the additional delay set by
TimeTaggerBase.setDelayHardware(). Otherwise,therawTDCtimestampisused. Inbothcases,thetime
orderofthesestampscandeviatefromtheorderoftheinputtimestampsthatyouaredealingwithusually. Note:
Intheedgecaseofeventsarrivingatthesametime(dt=0)onatriggerandfilteredchannel, itisnotspecified
whethertheeventonthefilteredchannelatdt=0ispassedthrough,orthesubsequent,orboth.
6. EventDivider:Asathirdfilterstage,theEventDividercanbeapplied. Onlyeveryn-thtimetagoftherespective
channelistransmitted,allothersaredismissed.
7. Thebottleneck-USBtransfer:ThetimetagsarebufferedandtransmittedtothePC.Atthispoint,afterapplying
ConditionalFilterandEventDivider,itisimportantthattheresultingdatarateonaveragedoesnotexceedthe
maximumdatarate.
8. setDelaySoftware: From now on, the Time Tagger hardware is not involved anymore. If your device does
not provide an adjustable hardware delay, the software compensates now the TDC time stamp for the hard-
waredelaytoprovideyoutheinputtimestamp(itispossibletodisablethehardwaredelaycompensation,see
Controlhardwaredelaycompensation). Inanycase,youcanmodifythiscompensationbyTimeTaggerBase.
setDelaySoftware().
9. DelayedChannel: ThemostflexiblewaytocontroltherelativedelayofyoursignalsareVirtualChannels.
162 Chapter8. InDepthGuides

TimeTaggerUserManual,Release2.17.4.0
Consequences
Thenatureofthefilteringprocesscanproducecounterintuitiveresultsthatneedtobehandled. Wewillexplorethese
cases based on the example of a fluorescence lifetime measurement. The sample is excited by a pulsed laser with a
repetitionrateof80MHz(periodof12.5ns),thelasersynchronizationsignalisconnectedtochannel#8. Sochannel
#8isthehigh-frequencyinputthatneedstobefiltered. Fluorescencephotonsarecollectedbyasingle-photondetector
connected to channel #1 that will trigger the Conditional Filter. We set up a correlation measurement and look at
differentcases:
TimeTagger.Correlation(tagger, 1, 8)
Case 1:
without CF
Case 2:
with CF
Case 3:
with CF,
shifted
Case 4:
click prob.
@ 40%
30 20 10 0 10 20 30
Time (ns)
Case 1: Without the Conditional Filter set up, the Correlation measurement class provides a periodic signal. The
periodicityisaresultofthemulti-start/multi-stopapproachoftheCorrelationmeasurement: Aclickonthedetector
will contribute together with any laser synchronization pulse to the correlation, not only with the one that actually
stimulatedthephoton. WithouttheConditionalFilter,therewillbealasertimetagevery12.5ns. Becausethishigh
frequencycannotbetransferredforalongtime,bufferoverflowswillleadtodiscardeddata.
Case2: WiththeConditionalFilteron,thedatarateishighlyreducedatthecostoflosingthefullperiodicityofthe
signal:
tagger.setConditionalFilter(trigger=[1], filtered=[8])
Now we observe that the majority of the events is in the range of a few nanoseconds. However, the signal does not
looklikeexpected: InsteadofasignalresemblingoneofthepeaksfromCase1,adoublepeakappears. Ifyoulook
carefullyatthesignal,youcanseethatthelifetimecurveiscutalongthedottedlineandonepartisshiftedbyoneperiod.
Thisindicatesthatthephysicaldelaybetweentheinputchannelsisnotdesignedproperly. Theschemeillustratesthe
problem:
Trigger #1 2 8
Filtered #8 1 3 4 5 6 7 9 10 11 12 13
0 10 20 30 40 50 60 70 80
Time (ns)
Thedashedlineindicateswhichpulseexcitedthesample. Ifthephotonisemittedearlybythesample(click2),itwill
8.1. ConditionalFilter 163

TimeTaggerUserManual,Release2.17.4.0
triggerthefirstpulse(click3)afterthestimulatingone(click1). Inthesecondcase,thephotonisemittedlateandthe
subsequentlaserpulse(click7)hasalreadypassed. Inthiscase,click9ispassedandclick8seemstobeveryearly,
althoughitisquitelate,infact.
Case3: Toalignthesignalproperly,havingthesignalinbetweentwolaserevents,thestrategydependsonyourdevice:
WithTimeTaggerUltra(withsoftwareversion2.8.0andlater)andTimeTaggerX(withsoftwareversion2.12.0and
later),youcanuseTimeTaggerBase.setDelayHardware()toalignyoursignals. InthecaseofaTimeTagger20,
however,youneedtoadjustyourexternaldelays. Youmighteithermodifyopticalpathlengthsorusecablesofdifferent
lengths.
Case4: Thiscaseillustratesthattheheightofthehigher-orderpeaksisdeterminedbythecountrateofyourdetector.
Therelativeheight(comparedtothecenterpeak)isproportionaltotheprobabilityforalasersynchronizationpulse
to pass the Conditional Filter in the higher-order period. This probability is given by the probability that a detector
clickoccursintherespectiveperiodandgatesthesynchronizationclick. InCase1,withouttheConditionalFilter,the
probability is 100% - every synchronization pulse is passed. For Case 2 and Case 3, the probability has been set to
10%,inCase4ithasbeenincreasedto40%.
Note: InCases3and4,withexternaldelayswelladjustedtoeachother,youcanseeasignalatnegativetimes. How
isthispossible? Wouldn’tthismeanthatthelasersynchronizationclickarrivedearlierthanthephotonclickthatgated
it? DoesmyTimeTaggerviolatecausality?
Theansweris: No,itdoesnot. Theoccurrenceofnegativedelaysiscausedbythedifferencebetweentheinputtime
stamps and the TDC time stamps. Negative delays occur in input time stamps, but causality must only be obeyed in
TDCtimestamps(plusadjustableonboarddelays,ifavailable). Theoccurrenceofnegativedelaysindicatesthatthe
hardwaredelayofchannel#8(lasersynchronization)islargerthanthatofchannel#1(detector).
8.1.3 Setup of the Conditional Filter
The TimeTagger.setConditionalFilter() method expects two arguments, trigger and filtered, and accepts the
optionalbooleanargumenthardwareDelayCompensation:
tagger.setConditionalFilter(trigger: list[int],
filtered: list[int],
hardwareDelayCompensation: bool = True)
TheeffectoftriggerandfiltercanbereviewedintheExampleconfigurationssection.
Controlhardwaredelaycompensation
WiththeargumenthardwareDelayCompensationyoucandecidewhetherthehardwaredelayiscompensatedornot.
Thismeans,infact,thatyoucandecidewhetheryouworkwithinputtimestampsorwithTDCtimestamps. Ifyour
devicesupportsadjustableonboarddelays,youshouldneversetthisvaluetoFalseandyoucanignorethissection.
hardwareDelayCompensation=True(default)
Pros
• Timetagsareprovidedinthewayyouareusedtoit
• Thesignalpositionwillnotdependonthesoftwareversion
Cons
• Negativetimedifferencescanoccurbetweentrigger-channelandfiltered-channelandseeminglyvio-
latecausality
164 Chapter8. InDepthGuides

TimeTaggerUserManual,Release2.17.4.0
hardwareDelayCompensation=False
Pros
• ProvidedTimetagswillbeinthesametemporalorderasfortheConditionalFilter,nonegativetime
differenceswilloccur
Cons
• Signalpositionsmaychangeuponsoftwareupdate
• Affectsallchannels,notonlytheoneslistedintriggerandfiltered.
DisabletheConditionalFilter
To disable the Conditional Filter, you can either pass an empty lists or use the TimeTagger.
clearConditionalFilter()method:
tagger.setConditionalFilter([], [])
# or
tagger.clearConditionalFilter()
8.2 Raw Time-Tag-Stream access
ThereareseveralwaystoaccesstherawtimetagswiththeTimeTaggerAPI.Theycanbesplitintotwocategories:
dumpingtogetherwithpost-processingandon-the-flyprocessing. Bothwayswillbeexplainedinthefollowing. They
arenotexclusivesothatyoucancombinethem,also,withothermeasurementsfromourAPIinparallel.
8.2.1 Dumping and post-processing
AllincomingtimetagsorselectedchannelsoftheTimeTaggercanbestoredontheharddriveviatheFileWriter.
PleasevisitthedocumentationandtheprovidedprogrammingexamplesofFileWriterforfurtherdetails.
Therearetwowaysforpost-processingthedumpeddata:
FileReader
ByreadinginthestoredtimetagswiththeFileReader,thetagsstoredcanbeprocessednativelyinyourpreferred
programminglanguage. YoufindexamplesofhowtousetheFileReaderinyourexamplesfolder.
VirtualTimeTagger
ThesecondoptiontoprocessstoredtimetagsistheTimeTaggerVirtual. TheTimeTaggerVirtualallowsyoutouse
thefullTimeTaggerAPItopost-processyourdata. YoufindexamplesofhowtousetheTimeTaggerVirtualinyour
examplesfolder.
8.2. RawTime-Tag-Streamaccess 165

TimeTaggerUserManual,Release2.17.4.0
8.2.2 On-the-fly processing
Therearetwooptionstoprocessrawincomingdata,theTimeTagStream andtheCustomMeasurement,whichwill
beexplainedinthefollowing:
TimeTagStream-high-level,lowerperformance
TheTimeTagStream bufferstheincomingrawdataforon-the-flyprocessing. TheTimeTagStream buffermustbe
polledtoretrievethetags. YoufindexamplesofhowtousetheTimeTagStream inyourexamplesfolder.
CustomMeasurement-low-level,higherperformance
The CustomMeasurement functionality allows you to access the raw time tag stream with very little overhead.
By inheriting from CustomMeasurement, you can implement your fully customized measurement class. The
CustomMeasurement.process()methodofthisclasswillbeinvokedassoonasnewdataisavailable. Notethatthis
functionalityisonlyavailableforC++,C#,andPython. YoufindexamplesofhowtousetheCustomMeasurementin
yourexamplesfolder.
CustomVirtualChannel-modifythetimetagstream-C++only
Itisnowpossibleforyoutomodifythetimetagstream,likeourAPIdoesbyinsertingtimetags,e.g.,viaCoincidence
orDelayedChannel. Ifyouwanttousethisfunctionality,pleasecontactSwabianInstrumentssupport.
IteratorBase-C++only
AllmeasurementsandvirtualchannelsarederivedfromtheIteratorBaseclass. Youcanseehowtoaccessthetime
tagstreamonthedeepestlevelwiththeprovidedC++examples.
8.3 Synchronization of the Time Tagger pipeline
In order to achieve a real-time evaluation of the events with high data rates, the Time Tagger series uses a pipeline
basedparallelprocessing.
Thehardwarerecordsatimestampforeveryincomingeventandstoresitinalargeon-devicebuffer. Thesizeofthis
buffer can be configured with setHardwareBufferSize(). The buffer contents are read by computer over USB,
typicallyinblocksof128keventsorwhenthetimebetweentheblocksexceeds20ms. Waitinguntilablockofdata
isavailableisaimedatoptimizingtheUSBthroughputwhilelimitingthetimebetweenconsecutiveblockallowsfor
reducingdatalatencyonsloweventrates. TheblocksizecanbetunedbyauserwithsetStreamBlockSize(). Onthe
computer,theblocksofdataareprocessedbyallrunningmeasurementsintheorderinwhichthemeasurementswere
created. Onlyonemeasurementhasaccesstoablockatanygiventime. Onceameasurementhasfinishedprocessing
theblock,itisreadytoprocessthenextblockwhilethepreviousblockbecomesavailabletothenextmeasurement.
Naturally,thetransferringandprocessingofthedatatakestimeandresultsinthelatency. Thelatencybetweensignal
arrivalanditsappearanceinthemeasurementdataisusuallybelow100ms;however,itcanbecomeaslargeasafew
secondsiftheon-devicebufferfillsupfasterthanthecomputercantransferandprocessthedata.
Properoperationofthepipelineandthecontrolofthedeviceparametersrequiresasuitablesynchronizationmethod.
TimeTaggerusestheconceptoffencing. Afenceisauniqueidentifierthatissentbythesoftwaretothehardware. Itis
addedattheendoftheon-devicebufferdata,streamedbacktothecomputeralongwithtimestampdata,andprocessed
by all measurement classes. Once the Time Tagger software detects the fence, it knows that it is located at the data
positionwhichwasinthebufferwhenthefencewascreated. Theusefulnessoffencingiseasilydemonstratedwitha
166 Chapter8. InDepthGuides

TimeTaggerUserManual,Release2.17.4.0
followingexample. Whenyoucreateameasurement,youexpectthatitstartsprocessingdatafromthatveryinstance
oftime;however,itstartsprocessingthedata,whichwasrecordedearlierandisalreadyavailableinthebuffer. With
fencing,themeasurementcreatesafenceandbeginsdataaccumulationonlywhenitreceivesthefenceback. Inthis
way, themeasurementisdealingwiththedatarecordedasclosetothemeasurementcreationaspossibleandavoids
processingoftheolderdata.
You can use the fencing mechanism manually. First, you have to create a new fence with TimeTaggerBase.
getFence() and then wait for it to be signaled with waitForFence() at any time later. If you want to create a
fenceandimmediatelywaitforitthenusingthesync()methodismoreconvenient.
8.4 FPGA link
Warning: The reference design and the on-the-wire format are not stable and will be subject to incompatible
changeswithfurtherdevelopment.
TheFPGAlinkoutputoftheTimeTaggerX allowsyoutoconnectanFPGAofyourowndesigntotheTimeTaggerX
viaanEthernet-basedprotocolandbenefitfromhigherdatathroughputandlowerlatencycomparedtoUSB.
Inatypicalusecase,youwanttouseeitherprocesstagsatahigherratethantheUSBconnectiontothePCallowsor
integratethemeasurementsintoatestfixtureandtriggereventsbasedonthemeasurements.
TheSFP+portontheTimeTaggerXcanbeusedeitherwithaDACorfibertransceiverstoconnecttoyourownFPGA.
WerecommendusingtheOpalKellyXEM8320foryourcustomdesign.
TheQSFP+portontheTimeTaggerX shouldbeusedwithafibertransceivertoconnecttoyourownFPGA.Wealso
recommendusingtheOpalKellyXEM8320togetherwiththeSZG-QSFPforyourcustomdesign.
Note: WerecommendusingtheSFP+portunlessthehigherbandwidthisnecessary.
Warning: Thereiscurrentlynoretransmissionsupportsoifcorruptionoccursduringtransmission,tagswillbe
permanentlylost. Pleaseverifythatyourdatalinkisofhighqualityorthattaglosscanbetolerated.
8.4.1 Getting Started with SFP+
To enable the FPGA link output of the Time Tagger use enableFpgaLink(). Start by enabling the FPGA link on
channel1:
import TimeTagger
tagger = TimeTagger.createTimeTagger()
tagger.enableFpgaLink([1], "", TimeTagger.FpgaLinkInterface.SFPP_10GE, True)
Toreceivethetags,useourTimeTaggerFPGAlinkreferencedesign. FollowtheinstructionsintheXEM8320readme
tobuildthereferencedesign. ConnecttheSFP+portontheTimeTaggerX totheSFP 1portontheXEM8320and
loadthebitstreamontheXEM8320. YoushouldnowbeabletoobservetheLEDD1ontheXEM8320matchingthe
inputstateonchannel1oftheTimeTaggerX.
Toverifythelinkquality,activateatestsignalasfollows:
tagger.setTestSignal([1], True)
8.4. FPGAlink 167

TimeTaggerUserManual,Release2.17.4.0
andreloadthebitstreamontheXEM8320. LEDD6shouldstaydark,indicatingthatthechannel1eventsarearriving
attheexpectedtimewithoutdrops.
8.4.2 Using QSFP+
QSFP+isquitesimilartousingSFP+. StartbyenablingtheFPGAlinkfortheQSFP+interfaceforinputchannel1of
theTimeTaggerX:
import TimeTagger
tagger = TimeTagger.createTimeTagger()
tagger.enableFpgaLink([1], "", TimeTagger.FpgaLinkInterface.QSFPP_40GE, True)
Similarly use our Time Tagger FPGA link reference design, but follow the instructions in the [40G readme](https:
//github.com/swabianinstruments/TimeTagger-FPGALink-Reference/tree/main/target/opalkelly-xem8320-qsfp).
ConnecttheQSFP+portoftheTimeTaggerX withtheSZG-QSFPmodulewhichhastobeconnectedtoPortEofthe
XEM8320. YoushouldnowbeabletoobservetheLEDD1ontheXEM8320matchingtheinputstateonchannel1of
theTimeTaggerX.
Note: UsingthereferencedesignwithQSFP+requirestheXilinxEF-DI-LAUI-SITEIPcorelicense. Werecommend
startingwiththeSFP+connection.
Warning: Only one output is active at the same time. Enabling the QSFP+ port disables the SFP+ port and
vice-versa.
8.4.3 Modifying the reference design
FollowtheinstructionsinBuildingyouowndesign.
168 Chapter8. InDepthGuides

CHAPTER
NINE
USAGE STATISTICS COLLECTION
YoucanhelpusdevelopingandimprovingtheTimeTaggerbyenablingautomatedusagestatisticscollection. Theusage
statisticsdatacollectionisdesignedtohelpusbetterunderstandhowtheTimeTaggerhardwareandsoftwareareused.
Thisdataincludestheperformanceindicators,configuration,thestateoftheTimeTagger,andAPIusagepatterns. The
usagestatisticsdataispseudonymized1andcannotbelinkedtoaspecificuserorspecifichardwareunit. Oninstallation
oftheTimeTaggersoftware,arandomuser_idwillbecreatedandaddedtotheusagestatisticsreports. Userscanreview
thecontentsofusagestatisticsdatabyusingthegetUsageStatisticsReport(). Alsouserscandisableusagestatis-
ticsdatacollectionatanytimeviaTimeTaggerAPIassetUsageStatisticsStatus(UsageStatisticsStatus.
Disabled). Itispossibletoenabletheusagestatisticscollectiontemporarilyandwithoutautomaticuploadingwhich
maybehelpfulfordebugging.
9.1 Contents of the usage statistics data
• Internalcalibrationdata.
• HardwaresensordataobtainablewithTimeTagger.getSensorData()butwiththeserialnumberobscured.
• TimeTagger’sconfigurationasreturnedbygetConfiguration()butwiththeserialnumberobscured.
• AllwarninganderrormessagesproducedbytheTimeTaggersoftware. Allidentifyinginformationlikeserial
numbersisobscured.
• Average,minimal,andmaximalaggregatedataratesentoverUSBineachusagesession.
• Usageandconfigurationofthemeasurementsandtheirperformanceindicators.
• Computer’sprocessornameandcapabilities,aswellastheRAMsize.
9.2 Ways of control
YouwillbeaskedtojoinTimeTaggerimprovementprogramduringsoftwareinstallation. Youcanchangeyourdecision
atanylatertimebyuninstallingandinstallingtheTimeTaggersoftwareagain.
Youcanalsocontrolusagestatisticscollectionthroughtheprogramminginterface. Thefollowingexamplesshowhow
to perform key operations of enabling, disabling, and retrieving the usage statistics data. See also Usage statistics
functions.
1Here“pseudonymized”meansthattheuserretainsprivacyoftheirdataandremainunidentifiedaslongastheiruser_id(pseudonym)isnot
matchedtotheirpersonalidentity.
169

TimeTaggerUserManual,Release2.17.4.0
Getandsetusagestatisticscollectionstatus
# 0 - UsageStatisticsStatus.Disabled
# 1 - UsageStatisticsStatus.Collecting
# 2 - UsageStatisticsStatus.CollectingAndUploading
| status   | = getUsageStatisticsStatus() |            |                   |     |     |
| -------- | ---------------------------- | ---------- | ----------------- | --- | --- |
| # Enable | usage statistics             | collection | without uploading |     |     |
setUsageStatisticsStatus(UsageStatisticsStatus.Collecting)
| # Enable | usage statistics | collection | with uploading |     |     |
| -------- | ---------------- | ---------- | -------------- | --- | --- |
setUsageStatisticsStatus(UsageStatisticsStatus.CollectingAndUploading)
| # Disable | usage statistics | collection |     |     |     |
| --------- | ---------------- | ---------- | --- | --- | --- |
setUsageStatisticsStatus(UsageStatisticsStatus.Disabled)
Getcurrentusagestatisticsdata
| json_string | = getUsageStatisticsReport() |                 |     |     |     |
| ----------- | ---------------------------- | --------------- | --- | --- | --- |
| 9.3 Time    | Tagger                       | Lab diagnostics |     |     |     |
WhenTimeTaggerLabisused,itcanautomaticallysendapplicationerrorreportsandrelateddiagnostics(later: “ap-
plicationerrordiagnostics”),asdescribedintheEULA.Userscanenable/disablesendingapplicationerrordiagnostics
and sendingTime Tagger usage statisticsindependently. Bydefault sending applicationerror diagnostics is enabled
whensendingusagedataisenabled.
| 170 |     |     |     | Chapter9. | UsageStatisticsCollection |
| --- | --- | --- | --- | --------- | ------------------------- |

CHAPTER
TEN
LEGAL & SAFETY
| 10.1 Time | Tagger | X - Safety | notice |
| --------- | ------ | ---------- | ------ |
SwabianInstruments’sTimeTaggerX isahigh-resolutionstreamingtime-to-digitalconverterwithatimingresolution
of1.5psandupto18inputchannels. Itcomesbundledwithauniquedataprocessingarchitecturethatmakesitthe
preferredchoiceforapplicationslikeTime-CorrelatedSingle-PhotonCounting(TCSPC),time-intervalcountingand
manymore.
10.1.1 Symbols
Caution: generalwarning
Caution: highvoltage
Functionalearth
| 10.1.2 Operation | environment |     |     |
| ---------------- | ----------- | --- | --- |
TheTimeTaggerX isdesignedforoperationinacleananddryindoorlaboratoryenvironmentbyqualifiedpersonnel.
The product or its external components shall not be exposed to corrosive and/or flammable substances, liquids or
| extremeheat. | Donotoperatewithhighdustandhumiditylevels. |                  |                                |
| ------------ | ------------------------------------------ | ---------------- | ------------------------------ |
|              |                                            | Table1:          | Operationenvironmentconditions |
|              |                                            | Parameter        | Value                          |
|              |                                            | Temperature      | +5°Cto+45°C                    |
|              |                                            | Relativehumidity | <80%,nocondensation            |
|              |                                            | Maximumaltitude  | 2000meters                     |
|              |                                            | Protectionlevel  | IP20(IEC60529)                 |
171

TimeTaggerUserManual,Release2.17.4.0
10.1.3 Electrical characteristics
Table2: Powersupplyratings
Parameter Value
Voltage 100-240VAC
Frequency 47-63Hz
Power max. 60W
ThemaximumvoltageandcurrentratingsofthesignalinputsandoutputsarespecifiedontheTimeTaggerX’shousing
andmustnotbeexceeded.
10.1.4 Electrostatic-sensitive device
TheTimeTaggerXisasensitiveelectronicdeviceandmustbehandledwithcare. Theinputandoutputcircuitryofthe
TimeTaggerX maybedamagedbyanelectrostaticdischargeortheirfunctionalitymaybeimpaired. Takeappropriate
precautionstominimizetheriskofanelectrostaticdischargeintotheconnectionsorsignalwiringduringinstallation
andoperationoftheTimeTaggerX.
TheTimeTaggerX issensitivetoelectrostaticdischarge! Takeappropriateprotectivemeasureswhen
performingsysteminstallationormaintenance.
10.1.5 Equipment installation
The Time Tagger X does not require assembly and is supplied fully assembled. It can be installed as a table top
instrumentorinastandardized19-inchrack. Anyoperatingpositionshallprovideadequatespaceforcableconnections
andaircirculation.
Atabletopinstallationrequiresanevenandhorizontalsurfacewithenoughspaceforeasyaccessofthedevice.
Installationinastandardized19-inchrackrequires2heightunits. Therackshallprovidesufficientventilationandmust
notobstructtheventilationopeningsoftheTimeTaggerX’srearpanel.
PositiontheTimeTaggerX inamannerthatallowstheusertodisconnectthedevicefromthemainsatanytimeand
withoutrestrictions.
Beforeconnectingtothemains,inspecttheproductandthepowercordforvisibledamage. Connectiontothemains
shallbedoneonlywiththesupplieddetachablepowercord. Incaseofdoubt,donotoperatetheproductandseekfor
assistancefromaqualifiedelectricianorapersonresponsibleforelectricalsafety.
Safeoperationcannolongerbeassumed:
-afterroughhandlingduringtransportorinstallation,
-incaseofvisibledamagetotheproductoritspowercord,
-incaseoflooseinternalpartsbeingnoticed,
-incaseofingressofanyliquidsinsidetheproduct’shousing.
172 Chapter10. Legal&Safety

TimeTaggerUserManual,Release2.17.4.0
TheTimeTaggerX providesonefunctionalgroundterminalontherearpanellocatednexttothepowercordrecepta-
cle. AllconnectorsthatfeaturegroundterminalsareelectricallyconnectedtotheTimeTaggerX housingandtothe
functionalgroundterminal. ThisincludesshieldterminalsontheSMAconnectorsandtheUSB-Cconnector.
Takecareofappropriategroundingpracticesandensurethatallconnectedaccessoryandequipmentsharescommon
groundwiththeTimeTaggerX.Connectionofadditionalaccessoriesorequipmentthataregroundedtoanindepen-
dentgroundingcircuithasthepotentialriskofelectricalshock. AninappropriatelygroundedTimeTaggerX and/or
connectedequipmentmayresultinproductdamage,malfunction,degradedperformanceorpoorsignalquality.
| Functionalearth | Mainsconnector |     | Airvents.Donotblock! |     |     |     |
| --------------- | -------------- | --- | -------------------- | --- | --- | --- |
| terminal        | IEC60320-C14   |     |                      |     |     |     |
10407--26 643 00H WVz
|     | FDBKOU LOOPOU LOOP | SYNC CLK CLKO | USB | FP+ | AUX AUX A |     |
| --- | ------------------ | ------------- | --- | --- | --------- | --- |
Fuse:250V/0.5A
4AVCpp 2AVCpp
|     | SwabianInstrumentsSynchronizatio |     |     |     | PRG |     |
| --- | -------------------------------- | --- | --- | --- | --- | --- |
Mainsfuse
TimeTaggerX
|     |     | Fig.1: ViewoftheTimeTaggerX |     | rearpanel. |     |     |
| --- | --- | --------------------------- | --- | ---------- | --- | --- |
Powerstatebutton
Standby:Blue
Ready:Green
|     | Fig.2: ViewoftheTimeTaggerX |     | frontpanelwithpowerstatebuttonindicated. |     |     |     |
| --- | --------------------------- | --- | ---------------------------------------- | --- | --- | --- |
AfterconnectingtheTimeTaggerX tothemains,itwillbeina“Standby”powermodeindicatedbythepowerbutton
lightpulsatingblue. Pressthepowerbuttontoswitchtheproductintothe“Ready”state-thepowerbuttonlightwill
turn green. By pressing the power button again, the Time Tagger X can be switched back into the “Standby” power
mode.
TheTimeTaggerX produceswasteheatduringregularoperation. Long-termcontinuousoperationatelevatedenvi-
ronmenttemperaturesmayleadtoawarmproductsurface,thisisnotamalfunction. Stopoperationimmediatelyand
contactthemanufacturerincasetheproduct’ssurfacetemperatureexceeds55°C(hotonbrieftouch).
| 10.1.6 Maintenance | and | repair |     |     |     |     |
| ------------------ | --- | ------ | --- | --- | --- | --- |
TheTimeTaggerX doesnotcontainanyuserserviceableoruserrepairableparts. Incaseofmalfunctionordamage,
stopoperatingtheTimeTaggerX,disconnectitfromthemainsandcontactthemanufacturer.
TheTimeTaggerX mayonlybeopenedbypersonnelauthorizedbythemanufacturer.
DisconnecttheTimeTaggerXfromthemainsbeforeopeningitandworkingontheinternalcomponents.
Otherwisethepersonnelmaybeexposedtotheriskofelectricshock.
Adjustments,replacementsofpartsandrepairmaybecarriedoutonlybypersonnelauthorizedbythe
manufacturer.
| 10.1. TimeTaggerX | -Safetynotice |     |     |     |     | 173 |
| ----------------- | ------------- | --- | --- | --- | --- | --- |

TimeTaggerUserManual,Release2.17.4.0
All Time Tagger X units repaired by the manufacturer undergo verification and testing procedures in the same way
as new units. The electrical safety of every new and repaired Time Tagger X is verified with a Gossen Metrawatt
SECUTESTPROtestinginstrument.
Powercord
The detachable power cord must be adequately rated for the operation voltage and power consumption of the Time
TaggerX,seethetablePowersupplyratings.
Itisstrictlyforbiddentouseadamagedpowercordoracordwithinadequateratings. Incaseofdoubt,
donotoperatetheproductandcontactthemanufacturerorseekforassistancefromatrainedelectrician
orapersonresponsibleforelectricalsafety.
Safetyfuse
TheTimeTaggerX isequippedwithamainsfuselocatedontherearpanelbeneaththepowercordreceptacle. The
fusecompartmentcanonlybeaccessedwhenthepowercordisdetachedfromtheTimeTaggerX.Thefusetypeand
fuseratingmustcomplywiththespecificationinthetableSafetyfuseratingsandthelabelingontheTimeTaggerX.
Table3: Safetyfuseratings
Parameter Value
VoltageRating 250VAC
CurrentRating 500mA
Dimensions 5x20mm
ResponseTime SlowBlow
Cleaning
BeforecleaningtheTimeTaggerX,pleasemakesurethatithasbeenswitchedoffanddisconnectedfromthemains.
Cleantheouterhousingwithasoft,lint-freedustcloth. NopartsoftheTimeTaggerX maybecleanedwithchemical
cleaningagents.
10.1.7 Disposal and recycling
NeverdisposeoftheTimeTaggerXwiththehouseholdwaste. Pleaseinformyourselfabout
thelocalrulesonseparatecollectionofelectricalandelectronicproducts.
174 Chapter10. Legal&Safety

TimeTaggerUserManual,Release2.17.4.0
10.1.8 Contact, support and service
SwabianInstrumentsGmbHcanbereacheddirectlyviaphone,emailorperpost.
SwabianInstrumentsGmbH
StammheimerStraße41
70435Stuttgart
Germany
+49711400479-0
info@swabianinstruments.com
https://www.swabianinstruments.com
10.1. TimeTaggerX -Safetynotice 175

TimeTaggerUserManual,Release2.17.4.0
| 176 | Chapter10. | Legal&Safety |
| --- | ---------- | ------------ |

CHAPTER
ELEVEN
REVISION HISTORY
11.1 V2.17.4 - 17.07.2024
Improvement
• Python: addssupportfornumpy2.0.0.
11.2 V2.17.2 - 02.07.2024
Improvement
• AddssupportforUbuntuLongTermSupportrelease24.04.
• AddsIteratorBase.abort()foranon-blockinghinttoabortmeasurementsquickly.
• AddsatutorialforODMRmeasurements.
TimeTaggerbugfixes
• FixeswronginitialUTCtimestampinPulsePerSecondMonitor andimprovedformattinginitsdataexport
file.
• FixesHistogramND forN>4.
• Fixesabugwithmissingtimetagswhenmultiplesmallsavedfilesaremergedandreplayed.
TimeTaggerLabbugfixes
• FixesacrashwhenswitchingbetweenFileWriterandothermeasurements.
• AddsmissingdataexportoptionforPulsePerSecondMonitorandFrequencyCounter.
• FixesvisualizationofavailableHighReschannelsforTimeTaggerX onthelandingpage.
• FixesabugwhenstoppingandrestartingtheLogarithmicHistogramDLSsimulation.
• Fixesacrashintheapplication’swindowdockingmanager.
• IncludesseveralsmallerUIandstabilityimprovements.
177

TimeTaggerUserManual,Release2.17.4.0
11.3 V2.17.0 - 22.04.2024
Highlights
• WiththenewFrequencyCountermeasurement,theTimeTaggerbecomesafullfeatureOmega-typefrequency
counter.
• ThenewPulsePerSecondMonitormeasurementallowstomonitorthesynchronicityofdifferentPPSsources.
• ThesupportofvariableintegrationtimeperbininHistogramLogBinsprovidestheaccurateg2normalization
withimmediatestartandgatedinputs.
• ImprovetheperformanceoftheSynchronizertoreachthefull80MTags/sperdevice.
Improvement
• NewvirtualchannelCombinationsforexclusivecoincidences.
• AddssupportforthePythonStableABItosupportPython3.12andlikelymanymorefurtherreleases.
• AddssupportfortheMinGWC++ABIfortheMINGW32andUCRT64environment.
TimeTaggerUltraandTimeTaggerX
• Significantlyreducedon-devicelatencynoticeablebothoverUSBandFPGAlink.
• Supportforhigh priority input channels,whichwillstillbetransmittedwhileinoverflowdomain.
• Thetimestampsofrisingandfallingeventscanbeaveraged on hardwareforahigherprecisionofevents.
• Enhancedversionofthedeadtime filter,whichcanbeconfiguredwithanydeadtimeinpicosecondpreci-
sion.
TimeTaggerX
• FullsupportfortheHigh-ResolutionmodeontheTimeTaggerX withatimingjitterof1.5psRMSperchannel.
• SupportfortheQSFP+FPGAlinkwithadatarateof1200MTags/s.
• Supportforthereadoutofmoredevicesensorsonthehardware.
• Theselfverificationofthehardwareinputstageofthebuilt-intestsignalisrevertedontheTimeTaggerX.
• Allinputportsstayatthehigh-impedancemodebeforetheirfirstusageandafterfreeTimeTagger().
• Changesthedefaulthysteresisfrom1mVto20mV.
TimeTaggerUltra
• AddssupportforTimeTaggerUltrawithhardwarerevision1.8.
• Theimprovedauto-calibrationforperiodicsignalsanditserrorhandlingisbackportedfromtheTimeTaggerX
totheTimeTaggerUltra.
• ImprovestheUSBperformanceformanyalignedinputs.
178 Chapter11. RevisionHistory

TimeTaggerUserManual,Release2.17.4.0
TimeTaggerLabfeaturesandenhancements
• Improvedandmoreinformativelandingpagelayout.
• Existingmeasurementscannowbeclonedeasily(byrightclicking).
• Thelivecountrateisnowvisibleinthedetaileddeviceview.
• Applicationwindowpositionsandthemeasurementlistorderarenowsavedtoworkspace.
• A notification appears when the measurement dead time is automatically adjusted to a multiple of the Time
Taggerclock.
• Newstartupcommandlineoptions–select-deviceand–start-measurement.
• MaximumfilesizefortheFileWritermeasurementisnowshowninmegabytes.
• “Forcehighimpedance”optionforTimeTaggerX start-upwithoutimpedanceswitch.
• ManysmallerUIimprovementsandfixes.
TimeTaggerLabbugfixes
• Fixedvariouscrashesrelatedtodevicelicensechecks,sendingfeedbackandexportinglargedatasetstofile.
• Fixedoccasionalmisalignedaxisticksandmissingaxistickswhenzoomingin.
• Fixedlimitedapplicationvisibilityforhighscreenscalingsettings.
• Fixedoccasionallymissingchartcursorvalues.
• ChangedlogarithmicaxislabelsfromE^to10^.
11.4 V2.16.2 - 28.06.2023
TimeTaggerhardwaresupport
• AddssupportforTimeTagger20withhardwarerevision2.5.
• AddssupportforTimeTaggerX withhardwarerevision1.2.
TimeTaggerbugfix
• FixesCountershowingwrongvalueswhenthesamechannelisusedmultipletimes,nowthrowinganexception
oncreating.
• FixesFileReader inMatlabnotloadingthe.NETAssemblyinitsconstructor. Allmeasurementclassesnow
loadtheassembly.
11.4. V2.16.2-28.06.2023 179

TimeTaggerUserManual,Release2.17.4.0
TimeTaggerLab
• Fixesnon-visiblenumbersforcursorvalues.
• MovedlegendofCountertimetracetothetopleft.
• Higherprecisionformattingvalueswhennecessary.
11.5 V2.16.0 - 05.06.2023
Highlights
• TimeTaggerLab: VirtualAntibunchingandFluorescencelifetimesetups.
TimeTaggerLabfeaturesandenhancements
• AntibunchingandFluorescencelifetimesetupsandcorrespondingsimulationmeasurements. Thedetectorsig-
nalsarefullysimulatedforthosemeasurementsandnophysicaldetectorsareneeded.
• Optiontosuppresscountsfordt=0withautocorrelationmeasurements.
• Notificationthatsoftwareupdatesareavailable.
• Improvedcrashanderrorreporting.
• Improvedticksandlabelsoflogarithmicplots.
TimeTaggerLabbugfixes
• Fixedvariouscrashesrelatedtoexportingdata,openingamessagebox,andcreatinglogfiles.
• FixedHistogram2Dexport.
• Fixedauto-restartingwithno-plotmeasurementsonconfigurationchange.
• Missinglog-ylabelsandticksareaddedtochartdisplay.
Improvement
• AddssupportforPython3.11.
• Thebuilt-intestsignalverifiesthehardwareinputstageonTimeTaggerX startingfromhardwarerevision1.1.
Bugfixes
• FixesfaninformationofgetSensorData()ontheTimeTaggerUltra.
• FixesthesupportforTimeTimeTaggerUltradeviceswiththeserialsstartingwith17.
• Fixes GatedChannel, FrequencyMultiplier and TriggerOnCountrate to switch to the initial state on
clear()andstartFor().
• FixesautoCalibration()tocleartheoldcalibrationdata.
• FixestheerrorhandlingonLinuxifpartsofthePythonwrapperaremissing.
• Fixesaonebitoutofboundsmemoryaccessonverifyingthehardwarelicense.
180 Chapter11. RevisionHistory

TimeTaggerUserManual,Release2.17.4.0
• FixesthejaggedarrayhandlingoftheMatlabWrapperforCoincidences.
11.6 V2.15.0 - 06.03.2023
Highlights
• ReworkoftheMatlabwrapper,nowreflectingthefullfunctionalityoftheTimeTaggerAPI.
Matlabwrapper
• Supportsclassinheritance,newTTclassesareclosertotheirC++,andPythoncounterparts.
• SupportscreationofTimeTaggerobjectsviaTimeTagger.createTimeTagger().
• SupportsnativeMatlabenums.
• Supportsjaggedarraysviaconversionfrom/intoMatlabcells.
Behaviorchange
• Disallowaneventdividervalueof0. Pleaseuse1instead.
• Matlab: RemovedMatlabappdesignerexamples.
OtherChanges
• UpdatedOpalKellyFrontpanellibraryto5.2.12.
Bugfixes
• Python: FixreturntypeannotationforcreateTimeTagger().
• FixescertaindeadlockissuesinMatlabcausedbyasynchronousfunctions.
• FixestheoverflowtrackingwithaUSBerrorwhileinoverflow.
• Fixeshandlingoftagswithrespectto<->missedeventsatthetimestampofanOverflowBeginerror.
• Counter: FixesatransposeissueoftheNaNgenerationinCounterData.getDataNormalized().
• FrequencyStability: FixesanintegeroverflowintheMDEV/TDEVcalculation.
• FixedissuewithLicenseRequestGenerator.exenotworkingonsomesystems.
11.6. V2.15.0-06.03.2023 181

TimeTaggerUserManual,Release2.17.4.0
TimeTaggerLabfeaturesandenhancements
• DeviceLEDscanbeswitchedonandoff(notTimeTagger20).
• Improvedsettingofthereferencesoftwareclockforsignalswithaneventdividergreaterthan1.
• TimeTagger20Eduissupported.
TimeTaggerLabbugfixes
• Fixthecrashwhencapturinghigh-resolutioncounter-timetraces.
• FixthecrashwhentheUSBconnectiontothedeviceisunstable.
• FixthecrashwhenexportinglargeScopemeasurementdata.
• FixthecrashwhenexportingaplottoaPNGfile.
• Fixthecrashwhenmeasurementsrequiretoomuchmemoryoninitialization.
• Userinterfaceissueswithsmallscreensaresolved.
11.7 V2.14.0 - 23.12.2022
TimeTaggerX
• AddssupportforTimeTaggerX withhardwarerevision1.1.
• AddssupportforSynchronizerwithTimeTaggerX andalsomixedsetupswithTimeTaggerUltra.
• ProvidespreliminaryEthernetsupportontheSFP+.
• Improvestheauto-calibrationforperiodicsignals.
• BetterCPUperformanceforalignedtags.
• ImprovesthechannelLEDblinkingfor1ppssignals.
• ShowscalibrationerrorsonthechannelLEDinred.
• Fixesarandomskewjumpof1333psperinputchannelonUSBerrors.
• FixesthechannelLEDindicationforfallingevents.
Bugfix
• FixPowerLEDturningoffaftercallingfreeTimeTagger()ontheTimeTaggerUltra.
182 Chapter11. RevisionHistory

TimeTaggerUserManual,Release2.17.4.0
11.8 V2.13.2 - 22.11.2022
Highlight
• ReleaseofTimeTaggerLab-thenativeUIforWindows.
11.9 V2.12.4 - 09.11.2022
Improvement
• AddssupportforTimeTaggerUltrawithhardwarerevision1.7.
Bugfix
• FixedWebApplicationdataexportforHistogramLogBins.
11.10 V2.12.2 - 04.10.2022
Bugfixes
• FixeswrongErroreventgenerationandchanneldetectioninmergeStreamFiles().
• FixeshostlicensequeryingforTimeTaggerNetwork clients(brokeninv2.12.0)
• Python: Fixes the decoding of the return values of getDeviceLicense() and getSensorData() of
TimeTaggerNetwork.
• C++: Fixesstd::stringunmarshallingwithintheNetworkTimeTagger.
Variousimprovements
• AddsmethodgetTraceFrequencyAbsolute()toFrequencyStability.
• AddsmethodgetChannelList()toFileReader.
11.11 V2.12.0 - 01.09.2022
Highlights
• Addsupportforournewhighprecisionmeasurementdevice,theTimeTaggerX,withatypicaltimingresolution
of2.0picoseconds.
11.8. V2.13.2-22.11.2022 183

TimeTaggerUserManual,Release2.17.4.0
WebApp
• ChangedefaultaccessmodetoAccessMode.ControlforTimeTaggerNetwork.
Features
• ImprovetheperformanceoftheSynchronizer. TwoTimeTaggerUltradevicesnowcanachieveatotaldatarate
ofover100Mtagspersecond.
• AddsupportforthenewUbuntuLongTermSupportrelease22.04JammyJellyfish.
Behaviorchange
• AllprovidedstringstotheC++APImustbeencodedasUTF-8,returningstringsarealsoUTF-8encoded.
• RenamegetLicenseInfo()toTimeTagger.getDeviceLicense(). ItreturnsaJSONformattedstringforeasier
processing.
• Drop support for obsolete Python versions 2.7 and 3.5 and for the obsolete Linux distributions CentOS 7 and
Ubuntu16.04.
Examples
• JitterverificationrequeststhespecifiedjittervaluesdirectlyfromtheTimeTaggerbackend.
• FLIMexampleisnowavailableforMatlab
VariousFixesandImprovements
• FixUnicodecharactersinallfilenamesofFileWriterandFileReader.
• FixCoincidenceFactoryforMatlabandLabview.
• FixtheFlim measurementforMatlab.
• FixthecrashonafailinglicensedownloadwithintheinitializationoftheNetworkTimeTagger.
• Preferahost-lockedlicenseoverauser-lockedlicenseintheVirtualTimeTagger. Thisreducesthechanceofa
false-positiveanti-viruswarning.
• ImprovetheroundingbehaviorofTimeTagger.getTriggerLevel().
• UpdateoftheUSBdriverforvariousfixes.
11.12 V2.11.0 - 22.04.2022
Highlights
• IntroducedmergeStreamFiles()tocombineseveralFileWriterfilesintoone.
184 Chapter11. RevisionHistory

TimeTaggerUserManual,Release2.17.4.0
TimeTaggerNetwork
• NewProtocolversion3.1withanewsetoffeatures. Backwardcompatiblewith3.0.
• Improved messages for connection loss and disconnection. Additionally, messages for connecting to new and
oldversionsofTTNwillbepresented.
• Fixedissuerelatedtoimplicitcallofsync()onmeasurementcreationinAccessMode.Listen mode.
• ServerandnetworkinformationhasbeenaddedtogetConfiguration().
• Fixedcrasheswhenstreamingover250channels.
• Variousraceconditionsandpossiblefreezeshavebeenfixed.
• Fasterinitializationofmeasurementswithmanychannels.
• Fixederrorhandlingondisconnection.
• Reducedconnectiontimeoutto10seconds.
• Fixedanissuewherechannelsusedbyaclientremainedregisteredafteradisconnect.
• TimeTagger.setTimeTaggerNetworkStreamCompression()canbeutilizedtodoublethemaximumtrans-
ferrateinaveryslownetworkenvironment(<=100Mbit/s).
TimeTaggerVirtual
• The TimeTaggerVirtual will now wait for a test signal channel to be registered before starting to stream it
(behavioridenticaltoahardwareTimeTagger).
GatedChannel
• OptionalconstructorargumentinitialoftypeGatedChannelInitialtoinitializethegateoptionallyinanopen
state.
• Changedbehaviorifinput_channelequalsgate_start_channelorgate_stop_channeltoallowforoperationsim-
ilartotheConditionalFilter.
FrequencyStability
• FixedgetTraceFrequency();nowitreturnstherelativefrequencyerrorinsteadoftherelativeperioderror.
• Tracesarenolongertruncatedtothelengthofthemaximumsteps.
• Correctedbehaviorifstoppedandrestartedwithoutclearing.
Othermeasurementclasses
• HistogramLogBins: Removedbinswhichhaveabinwidthof0ps.
• SynchronizedMeasurements: Methods calls on a SynchronizedMeasurements object without any regis-
teredmeasurementswillnolongergenerateanexceptionbutawarning.
• TimeDifferences: AddedgetHistogramIndex()toreturntheindexofthehistogrambeingprocessedcur-
rently.
• ExposedTagTypetobeusedwithTimeTagStream andCustomMeasurement.
11.12. V2.11.0-22.04.2022 185

TimeTaggerUserManual,Release2.17.4.0
Synchronizer
• Improvederrormessages.
• FixedUSBerrorsoccurringunderveryhighdatarates.
Examples
• AddedVisualBasic.NETexample
VariousFixes
• FixedcrashoncreateTimeTagger()duringaUSBerror.
• Fixed an issue where startFor() could run further than the specified time on HistogramLogBins and
FileWriter.
• WebApp: FixedargumenthandlingonLinux.
• Matlab: SupportsnowResolution forHighRes.
• Matlab: Verifiesthattheversionoftheinstalledbackendmatchesthewrapperversion.
11.13 V2.10.6 - 16.03.2022
Improvements
• AddssupportforTimeTaggerUltrawithhardwarerevision1.6b.
11.14 V2.10.4 - 23.02.2022
WebApp
• FixedInputDelayfornegativevalues.
• FixedaddingnewchannelsforCountratemeasurement.
• FixedHistogramLogBinsforlowstarttimes(<10ps).
• FixedunitsfordataexportofCounter,Correlation,Histogram2D,andHistogramLogBinsmeasurements.
11.15 V2.10.2 - 31.12.2021
Improvements
• AddedsupportforPython3.10.
186 Chapter11. RevisionHistory

TimeTaggerUserManual,Release2.17.4.0
Fixesforissuessincev2.10.0
• FixedHistogramLogBinsintheWebApplication.
• FixedDelayedChannelfornegativedelays.
• FixedanissuewithCounter.getDataTotalCounts()notresettingto0onclear().
• FixedsomeMatlabexamplesnotbeingcompatiblewith2016borolder.
11.16 V2.10.0 - 22.12.2021
Highlights
• Time Tagger Network: All Time Tagger devices and the acquired data can be accessed via the network from
multiple clients or locally across the different programming languages. The clients can use all TimeTagger
measurementclassesandmayoptionallycontrolthesettingsofthephysicalTimeTagger.
• Anewfrequencystabilitytoolbox: Itofferson-the-flyevaluationofperiodicsignalsbycalculatingseveralanal-
ysismetrics,including,forexample,theAllandeviation(ADEV)andtimedeviation(TDEV).
• Software Clock: The new recommended method for using an external clock on the Time Tagger Ultra. The
timetagstreamisrescaledonthesoftwaresidewithrespecttotheconnectedclock. Itallowsforabroadinput
frequencyrangeandalsocalculatesphaseerrorestimators. Inaddition,theinputjitteroftheclockchannelwill
beaveragedout,resultinginalowerjitterformeasurementsincludingtheclockchanneldirectly.
Features
• Counter: NewCounter.getDataObject()returningdataasanobjectofCounterDataandallowingforcon-
tinuous chunkwise data acquisition. This object contains the Counter data, timing information and overflow
flags.
• NewHistogramND measurement,whichisamultidimensionalgeneralizationoftheolderHistogram2D.
• NewSamplermeasurementclassforatriggeredsamplingofthecurrentstateofotherchannels.
• MeasurementandvirtualchannelsettingscannowberequestedwithgetConfiguration()method. Theset-
tingsofallmeasurementsarealsoavailableinthereturnvalueofgetConfiguration()method.
WebApp
• ATimeTaggerNetworkservercanbeactivatedinthesettings.
• IncludestheSoftwareClockfeature.
• AddsEventDividersettings.
• ShowsspecifiedRMSjitterforeachchannelinHighResmode.
• Itisnowpossibletospecifytheintegrationtimeinasingle-shotorcyclicmode(internallyusesstartFor())
forallavailablemeasurementclasses.
11.16. V2.10.0-22.12.2021 187

TimeTaggerUserManual,Release2.17.4.0
Performance
• Improved performance of Counter, Countrate, TimeTagStream, Combiner, DelayedChannel for many
channels.
• HistogramLogBinswithanimprovedalgorithm,multithreading,andAVX2+AVX512tuning.
• Coincidencesimprovedforhighinputrateswithlowcoincidencerates.
Behaviorchange
• TimeTagStream nowalwaysrequiresalistofchannels.
• CustomMeasurementinPython: with self.mutexreplacesself.lockandself.unlock.
• ASynchronizerwithonlyoneTimeTaggerwillusethetimestampsoftheSynchronizerbutthechannelidentifiers
ofthesingledeviceitself.
• NomessagesontheINFOlevelwillbeshowninMatlabtoavoidrunningintodeadlocks.
• std::invalid_argumentexceptionsarenowwrappedasValueErrorinPython.
Examples
• NewPythonexampletomeasurethemaximumtransferrateandthejitter.
• NewPythonexampletoshowcoincidencecountingapplications.
• New example to show the use of the software clock and measure the frequency stability of the test signal in
Python,MatlabandLabVIEW.
• UpdatetheCounterexampleinPythonandMatlabtoshowtheuseofthenewCounterData.
Fixes
• SkipsanunlikelyblockingfreeTimeTagger()callforupto10seconds.
• Fixesthe64-bitsignedintegeroverflowafter106daysonLinux.
• StopsplayingthelastsoundofsetSoundFrequency()afterfreeTimeTagger().
• FixesthetimingofTimeTagStreamBuffer.tGetData inthelastblockofFileReader.
• AddssupportforTTUHWrevision1.6andTT20Value.
• FixestheemptyconfigurationandchannellistinFileReaderbeforefetchingthefirsttimetag.
• Fixes a race condition on the Time Tagger Ultra, which may yield one invalid time tag after USB connection
errors.
• Fixesacrashonusingwith CustomMeasurement() as cinPython.
• FixesincorrectlydisplayedunitsintheWebAppifmeasurementsettingschangedduringameasurement.
• FixesthebehaviorofHistogram2Difstart_channelmatchesastopchannel.
• FixesthebehaviorofCountratewithstartForifitendswithinanoverflowinterval.
188 Chapter11. RevisionHistory

TimeTaggerUserManual,Release2.17.4.0
11.17 V2.9.0 - 07.06.2021
Highlights
• ReducedcommunicationlatencyofallTimeTaggers.
• ReducedTimeTagger20crosstalkonchannel1and2.
• ImprovedUSBconnectionstabilityforTimeTagger20.
• Optionalcollectionandreportingofpseudonymoususagestatistics. Improvementprogram.
• Pleaseuseatleastv2.9.0fordevicesshippedfrom2021on.
Changes
• TimeTaggerBase.getConfiguration() and TimeTagger.getSensorData() return a JSON string with
partiallyrenamedsensornames.
• AlteredCountrate.getData()toreturnNaN(NotaNumber)forzerocapturedurations.
• Usesenum.EnumasbaseclassforallenumeratorsinthePythonwrapper(Python>=3.5).
• ImprovedtheformatoftheTimeTaggererrormessages.
Features
• AddedTimeTagger.setHardwareBufferSize()fortheTimeTagger20.
• AddedanexampleandtutorialonhowtoworkwitharemoteTimeTaggerusingPythonandthePyro5package.
• LicenseupgradescanbeflashednowfortheTimeTagger20viathewebapplication.
Bugfixes
• FixedTimeTagger.setStreamBlockSize()blocksizeheuristicwhileuploadingnewconfiguration.
• FixedslowperformanceoffreeTimeTagger()inoverflowmode.
• FixedwaitUntilFinished()invokenodesinLabVIEWexamples.
• FixederrormessageintheWebApplicationfornoncompatibledevices.
• Fixed TimeTaggerVirtual.getConfiguration(). Now it is returning configuration data for
TimeTaggerVirtualclass.
• FixedapossiblecrashonPythoninterpreterexitwhilerunningCustomMeasurement.
• FixedTimeTaggerBase.sync()signalingoneblocktoolate. Thefixreducesthesync,measurementstartand
cleartimes.
11.17. V2.9.0-07.06.2021 189

TimeTaggerUserManual,Release2.17.4.0
11.18 V2.8.4 - 04.05.2021
• FixedtheinitializationforaVirtualTimeTaggerintheWebApplication
11.19 V2.8.2 - 26.04.2021
• FixednonappearingoptiontoinitializeinHighResmodeafterupgrading/flashingthedeviceintheWebAppli-
cation.
11.20 V2.8.0 - 29.03.2021
Highlights
• High-resolutionoptionsfortheTimeTaggerUltraserieswithatimingjitterofdownto4psRMSperchannel.
• HardwareinputdelayontheTimeTaggerUltraserieswithpicosecondsaccuracybeforetheconditionalfilter.
• ReducedCPUloadforTimeTaggerUltra.
Note: ThereleaseisfullycompatiblewithallTimeTagger20 devices. ItiscompatiblewithallTimeTaggerUltra
devicesshippedfromMarch2021andallearlierTimeTaggerUltradeviceswith8orlesschannelswithoutHighRes
option. If you received Time TaggerUltra before March2021 and it hasmore than 8channels or HighRes, it is not
compatiblewiththerelease. Pleasecontactsupporttogetafreedeviceexchangetobefullycompatibleagain.
NewTimeTaggerUltrafeatures
• Reducedcrosstalkandthermaldriftonallchannels.
• TheTimeTaggerhardwaresoundmodulecanbeactivatedandsetviaTimeTagger.setSoundFrequency().
Itcanbeused,e.g.,foropticalalignmentpurposes(countrate->frequency).
Changes
• Split TimeTaggerBase.setInputDelay() into TimeTaggerBase.setDelayHardware() and
TimeTaggerBase.setDelaySoftware().
• TimeTagger.getChannelList()filterenumrenamedtoChannelEdge.
• TimeTagger.setNormalization()cannowbeconfiguredperchannel.
• ChangedthedefaultportoftheWebAppto50120toavoidcollisionwithJupiterNotebooks.
• MaximuminputfrequencyoftheTimeTaggerUltraisreducedto475MHz.
• ThedeadtimespecificationoftheTimeTaggerUltrachangedto2.1ns. Itcandetecteventsseparatedby2ns
withpossiblelossofsomeevents.
190 Chapter11. RevisionHistory

TimeTaggerUserManual,Release2.17.4.0
Features
• AddedaTriggerOnCountratevirtualchannelthatgenerateseventswhenacountratecrossesthegiventhresh-
oldvalue.
• AddedsupportforPython3.9.
• waitUntilFinished()andsynchaveanoptionaltimeoutparameter.
Examples
• Mathematica: AddedexampleforFileWriterandTimeTaggerVirtual().
• LabVIEW:Fixedbrokenexample(#14)andaddedittotheLabVIEWproject.
• C++: AddedanexampleforCustomVirtualChannel.
Bugfixes
• HistogramcanbeusedwithwaitUntilFinished()andSynchronizedMeasurements. Histogram isnow
derivedfromIteratorBase().
• DisplayingthesingletonwarningofcreateTimeTaggerjustonce.
• FixedstringconversionissueforoldMatlabversions.
• Hide“unusedargument”warningsintheTimeTaggerC++headers.
11.21 V2.7.6 - 26.04.2021
• FixedRuntimeError“GottheUSBerror‘UnsupportedFeature’”whencallingcreateTimeTagger()
11.22 V2.7.4 - 19.04.2021
• FixedabugforoldTimeTaggerUltradevices,wheretheWebApplicationcouldnotapplythelicenseupgrade.
11.23 V2.7.2 - 22.12.2020
Highlights
• ReworkedFlimimplementation. Versatilehigh-levelfunctionalitywithFlim andlow-levelCPU-andmemory-
efficientaccessviaFlimBaseandcallbacks.
• HighlyimprovedTimeTaggerVirtualperformancetakinguseofmultithreading.
• Support for direct time tag stream access via Custom Measurements in C# and Python - see examples in the
installationfolder.
11.21. V2.7.6-26.04.2021 191

TimeTaggerUserManual,Release2.17.4.0
Improvements
• AddedAnyCPUtargeted.NETAssemblyforC#wrappers. AvailableinGAC_MSILandtheinstallationfolder.
• Moredetailederrorhandlingandhuman-readableerrormessages.
• AddedConditionalFilterforTimeTaggerVirtual.
• RemovedIntel’slibmmd.dlllibrarydependency.
• AllmeasurementshavethenewcommonmethodwaitUntilFinished(),whichcanbeusedwithstartFor().
• Warningsareprintedwithtimeinformation.
• CleanupoftheC++measurements’headerfile.
• Remotelicenseupgradescanbeperformedviathewebapplication.
• ReworkedPythonandC#examples.
Fixes
• Countratenolongerclearstotalcountsonstart().
• ImplementedTimeTagger.getChannelList()andTimeTaggerBase.waitForFence()inMatlab.
• FixedTimeTaggerBase.setDeadtime()fortheTimeTaggerVirtualusingTimeTagger.setTestSignal().
• FixedafrequentcrashinFileWriterwithhighdataratesandmultiplefiles.
• FixedacrashindeletingmeasurementsstillregisteredtoSynchronizedMeasurements.
• Fixedanunlikelyraceconditionoffreeingmeasurements.
APIchanges
• TheoldFLIMclassisreplacedbyanewimplementation: Flim. Incaseyouneedtheoldimplementation,there
isa1to1replacement,seehere.
• Allmethodsandmeasurementsnowthrowexceptionsinsteadofwarningonwrongargumentslikeinvalidchan-
nelsorout-of-rangeparameters.
• AutomaticallycallfreeTimeTaggerondel/clear/DisposeinPython/Matlab/LabVIEW/C#.
• RemovedthefreeAllTimeTaggermethod.
• Deprecate the multiple use of createTimeTagger() for one physical device. Pass on the timetagger object
instead.
• _LogisrenamedtoLogBase.
• OurlibrariesarecompiledwithVS2019now,soatleastversion142oftheVCruntimeisrequiredinthefinal
application.
192 Chapter11. RevisionHistory

TimeTaggerUserManual,Release2.17.4.0
11.24 V2.7.0 - 01.10.2020
Highlights
• Newmeasurementsareautomaticallysynchronizedtothehardware. Alldataanalyzedisguaranteedtobetem-
porallaterthanthemeasurement’sinitialization,start,orclear. Datacomingfromtheinternalbuffer,whichwas
acquiredbeforethemeasurementwasinitialized, started, orcleared, willnotbeanalyzed. Beforethisrelease,
the.sync()methodwasrequiredforthesetasks.
Fixesandimprovements
• AddedaMatlabexampleforSynchronizedMeasurements.
• FixedabuginMatlab,creatingsyncedmeasurementsviaSynchronizedMeasruementsand.getTagger().
• Thelastdatapointfromascopemeasurementisnotmarkedasinvalidanymore.
11.25 V2.6.10 - 07.09.2020
Fixesandimprovements
• Fixesinputdelay,deadtimeandtestsignalgeneratorfortheTimeTaggerVirtual.
• Fixes getInvertedChannel with the Swabian Synchronizer and with Time Tagger Ultra 8 devices with the old
channelnumberingschema.
• xaxisiszoomablewithScopemeasurement.
• Bettererrorhandlingfornon-existentfileswithTimeTaggerVirtualandFileReader.
Python
• Changed the constants CoincidenceTimestamp_ to a Python enum (e.g., CoincidenceTimestamp_First is now
CoincidenceTimestamp.First).
Matlab
• EnumfortimestampargumentforCoincidence(s)isavailableviaTTCoincidenceTimestamp.
Linux
• FixforslowLinuxdeviceopening.
11.24. V2.7.0-01.10.2020 193

TimeTaggerUserManual,Release2.17.4.0
11.26 V2.6.8 - 21.08.2020
Highlights
• SupportfortheTimeTaggerValueedition. Thisisanupgradeableandcost-efficientversionoftheTimeTagger
Ultraforapplicationswithmoderatetimingprecisionrequirements.
Webapp
• AddedHistogram2D tothemeasurementlist.
• Improvedperformanceandresponsivenessforlargedatasets.
• 32-bitversionoftheWebApplicationworksagain.
• Fixedabugthatdataofstoppedmeasurementscouldnotbesaved.
• Fixedabugthatsettingssavedhadthefileextension.jsoninsteadof.ttconfending.
• FixedabugwhenusingfallingedgesforTimeTaggerstartingwithchannel0.
Python
• Fixedabugthatsomenamedargumentscouldnotbeusedanymore.
API
• Added the method SynchronizedMeasurements.unregisterMeasurement() to remove measurements
fromSynchronizedMeasurements.
Backend
• ImprovedperformanceoftheFileWriter,exceeding100Mtags/sonhigh-endCPUs.
• Improved binning performance of all histogram measurements: Correlation, FLIM, Histogram, StartStop,
TimeDifferences,TimeDifferencesND.
• FixesadeadlockinthevirtualTimeTaggerifameasurementaccessessomepublicmethodsoftheTimeTagger.
11.27 V2.6.6 - 10.07.2020
Highlights
• SwabianSynchronizersupport. TheSynchronizerhardwarecancombine8TimeTaggerUltradevoceswithup
to144channels. ThecombinedTimeTaggercanbeinterfacedtheverysameasitwouldbeonlyonedevice.
• SupportforcustommeasurementsinPython. Pleaseseetheprovidedprogrammingexampleintheinstallation
folderforfurtherdetails.
194 Chapter11. RevisionHistory

TimeTaggerUserManual,Release2.17.4.0
Webapp
• SupportfortheSynchronizer
• ShowingerrormessagesfromsetLoggerAPIinamodalwindow
• Load/savesettingsisnowsupportedfortheTimeTaggerVirtual
TimeTaggerUltra
• Hardwarerevision1.1nowwiththesameperformanceenhancementof500MHzmaximumsyncrate,2nsdead
timeandbetterphasestability,asintroducedbeforeforHardwarerevision>1.1
• Dropped support for the very first Time Tagger Ultra devices, an error will be shown on initialization - free
exchangeprogramavailable
• MoreintuitivebyteorderofthebitmaskinsetLED
• Smallmodificationstothehardwarechanneltochanneldelay
Backend
• Coincidence and Coincideces have an optional parameter to select which timestamp should be inserted, the
last/firstcompletingthecoincidence,theaverageoftheeventtimestamps,orthefirstofthecoincidencelist.
• Fixed.net/Matlab/LabVIEWwrappersfordatawithempty2Dor3Darrays
• Provideagloballyregistered.NETpublisherpolicyforC#,avoidingthe‘wrongdllversion’messageinLabview
whenupdatingtheTimeTaggersoftware
• setConditionalFilterthrowsanexceptionwheninvalidargumentsareapplied
• HidethewarningonfetchingtheTimeTaggerVirtuallicensewithoutaninternetconnection
• DelayedChannelsupportsanegativedelay
• PerformanceenhancementsinStartStop
11.28 V2.6.4 - 27.05.2020
WebApp
• Optiontoenablelogarithmicy-axisscalingforCounter,Histogram,HistogramLogBinsandCorrelation
• Redesign“Createmeasurement”dialogwithlinkstotheonlinedocumentation
• Fixedflickeringwhenswitchingbetweenplots
• Fixedplottingwrongdatarangewhenchangingthenumberofdatapoints
• AddedthebasicfunctionalityoftheTimeTaggerVirtual(testsignalonly)
11.28. V2.6.4-27.05.2020 195

TimeTaggerUserManual,Release2.17.4.0
Newfeaturesandimprovements
• AddedthetestsignaltoTimeTaggerVirtual
• SupportforUbuntu20.04andCentOS8
• LabVIEWexampleforFileWriterandFileReader
• ImprovedMatlabAPIforVirtualTimeTagger,addingoptionalparameters
• Makethedatatransfersizeconfigurableby.setStreamBlockSize
• PerformanceimprovementsforHistogramLogBins
• SlightlyimprovedtimingjitteratlargetimedifferencesfortheTimeTagger20
• TimeTaggerApplicationworksagainwith32bitoperatingsystems
• ConnectionerrorsareshownintheMatlabconsoleorcanbehandledwiththenewloggerfunctionality
• AddedcustomloggerexamplesforMatlab/Python/C#
Changes
• UpdatedtheUSBlibrary
• StopmeasurementswhenfreeTimeTaggeriscalled(e.g. closesfilesondump,isRunningnowreturnsfalse)
• Reducedpollingrate(0.1s)forUSBreconnections
APIchanges
• Added.setLogger()toattachacallbackfunctionforcustominfo/errorlogging
• RenameofenumerationErrorLeveltoLogLevel
• Renameofloglevelconstantsandwithnewcorrespondingintegervalues
11.29 V2.6.2 - 10.03.2020
Highlights
• TimeTaggerVirtual,FileWriter,andFileReaderhavereachedastablestate
• ImprovedLinuxsupport(documentation,compilingcustomPythonwrappers)
Newfeatures
• AddedsetInputDelay,setDeadtime,getOverflows,andmoretotheTimeTaggerVirtual
• AddanoptionalparameterinsetConditionalFilterfordisablingthehardwaredelaycompensation
• InfinitedumpinginDumpfornegativemax_count
• CreateafreeAllTimeTagger()method,whichiscalledbyPythonatexit
• ReimplementSynchronizedMeasurementsasaproxytaggerobject,whichautoregistersnewmeasurementswith-
outstartingthem
196 Chapter11. RevisionHistory

TimeTaggerUserManual,Release2.17.4.0
• ThenewSynchronizedMeasurements.isRunning()methodreturnsifanymeasurementisstillrunning
• Python: DistributethegeneratedC++wrappersourceforsupportingfuturePythonrevisions
• C++: NewIteratorBase.getLockmethodreturningastd::unique_lock
• C++: Improvedexceptionhandlingforcustommeasurements: exceptionsnowstopthemeasurement,runSyn-
chronizedforwardsexceptionstothecaller
APIchanges
• TimeTagger.getVersionreturnvalueischangedtoastring
• C++: Use64bitintegersforthedimensionsinthearray_outhelpers
• C++: Renamethebaseclassforcustommeasurementsfrom_IteratortoIteratorBase
• C++: ConstructorsofcustommeasurementsshallcallfinishInitializationinsteadofIteratorBase.start
• Python2.7: UpdatethenumpyCheadersto1.16.1
Examplesanddocumentation
• ImprovedHistogram2Dexample
• ClarifysetInputDelayvsDelayedChannel
Bugfixes
• RelaxthevoltagesupplycheckintheTimeTaggerUltrahardwarerevision1.4
• Usea1MBbufferforDump,FileWriter,andFileReadertoachievefullspeedespeciallyonnetworkdevices
• FixgetTimeTaggerModelonanactivedevice
• Fixdeadlockwithinsync()whilethedeviceisdisconnected
• ProvidethedocumentationonLinux
• SeveralfixesandimprovementsfortheFileWriterandTimeTaggerVirtual
WebApp
• Improveddefaultnamesformeasurements
• Notrelyingondatastoredwithinthebrowseranymore
• Disablingmousescrollingwithinnumericinputs
• Variousbuxfixes
11.29. V2.6.2-10.03.2020 197

TimeTaggerUserManual,Release2.17.4.0
11.30 V2.6.0 - 23.12.2019
Highlights
• FileWriter: New space-efficient file writer for storing time tag stream on a disk. The file size is reduced by a
factorof4to8. ReplacestheDumpfunction.
• VirtualTimeTaggerallowstoreplaypreviouslydumpedeventsbackintotheTimeTaggersoftwareengine.
• Improvedbehaviorintheoverflowmode. Thehardwarenowalsoreportstheamountofmissedeventsperinput
channelandprovidesthestartandtheendtimestampsoftheoverflowinterval.
• Newtutorialonhowtoimplementthedataacquisitionforaconfocalmicroscope
• NewmeasurementHistogram2Dfor2-dimensionalhistogrammingwithexamples
• WebApp: Selectableinputunits(s/ms/µs/ps)insteadofpsonly
Knownissues
• FileWriterandFileReaderhavealowperformanceonnetworkdevices
APIchanges
• deprecatedTimeTagStreamBuffer.getOverflows()–use.getEventTypes()instead
• renamedHistogramLogBin.getDataNormalized()to.getDataNormalizedCountsPerPs()
• removeddeprecatedTimeTagger.getChannels()-use.getChannelList()instead
• removeddeprecatedCHANNEL_INVALID-useCHANNEL_UNUSEDinstead
• removeddeprecatedTimeTagger.setFilter()andTimeTagger.getFilter()-use.setConditionalFilter(),.getCondi-
tionalFilter(),and.clearConditionalFilter()instead
• C++: Allcustommeasurementclassconstructorsmustbemodified,suchthattheparametercontainingtheTime
TaggerisofthetypeTimeTaggerBase. ThisallowsforusingthecustommeasurementwithinarealTimeTagger
objectandtheTimeTaggerVirtual.
• C++: ThestructTagincludesthetypeofeventandtheamountofmissedevents. Theyhavereplacedtheoverflow
field.
• C++/Windows: Weadditionallydistributebinariesforthedebugruntime(/MDd)
• Matlab: TimeTagger.free()isnowdeprecated,use.freeTimeTagger()
Newfeatures
• WebApp: Normalization(counts/s)fortheCountermeasurement
• getConfigurationreturnsthecurrenthardwareconfigurationasaJSONstring
• addedg2normalizationforHistogramLogBinswithgetDataNormalizedG2
• improvedoverflowbehaviorforCountrateduetothemissedeventcounters
• improvedoverflowhandlingfortheg2normalizationofCorrelationandHistogramLogBin
• supportforPythonversion3.8
• smallerlatencyonlowdataratesduetoadaptivechunksizesof<=20ms
198 Chapter11. RevisionHistory

TimeTaggerUserManual,Release2.17.4.0
• supportfortheTimeTaggerUltrahardwarerevision1.4
Examples
• Matlab: FasterloadingofeventsfromdiskfornowdeprecatedDumpfileformat
• C++: Loadingeventsfromdiskstoredinthenewdataformat
• Labview: Scopeexample,.NETversionredirection
• Mathematica: Improvedexample
• Python: Added“Stop”buttontothecountratefigure.
Bugfixes
• fixedstaticinputdelayerrorwithconditionalfilterenabledsincev2.2.4
• addedmissingTimeTagger.getTestSignalDivider()method
• Scope: Fixtheoutputifonechannelhashadnoevents
• resolveoverflowsaftertheinitializationoftheTimeTagger20
• fixesanissuewithwronglysortedeventsonthereconfigurationofinputdelays
• alwaysemitanerroreventonplugginganexternalclocksource
• fixesanunlikelycasewhenthesynchronizationoftheexternalclockgotlost
• thenewUSBdriverversionfixessomerandomdataabruption
• TTU1.3: Fixabugwhichmayselectawrongclocksourceinthefirst21secondsandwronglyactivatedextclock
LED
• Matlab: SynchronizedMeasurementsworknowinMatlab,too
• differentimprovementswithinthepythonandC#wrappers
• LEDturnsoffandnotredafterfreeingaTimeTagger
• DumpnowreleasesthefilehandleaftertheendofthestartForduration
• WebApp: Removedcachingissueswhenupordowngradingthesoftware
11.31 V2.4.4 - 29.07.2019
• reducedcrosstalkbetweennonadjacentchannelsoftheTimeTaggerUltra
• fixedabugleadingtohighcrosstalkwithV2.4.2forspecificchannels
• fixedarareclockselectionissueontheTimeTagger20
• improvedandmoredetaileddocumentation
• newmethodCountrate.getCountsTotal(),whichreturnstheabsolutenumberofeventscounted
• newMathematicaquickstartexample
• newScopeexampleforLabVIEW
• supportoftheTimeTagger20serieswithhardwarerevision2.3
11.31. V2.4.4-29.07.2019 199

TimeTaggerUserManual,Release2.17.4.0
• releasethePythonGILwhileintheTimeTaggerenginecode
• fixedabuginConstantFractionDiscriminator,whichcouldcausethatnovirtualtagsweregenerated
11.32 V2.4.2 - 12.05.2019
• supportoftheTimeTaggerUltraserieswithhardwarerevision1.3
• improveperformanceofshortpulsesequencesontheTimeTagger20series
• improveoverflowbehaviorattoohighinputdatarates
• fixthenameofthe‘SynchronizedMeasurements’measurementclass
11.33 V2.4.0 - 10.04.2019
Libraries
• 32bitC++libraryadded
• C++and.NETlibrariesrenamedandregisteredglobally
API
• virtualconstantfractiondiscriminatorchannel‘ConstantFractionDiscriminator’added
• ‘TimeDifferenceND’addedformultidimensionaltimedifferencesmeasurements
• fasterbinningin‘TimeDifferences’and‘Correlation’measurements
• improvedmemoryhandlingfor‘TimeTageStream’
• improvedPythonlibraryinclude
• fixed‘.getNormalizedData’for‘Correlation’measurements
• variousminorbugfixesandimprovements
Examples
• LabVIEWprojectfor32and64bit
• improvedLabVIEWexamples
TimeTaggerUltra
• 10MHzEXTinputclockdetectionenabled
• internalbuffersizecanbeincreasedfrom40MTagsto512MTagswith‘setHardwareBufferSize’
• reducedcrosstalkandtimingjitter
• increasedmaximumtransferratetoabove65MTags/s(Intel5GHzCPUon64bit)
• variousperformanceimprovements
• reduceddeadtimeto2nsonhardwarerevision>=1.2
200 Chapter11. RevisionHistory

TimeTaggerUserManual,Release2.17.4.0
TimeTagger20
• 166.6MHzEXTinputclockdetectionenabled
Operatingsystems
• equivalentsupportforWindows32and64bit,Ubuntu16.04and18.0464bit,CentOS764bit
11.34 V2.2.4 - 29.01.2019
• fixtheconditionalfilterwithfilterandtriggereventsarrivingwithinoneclockcycle
• fixissuewithnegativeinputdelays
• calling.stop()whiledumpingdatastopsthedumpandclosesthefile
• fixdeviceselectiononreconnectionaftertransfererrors
• synchronizetagsoffallingedgestotheirrisingones
11.35 V2.2.2 - 13.11.2018
• RemovednotrequiredMicrosoftprerequisites.
• 32bitversionavailable
11.36 V2.2.0 - 07.11.2018
Generalimprovements
• supportfordevicesstartingwithchannel1insteadof0
• undercertaincircumstances,thecrosstalkfortheTimeTagger20 ofchannel0-2,0-3,1-2,and1-3washighly
increased,whichhasbeenfixednow
• updatedandextendedexamplesforallprogramminglanguages(Python,Matlab,C#,C++,LabVIEW)
• C++examplesforVisualStudio2017,withdebugsupport
• documentationforvirtualchannels
• Webappincludedinthe32bitinstaller
• LinuxpackageavailableforUbuntu16.04
• SupportforPython3.7
11.34. V2.2.4-29.01.2019 201

TimeTaggerUserManual,Release2.17.4.0
API
• ‘HistogramLogBin’allowsanalyzingincomingtagswithlogarithmicbinsizes.
• ‘FrequencyMultiplier’virtualchannelclassforupscalingasignalattachedtotheTimeTagger. Thismethodcan
beusedasanalternativetothe‘ConditonalFilter’.
• ‘SynchronizedMeasurements’ class available to fully synchronize start(), stop(), clear() of different measure-
ments.
• Secondparameterfrom‘setConditionalFilter’changedfrom‘filter’to‘filtered’.
Webapplication
• full‘setConditionalFilter’functionalityavailablefromthebackendwithintheWebapplication
11.37 V2.1.6 - 17.05.2018
fixedanerrorwithgetBinWidthsfromCountBetweenMarkersreturningwrongvalues
11.38 V2.1.4 - 21.03.2018
fixedbinequilibrationerrorappearingsinceV2.1.0
11.39 V2.1.2 - 14.03.2018
fixedissueinstallingtheMatlabtoolbox
11.40 V2.1.0 - 06.03.2018
TimeTaggerUltra
• efficientbufferingofupto60MTagswithinthedevicetoavoidoverflows
11.41 V2.0.4 - 01.02.2018
Bugfixes
• Closingthewebapplicationserverwindowworksproperlynow
202 Chapter11. RevisionHistory

TimeTaggerUserManual,Release2.17.4.0
11.42 V2.0.2 - 17.01.2018
Improvements
• MatlabGUIexampleadded
• Matlabdump/loadexampleadded
Bugfixes
• dumpclasswritingtagsmultipletimeswhentheoptionalchannelparameterisused
• CounterandCountrateskipthetimeinbetweena.stop()anda.start()call
• TheCounterclassnowhandlesoverflowsproperly. Assoonasanoverflowoccursthelostdatajunkisskipped
andtheCounterresumeswiththenewtagsarrivingwithnogaponthetimeaxis.
11.43 V2.0.0 - 14.12.2017
ReleaseoftheTimeTaggerUltra
Note: Theinputdelaysmightbeshifted(uptoafewhundredps)comparedtoolderdriverversions.
Documentationchanges
• newsection‘InDepthGuides’explainingthehardwareeventfilter
Webapp
• fixedabugsettingtheinputvaluesto0whentypinginanewvalue
• newserverlauncherscreenwhichstopstheserverreliablywhentheapplicationisclosed
11.44 V1.0.20 - 24.10.2017
VirtualChannels
• DelayedChannelclonesandoptionallydelaysastreamoftimetagsfromaninputchannel
• GatedChannelclonesaninputstream,whichisgatedviaastartandstopchannel(e.g. risingandfallingedgeof
anotherphysicalchannel)
11.42. V2.0.2-17.01.2018 203

TimeTaggerUserManual,Release2.17.4.0
API
• startFor(duration)methodimplementedforallmeasurementstoacquiredataforapredefinedduration
• getCaptureDuration()availableforallmeasurementstoreturnthecurrentcaptureduration
• getDataNormalized()availableforCorrelation
• setEventDivider(channel,divider)alsotransmitseverynthevent(divider)onchanneldefined
Webapp
• labelfor0onthex-axisisnow0insteadofatinyvalue
C++API:
• internalchangesothatclear_impl()andnext_impl()mustbeoverwritteninsteadofclear()andnext()
Otherbugfixes/improvements
• improveddocumentationandexamples
11.45 V1.0.6 - 16.03.2017
Webapplication(GUI)
• load/savesettingsavailablefortheTimeTaggerandthemeasurements
• correctx-axisscaling
• inputchannelscanbelabeled
• savedataastabseparatedoutputfile(forMatlab,Excel,... import)
• fixed: savingmeasurementdatanowworksreliably
• fixed: ‘Initialize’buttonofmeasurementsworksnowwithtabletsandphones
API
• directtimestreamaccesspossiblewithnewclassTimeTagStream(beforethestreamcouldbeonlydumpedwith
Dump)
• Python3.6support
• bettererrorhandling(throwingexceptions)whenlibrariesnotfoundornoTimeTaggerattached
• setTestSignal(...) canbeusedwithavectorofchannelsinsteadofasinglechannelonly
• Dump(...) nowwithanoptionalvectorofchannelstoexplicitlydumpthechannelspassed
• CHANNEL_INVALIDisdeprecated-useCHANNEL_UNUSEDinstead
• Coincidencesclass(multipleCoincidences)canbeusednowwithinMatlab/LabVIEW
204 Chapter11. RevisionHistory

TimeTaggerUserManual,Release2.17.4.0
Documentationchanges
• documentationofeverymeasurementnowincludesafigure
• updateandincludewebapplicationinthequickstartsection
Otherbugfixes/improvements
• nointernaltesttagsleakingthroughfromtheinitializationoftheTimeTagger
• Counterclassnotclearingthedatabufferintimewhennotagsarrive
• searchpathforbitfileandlibrariesinLinuxnowworkastheyshould
• installerfor32bitOSavailable
11.46 V1.0.4 - 24.11.2016
Hardwarechanges
• extendedeventfiltertomultipleconditionsandfilterchannels
• improvedjitterforchannel0
• channeldelaysmightbedifferentfromthepreviousversion(<1ns)
APIchanges
• newfunctionsetConditionalFilterallowsformultiplefilterandeventchannels(replacessetFilter)
• ScopeclassimplementsfunctionalitytousetheTimeTaggerasa50GHzdigitizer
• Coincidencesclassnowcanhandlemultiplecoincidencegroupswhichismuchfasterthanmultipleinstancesof
Coincidence
• addedexamplesforC++and.net
Softwarechanges
• improvedGUI(Webapplication)
Bugfixes
• Matlab/LabVIEWisnotrequiredtohavetheVisualStudioRedistributablepackageinstalled
11.46. V1.0.4-24.11.2016 205

TimeTaggerUserManual,Release2.17.4.0
| 11.47 V1.0.2 | - 28.07.2016 |     |     |     |     |
| ------------ | ------------ | --- | --- | --- | --- |
Majorchanges:
• LabVIEWsupportincludingvariousexampleVIs
• Matlabsupportincludingvariousexamplescripts
• .netassembly/classlibraryprovided(32and64bit)
• WebAppgraphicaluserinterfacetogetstartedwithoutwritingasinglelineofcode
• Improvedperformance(multicoreCPUsaresupported)
APIchanges:
• reset()functionaddedtoresetaTimeTaggerdevicetothestartupstate
• getOverflowsAndClear()andclearOverflows()introducedtobeabletoresettheoverflowcounter
• supportforpython3.5(32and64bit)insteadof3.4
11.48 V1.0.0
initialreleasesupportingpython
| 11.49 Channel | Number | Schema | 0 and 1 |     |     |
| ------------- | ------ | ------ | ------- | --- | --- |
TheTimeTaggersdeliveredbeforemid2018startedwithchannelnumber0,whichisveryconvenientformostofthe
programminglanguages.
Nevertheless,withtheintroductionoftheTimeTaggerUltraandnegativetriggerlevels,thefallingedgesbecamemore
andmoreimportant,andwiththeoldchannelschema,itwasnotintuitivetogetthechannelnumberofthefallingedge.
Thisiswhywedecidedtomakeaprofoundchange,andweswitchedtothechannelschemawhichstartswithchannel1
insteadof0. Thefallingedgescanbeaccessedviathecorrespondingnegativechannelnumber,whichisveryintuitive
touse.
| TimeTagger20andUltra8 |         | TimeTaggerUltra18 |         | Schema |     |
| --------------------- | ------- | ----------------- | ------- | ------ | --- |
| rising                | falling | rising            | falling |        |     |
| old 0to7              | 8to15   | 0to17             | 18to35  |        |     |
TT_CHANNEL_NUMBER_SCHEME_ZERO
| new 1to8 | -1to-8 | 1to18 | -1to-18 | TT_CHANNEL_NUMBER_SCHEME_ONE |     |
| -------- | ------ | ----- | ------- | ---------------------------- | --- |
WithreleaseV2.2.0,thechannelnumberwasdetectedautomaticallyforthedeviceinuse. Itwasaccordingtothelabels
onthedevice. WithreleaseV2.17.0,thechannelnumberstartswiththenumber1bydefaultforalldevices,regardless
ofthelabelsonthedevice.
Incaseanotherchannelschemaisrequired,pleaseusesetTimeTaggerChannelNumberScheme(int scheme)be-
forethefirstTimeTaggerisinitialized.
int getInvertedChannel(int channel)wasintroducedtogettheoppositeedgeofagivenchannelindependent
ofthechannelschema.
| 206 |     |     |     | Chapter11. | RevisionHistory |
| --- | --- | --- | --- | ---------- | --------------- |

INDEX
A Coincidence(built-inclass),97
abort()(IteratorBasemethod),108
Coincidences(built-inclass),99
AccessMode(built-inclass),68
CoincidenceTimestamp(built-inclass),69
align_to_reference (FrequencyCounterData at-
Collecting(UsageStatisticsStatusattribute),71
tribute),142 CollectingAndUploading (UsageStatisticsStatus at-
tribute),71
All(ChannelEdgeattribute),69
autoCalibration()(TimeTaggermethod),85
Combinations(built-inclass),100
Average(CoincidenceTimestampattribute),69
Combiner(built-inclass),101
averaging_periods(SoftwareClockStateattribute),95 ConstantFractionDiscriminator (built-in class),
102
B Control(AccessModeattribute),68
Correlation(built-inclass),123
bins(FlimFrameInfoattribute),133
CountBetweenMarkers(built-inclass),114
built-in function
Counter(built-inclass),111
createTimeTagger(),71
CounterData(built-inclass),112
createTimeTaggerNetwork(),71
Countrate(built-inclass),110
createTimeTaggerVirtual(),71
createTimeTagger()
freeTimeTagger(),72
built-in function,71
getTimeTaggerChannelNumberScheme(),73
createTimeTaggerNetwork()
getTimeTaggerServerInfo(),72
built-in function,71
getUsageStatisticsReport(),75
createTimeTaggerVirtual()
getUsageStatisticsStatus(),74
built-in function,71
getVersion(),74
CustomMeasurement(built-inclass),157
mergeStreamFiles(),73
scanTimeTagger(),72
D
scanTimeTaggerServers(),72
setLogger(),73
DelayedChannel(built-inclass),102
setTimeTaggerChannelNumberScheme(),73
Disabled(UsageStatisticsStatusattribute),71
setUsageStatisticsStatus(),74
disableFpgaLink()(TimeTaggermethod),88
disableLEDs()(TimeTaggermethod),87
C disableSoftwareClock() (TimeTaggerBase method),
79
CHANNEL_UNUSED(built-invariable),68
dropped_bins(CounterDataattribute),112
ChannelEdge(built-inclass),69
Dump(built-inclass),151
ChannelGate(built-inclass),75
clear()(Dumpmethod),151
E
clear()(IteratorBasemethod),108
clear()(SynchronizedMeasurementsmethod),156
enabled(SoftwareClockStateattribute),95
clearConditionalFilter()(TimeTaggermethod),82
enableFpgaLink()(TimeTaggermethod),88
clearOverflows()(TimeTaggerBasemethod),78
Error(TagTypeattribute),70
clearOverflowsClient() (TimeTaggerNetwork
error_counter(SoftwareClockStateattribute),95
method),94
Event(built-inclass),153
clock_period(SoftwareClockStateattribute),95
EventGenerator(built-inclass),103
Closed(GatedChannelInitialattribute),70 External delay,162
207

TimeTaggerUserManual,Release2.17.4.0
F getCurrentFrame()(Flimmethod),129
Falling(ChannelEdgeattribute),69
getCurrentFrameEx()(Flimmethod),130
FileReader(built-inclass),150
getCurrentFrameIntensity()(Flimmethod),130
FileWriter(built-inclass),149
getDACRange()(TimeTaggermethod),85
First(CoincidenceTimestampattribute),69
getData()(Correlationmethod),123
Flim(built-inclass),128
getData()(CountBetweenMarkersmethod),114
FlimBase(built-inclass),134
getData()(Countermethod),111
FlimFrameInfo(built-inclass),132
getData()(CounterDatamethod),113
FpgaLinkInterface(built-inclass),69
getData()(Countratemethod),110
frame_number(FlimFrameInfoattribute),133
getData()(FileReadermethod),150
frameReady()(Flimmethod),132
getData()(Histogrammethod),117
frameReady()(FlimBasemethod),135
getData()(Histogram2Dmethod),121
getData()(HistogramLogBinsmethod),119
freeTimeTagger()
built-in function,72
getData()(HistogramNDmethod),122
FrequencyCounter(built-inclass),141
getData()(Samplermethod),154
FrequencyCounterData(built-inclass),142
getData()(Scopemethod),152
FrequencyMultiplier(built-inclass),104
getData()(StartStopmethod),116
FrequencyStability(built-inclass),137
getData()(TimeDifferencesmethod),125
FrequencyStabilityData(built-inclass),137
getData()(TimeTagStreammethod),147
getDataAsMask()(Samplermethod),155
G getDataNormalized()(Correlationmethod),123
GatedChannel(built-inclass),104
getDataNormalized()(Countermethod),112
GatedChannelInitial(built-inclass),70
getDataNormalized()(CounterDatamethod),113
getADEV()(FrequencyStabilityDatamethod),138 getDataNormalizedCountsPerPs() (HistogramLog-
Binsmethod),119
getADEVScaled() (FrequencyStabilityData method),
139
getDataNormalizedG2()(HistogramLogBinsmethod),
119
getBinEdges()(HistogramLogBinsmethod),119
getBinWidths()(CountBetweenMarkersmethod),115
getDataObject()(Countermethod),112
getCaptureDuration()(IteratorBasemethod),109
getDataObject()(FrequencyCountermethod),142
getChannel()(Combinationsmethod),100
getDataObject()(FrequencyStabilitymethod),137
getChannel()(VirtualChannelmethod),97
getDataObject()(HistogramLogBinsmethod),119
getChannelAbove() (TriggerOnCountrate method), getDataObject() (PulsePerSecondMonitor method),
145
106
getChannelBelow() (TriggerOnCountrate method),
getDataTotalCounts()(Countermethod),112
106
getDataTotalCounts()(CounterDatamethod),113
getChannelList()(FileReadermethod),151
getDeadtime()(TimeTaggerBasemethod),77
getChannelList()(TimeTaggermethod),85
getDelayClient()(TimeTaggerNetworkmethod),94
getChannels()(TimeTagStreamBuffermethod),148
getDelayHardware()(TimeTaggerBasemethod),76
getChannels()(TriggerOnCountratemethod),106
getDelaySoftware()(TimeTaggerBasemethod),77
getChannels()(VirtualChannelmethod),97
getDeviceLicense()(TimeTaggermethod),87
getCombination()(Combinationsmethod),100
getDistributionCount()(TimeTaggermethod),85
getConditionalFilterFiltered() (TimeTagger
getDistributionPSec()(TimeTaggermethod),86
method),82
getEventDivider()(TimeTaggermethod),82
getConditionalFilterTrigger() (TimeTagger
getEventTypes()(TimeTagStreamBuffermethod),148
method),82
getFence()(TimeTaggerBasemethod),79
getConfiguration()(FileReadermethod),151
getFrameNumber()(FlimFrameInfomethod),133
getConfiguration()(IteratorBasemethod),109
getFramesAcquired()(Flimmethod),130
getConfiguration()(TimeTaggerBasemethod),80
getFrequency()(CounterDatamethod),113
getConfiguration()(TimeTaggerVirtualmethod),93
getFrequency()(FrequencyCounterDatamethod),143
getCounts()(HistogramLogBinsDatamethod),120 getFrequencyInstantaneous() (FrequencyCounter-
Datamethod),143
getCounts()(TimeDifferencesmethod),126
getCountsTotal()(Countratemethod),110
getG2()(HistogramLogBinsDatamethod),120
getCurrentCountrate() (TriggerOnCountrate getG2Normalization() (HistogramLogBinsData
method),120
method),106
208 Index

TimeTaggerUserManual,Release2.17.4.0
|     |     | (TimeTagger getReadyFrameIntensity()(Flimmethod),131 |     |     |     |
| --- | --- | ---------------------------------------------------- | --- | --- | --- |
getHardwareDelayCompensation()
| method),81                                  |     | getReferenceOffsets() |             | (PulsePerSecondData |     |
| ------------------------------------------- | --- | --------------------- | ----------- | ------------------- | --- |
| getHDEV()(FrequencyStabilityDatamethod),138 |     |                       | method),145 |                     |     |
getHDEVScaled() (FrequencyStabilityData method), getReplaySpeed()(TimeTaggerVirtualmethod),93
| 140 |     | getSensorData()(TimeTaggermethod),87 |     |     |     |
| --- | --- | ------------------------------------ | --- | --- | --- |
getHistogramIndex()(TimeDifferencesmethod),125 getSerial()(TimeTaggermethod),84
getHistograms()(FlimFrameInfomethod),133 getSignalOffsets() (PulsePerSecondData method),
| getIndex()(Correlationmethod),124 |     |     | 146 |     |     |
| --------------------------------- | --- | --- | --- | --- | --- |
getIndex()(CountBetweenMarkersmethod),114 getSoftwareClockState() (TimeTaggerBase
| getIndex()(Countermethod),112 |     |     | method),79 |     |     |
| ----------------------------- | --- | --- | ---------- | --- | --- |
getIndex()(CounterDatamethod),112 getStatus()(PulsePerSecondDatamethod),146
getIndex()(Flimmethod),130 getSTDD()(FrequencyStabilityDatamethod),139
getIndex()(FrequencyCounterDatamethod),142 getSumChannel()(Combinationsmethod),100
getIndex()(Histogrammethod),117 getSummedCounts()(FlimFrameInfomethod),133
getIndex()(Histogram2Dmethod),121 getSummedFrames()(Flimmethod),131
getIndex()(HistogramNDmethod),122 getSummedFramesEx()(Flimmethod),131
getIndex()(TimeDifferencesmethod),125 getSummedFramesIntensity()(Flimmethod),131
getIndex_1()(Histogram2Dmethod),121 getTagger()(SynchronizedMeasurementsmethod),156
getIndex_2()(Histogram2Dmethod),121 getTau()(FrequencyStabilityDatamethod),137
getIndices()(PulsePerSecondDatamethod),145 getTDEV()(FrequencyStabilityDatamethod),139
getInputDelay()(TimeTaggerBasemethod),76 getTestSignal()(TimeTaggermethod),84
getInputHysteresis()(TimeTaggermethod),83 getTestSignalDivider()(TimeTaggermethod),87
getInputImpedanceHigh()(TimeTaggermethod),83 getTime()(CounterDatamethod),113
getIntensities()(FlimFrameInfomethod),133 getTime()(FrequencyCounterDatamethod),142
getInvertedChannel()(TimeTaggerBasemethod),80 getTimestamps()(TimeTagStreamBuffermethod),147
getMaxFileSize()(FileWritermethod),149
getTimeTaggerChannelNumberScheme()
getMDEV()(FrequencyStabilityDatamethod),138 built-in function,73
getMissedEvents() (TimeTagStreamBuffer method), getTimeTaggerServerInfo()
| 148 |     |     | function,72 |     |     |
| --- | --- | --- | ----------- | --- | --- |
built-in
getModel()(TimeTaggermethod),84 getTotalEvents()(FileWritermethod),149
getNormalization()(TimeTaggermethod),84 getTotalSize()(FileWritermethod),150
getOverflowMask()(CounterDatamethod),113 getTraceFrequency() (FrequencyStabilityData
| getOverflowMask() | (FrequencyCounterData | method), | method),140 |                      |     |
| ----------------- | --------------------- | -------- | ----------- | -------------------- | --- |
| 143               |                       |          |             | (FrequencyStability- |     |
getTraceFrequencyAbsolute()
| getOverflows()(TimeTaggerBasemethod),78 |     |     | Datamethod),140 |     |     |
| --------------------------------------- | --- | --- | --------------- | --- | --- |
getOverflows()(TimeTagStreamBuffermethod),148 getTraceIndex() (FrequencyStabilityData method),
|     | (TimeTaggerBase | method), | 140 |     |     |
| --- | --------------- | -------- | --- | --- | --- |
getOverflowsAndClear()
| 78  |                 | getTracePhase() | (FrequencyStabilityData |     | method), |
| --- | --------------- | --------------- | ----------------------- | --- | -------- |
|     | (TimeTaggerNet- |                 | 140                     |     |          |
getOverflowsAndClearClient()
| workmethod),95 |     | getTriggerLevel()(TimeTaggermethod),81 |     |     |     |
| -------------- | --- | -------------------------------------- | --- | --- | --- |
getOverflowsClient()(TimeTaggerNetworkmethod), getUsageStatisticsReport()
| 94  |     |     | function,75 |     |     |
| --- | --- | --- | ----------- | --- | --- |
built-in
getPcbVersion()(TimeTaggermethod),85 getUsageStatisticsStatus()
|                   | (FrequencyCounterData | method),                                    | function,74 |     |     |
| ----------------- | --------------------- | ------------------------------------------- | ----------- | --- | --- |
| getPeriodsCount() |                       |                                             | built-in    |     |     |
| 142               |                       | getUtcDates()(PulsePerSecondDatamethod),146 |             |     |     |
getPeriodsFraction() (FrequencyCounterData getUtcSeconds()(PulsePerSecondDatamethod),146
method),143
getVersion()
getPhase()(FrequencyCounterDatamethod),143 built-in function,74
getPixelBegins()(FlimFrameInfomethod),133
H
getPixelEnds()(FlimFrameInfomethod),134
| getPixelPosition()(FlimFrameInfomethod),133 |     |     | delay,161 |     |     |
| ------------------------------------------- | --- | --- | --------- | --- | --- |
Hardware
getPsPerClock()(TimeTaggermethod),86
hasData()(FileReadermethod),151
getReadyFrame()(Flimmethod),130 hasOverflows(TimeTagStreamBufferattribute),147
getReadyFrameEx()(Flimmethod),130
HIGH(Stateattribute),153
| Index |     |     |     |     | 209 |
| ----- | --- | --- | --- | --- | --- |

TimeTaggerUserManual,Release2.17.4.0
HighResA(Resolutionattribute),70 OverflowBegin(TagTypeattribute),70
HighResAll(ChannelEdgeattribute),69 OverflowEnd(TagTypeattribute),70
HighResB(Resolutionattribute),70
HighResC(Resolutionattribute),70 P
HighResFalling(ChannelEdgeattribute),69 period_error(SoftwareClockStateattribute),95
HighResRising(ChannelEdgeattribute),69 phase_error_estimation (SoftwareClockState at-
Histogram(built-inclass),116 tribute),95
Histogram2D(built-inclass),120 pixel_position(FlimFrameInfoattribute),133
HistogramLogBins(built-inclass),118 pixels(FlimFrameInfoattribute),132
HistogramLogBinsData(built-inclass),119 process()(CustomMeasurementmethod),157
HistogramND(built-inclass),122 PulsePerSecondData(built-inclass),145
PulsePerSecondMonitor(built-inclass),144
I
ideal_clock_channel (SoftwareClockState attribute), Q
95 QSFPP_40GE(FpgaLinkInterfaceattribute),70
initialize()(Flimmethod),132
initialize()(FlimBasemethod),135 R
injectCurrentState()(TriggerOnCountratemethod),
ready()(CountBetweenMarkersmethod),115
106
ready()(Scopemethod),153
Input time stamp,161
ready()(TimeDifferencesmethod),126
input_channel(SoftwareClockStateattribute),95
registerMeasurement() (SynchronizedMeasurements
is_locked(SoftwareClockStateattribute),95
method),155
isAbove()(TriggerOnCountratemethod),106
replay()(TimeTaggerVirtualmethod),92
isAcquiring()(Flimmethod),132
reset()(TimeTaggermethod),81
isAcquiring()(FlimBasemethod),135
Resolution(built-inclass),70
isBelow()(TriggerOnCountratemethod),106
Rising(ChannelEdgeattribute),69
isConnected()(TimeTaggerNetworkmethod),94
isRunning()(IteratorBasemethod),109
S
isRunning()(SynchronizedMeasurementsmethod),156
isServerRunning()(TimeTaggermethod),88
sample_offset(FrequencyCounterDataattribute),142
isUnusedChannel()(TimeTaggerBasemethod),80
Sampler(built-inclass),154
isValid()(FlimFrameInfomethod),133 sampling_interval (FrequencyCounterData at-
tribute),142
IteratorBase(built-inclass),108
scanTimeTagger()
L built-in function,72
scanTimeTaggerServers()
Last(CoincidenceTimestampattribute),69
built-in function,72
last_ideal_clock_event (SoftwareClockState at-
Scope(built-inclass),152
tribute),95
setConditionalFilter()(TimeTaggermethod),81
ListedFirst(CoincidenceTimestampattribute),69
setDeadtime()(TimeTaggerBasemethod),77
Listen(AccessModeattribute),68
setDelay()(DelayedChannelmethod),102
LOW(Stateattribute),153
setDelayClient()(TimeTaggerNetworkmethod),94
setDelayHardware()(TimeTaggerBasemethod),76
M
setDelaySoftware()(TimeTaggerBasemethod),76
mergeStreamFiles() setEventDivider()(TimeTaggermethod),82
built-in function,73 setHardwareBufferSize()(TimeTaggermethod),85
MissedEvents(TagTypeattribute),70
setInputDelay()(TimeTaggerBasemethod),76
mutex(CustomMeasurementattribute),157
setInputHysteresis()(TimeTaggermethod),83
setInputImpedanceHigh()(TimeTaggermethod),82
O
setLED()(TimeTaggermethod),87
Open(GatedChannelInitialattribute),70 setLogger()
overflow(CounterDataattribute),112 built-in function,73
overflow_samples (FrequencyCounterData attribute), setMaxCounts()(TimeDifferencesmethod),125
142 setMaxFileSize()(FileWritermethod),149
210 Index

TimeTaggerUserManual,Release2.17.4.0
setNormalization()(TimeTaggermethod),84 TimeTagStream(built-inclass),147
setReplaySpeed()(TimeTaggerVirtualmethod),93 TimeTagStreamBuffer(built-inclass),147
setSoftwareClock()(TimeTaggerBasemethod),78 triggered()(Scopemethod),153
setSoundFrequency()(TimeTaggermethod),88 TriggerOnCountrate(built-inclass),106
setStreamBlockSize()(TimeTaggermethod),86 tStart(TimeTagStreamBufferattribute),147
setTestSignal()(TimeTaggermethod),84
setTestSignalDivider()(TimeTaggermethod),86 U
setTimeTaggerChannelNumberScheme() UNKNOWN(Stateattribute),153
built-in function,73 unregisterMeasurement() (SynchronizedMeasure-
setTimeTaggerNetworkStreamCompression() mentsmethod),156
(TimeTaggermethod),86 UsageStatisticsStatus(built-inclass),71
setTriggerLevel()(TimeTaggermethod),81
setUsageStatisticsStatus() W
built-in function,74
waitForCompletion()(TimeTaggerVirtualmethod),92
SFPP_10GE(FpgaLinkInterfaceattribute),70
waitForFence()(TimeTaggerBasemethod),79
size(CounterDataattribute),112
waitUntilFinished()(IteratorBasemethod),109
size(FrequencyCounterDataattribute),142
size(PulsePerSecondDataattribute),145 X
size(TimeTagStreamBufferattribute),147
xtra_getAuxOut()(TimeTaggermethod),90
SoftwareClockState(built-inclass),95
xtra_getAuxOutSignalDutyCycle() (TimeTagger
split()(FileWritermethod),149
method),90
Standard(Resolutionattribute),70
xtra_getAvgRisingFalling() (TimeTagger method),
StandardAll(ChannelEdgeattribute),69
89
StandardFalling(ChannelEdgeattribute),69
xtra_getClockAutoSelect() (TimeTagger method),
StandardRising(ChannelEdgeattribute),69
91
start()(IteratorBasemethod),108
xtra_getClockSource()(TimeTaggermethod),91
start()(SynchronizedMeasurementsmethod),156
xtra_getHighPrioChannel() (TimeTagger method),
startFor()(IteratorBasemethod),108
89
startFor()(SynchronizedMeasurementsmethod),156
xtra_measureTriggerLevel() (TimeTagger method),
startServer()(TimeTaggermethod),88
91
StartStop(built-inclass),116
xtra_setAuxOut()(TimeTaggermethod),90
State(built-inclass),153
xtra_setAuxOutSignal()(TimeTaggermethod),90
state(Eventattribute),153
xtra_setAvgRisingFalling() (TimeTagger method),
stop()(Dumpmethod),152
89
stop()(IteratorBasemethod),108
xtra_setClockAutoSelect() (TimeTagger method),
stop()(SynchronizedMeasurementsmethod),156
91
stop()(TimeTaggerVirtualmethod),92
xtra_setClockOut()(TimeTaggermethod),91
stopServer()(TimeTaggermethod),88
xtra_setClockSource()(TimeTaggermethod),91
sync()(TimeTaggerBasemethod),79
xtra_setHighPrioChannel() (TimeTagger method),
SynchronizedMeasurements(built-inclass),155
89
SynchronousControl(AccessModeattribute),68
T
TagType(built-inclass),70
TDC time stamp,161
tGetData(TimeTagStreamBufferattribute),147
time(Eventattribute),153
TimeDifferences(built-inclass),125
TimeDifferencesND(built-inclass),127
TimeTag(TagTypeattribute),70
TimeTagger(built-inclass),81
TimeTaggerBase(built-inclass),76
TimeTaggerNetwork(built-inclass),93
TimeTaggerVirtual(built-inclass),92
Index 211