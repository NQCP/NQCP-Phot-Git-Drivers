#!/usr/bin/env python2

# V5015CM

from __future__ import print_function
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk
import time

import VSerialPort
import Menu
import MainWindow
import StatusBar
import Dall

#-------------------
class Main( tk.Tk ):
# -------------------
    """ This is the Top-Level window.
        It will house the menuBar, the mainWindow, the lockBar, and two status bars.
    """

    # Static data

    menuBar = None
    mainWindow = None
    lockBar = None  # Lock Indicator below the main window
    status1 = None  # Status bar for commands sent to the synthesizer
    status2 = None  # Status bar for replies from the synthesizer
    sp = None       # Serial Port object
    dall = None     # Issues the Display ALL command and parses the reply

    # ----- Main Constructor -----
    def __init__( self ):
        # Call the base constructor
        tk.Tk.__init__( self )
        self.Name = "Main"

        self.dallFile = None
        self.Children = None

        #ttk.Style().theme_use( 'clam' )
        #ttk.Style().theme_use( 'alt' )
        #ttk.Style().theme_use( 'vista' )
        #ttk.Style().theme_use( 'default' )
        ttk.Style().theme_use( 'classic' )

        ttk.Style().configure( "TFrame", background="ivory" )
        ttk.Style().configure( "TLabel", background="ivory" )
        ttk.Style().configure( "TCombobox", fieldbackground="ivory" )
        ttk.Style().configure( "TEntry", fieldbackground="ivory" )
        ttk.Style().configure( "TCheckbutton", background="ivory" )
        ttk.Style().configure( "TCheckbutton", activeforeground="ivory" )   # not working

        ttk.Style().configure( 'Green.TLabel', background="dark green", foreground="white" )

        ttk.Style().configure( 'Locked.TLabel', background="light green", foreground="black" )
        ttk.Style().configure( 'Unlocked.TLabel', background="red", foreground="white" )

        ttk.Style().configure( 'Locked.TEntry', background="light green", foreground="black" )
        ttk.Style().configure( 'Unlocked.TEntry', background="red", foreground="white" )

        ttk.Style().configure( 'Green.TEntry', fieldbackground="dark green", foreground="white" )

        ttk.Style().configure( 'Green.TCheckbutton', background='PaleGreen' )
        ttk.Style().configure( 'Red.TCheckbutton', background='MistyRose' )

        self.title('V5015 / V5019 Configuration Manager')
        self.bg = 'ivory'

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        ttk.Style().configure( "TFrame", background="ivory" )

        # Fetch the sp address from our caller
        #Main.sp = sp

        # Instantiate the "Dall" (Display All values) class
        # Do this before building the Menu Bar
        Main.dall = Dall.Dall( self )

        Main.menuBar = Menu.ValonMenu( self ) # based on tk.Menu
        self[ 'menu' ] = Main.menuBar

        # Instantiate the main window which contains the Mode Panel and Header Panel
        # and CW or Sweep Panel and Power Panel and Reference Frequency Panel
        Main.mainWindow = MainWindow.MainWindow( self )
        Main.mainWindow.grid( row=0, sticky='NSEW' )
        Main.menuBar.setMainWindowAddress( Main.mainWindow )

        Main.lockBar = StatusBar.LockBar( self )
        Main.lockBar.grid(  pady=2 )
        Main.lockBar.Name = "LockBar"

        Main.status1 = StatusBar.StatusBar( self )
        Main.status1.grid( pady=2, sticky='NSEW' )
        Main.status1.Name = "Status1"

        Main.status2 = StatusBar.StatusBar( self )
        Main.status2.grid( pady=2, sticky='NSEW' )
        Main.status2.Name = "Status2"

        Main.mainWindow.setStatusBarAddresses( Main.lockBar, Main.status1, Main.status2 )

        # Share the Dall object with mainWindow
        # Main.mainWindow.setClassAddresses( Main.dall )

        # Ask mainWindow to share its panel addresses
        Main.mainWindow.propagatePanelAddresses()

        if Main.sp.isOpen():
            Main.dall.statusQuery()
            Main.dall.dallQuery()
            Main.dall.listQueryCmd()
        else:
            Main.status2.set( "Synthesizer is offline" )

        #self.resizable( True,True )

        # ----- end of constructor -----

    # ----- Menu Event Handlers -----
    def fileLoadConfig( self ):
        """ Read DALL.txt and store its values into the widgets.
            Send new values to the synthesizer.
        """

        self.fileName = \
            askopenfilename( title="Select file",
                             filetypes=(("text files", "*.txt"), ("all files", "*.*"))
                           )

        if ( self.fileName == '' ):
            return

        dallFile = open( self.fileName, 'rU' )
        try:
            for line in dallFile:
                Main.dall.parseQueryLine( line )
        finally:
            dallFile.close()

    def fileSaveConfig( self ):
        self.fileName = \
            asksaveasfilename( title="Select file",
                             filetypes=(("text files", "*.txt"), ("all files", "*.*"))
                           )
        if ( self.fileName == '' ):
            return

        dallFile = open( self.fileName, 'w' )
        sp.writeline("DALL")
        sp.readAll()
        sp.lineGet()   #Discard the echo
        line = sp.lineGet()
        while ( line != "" ):
            if ( line[0:4] == "MAIN" ):
                pass
            line = line.rstrip()
            dallFile.write( line + '\n' )
            line = sp.lineGet()
        dallFile.close()

    def fileTelnet( self ):
        pass

    def synthReadRegisters( self ):
        Main.dall.dallQuery()

    def cycleThroughChildren( self, widget ):
        # Trigger widgets to send their values to the synthesizer.
        widgetClass = widget.winfo_class()
        if ( ( widgetClass == "TLabel" ) or
             (widgetClass == "Tk") or (widgetClass == "Menu") or
             (widgetClass == "TButton")
           ):
            pass
            #print( widgetClass, widget.Name )
        elif ( widgetClass == "TFrame" ):
            print( widgetClass, widget.Name )
        elif ( widgetClass == "TCombobox" ):
            #print( widgetClass, widget.Name )
            #widget.focus_set()
            #widget.event_generate( "<Return>" )
            #widget.event_generate( "<<ComboboxSelected>>" )
            Main.mainWindow.sendCommand( widget )
        elif ( widgetClass == "Spinbox" ):
            #print( widgetClass, widget.Name )
            #widget.focus_set()
            #widget.event_generate("<Return>")
            Main.mainWindow.sendCommand( widget )
        elif ( widgetClass == "TEntry" ):
            #print( widgetClass, widget.Name )
            #widget.focus_set()
            #widget.event_generate( "<Return>" )
            Main.mainWindow.sendCommand( widget )
        elif ( widgetClass == "TCheckbutton" ):
            #print( widgetClass, widget.Name )
            #widget.focus_set()
            #widget.event_generate("<Button-1>")
            if ( widget.writeRegisters ):
                Main.mainWindow.sendCommand( widget )
        else:
            print( widgetClass, widget.Name, " Unhandled" )
            pass

        self.Children = widget.winfo_children()
        count = len( self.Children )
        #print( count, " children")
        if ( count == 0 ):
            return
        for self.child in self.Children:
            self.cycleThroughChildren( self.child )
            #print( '-----' )

    def synthWriteRegisters( self ):
        # self is the top-level window.
        saveSuppressLockCheck = Main.mainWindow.suppressLockCheck
        Main.mainWindow.suppressLockCheck = True

        self.cycleThroughChildren( Main.mainWindow.headerPanel )
        self.cycleThroughChildren( Main.mainWindow.modePanel )

        if ( Main.mainWindow.visiblePanel == Main.mainWindow.CwPanel ):
            Main.mainWindow.invisiblePanel[0] = Main.mainWindow.sweepPanel
            Main.mainWindow.invisiblePanel[1] = Main.mainWindow.listPanel
        elif ( Main.mainWindow.visiblePanel == Main.mainWindow.sweepPanel ):
            Main.mainWindow.invisiblePanel[0] = Main.mainWindow.CwPanel
            Main.mainWindow.invisiblePanel[1] = Main.mainWindow.listPanel
        elif ( Main.mainWindow.visiblePanel == Main.mainWindow.listPanel ):
            Main.mainWindow.invisiblePanel[0] = Main.mainWindow.CwPanel
            Main.mainWindow.invisiblePanel[1] = Main.mainWindow.sweepPanel

        # cycleThroughChildren( panel ) requires that panel be visible
        self.cycleThroughChildren( Main.mainWindow.visiblePanel )

        Main.mainWindow.visiblePanel.grid_remove()
        Main.mainWindow.invisiblePanel[0].grid()
        self.cycleThroughChildren( Main.mainWindow.invisiblePanel[0] )
        Main.mainWindow.invisiblePanel[ 0 ].grid_remove()

        Main.mainWindow.invisiblePanel[1].grid()
        self.cycleThroughChildren( Main.mainWindow.invisiblePanel[1] )
        Main.mainWindow.invisiblePanel[ 1 ].grid_remove()
        Main.mainWindow.visiblePanel.grid()

        Main.mainWindow.suppressLockCheck = saveSuppressLockCheck
        Main.dall.lockQuery()

    def synthSelectEH( self, *args ):     # ie. args are accepted as a tuple
        """ If more that one USB/Serial device is connected, the user
            is prompted to choose which one to use.
        """
        widget = args[0]
        ix = args[1]
        mode = args[2]
        portName = Main.menuBar.synthSelection.get()

        if ( Main.sp.isOpen() ):
            Main.sp.close()
            time.sleep( 1 )

        # Instantiate a new serial port object
        #sp = Main.sp = VSerialPort.VSerialPort( portName )
        Main.sp = VSerialPort.VSerialPort( portName )

        # Share the new sp with other modules
        Main.mainWindow.setSpAddr( Main.sp )
        Main.dall.setSpAddr( Main.sp )

        if Main.sp.isOpen():
            Main.dall.statusQuery()
            Main.dall.dallQuery()
        else:
            Main.status2.set( "Synthesizer is offline" )

    def  panelSelectEH( self, modeParam ):
        headerLabel = Main.mainWindow.headerPanel.panelName
        if ( modeParam == 'CW'):
            if ( Main.mainWindow.visiblePanel == Main.mainWindow.cwPanel ):
                return

            Main.mainWindow.cwPanel.grid()
            Main.mainWindow.sweepPanel.grid_remove()
            Main.mainWindow.listPanel.grid_remove()

            if (Main.mainWindow.visiblePanel == Main.mainWindow.listPanel):
                Main.mainWindow.powerPanel.grid()
                Main.mainWindow.refPanel.grid()
                Main.mainWindow.headerPanel.actualLabel[ 'text' ] = "Actual"

            Main.mainWindow.visiblePanel = Main.mainWindow.cwPanel
            #Main.mainWindow.invisiblePanel = Main.mainWindow.sweepPanel
            headerLabel[ 'text' ]='Main (CW) Panel'
            # Main.mainWindow.listPanel.grid_remove()
        elif ( modeParam == 'Sweep'):
            if ( Main.mainWindow.visiblePanel == Main.mainWindow.sweepPanel ):
                return
            Main.mainWindow.cwPanel.grid_remove()
            Main.mainWindow.listPanel.grid_remove()
            Main.mainWindow.sweepPanel.grid()

            if (Main.mainWindow.visiblePanel == Main.mainWindow.listPanel):
                Main.mainWindow.powerPanel.grid()
                Main.mainWindow.refPanel.grid()
                Main.mainWindow.headerPanel.actualLabel[ 'text' ] = "Actual"

            Main.mainWindow.visiblePanel = Main.mainWindow.sweepPanel
            #Main.mainWindow.invisiblePanel = Main.mainWindow.cwPanel
            headerLabel[ 'text' ]='Sweep Panel'
        elif ( modeParam == 'List'):
            if ( Main.mainWindow.visiblePanel == Main.mainWindow.listPanel ):
                return
            Main.mainWindow.cwPanel.grid_remove()
            Main.mainWindow.sweepPanel.grid_remove()
            Main.mainWindow.powerPanel.grid_remove()
            Main.mainWindow.refPanel.grid_remove()
            Main.mainWindow.listPanel.grid()
            Main.mainWindow.visiblePanel = Main.mainWindow.listPanel
            headerLabel[ 'text' ] = 'List Panel'
            Main.mainWindow.headerPanel.actualLabel[ 'text' ] = ""

    # ----- end of Main class -----

if __name__ == "__main__":

    # Instantiate the Serial Port
    Main.sp = VSerialPort.VSerialPort('COM13')

    # instantiate our root class
    app = Main()

    # Wait for events
    app.mainloop()
    
