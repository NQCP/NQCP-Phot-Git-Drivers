# ----- Reference Panel -----
#   Reference Source    Combobox
#   Reference Frequency SpinBox

from __future__ import print_function
import tkinter as tk
from tkinter import ttk

import MyWidgets

# -------------------------
class RefPanel( ttk.Frame ):
    # Static data
    refSourceBox = None
    refSourceActual = None

    refFreqBox = None
    refFreqActual = None

    # ----- Constructor -----
    def __init__(self, parent):
        # Call the base constructor
        ttk.Frame.__init__( self, parent, borderwidth=5, relief=tk.GROOVE )
        self.parent = parent
        self.Name = "RefPanel"

        self.columnconfigure( 0, minsize= parent.labelColPixels )
        self.columnconfigure( 1, minsize= parent.labelColPixels )
        self.columnconfigure( 2, minsize= parent.labelColPixels )

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        #self["bg"] = 'ivory'
        defaults = parent.defaults.Reference()

        nextCol = 0
        nextRow = 0

        # ----- Reference Source Selector -----
        # ----- Col-1 Label -----
        temp = ttk.Label(self, text='Ref Source ')
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        nextCol += 1
        temp[ 'anchor' ] = tk.E

        # ---------------------------------
        # ----- Ref Source Combobox -------
        # ---------------------------------
        #temp = ttk.Combobox( self )
        temp = MyWidgets.MyCombobox( self, defaults.RefSourceName,  # "Refs"
                                     defaults.RefSourceValues,      # ('Internal', 'External')
                                     defaults.RefSourceDefault
                                    )
        temp.grid( column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        temp.Value.set( temp.current() )
        temp.bind('<<ComboboxSelected>>', parent.ComboboxIndexEH)
        temp.bind("<Return>", parent.ComboboxIndexEH)
        RefPanel.refSourceBox = temp

        # Ref Source Actual
        temp = ttk.Label(self)
        temp.grid(column=nextCol, row=nextRow, sticky='EW' )
        nextCol += 1
        temp[ 'anchor' ] = tk.CENTER
        temp[ 'text' ] = RefPanel.refSourceBox.Text.get()
        RefPanel.refSourceActual = temp

        nextCol = 0
        nextRow += 1

        # -------------------------------------
        # ----- Col-1 Reference Frequency -----
        # -------------------------------------
        temp = ttk.Label(self, text="Ref Freq ")
        temp.grid( column=nextCol, row=nextRow, sticky='EW' )
        nextCol += 1
        temp[ 'anchor' ] = tk.E

        # ----- Ref Freq Box -----
        # REF
        temp = MyWidgets.MySpinbox( self, defaults.RefFreqName,
                                    defaults.RefFreqMin, defaults.RefFreqMax,
                                    defaults.RefFreqDefault
                                    )
        temp.grid(column=nextCol, row=nextRow, pady=2, sticky='EW' )
        nextCol += 1
        #temp.Name = defaults.RefFreqName    # "REF"
        #temp['bg'] = 'ivory'
        #temp['to'] = defaults.RefFreqMax    # 100
        #temp['from_'] = defaults.RefFreqMin # 5
        #temp.Value = tk.DoubleVar()
        #temp.Value.set( defaults.RefFreqDefault )    # 10
        #temp['textvariable'] = temp.Value
        #temp['increment'] = 1

        # EH for up/down arrows
        #temp[ "command" ] = lambda : parent.SpinboxEH (RefPanel.refFreqBox)
        # EH for the return key
        #temp.bind( "<Return>", parent.SpinboxReturnEH )
        RefPanel.refFreqBox = temp

        # ----- Ref Freq Actual -----
        temp = ttk.Label( self )
        temp.grid(column=nextCol, row=nextRow)
        nextCol += 1
        #temp.Text = tk.StringVar()
        #temp['textvariable'] = temp.Text
        #temp.Text.set( self.refFreqBox.Value.get() )
        temp[ 'text' ] = self.refFreqBox.Value.get()
        RefPanel.refFreqActual = temp

        nextCol = 0
        nextRow += 1

