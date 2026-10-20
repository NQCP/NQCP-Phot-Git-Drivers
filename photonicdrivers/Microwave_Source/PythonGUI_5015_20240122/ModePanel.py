# ----- Mode Panel -----
#   Contains a row of labels at the top
#   Mode Selector   Combobox

from __future__ import print_function
import tkinter as tk
from tkinter import ttk

import MyWidgets

class ModePanel( ttk.Frame ):

    # Class data
    #modeOptions = ( 'CW', 'Sweep', 'List' )
    modeBox = None  # mode = CW or Sweep or List
    modeValue = None

    modeActual = None

    # ----- Constructor -----
    def __init__( self, parent ):
        # Call the base constructor
        ttk.Frame.__init__(self, parent, borderwidth=5, relief=tk.GROOVE)
        self.parent = parent  # parent = mainWindow
        self.Name = "ModePanel"

        self.columnconfigure( 0, weight=1 )
        self.columnconfigure( 1, weight=1 )
        self.columnconfigure( 2, weight=1 )

        self.columnconfigure( 0, minsize = parent.labelColPixels )
        self.columnconfigure( 1, minsize = parent.labelColPixels )
        self.columnconfigure( 2, minsize = parent.labelColPixels )

        defaults = parent.defaults.Mode()
        nextCol = 0

        # ----- Mode (CW, Sweep, List) -----
        # ----- Label -----
        temp = ttk.Label(self, text="Mode")
        temp.grid( column=nextCol, row=0, sticky='EW' )
        temp[ 'anchor'] = tk.CENTER
        nextCol += 1

        # ----- Mode Selector Combobox -----
        # Instantiate the Mode menu
        temp = MyWidgets.MyCombobox( self, defaults.ModeName,
                                        defaults.ModeValues,
                                        defaults.ModeDefault
                                   )
        temp.grid(column=nextCol, row=0, sticky='EW', pady=2 )
        nextCol += 1
        temp.bind( "<<ComboboxSelected>>", parent.ComboboxValueEH )
        temp.bind( "<Return>", parent.ComboboxValueEH )
        ModePanel.modeBox = temp

        # Mode Actual
        temp = ttk.Label(self)
        temp.grid( column=nextCol, row=0 )
        nextCol += 1

        temp[ 'anchor' ] = tk.CENTER
        #temp.Text = tk.StringVar()
        #temp["textvariable"] = temp.Text
        #temp.Text.set( ModePanel.modeBox.Text.get() )
        temp[ "text" ] = ModePanel.modeBox.Text.get()
        ModePanel.modeActual = temp
