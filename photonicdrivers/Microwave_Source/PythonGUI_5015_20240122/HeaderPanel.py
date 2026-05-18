# ----- TopLabelPanel -----

from __future__ import print_function
import tkinter as tk
from tkinter import ttk

# ----- A row of Labels at the top of the Main Window
#   <Panel Name>     <Source Name>     <"Actual">

class HeaderPanel( ttk.Frame ):
    # Class data
    panelName = None        # Label
    panelNameText = None    # textvariable

    sourceName = None       # Entry
    #sourceNameText = None   # textvariable

    actualLabel = None      # A label that is displayed except when the ListPanel is active

    # ----- Constructor -----
    def __init__( self, parent ):
        ttk.Frame.__init__( self, parent, borderwidth=5, relief=tk.GROOVE )
        self.parent = parent
        self.Name = "HeaderPanel"
        #self.width = parent.labelColWidth * 2 + parent.widgetColWidth
        #self[ 'bg' ] = 'ivory'
        nextCol = 0
        nextRow = 0

        self.columnconfigure( 0, weight=1, minsize= parent.labelColPixels )
        self.columnconfigure( 1, weight=1, minsize= parent.labelColPixels )
        self.columnconfigure( 2, weight=1, minsize= parent.labelColPixels )

        #-----------------------------------
        # Panel Name ( CW or Sweep or List )
        # ----------------------------------
        label = ttk.Label( self )
        label[ 'style' ] = 'Green.TLabel'
        label.grid( column = nextCol, row = 0, pady=2, ipady=2, sticky='EW' )
        label[ 'anchor' ] = tk.CENTER
        nextCol += 1

        label[ 'text' ] = 'Main (CW) Panel'
        HeaderPanel.panelName = label

        # -----------------------
        # ----- Source Name -----
        # -----------------------
        # You can assign a unique name to your synthesizer.
        # Maybe "Lab321"
        # The name is displayed on all panels
        # Perhaps this will prevent someone from doing a full reset on the wrong synthesizer.
        temp = ttk.Entry( self, text="Source" )
        temp.grid( column = nextCol, row = 0, padx=2, sticky='EW' )
        nextCol += 1

        temp.Name = 'Name'
        temp.Units = None
        temp[ 'style' ] = 'Green.TEntry'     # Green background
        temp.Value = tk.StringVar()
        temp[ 'textvariable' ] = temp.Value
        temp.Value.set( 'Source' )
        temp.bind( '<Return>', parent.EntryEH )
        HeaderPanel.sourceName = temp

        # ----- Actual Value Label -----
        label = ttk.Label( self, text="Actual" )
        label.grid( column = nextCol, row = 0, pady=2, ipady=2, sticky='EW' )
        label[ 'anchor'] = tk.CENTER
        label[ 'style' ] = 'Green.TLabel'
        HeaderPanel.actualLabel = label

