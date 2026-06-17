# ----- Sweep Panel -----
#   Contents 
#   Start Freq      Spinbox
#   Stop Freq       Spinbox
#   Step Freq       Spinbox
#   Rate            Spinbox
#   Retrace Time    Spinbox
#   Trigger Mode    Combobox
#   Run / Halt      CheckButton
#   Trigger         Button

from __future__ import print_function
import tkinter as tk
from tkinter import ttk
import MyWidgets

class SweepPanel( ttk.Frame ):

    # Class data
    startFreqBox = None         # Spinbox START 23 MHz; // Act 23 MHz
    startFreqActual = None
    
    stopFreqBox = None         # Spinbox STOP 6000 MHz; // Act 6000 MHz
    stopFreqActual = None
    
    stepFreqBox = None         # Spinbox STEP 1 MHz;
    stepFreqActual = None
    
    rateBox = None              # Spinbox RATE 1000; // ms
    rateActual = None
    
    retraceBox = None           # Spinbox RTIME 0; // ms
    retraceActual = None
    
    triggerModeBox = None          # Combobox TMODe AUTO;
    triggerModeActual = None
    
    haltRunBtn = None           # Checkbutton HALT
    haltRunActual = None

    triggerBtn = None           # Button
    triggerActual = None

    # ----- Constructor -----
    def __init__( self, parent ):
        ttk.Frame.__init__( self, parent, borderwidth=5, relief=tk.GROOVE )
        self.parent = parent
        self.Name = "SweepPanel"

        # Set the column widths
        self.columnconfigure(0, minsize=parent.labelColPixels, weight=1 )
        self.columnconfigure(1, minsize=parent.labelColPixels, weight=1 )
        self.columnconfigure(2, minsize=parent.labelColPixels, weight=1 )

        # The following is part of allowing the window to be resized.
        self.rowconfigure( 0, weight=1 )

        #self[ "bg" ] = 'ivory'

        # Get default values for the widgets
        defaults = parent.defaults.Sweep()

        nextCol = 0
        nextRow = 0

        # ----- Start Frequency ----------------------------
        # ----- Col-1 Label -----
        temp = ttk.Label( self, text="Start Freq" )
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        nextCol += 1
        temp[ 'anchor' ] = tk.E

        # ----- Start Freq Spinbox -----
        temp = MyWidgets.MySpinbox( self, defaults.StartName,
                                    defaults.Min, defaults.Max,
                                    defaults.StartDefault )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        SweepPanel.startFreqBox = temp

        # ----- Start Freq Actual -----
        temp = ttk.Label( self )
        temp.grid( column=nextCol, row=nextRow )
        nextCol += 1
        temp[ 'text' ] = "MHz"
        SweepPanel.startFreqActual = temp

        nextCol = 0
        nextRow += 1

        # ----- Stop Frequency ------------------------------
        # ----- Col-1 Label -----
        temp = ttk.Label( self, text="Stop Freq" )
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        nextCol += 1
        temp[ 'anchor' ] = tk.E

        # ----- Stop Freq Spinbox -----
        temp = MyWidgets.MySpinbox( self, defaults.StopName,
                                    defaults.Min, defaults.Max,
                                    defaults.StopDefault )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        #temp[ 'to' ] = defaults.Max
        #temp[ 'from_' ] = defaults.Min
        #temp[ "command" ] = lambda : parent.SpinboxEH (SweepPanel.startFreqBox)
        SweepPanel.stopFreqBox = temp

        # ----- Stop Freq Actual -----
        temp = ttk.Label( self )
        temp.grid( column=nextCol, row=nextRow )
        nextCol += 1
        temp[ 'text' ] = "MHz"
        SweepPanel.stopFreqActual = temp

        nextCol = 0
        nextRow += 1

        # ----- Step Frequency -----------------------------
        # ----- Col-1 Label -----
        temp = ttk.Label( self, text="Step Freq" )
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        nextCol += 1
        temp[ 'anchor' ] = tk.E

        # ----- Step Freq Spinbox -----
        temp = MyWidgets.MySpinbox( self, defaults.StepName,
                                    defaults.StepMin, defaults.StepMax,
                                    defaults.StepDefault )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        #temp.Units = 'MHz'
        #temp[ 'to' ] = defaults.StepMax
        #temp[ 'from_' ] = defaults.StepMin
        #temp[ "command" ] = lambda : parent.SpinboxEH (SweepPanel.startFreqBox)
        SweepPanel.stepFreqBox = temp

        # ----- Step Freq Actual -----
        temp = ttk.Label( self )
        temp.grid( column=nextCol, row=nextRow )
        nextCol += 1
        temp[ 'text' ] = "MHz"
        SweepPanel.stepFreqActual = temp

        nextCol = 0
        nextRow += 1

        # ----- Sweep Rate ----------------------------
        # ----- Col-1 Label -----
        temp = ttk.Label( self, text="Rate (millSec)" )
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        nextCol += 1
        temp[ 'anchor' ] = tk.E

        # ----- Sweep Rate Spinbox -----
        temp = MyWidgets.MySpinbox( self, defaults.RateName,
                                    defaults.RateMin, defaults.RateMax,
                                    defaults.RateDefault )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        temp.Units = None
        SweepPanel.rateBox = temp

        # ----- Sweep Rate Actual -----
        temp = ttk.Label( self )
        temp.grid( column=nextCol, row=nextRow )
        nextCol += 1
        temp[ 'text' ] = "milliSec"
        SweepPanel.rateActual = temp

        nextCol = 0
        nextRow += 1

        # ----- Retrace Time ------------------------
        # ----- Col-1 Label -----
        temp = ttk.Label( self, text="Retrace Time" )
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        nextCol += 1
        temp[ 'anchor' ] = tk.E

        # ----- Retrace Time Spinbox -----
        temp = MyWidgets.MySpinbox( self, defaults.RetraceTimeName,
                                    defaults.RetraceMin, defaults.RetraceMax,
                                    defaults.RetraceDefault )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        #temp[ 'to' ] = defaults.RetraceMax
        #temp[ 'from_' ] = defaults.RetraceMin
        temp.Units = ""
        SweepPanel.retraceBox = temp

        # ----- Retrace Time Actual -----
        temp = ttk.Label( self )
        temp.grid( column=nextCol, row=nextRow )
        nextCol += 1
        temp[ 'text' ] = "milliSec"
        SweepPanel.retraceActual = temp

        nextCol = 0
        nextRow += 1

        # ----- Trigger Mode ---------------------------------------
        # ----- Col-1 Label -----
        temp = ttk.Label( self, text="Trigger Mode", anchor = tk.E )
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        nextCol += 1

        # ----- Trigger Mode Combobox -----
        temp = MyWidgets.MyCombobox( self, defaults.TModeName,
                                     defaults.TModeValues,
                                     defaults.TModeDefault
                                   )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        temp.bind("<<ComboboxSelected>>", parent.ComboboxValueEH)
        temp.bind("<Return>", parent.ComboboxValueEH)
        SweepPanel.triggerModeBox = temp

        # ----- Trigger Mode Actual -----
        temp = ttk.Label( self )
        temp.grid( column=nextCol, row=nextRow )
        nextCol += 1
        temp[ 'text' ] = SweepPanel.triggerModeBox.Text.get()
        SweepPanel.triggerModeActual = temp

        nextCol = 0
        nextRow += 1

        # ----- Halt / Run Checkbutton ----------------------------
        # ----- Col-1 Label -----
        temp = ttk.Label( self, text="Run / Halt", anchor = tk.E )
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        nextCol += 1

        temp = ttk.Checkbutton( self )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        temp.Name = defaults.HaltRunName    # "HaltRun"
        temp.writeRegisters = False
        temp[ 'offvalue' ] = defaults.HaltRunValues[ 0 ]    # "HALT"
        temp[ 'onvalue' ] = defaults.HaltRunValues[ 1 ]     # "RUN"
        temp.Value = tk.StringVar()
        temp[ 'variable' ] = temp.Value
        temp.Value.set( defaults.HaltRunDefault )   # "HALT"
        temp.Values = defaults.HaltRunValues    # ( "HALT", "RUN" )
        temp.States = defaults.HaltRunStates    # ( "Halted", "Running" )
        # When the Value is 0 (ie. Halted) the Button text will be "Run"
        #temp[ 'text' ] = temp.Values[ 1 ]
        temp[ 'text' ] = ( "Run" if temp.Value.get == "HALT" else "HALt" )
        temp.Units = None
        temp[ 'command' ] = lambda : parent.RunHaltCheckbuttonEH( SweepPanel.haltRunBtn )
        SweepPanel.haltRunBtn = temp

        # ----- Run / Halt Actual -----
        temp = ttk.Label( self )
        temp.grid( column=nextCol, row=nextRow )
        nextCol += 1
        #temp[ 'text' ] = ( 'Halted', 'Running' )[ SweepPanel.haltRunBtn.Value.get() ]
        temp[ 'text' ] = \
            "Halted" if ( SweepPanel.haltRunBtn.Value.get() == "HALT" ) else "Running"

        SweepPanel.haltRunActual = temp
        nextCol = 0
        nextRow += 1

        # ----- Trigger Button ----------------------------
        # ----- Col-1 Label -----
        temp = ttk.Label( self, text="Trigger", anchor = tk.E )
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        nextCol += 1

        temp = ttk.Button( self )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        temp[ 'text' ] = "Trigger"
        temp.Name = defaults.TriggerName
        # sendCommand wants every widget to have a Value.  It won't be used.
        temp.Value = tk.IntVar()
        temp.Value.set( -1 )
        temp[ 'state' ] = tk.DISABLED
        temp.Units = None
        temp[ 'command' ] = lambda : parent.ButtonEH( SweepPanel.triggerBtn )
        SweepPanel.triggerBtn = temp

        # ----- Run / Halt Actual -----
        temp = ttk.Label( self )
        temp.grid( column=nextCol, row=nextRow )
        nextCol += 1
        temp['text'] = 'Enabled' if ( SweepPanel.triggerModeBox.current() == 1 ) else 'Disabled'
        SweepPanel.triggerActual = temp

