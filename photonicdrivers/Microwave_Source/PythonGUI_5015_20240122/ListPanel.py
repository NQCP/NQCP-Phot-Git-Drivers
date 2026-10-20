#   ListPanel
#   32 frequencies and RF Levels can be entered into the synthesizer
#   to be selected when it is not connected to a computer.

import tkinter as tk
from tkinter import ttk
from functools import partial
import MyWidgets

class ListPanel( ttk.Frame ):
    # Class Data
    listWidgets = []    # an empty list to hold [ Freq Widget, RF-Level Widget ] pairs

    # ----- Constructor -----
    def __init__( self, parent ):
        # Call the base constructor
        ttk.Frame.__init__( self, parent, borderwidth=5, relief=tk.GROOVE )
        self.parent = parent    # parent = Main window
        self.Name = "ListPanel"

        self.freq = 2400.0000
        self.RfLevel = 10
        CwDefaults = parent.defaults.CW()
        powerDefaults = parent.defaults.Power()

        """
        # Set the column widths
        colWidth = parent.labelColPixels >> 1
        self.columnconfigure( 0, minsize=10 )
        self.columnconfigure( 1, minsize=colWidth )
        self.columnconfigure( 2, minsize=colWidth )
        self.columnconfigure( 3, minsize=10 )
        self.columnconfigure( 4, minsize=colWidth )
        self.columnconfigure( 5, minsize=colWidth )
        """

        # The following is part of allowing the window to be resized.
        for ix in range( 18 ):
            self.rowconfigure( ix, weight=1 )

        self.columnconfigure( 0, weight=1 )
        self.columnconfigure( 1, weight=3 )
        self.columnconfigure( 2, weight=3 )
        self.columnconfigure( 3, weight=1 )
        self.columnconfigure( 4, weight=3 )
        self.columnconfigure( 5, weight=3 )

        nextCol = 0
        nextRow = 0

        # Print a row of labels at the top of the panel
        for ix in range( 2 ):
            temp = ttk.Label( self, text = "Num " )
            temp.grid( column=nextCol, row=nextRow, sticky='EW' )
            nextCol += 1
            #temp[ 'anchor' ] = tk.E

            temp = ttk.Label( self, text = "Freq" )
            temp.grid( column=nextCol, row=nextRow, sticky='E' )
            nextCol += 1

            temp = ttk.Label( self, text = "RF Level" )
            temp.grid( column=nextCol, row=nextRow, sticky='E' )
            nextCol += 1

        nextCol = 0
        nextRow += 1

        # Instantiate 32 widget pairs (ie. [ Freq number box, RF-Level Spinbox ]
        for rowIndex in range( 32 ):
            # ----- AInstantiate a customized Spinbox to hold the frequency value -----
            temp1 = MyWidgets.MyListBox( self, "List",
                                         CwDefaults.FreqMin, CwDefaults.FreqMax,
                                         self.freq )
            temp1.rowIndex = rowIndex
            self.freq += 10

            # ----- A number box for the RF Level -----
            temp2 = MyWidgets.MyListBox( self, "List",
                                        powerDefaults.RfLevelMin, powerDefaults.RfLevelMax,
                                        self.RfLevel )
            temp2.rowIndex = rowIndex
            temp2.Units = None

            ListPanel.listWidgets.append( [temp1, temp2] )

        # Display 16 lines with [Index] [[Freq SpinBox] [RF-Level SpinBox] | [Index] [[Freq SpinBox] [RF-Level SpinBox]
        # Rows 1 and 17 will appear on the top line, etc.
        for ix in range( 16 ):
            rowIndex = ix
            for ix2 in range( 2 ):
                # A label with an index between 1 and 32
                temp = ttk.Label( self, text = rowIndex + 1 )
                temp.grid( column=nextCol, row=nextRow, sticky='EW' )
                nextCol += 1
                temp[ 'anchor' ] = tk.CENTER

                widget1, widget2 = ListPanel.listWidgets[ rowIndex ]

                widget1.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
                nextCol += 1

                widget2.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
                nextCol += 1

                # ListPanel.listTriplet.append( (temp1, temp2, temp3) )
                # ListPanel.listTriplet.insert( rowIndex, ( rowIndex, temp1, temp2 ) )
                rowIndex += 16

            nextCol = 0
            nextRow += 1
