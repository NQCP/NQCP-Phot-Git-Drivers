from __future__ import print_function
import tkinter as tk
from tkinter import ttk

class StatusBar( ttk.Frame ):
    """ Two of these status bars are instantiated at the bottom of the Main window. """

    def __init__(self, parent ):
        ttk.Frame.__init__(self, parent, borderwidth=5, relief = tk.GROOVE )
        self.parent = parent    # The Top-level window

        self.columnconfigure(0, minsize=self.parent.mainWindow.labelColPixels * 3 )

        self.entry = ttk.Entry( self )
        self.entry.Name = None
        self.entry.Text = tk.StringVar()
        self.entry[ 'textvariable' ] = self.entry.Text
        #self.label[ 'anchor' ] = tk.W
        self.entry.grid( sticky='EW' )

    def set(self, arg ):
        #self.label.config(text=format % args)
        #self.label.config( text=arg )
        self.entry.Text.set( arg )

    def clear(self):
        self.label.config(text="")

# --------------------------
class LockBar( ttk.Frame ):
    """ Reports the Lock status of the synthesizer """

    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.label = ttk.Label(self, width=12, relief=tk.GROOVE, borderwidth=5 )
        self.label.grid()

    def set(self, bool ):
        #self.label.config( text= ( " Locked " if bool else " Not Locked " ) )
        self.label[ 'text' ] = ( " Locked " if bool else " Not Locked " )
        self.label[ 'style' ] = ( 'Locked.TLabel' if bool else 'Unlocked.TLabel' )
