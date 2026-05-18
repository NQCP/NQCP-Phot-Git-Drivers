# ----- CW Panel -----
#   Frequency       Spinbox
#   Frequency Step  Spinbox
#   Freq Offset     Spinbox
#   Spur Mode       combobox
#   AM Modulation   Spinbox
#   AM Freq         Spinbox
from __future__ import print_function
import tkinter as tk
from tkinter import ttk
import MyWidgets

class CwPanel( ttk.Frame ):

    # Class data
    freqBox = None
    freqActual = None

    freqStepBox = None
    freqStepActual = None

    freqOffsetBox = None
    freqOffsetActual = None

    spurModeBox = None  # Combobox
    spurModeActual = None  # Label

    AmModulationBox = None
    AmModulationActual = None

    AmFreqBox = None
    AmFreqActual = None

    # ----- Constructor -----
    def __init__( self, parent ):
        # Call the base constructor
        ttk.Frame.__init__( self, parent, borderwidth=5, relief=tk.GROOVE )
        self.parent = parent    # parent = Main window
        self.Name = "CwPanel"

        # Set the column widths
        self.columnconfigure(0, minsize=parent.labelColPixels )
        self.columnconfigure(1, minsize=parent.labelColPixels )
        self.columnconfigure(2, minsize=parent.labelColPixels )

        # The following is part of allowing the window to be resized.
        self.rowconfigure( 0, weight=1 )

        self.columnconfigure( 0, weight=1 )
        self.columnconfigure( 1, weight=1 )
        self.columnconfigure( 2, weight=1 )

        #self[ "bg" ] = 'ivory'

        # Get default values for the widgets
        defaults = parent.defaults.CW()

        nextCol = 0
        nextRow = 0

        # ----- Frequency -----
        # ----- Col-1 Label -----
        temp = ttk.Label( self, text="Frequency" )
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        nextCol += 1
        temp[ 'anchor' ] = tk.E

        # ----- Freq Control Box -----
        temp = MyWidgets.MySpinbox( self, defaults.FreqName,    # FREQ
                                    defaults.FreqMin, defaults.FreqMax,
                                    defaults.FreqDefault )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        CwPanel.freqBox = temp

        # ----- Freq Actual -----
        temp = ttk.Label( self )
        temp.grid( column=nextCol, row=nextRow )
        nextCol += 1
        temp[ 'text' ] = CwPanel.freqBox.Units
        CwPanel.freqActual = temp

        nextCol = 0
        nextRow += 1


        # ---------------------
        # ----- Freq Step -----
        # ----- Col-1 Label -----
        temp = ttk.Label(self, text="Freq Step")
        temp.grid( column=nextCol, row=nextRow, sticky=tk.E )
        nextCol += 1

        # ----- Step Freq (FSTEP) Box -----
        """
        temp = tk.Spinbox( self )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        temp.Name = defaults.FreqStepName   # FSTEP
        temp['bg'] = 'ivory'
        temp['from_'] = defaults.FreqStepMin
        temp['to'] = defaults.FreqStepMax
        temp.Value = tk.DoubleVar()
        temp.Value.set( defaults.FreqStepDefault )
        temp['textvariable'] = temp.Value
        temp['increment'] = defaults.FreqStepIncrement

        temp[ "command" ] = lambda : parent.SpinboxEH( CwPanel.freqStepBox )
        temp.bind("<Return>", parent.SpinboxReturnEH)
        """
        temp = MyWidgets.MySpinbox( self, defaults.FreqStepName,    # FSTEP
                                    defaults.FreqStepMin, defaults.FreqStepMax,
                                    defaults.FreqStepDefault
                                )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        CwPanel.freqStepBox = temp
        CwPanel.freqBox[ 'increment' ] = CwPanel.freqStepBox.Value.get()

        # ----- Frequency Step Actual -----
        temp = ttk.Label(self)
        temp.grid(column=nextCol, row=nextRow)
        nextCol += 1
        #temp.Text = tk.StringVar()
        #temp['textvariable'] = temp.Text
        #temp.Text.set("MHz")
        temp[ 'text' ] = "MHz"
        CwPanel.freqStepActual = temp

        nextCol = 0
        nextRow += 1

        # -----------------------
        # ----- Freq Offset -----
        # ----- Col-1 Label -----
        temp = ttk.Label(self, text="Freq Offset")
        temp.grid( column=nextCol, row=nextRow, sticky=tk.E )
        nextCol += 1

        # ----- Freq Offset Box -----
        """
        temp = tk.Spinbox( self )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1

        temp.Name = defaults.FreqOffsetName     # "OFFSET"
        temp['bg'] = 'ivory'
        temp['from_'] = defaults.FreqOffsetMin
        temp['to'] = defaults.FreqOffsetMax
        temp.Value = tk.DoubleVar()
        temp.Value.set( defaults.FreqOffsetDefault )
        temp['textvariable'] = temp.Value
        temp['increment'] = defaults.FreqOffsetIncrement

        temp[ "command" ] = lambda : parent.SpinboxEH (CwPanel.offsetFreqBox)
        temp.bind("<Return>", parent.SpinboxReturnEH)
        """
        temp = MyWidgets.MySpinbox( self, defaults.FreqOffsetName,
                                    defaults.FreqOffsetMin, defaults.FreqOffsetMax,
                                    defaults.FreqOffsetDefault
                                  )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        temp['increment'] = defaults.FreqOffsetIncrement
        CwPanel.freqOffsetBox = temp

        # ----- Offset Actual -----
        temp = ttk.Label(self)
        temp.grid(column=nextCol, row=nextRow)
        nextCol += 1

        temp.Text = tk.StringVar()
        #temp['textvariable'] = temp.Text
        #temp.Text.set("MHz")
        temp[ 'text' ] = "MHz"
        CwPanel.freqOffsetActual = temp

        nextCol = 0
        nextRow += 1

        # ----- Spur Mode -----
        # Col-1 Label
        temp = ttk.Label(self, text="Spur Mode ")
        temp.grid(column=nextCol, row=nextRow, sticky='E', ipadx = 0 )
        nextCol += 1

        # ----- Spur Mode (SDN) Combobox -----
        # Values = ("Low Noise 1", "Low Noise 2", "Low Spur 1", "Low Spur 2")
        # Codes = ("LN1", "LN2", "LS1", "LS2")
        temp = MyWidgets.MyCombobox( self, defaults.SpurModeName,
                                     defaults.SpurModeValues,
                                     defaults.SpurModeDefault )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        temp.Codes = defaults.SpurModeCodes     # ( "LN1", "LN2", "LS1", "LS2" )
        temp.Value.set( temp.Codes[ temp.current() ] )
        temp.bind("<<ComboboxSelected>>", parent.ComboboxCodeEH)
        temp.bind("<Return>", parent.ComboboxCodeEH)
        CwPanel.spurModeBox = temp

        # Spur Mode Actual Label
        temp = ttk.Label(self)
        temp.grid(column=nextCol, row=nextRow)
        nextCol += 1
        value = CwPanel.spurModeBox.Value.get()
        temp[ 'text' ] = value
        CwPanel.spurModeActual = temp

        nextCol = 0
        nextRow += 1

        # ----- AM Modulation -----
        # ----- Col-1 Label -----
        temp = ttk.Label( self, text="AM Modulation" )
        temp.grid( column=nextCol, row=nextRow, sticky=tk.E )
        nextCol += 1
        self.freqLabel = temp

        # ----- AM Modulation Control Box -----
        """
        temp = tk.Spinbox( self )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        temp.Name = defaults.AmModulationName       # "AMD"
        temp[ 'bg' ] = 'ivory'
        temp[ 'to' ] = defaults.AmModulationMax     # 31.5000
        temp[ 'from_' ] = defaults.AmModulationMin  # 0.0000
        temp[ 'increment' ] = defaults.AmModulationStep # 0.5
        temp.Value = tk.DoubleVar()
        temp.Value.set( defaults.AmModulationDefault )   # 0
        temp[ 'textvariable' ] = temp.Value

        # EH for the arrows
        temp[ "command" ] = lambda : parent.SpinboxEH (CwPanel.AmModulationBox)
        # EH for the return key
        temp.bind( "<Return>", parent.SpinboxReturnEH )
        """
        temp = MyWidgets.MySpinbox( self, defaults.AmModulationName,
                                    defaults.AmModulationMin, defaults.AmModulationMax,
                                    defaults.AmModulationDefault
                                  )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        temp[ 'increment' ] = defaults.AmModulationStep # 0.5
        temp.Units = "dB"
        CwPanel.AmModulationBox = temp

        # ----- AM Modulation Actual -----
        temp = ttk.Label( self )
        temp.grid( column=nextCol, row=nextRow, sticky=tk.EW )
        nextCol += 1
        temp[ 'anchor' ] = tk.CENTER
        temp[ 'text' ] = CwPanel.AmModulationBox.Units
        CwPanel.AmModulationActual = temp

        nextCol = 0
        nextRow += 1

        # ----- AM Frequency -----
        # ----- Col-1 Label -----
        temp = ttk.Label( self, text="AM Frequency" )
        temp.grid( column=nextCol, row=nextRow, sticky=tk.E )
        nextCol += 1
        self.AmFreqLabel = temp

        # ----- AM Freq Control Box -----
        # AMF
        """
        temp = tk.Spinbox( self )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        temp.Name = defaults.AmFreqName     # "AMF"
        temp[ 'bg' ] = 'ivory'
        temp[ 'to' ] = defaults.AmFreqMax   # 10.000
        temp[ 'from_' ] = defaults.AmFreqMin    # 1.000
        temp[ 'increment' ] = defaults.AmFreqStep   # 0.100 KHz
        temp.Value = tk.DoubleVar()
        temp.Value.set( defaults.AmFreqDefault )    # 1.000 kHz
        temp[ 'textvariable' ] = temp.Value

        # EH for the arrows
        #temp.bind( '<Up>' , parent.SpinboxReturnEH )  # Worked
        temp[ "command" ] = lambda : parent.SpinboxEH (CwPanel.AmFreqBox)
        # EH for the return key
        temp.bind( "<Return>", parent.SpinboxReturnEH )
        """

        temp = MyWidgets.MySpinbox( self, defaults.AmFreqName,
                                    defaults.AmFreqMin, defaults.AmFreqMax,
                                    defaults.AmFreqDefault
                                    )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        temp.Units = "kHz"
        CwPanel.AmFreqBox = temp

        # ----- AM Freq Actual -----
        temp = ttk.Label( self )
        temp.grid( column=nextCol, row=nextRow, sticky=tk.EW )
        nextCol += 1

        temp[ 'anchor' ] = tk.CENTER
        #temp.Text = tk.StringVar()
        #temp.Text.set( "kHz" )
        #temp[ 'textvariable' ] = temp.Text
        #temp[ 'text' ] = "kHz"
        temp[ 'text' ] = CwPanel.AmFreqBox.Units
        CwPanel.AmFreqActual = temp

        # end of CwPanel constructor
