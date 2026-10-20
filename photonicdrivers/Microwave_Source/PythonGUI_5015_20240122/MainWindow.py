from __future__ import print_function
import tkinter as tk
from tkinter import ttk

import Defaults
import HeaderPanel
import ModePanel
import CwPanel
import SweepPanel
import ListPanel
import PowerPanel
import RefPanel

# Create a class that is derived from Frame
class MainWindow( ttk.Frame ):
    """
    The MainWindow is instantiated in the top-level window, in V5015CM.py.
    It houses the following panels:
    The top line is the Header Panel with three widgets.
        [Current Panel Name]    [Synthesizer Name]  ["Actual"]
    The second line is the Mode Panel.
            "Mode"  [Mode Selector]     [Current Mode]
    The third line is the top of the currently displayed panel.
        CW Panel or Sweep Panel or List Panel
    Next is the Power Panel.
        It is not displayed when the List Panel is active.
    Last is the Reference Panel
        It is also not displayed with the List Panel.
    """

    # Variables declared here are Class (ie. static) data
    # Some are copies of variables owned by the Main class.

    headerPanel = None      # <CW or Sweep or List>  <Source Name>  <Actual>
    modePanel = None
    cwPanel = None
    sweepPanel = None
    listPanel = None
    powerPanel = None
    refPanel = None

    sp = None               # serial port
    dall = None
    defaults = None

    visiblePanel = None     # This will be either the cwPanel or sweepPanel or listPanel
    invisiblePanel = [None, None]

    locked = False
    lockBox = None

    status1 = None
    status2 = None

    labelColPixels = 150

    # ----- MainWindow Constructor -----
    def __init__( self, parent ):
        # Call the base constructor
        ttk.Frame.__init__( self, parent, borderwidth=5, relief=tk.GROOVE )
        #tk.Frame.__init__( self, parent )
        self.parent = parent
        self.Name = "MainWindow"

        MainWindow.sp = parent.sp
        MainWindow.dall = parent.dall
        print( "MainWindow.dall = ", MainWindow.dall )

        # Variables declared here or in any other class method are instance data
        self.suppressCommands = False
        self.suppressLockCheck = False

        # Shipman says you need to call rowconfigure and columnconfigure on
        # both the toplevel window and the Main window and (I think)
        # all your frames to allow your window to be resized.  It works.

        # The following "resizable" attributes are true by default.
        # Note that it is not spelled "resizeable"
        # MainWindow.topLevel.resizable(True,True)

        # I assume we need a "rowconfigure" for each row
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        self.columnconfigure(0, weight=1)

        self.grid(sticky=tk.N + tk.S + tk.E + tk.W)

        self.bg = 'ivory'

        # Fetch the default values for the widgets
        MainWindow.defaults = Defaults.Defaults()

        rowNum = 0

        # Widgetss are instantiated by calling ModuleName.WidgetName
        # ModuleName may be <Filename>.py
        MainWindow.headerPanel = HeaderPanel.HeaderPanel( self )
        MainWindow.headerPanel.grid( row=rowNum, sticky='NESW' )
        rowNum += 1

        MainWindow.modePanel = ModePanel.ModePanel( self )
        MainWindow.modePanel.grid( row=rowNum, sticky='NESW' )
        rowNum += 1

        MainWindow.cwPanel = CwPanel.CwPanel( self )
        MainWindow.cwPanel.grid( row=rowNum, sticky='NSEW' )
        MainWindow.visiblePanel = MainWindow.cwPanel

        MainWindow.sweepPanel = SweepPanel.SweepPanel( self )
        # MainWindow.sweepPanel.grid( row=rowNum, sticky='NSEW' )
        # MainWindow.sweepPanel.grid_remove()
        #MainWindow.invisiblePanel[0] = MainWindow.sweepPanel

        MainWindow.listPanel = ListPanel.ListPanel( self )
        # MainWindow.listPanel.grid( row=rowNum, sticky='NSEW' )
        # MainWindow.listPanel.grid_remove()
        #MainWindow.invisiblePanel[1] = MainWindow.listPanel

        rowNum += 1

        MainWindow.powerPanel = PowerPanel.PowerPanel( self )
        MainWindow.powerPanel.grid( row=rowNum, sticky='NESW' )
        rowNum += 1

        MainWindow.refPanel = RefPanel.RefPanel( self )
        MainWindow.refPanel.grid( row=rowNum, sticky='NESW' )
        rowNum += 1

        MainWindow.cwPanel.freqBox.focus_set()

        #   ----- End of Main Window Constructor -----

    # Accept address of serial port from Main
    def setSpAddr( self, spAddr ):
        MainWindow.sp = spAddr

    def setStatusBarAddresses(self, lockBox, status1, status2 ):
        """ Called by Main() to pass addresses of its widgets. """
        MainWindow.lockBox = lockBox
        MainWindow.status1 = status1
        MainWindow.status2 = status2

    def setClassAddresses(self, dallAddr ):
        """ Called by Main() to propagate its dall object """
        MainWindow.dall = dallAddr

    def propagatePanelAddresses( self ):
        """
            Called by Main to pass some of our state to the Dall object
        """
        print( "MainWindow.propagatePanelAddresses" )
        print(  "self = ", self, "listPanel = ", MainWindow.listPanel, "MainWindow = ", self )
        MainWindow.dall.setPanelAddresses(  self,
                                            MainWindow.headerPanel,
                                            MainWindow.modePanel,
                                            MainWindow.cwPanel,
                                            MainWindow.sweepPanel,
                                            # MainWindow.listPanel,
                                            MainWindow.powerPanel,
                                            MainWindow.refPanel,
                                            MainWindow.lockBox,
                                            MainWindow.status1,
                                            MainWindow.status2
                                         )
        # print( "Returned from dall.setPanelAddresses" )
        # print ( "MainWindow.listPanel = ", MainWindow.listPanel, "Dall.listPanel = ", MainWindow.dall.listPanel )
        # MainWindow.listPanel,
        MainWindow.dall.listPanel = MainWindow.listPanel

    # ------------------------------
    def sendCommand( self, widget ):
        if ( self.suppressCommands ):
            return
        command = widget.Name
        value = widget.Value.get()
        units = widget.Units if widget.Units != None else ""
        if ( command == "HaltRun" ):    # Sweep "Run" and "Halt" have no parameters
            cmd = widget.Value.get()    # 'Run' or 'Halt'
        elif ( command == "TRGR" ):
            cmd = "TRGR"
        else:
            cmd = '{0} {1} {2}'.format( command, value, units )

        # Display the command on the status line
        if ( MainWindow.status1 != None ):
            MainWindow.status1.set( cmd )

        if ( not MainWindow.sp.isOpen() ):
            return

        MainWindow.sp.writeline( cmd )
        MainWindow.sp.readAll()
        line = MainWindow.sp.lineGet()      # the echo of the command
        line2 = MainWindow.sp.lineGet()
        if ( line2 == '\r-->' ):                # Some commands are not acknowledged.
            if ( ( cmd == "TRGR") or ( cmd == "HALT") or ( cmd == "RUN" )):
                MainWindow.dall.parseQueryLine( line )
            else:
                # SDN LN1 (maybe the only example) is not acknowledged by the firmware
                # If this never happened, the code will be simpler.
                print( "----- sendCommand: no acknowledgement to ", cmd )
                #raw_input( 'Press <enter> and document that this happens' )
                MainWindow.sp.writeline( command )  # Send a query to get the updated value
                MainWindow.sp.readAll()
                line = MainWindow.sp.lineGet()
                line = MainWindow.sp.lineGet()
                while ( line != "" ):
                    if ( line != '\r-->' ):
                        MainWindow.status2.set( line )
                        MainWindow.dall.parseQueryLine( line )
                    line = MainWindow.sp.lineGet()
        else:
            line = line2
            while ( line != "" ):
                if ( line != '\r-->' ):
                    MainWindow.status2.set( line )
                    MainWindow.dall.parseQueryLine( line )
                line = MainWindow.sp.lineGet()

        if not self.suppressLockCheck:
            MainWindow.dall.lockQuery()

    # ------------------------------
    def sendTextCommand( self, command ):
        if ( self.suppressCommands ):
            return

        # Display the command on the status line
        #if ( MainWindow.status1 != None ):
        MainWindow.status1.set( command )

        if ( not MainWindow.sp.isOpen() ):
            return

        MainWindow.sp.writeline( command )
        MainWindow.sp.readAll()
        line = MainWindow.sp.lineGet()      # the echo of the command
        line2 = MainWindow.sp.lineGet()

        MainWindow.status2.set( line2 )

        MainWindow.dall.dallQuery()

    # ----- Event Handlers -----

    def ComboboxIndexEH(self, event ):
        # eg. "REFS 0"
        # The widget's Value (ie. the command parameter it sends) will be a number.
        widget = event.widget
        widget.Value.set( widget.current() )
        self.sendCommand( widget )

    def ComboboxValueEH(self, event ):
        # Mode  (CW or Sweep)
        # TMode (Sweep Trigger Mode)
        # The widget's Value (ie. the command parameter it sends) will be
        # text from its "values" array.  eg "Mode CW"
        widget = event.widget
        widget.Value.set( widget.Text.get() )
        self.sendCommand( widget )

    def ComboboxCodeEH(self, event ):
        # Spur Mode
        # The widget's Value (ie. the command parameter it sends) will be
        # text from its "codes" array.  eg. "SDN LN1" sets spur noise reduction to "Low Noise"
        widget = event.widget
        ix = widget.current()
        widget.Value.set( widget.Codes[ ix ] )
        self.sendCommand( widget )

    # Spinbox EH for the up/down arrows
    def SpinboxReturnEH( self, event ):
        self.widget = event.widget
        print( "SpinBox EH, Event = ", event, "; Widget = ", self.widget.Name )
        self.sendCommand( self.widget )

    # Spinbox <Return> Key Event Handler
    def SpinboxEH( self, widgetParam ):
        print( "SpinBox Up/Down EH, widget = ", widgetParam.Name )
        self.sendCommand( widgetParam )

    # ListBox EH for the up/down arrows
    def ListBoxReturnEH( self, event ):
        freqWidget, powerWidget = ListPanel.ListPanel.listWidgets[ event.widget.rowIndex ]
        rowNumber = event.widget.rowIndex + 1
        freq = freqWidget.Value.get()
        units = freqWidget.Units if freqWidget.Units != None else ""
        power = powerWidget.Value.get()

        cmd = 'LIST {0} {1} {2} {3}'.format( rowNumber, freq, units, power )
        self.sendTextCommand( cmd )

    # ListBox <Return> Key Event Handler
    def ListBoxEH( self, widgetParam ):
        freqWidget, powerWidget = ListPanel.ListPanel.listWidgets[ widgetParam.rowIndex ]
        rowNumber = widgetParam.rowIndex + 1
        freq = freqWidget.Value.get()
        units = freqWidget.Units if freqWidget.Units != None else ""
        power = powerWidget.Value.get()
        cmd = 'LIST {0} {1} {2} {3}'.format( rowNumber, freq, units, power )
        self.sendTextCommand( cmd )

    def CheckbuttonEH( self, btn ):
        # RF Enable / Disable
        # Power Up / Down
        value = btn.Value.get()
        btn[ 'style' ] = ['Red.TCheckbutton', 'Green.TCheckbutton'][ value ]
        btn[ 'text' ] = btn.Values[ value ]
        self.sendCommand( btn )

    def RunHaltCheckbuttonEH( self, btn ):
        # Sweep run / halt
        value = btn.Value.get()
        self.sendCommand( btn )

    def EntryEH( self, event ):
        widget = event.widget
        #print( "Entry EH ", event, "; Widget = ", widget, " Name = ", widget.Name )
        if ( widget.Name != None ):
            self.sendCommand( event.widget )

    def ButtonEH( self, btn ):
        self.sendCommand( btn )

"""
    def OptionMenuEH(self, widget, *args):
        # Some 5015 commands take text.  Others take an index.
        # Widgets for commands that take text will store text in widget.Value.
        # Widgets for commands that take an index will store text
        # in widget.Text, with the index in Widget.Value
        # Here, we turn text into an index, for commands that need one.
        if ((widget.Text != None) and (widget.TextValues != None)):
            text = widget.Text.get()
            widget.Value.set(widget.TextValues.index(text))
        self.sendCommand( widget )
"""


#   End of Main Window Class
        
