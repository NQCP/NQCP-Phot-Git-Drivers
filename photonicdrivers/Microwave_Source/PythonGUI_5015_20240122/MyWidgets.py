from __future__ import print_function
import tkinter as tk
from tkinter import ttk
from functools import partial

class MySpinbox( tk.Spinbox ):

    def __init__( self, parent, name, min, max, initialValue ):
        tk.Spinbox.__init__( self, parent, from_=min, to=max )
    
        self.parent = parent
        self.Name = name
        self[ 'width' ] = 10
        self[ 'justify' ] = tk.RIGHT
        self[ 'bg' ] = 'ivory'
        self[ 'increment' ] = 1.0000
        self.Value = tk.DoubleVar()
        self.Value.set( initialValue )
        self[ 'textvariable' ] = self.Value
        self.Units = "MHz"
        # EH for the up/down arrows
        self[ 'command' ] = partial( parent.parent.SpinboxEH, self )
        #self.bind( '<Up>', parent.parent.SpinboxReturnEH )     # Works intermittantly
        #self.bind( '<Down>', parent.parent.SpinboxReturnEH )
        # EH for the return key
        self.bind( "<Return>", parent.parent.SpinboxReturnEH )


class MyListBox( tk.Spinbox ):
    def __init__( self, parent, name, min, max, initialValue ):
        tk.Spinbox.__init__( self, parent, from_=min, to=max )

        self.parent = parent
        self.Name = name
        self[ 'width' ] = 12
        self[ 'justify' ] = tk.RIGHT
        self[ 'bg' ] = 'ivory'
        self[ 'increment' ] = 1.0000
        self.Value = tk.DoubleVar()
        self.Value.set( initialValue )
        self[ 'textvariable' ] = self.Value
        self.Units = "MHz"
        # EH for the up/down arrows
        self[ 'command' ] = partial( parent.parent.ListBoxEH, self )
        # EH for the return key
        self.bind( "<Return>", parent.parent.ListBoxReturnEH )

class MyCombobox( ttk.Combobox ):
    def __init__( self, parent, name, choices, defaultIndex ):
        ttk.Combobox.__init__( self, parent, values=choices )
        #self.parent = parent
        self.Name = name
        self.Value = tk.StringVar()     # will be set in the event handler
        self.Value.set( "not set" )
        self.Text = tk.StringVar()
        self[ 'textvariable' ] = self.Text  # So the EH can fetch the selected entry
        self.current( defaultIndex )
        self.Units = None

class MyCheckbutton( ttk.Checkbutton ):
    def __init__( self, parent, name, values, initialIndex ):
        ttk.Checkbutton.__init__( self, parent )

        self.Name = name
        self.Values = values
        self.Value = tk.IntVar()
        self[ 'variable' ] = self.Value     # 0 or 1
        self.Value.set( initialIndex )
        self[ 'text' ] = self.Values[ self.Value.get() ]
        self.Units = None
        self.writeRegisters = True
        self[ 'style' ] = 'Green.TCheckbutton'
        self["command"] = partial(parent.parent.CheckbuttonEH, self)
