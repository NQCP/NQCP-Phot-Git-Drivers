# Valon 5015 / 5019 Constants
#  Default values and Limits
class Defaults:
    class Mode:
        ModeName = "Mode"
        ModeValues = ( "CW", "SWEEP", "LIST" )
        ModeDefault = 0   # ie. the default mode is Continuous Wave ("CW")
        
    class CW:
        FreqName = "Freq"
        FreqDefault = 2440.000000
        FreqMin = 10.0000       # MHz  updated for 5015
        # FreqMax = 15000.0000  #  5015
        FreqMax = 19000.0000    #  5019
        FreqIncrement = 1.0000

        FreqStepName = "FSTEP"
        FreqStepDefault = 1.0000
        FreqStepMin = 0.00000
        FreqStepMax =  100.0000
        FreqStepIncrement = 1.0000

        FreqOffsetName = "OFFSET"
        FreqOffsetDefault = 0
        FreqOffsetMin = -4000.0000
        FreqOffsetMax =  4000.0000
        FreqOffsetIncrement = 1.0000

        SpurModeName = "SDN"
        SpurModeDefault = 0
        SpurModeValues = ( "Low Noise 1", "Low Noise 2", "Low Spur 1", "Low Spur 2" );
        SpurModeCodes = ( "LN1", "LN2", "LS1", "LS2" )

        AmModulationName = "AMD"
        AmModulationDefault = 0.0
        AmModulationMin = 0.0
        AmModulationMax = 31.5
        AmModulationStep = 0.5

        AmFreqName = "AMF"
        AmFreqDefault = 1.000       #  1 kHz
        AmFreqMin = 0.0005          #  0.5 Hz
        AmFreqMax = 10.000          #  10 kHz
        AmFreqStep = 0.100


    class Power:
        #   Power Panel
        RfLevelName = 'PWR'
        RfLevelInitial = 1.00
        RfLevelMin = -50.00
        RfLevelMax = 20.00
        RfLevelStep = 1.00

        RfEnableName = 'OEN'
        OffOn = ( "Off", "On")
        RfEnableInitial = 1 # On

        PowerName = 'PDN'
        PowerInitial = 1

    class Reference:
        #   Reference Panel
        RefSourceName = "REFS"
        RefSourceValues = ( 'Internal', 'External' )
        RefSourceDefault = 0        #   Internal / External

        RefFreqName = "REF"
        RefFreqDefault = 10.0000    #  5015
        RefFreqMax = 120.0000       #  Todo: what is the 5015 value?
        RefFreqMin = 5.0000         #    "

        RefTrim10Default = 0        #  Updated 10 May 16
        RefTrim10Max = 511
        RefTrim10Min = -512

    class Sweep:
        StartName = "START"
        Min = 10
        Max = 19000
        Increment = 1.0000
        StartDefault = 2100.0000

        StopName = "STOP"
        StopDefault = 2800.0000
        #StopMax = 19000

        StepName = "STEP"
        StepDefault = 1
        StepMin = 0.00001
        StepMax = 4294

        RateName = "RATE"
        RateMin = 0.1
        RateMax = 1000000
        RateDefault = 1.0

        RetraceTimeName = "RTIME"
        RetraceMin = 0
        RetraceMax = 10000
        RetraceDefault = 0

        TModeName = "TMODE"
        TModeValues = ( "AUTO", "MANUAL", "EXTERNAL", "EXTSTEP" )
        TModeDefault = 0

        # HaltRunName is set at runtime to "RUN" or "HALT"
        HaltRunName = "HaltRun"
        HaltRunValues = ( "HALT", "RUN" )
        HaltRunStates = ( "Halted", "Running" )
        HaltRunDefault = "HALT"

        TriggerName = "TRGR"
        #TriggerModeAuto = 0
        #TriggerModeManual = 1
        #TriggerModeExternal = 2
        #TriggerModeExtstep = 3
