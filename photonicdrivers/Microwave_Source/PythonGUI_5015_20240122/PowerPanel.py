# ----- Power Panel -----
# RfLevel   Spinbox         PWR
# RfOutput  ToggleButton    OEN
# Power     ToggleButton    PDN

from __future__ import print_function
import tkinter as tk
from tkinter import ttk
import Defaults
import MyWidgets

class PowerPanel( ttk.Frame ):
    """ Power Panel Management """
    RfLevelBox = None
    RfLevelActual = None

    RfEnableBox = None
    RfEnableActual = None

    powerBox = None
    powerActual = None

    def __init__( self, parent ):
        # Call the base constructor
        ttk.Frame.__init__(self, parent, borderwidth=5, relief=tk.GROOVE)
        self.parent = parent
        self.Name = "PowerPanel"

        self.columnconfigure(0, minsize=parent.labelColPixels )
        self.columnconfigure(1, minsize=parent.labelColPixels )
        self.columnconfigure(2, minsize=parent.labelColPixels )

        self.columnconfigure( 0, weight=1 )
        self.columnconfigure( 1, weight=1 )
        self.columnconfigure( 2, weight=1 )

        # Instantiate the Power Panel's defaults class
        defaults = parent.defaults.Power()
        nextRow = nextCol = 0

        # ---------------------
        # ----- RF Level ------
        # ----- Col-1 Label -----
        temp = ttk.Label( self, text="RF Level" )
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        temp[ 'anchor' ] = tk.E
        nextCol += 1

        # ----- RF Level Spinbox -----
        temp = MyWidgets.MySpinbox( self, defaults.RfLevelName,
                                    defaults.RfLevelMin, defaults.RfLevelMax,
                                    defaults.RfLevelInitial
                                    )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        #temp.Name = defaults.RfLevelName    # "PWR"
        #temp[ 'bg' ] = 'ivory'
        #temp[ 'to' ] = defaults.RfLevelMax
        #temp[ 'from_' ] = defaults.RfLevelMin
        #temp.Value = tk.DoubleVar()
        #temp.Value.set( defaults.RfLevelDefault )
        #temp[ 'textvariable' ] = temp.Value

        # EH for the up/down arrows
        #temp[ "command" ] = lambda : parent.SpinboxEH (PowerPanel.RfLevelBox)
        # EH for the return key
        #temp.bind( "<Return>", parent.SpinboxReturnEH )
        temp.Units = None   # is actuall 'dBm'
        PowerPanel.RfLevelBox = temp

        # ----- RF Level Actual -----
        temp = ttk.Label( self )
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        nextCol += 1

        temp[ 'anchor' ] = tk.CENTER
        #temp.Text = tk.StringVar()
        #temp[ 'textvariable' ] = temp.Text
        #temp.Text.set( "MHz" )
        temp[ 'text' ] = 'dBm'
        PowerPanel.RfLevelActual = temp

        nextCol = 0
        nextRow += 1

        # ---------------------
        # ----- RF Enable -----
        # ----- Label -----
        temp = ttk.Label( self, text="RF Enable " )
        temp.grid( column=nextCol, row=nextRow, sticky=tk.E )
        nextCol += 1
        temp[ 'anchor' ] = tk.E

        # ----- RF Enable Checkbox -----
        temp = MyWidgets.MyCheckbutton( self, defaults.RfEnableName,
                                        defaults.OffOn, defaults.RfEnableInitial )
        temp.grid( column=nextCol, row=nextRow, stick='EW', pady=2 )
        nextCol += 1
        PowerPanel.RfEnableBox = temp

        # ----- RF Enable Actual -----
        temp = ttk.Label( self )
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        temp[ 'anchor' ] = tk.CENTER
        nextCol += 1
        temp[ 'text' ] = PowerPanel.RfEnableBox.Value.get()
        PowerPanel.RfEnableActual = temp

        nextCol = 0
        nextRow += 1

        # ----------------------
        # ----- PDN Button -----
        # ----- Label -----
        temp = ttk.Label( self, text="Synth Power" )
        temp.grid( column=nextCol, row=nextRow, sticky=tk.EW )
        nextCol += 1
        temp[ 'anchor' ] = tk.E

        # ----- PDN Checkbox -----
        temp = MyWidgets.MyCheckbutton( self, defaults.PowerName,
                                        defaults.OffOn, defaults.PowerInitial )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        PowerPanel.powerBox = temp

        # ----- Power (PDN) Actual -----
        temp = ttk.Label( self )
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        temp[ 'anchor' ] = tk.CENTER
        nextCol += 1
        #temp.Text = tk.StringVar()
        #temp[ 'textvariable' ] = temp.Text
        #temp.Text.set( PowerPanel.powerBox.Value.get() )
        temp[ 'text' ] = PowerPanel.powerBox.Value.get()
        PowerPanel.powerActual = temp
