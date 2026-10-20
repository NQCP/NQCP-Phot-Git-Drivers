"""
The Dall class parses input from the synthesizer DALL command,
and copies the values to the GUI widgets.
"""

from __future__ import print_function
import tkinter as tk
import Defaults

class Dall:

    # Class data
    sp = None
    mainWindow = None
    headerPanel = None    # <CW or Sweep or List>  <Source Name>  <Actual>
    cwPanel = None
    sweepPanel = None
    listPanel = None
    modePanel = None
    powerPanel = None
    refPanel = None
    lockBox = None
    status1 = None
    status2 = None

    sub1 = None
    sub2 = None
    mainSynth = None
    locked = None

    # ----- Dall Constructor -----
    def __init__( self, parent ):
        """ Sends the DALL command, and parses the reply,
        and sets values for all widgets
        """
        self.parent = parent
        Dall.sp = parent.sp
        Dall.defaults = Defaults.Defaults()
        # ----- end Dall Constructor -----

    # ----- setPanelAddresses -----
    # mainWindow shares these addresses with the Dall class
    def setPanelAddresses( self, mainAddr, headerAddr, modeAddr,
                           cwAddr, sweepAddr,
                           # listAddr,
                           powerAddr, refAddr, lockBoxAddr,
                           status1Addr, status2Addr
                         ):
        Dall.mainWindow = mainAddr
        Dall.headerPanel = headerAddr
        Dall.modePanel = modeAddr
        Dall.cwPanel = cwAddr
        Dall.sweepPanel = sweepAddr
        # Dall.listPanel = listAddr
        Dall.powerPanel = powerAddr
        Dall.refPanel = refAddr
        Dall.lockBox = lockBoxAddr
        Dall.status1 = status1Addr
        Dall.status2 = status2Addr

        Dall.listPanel = Dall.mainWindow.listPanel
        print( "Dall.listPanel = ", Dall.listPanel, "Dall.mainWindow.listPanel = ", Dall.mainWindow.listPanel )

    # ----- setSpAddr -----
    #   Called when a different synthesizer is selected via Synthesizer / Select menu
    def setSpAddr( self, spAddr ):
        if ( Dall.sp != spAddr ):
            print( "Changing Dall.sp from ", Dall.sp, " to ", spAddr )
            Dall.sp = spAddr
        else:
            print( "Dall.sp not changed")

    """
    # Debugging code
    def querySpAddr( self ):
        print( "Dall.sp (from querySpAddr): ", Dall.sp )
    """

    # ----- Convert other units to MHz -----
    def megahertz(self, n, units):
        if (units == "MHz"):
            return n
        elif (units == "KHz"):
            return n * 1000
        elif (units == "GHz"):
            return n / 1000
        else:
            print("Invalid value ", n, " ", units)
            return -1

    # ----- parseQueryLine -----
    # Move values from a line of DALL output to the appropriate widget
    def parseQueryLine( self, queryLine ):
        if ( queryLine == '\n' ):
            return
        value = -1
        queryLine = queryLine.replace( ';', '' )
        seg = queryLine.split()

        seg0 = seg[ 0 ].upper()

        if ( seg0 == 'DALL' ):
            return
        elif (seg0 == '-->'):
            return
        elif ( seg0 == 'NAME' ):
            # NAME 375
            # NAME
            widget = Dall.mainWindow.headerPanel.sourceName
            if ( len( seg ) > 1 ):
                widget.Value.set( seg[ 1 ] )
            else:
                widget.Value.set( "Source" )
        elif ( seg0 == 'F' ):
            #  F 2440 MHz; // Act 2440 MHz
            #widget = MainWindow.cwPanel.freqBox
            widget = Dall.cwPanel.freqBox
            if ( seg[2] == "MHz" ):
                value = seg[1]
            else:
                value = self.megahertz( seg[1], seg[2] )
            widget.Value.set( value )
            widget2 = Dall.cwPanel.freqActual
            widget2[ 'text' ] = seg[ 5 ] + ' ' + seg[ 6 ]
        elif ( seg0 == 'OFFSET' ):
            # OFFSET 0 MHz;
            widget = Dall.mainWindow.cwPanel.freqOffsetBox
            if ( seg[2] == "MHz"):
                value = seg[1]
            else:
                value = self.megahertz( seg[1], seg[2] )
            widget.Value.set( value )
            widget2 = Dall.cwPanel.freqOffsetActual
            #widget2.Text.set( seg[1] + ' ' + seg[2] )
            widget2[ 'text' ] = seg[1] + ' ' + seg[2]
        elif ( seg0 == 'FSTEP' ):
            #  FSTEP 10 MHz;
            widget = Dall.cwPanel.freqStepBox
            if (seg[2] == "MHz"):
                value = seg[1]
            else:
                value = self.megahertz( seg[1], seg[2] )
            widget.Value.set( value )
            Dall.cwPanel.freqBox['increment'] = value

            widget2 = Dall.cwPanel.freqStepActual
            # widget2.Text.set( seg[1] + ' ' + seg[2] )
            widget2[ 'text' ] = seg[1] + ' ' + seg[2]
        elif ( seg0 == 'START' ):
            # START 23 MHz; // Act 23 MHz
            widget = Dall.sweepPanel.startFreqBox
            value = self.megahertz(seg[1], seg[2])
            widget.Value.set( value )
            widget2 = Dall.sweepPanel.startFreqActual
            widget2[ 'text' ] = seg[5] + ' ' + seg[6]
        elif (seg0 == 'STOP'):
            # STOP 6000 MHz; // Act 6000 MHz
            widget = Dall.sweepPanel.stopFreqBox
            value = self.megahertz(seg[1], seg[2])
            widget.Value.set( value )
            widget2 = Dall.sweepPanel.stopFreqActual
            widget2[ 'text' ] = seg[5] + ' ' + seg[6]
        elif (seg0 == 'STEP'):
            # STEP 1 MHz;
            widget = Dall.sweepPanel.stepFreqBox
            value = self.megahertz(seg[1], seg[2])
            widget.Value.set( value )
            widget2 = Dall.sweepPanel.stepFreqActual
            widget2[ 'text' ] = seg[1] + ' ' + seg[2]
        elif (seg0 == 'RATE'):
            # RATE 1000; // ms
            widget = Dall.sweepPanel.rateBox
            value = seg[1]
            widget.Value.set( value )
            widget2 = Dall.sweepPanel.rateActual
            widget2[ 'text' ] = seg[1] + ' ' + seg[3]
        elif (seg0 == 'RTIME'):
            # RTIME 0; // ms
            widget = Dall.sweepPanel.retraceBox
            value = seg[1]
            widget.Value.set( value )
            widget2 = Dall.sweepPanel.retraceActual
            widget2[ 'text' ] = value + ' ' + seg[3]
        elif ( seg0 == 'TMODE' ):
            # TMODe AUTO;
            widget = Dall.sweepPanel.triggerModeBox
            widget.set( seg[1] )
            widget.Value.set( seg[1] )
            widget2 = Dall.sweepPanel.triggerBtn
            widget3 = Dall.sweepPanel.triggerActual
            if ( widget.current() == 1 ):
                widget2[ 'state' ] = tk.NORMAL
                widget3[ 'text' ] = "Enabled"
            else:
                widget2[ 'state' ] = tk.DISABLED
                widget3[ 'text' ] = "Disabled"

            widget4 = Dall.sweepPanel.triggerModeActual
            widget4[ 'text' ] = seg[1]

        elif ( seg0 == 'HALT' ):
            # HALT
            # todo: should set the Sweep haltRun Checkbutton
            widget = Dall.sweepPanel.haltRunBtn
            widget.Value.set( seg0 )
            widget[ 'text' ] = widget.Values[ 1 ]   # Run
            widget2 = Dall.sweepPanel.haltRunActual
            widget2[ 'text' ] = widget.States[ 0 ]
        elif (seg0 == 'RUN'):
            # RUN
            widget = Dall.sweepPanel.haltRunBtn
            widget.Value.set( seg0 )
            widget[ 'text' ] = widget.Values[ 0 ]  # Halt
            widget2 = Dall.sweepPanel.haltRunActual
            widget2[ 'text' ] = widget.States[ 1 ]  # "Running"
        elif ( seg0 == 'TRGR' ):
            pass
        elif ( seg0 == 'REFTRIM' ):
            pass    # No longer displayed by the GUI
        elif ( seg0 == 'PWR' ):
            # PWR 1.00;  // dBm
            widget = Dall.powerPanel.RfLevelBox
            widget.Value.set( seg[1] )
            widget2 = Dall.powerPanel.RfLevelActual
            #widget2.Text.set ( seg[1] + ' ' + seg[ 3 ] )
            widget2[ 'text' ] = seg[1] + ' ' + seg[ 3 ]
        elif ( seg0 == 'ATT' ):
            pass    # Replaced by RF level, but still present in DALL
            #  ATT 15.0; // dB
            #widget = MainWindow.cwPanel.attBox
            #widget.Value.set( seg[ 1 ] )
            #widget = MainWindow.cwPanel.attActual
            #if ( len( seg ) == 4 ):
            #    widget.Text.set( seg[ 3 ] )
            #elif ( len( seg ) == 5 ):
            #    widget.Text.set( seg[ 3 ] + ' ' + seg[ 4 ] )
            #else:
            #    pass

        elif ( seg0 == 'SDN' ):
            # SDN LN1
            widget = Dall.cwPanel.spurModeBox
            try :
                spurIx = widget.Codes.index( seg[1] )
            except ValueError as err:
                print( "Invalid Spur Mode Code - ", seg[1] )
                spurIx = -1
                return
            widget.current( spurIx )
            widget.Value.set( seg[1] )
            widget2 = Dall.cwPanel.spurModeActual
            #widget2.Text.set( widget.Codes[ widget.current() ] )
            widget2[ 'text' ] = seg[1]
        elif (seg0 == 'CP'):
            # CP 7; // charge-pump current = 15 mA
            pass
        elif ( seg0 == 'PDN' ):
            #  PDN 1
            widget = Dall.powerPanel.powerBox
            widget.Value.set( seg[ 1 ] )
            widget[ 'text' ] = widget.Values[ widget.Value.get() ]
            widget2 = Dall.powerPanel.powerActual
            #widget2.Text.set( seg[0] + ' ' + seg[ 1 ] )
            widget2[ 'text' ] = seg[0] + ' ' + seg[ 1 ]
        elif ( seg0 == 'OEN' ):
            #  OEN 1
            widget = Dall.powerPanel.RfEnableBox
            widget.Value.set( seg[ 1 ] )
            widget[ 'text' ] = widget.Values[ widget.Value.get() ]
            widget2 = Dall.powerPanel.RfEnableActual
            #widget2.Text.set( seg[0] + ' ' + seg[ 1 ] )
            widget2[ 'text' ] = seg[0] + ' ' + seg[ 1 ]

        elif ( seg0 == 'MODE' ):
            #  MODE CW;
            widget = Dall.modePanel.modeBox
            value = seg[1]
            try:
                ix = Dall.defaults.Mode.ModeValues.index( value )
            except:
                print( "Bad Mode value")
                ix = -1

            if ( 0 <= ix <= 2 ):
                # Set Mode Panel Mode-Selector-Index to the new value
                widget.current( ix )
                widget.Value.set( seg[1] )

                # Set Mode Panel Actual Text to the new Mode Name
                widget = Dall.modePanel.modeActual
                widget[ 'text' ] = seg[1]

                # Change the Panel Name in the Header Panel
                widget = Dall.headerPanel.panelName
                widget[ 'text' ] = seg[ 1 ]

                # Switch to the panel that is appropriate for the new Mode
                widget0 = Dall.mainWindow.cwPanel
                widget1 = Dall.mainWindow.sweepPanel
                widget2 = Dall.mainWindow.listPanel
                if ( ( ix == 0 ) and ( Dall.mainWindow.visiblePanel != widget0 ) ):     # CW Mode
                    widget0.grid()
                    widget1.grid_remove()
                    widget2.grid_remove()
                    Dall.mainWindow.visiblePanel = widget0
                    Dall.mainWindow.invisiblePanel[0] = widget1
                    Dall.mainWindow.invisiblePanel[1] = widget2
                elif ( ( ix == 1 ) and ( Dall.mainWindow.visiblePanel != widget1 ) ):   # Sweep Mode
                    widget0.grid_remove()
                    widget1.grid()
                    widget2.grid_remove()
                    Dall.mainWindow.visiblePanel = widget1
                    Dall.mainWindow.invisiblePanel[0] = widget0
                    Dall.mainWindow.invisiblePanel[1] = widget2
                elif ( ( ix == 2 ) and ( Dall.mainWindow.visiblePanel != widget2 ) ):   # List Mode
                    widget0.grid_remove()
                    widget1.grid_remove()
                    widget2.grid()
                    Dall.mainWindow.visiblePanel = widget2
                    Dall.mainWindow.invisiblePanel[0] = widget0
                    Dall.mainWindow.invisiblePanel[1] = widget1

        elif ( seg0 == 'AMF' ):
            # AMF 1 kHz
            widget = Dall.cwPanel.AmFreqBox
            widget.Value.set( seg[1] )
            widget2 = Dall.cwPanel.AmFreqActual
            widget2[ 'text' ] = seg[1] + ' ' + seg[2]
        elif ( seg0 == 'AMD' ):
            # AMD 0.0 dB
            widget = Dall.cwPanel.AmModulationBox
            widget.Value.set( seg[1] )
            widget2 = Dall.cwPanel.AmModulationActual
            #widget2.Text.set( seg[1] + ' ' + seg[2] )
            widget2[ 'text' ] = seg[1] + ' ' + seg[2]
        elif ( seg0 == 'HALT' ):
            pass
        elif ( seg0 == 'REFS' ):
            # REFS 0;
            widget = Dall.refPanel.refSourceBox
            try:
                index = int(seg[1])
            except ValueError:
                return  # or ignore line

            if index < 0 or index > 1:
                return
            widget.current( index )
            widget.Value.set( index )
            #widget.Text.set( widget.TextValues[ index ] )
            widget = Dall.refPanel.refSourceActual
            widget.config(text=seg0 + ' ' + seg[ 1 ])           
        elif ( seg0 == "REF" ):
            # REF 10 MHz;
            widget = Dall.refPanel.refFreqBox
            widget.Value.set( seg[ 1 ] )
            widget2 = Dall.refPanel.refFreqActual
            #widget.Text.set( seg[ 1 ] + ' ' + seg[ 2 ] )
            widget2[ 'text' ] = seg[ 1 ] + ' ' + seg[ 2 ]
        elif ( seg0 == 'REFT10' ):
            pass
        elif ( seg0 == 'SUB1' ):
            # SUB1       :     locked
            Dall.sub1 = ( seg[2] == 'locked')
        elif ( seg0 == 'SUB2' ):
            # SUB2       :     locked
            Dall.sub2 = ( seg[2] == 'locked')
        elif ( seg0 == 'MAIN'):
            # MAIN SYNTH :     locked
            Dall.mainsynth = ( seg[3] == 'locked')
            #Dall.mainWindow.locked = Dall.locked = ( Dall.sub1 and Dall.sub2 and Dall.mainsynth )
            Dall.locked = (Dall.sub1 and Dall.sub2 and Dall.mainsynth)
        else:
            print( "Unhandled DALL entry: ", queryLine )
            print( queryLine )
    # end parseQueryLine

    # ----- lockQuery -----
    def lockQuery( self ):
        """ lockQuery determines the "locked" value of the synthesizer,
            and updates the lockBox indicator on the window.
        """
        Dall.sp.writeline( "lock" )
        Dall.sp.readAll()

        Dall.sp.lineGet()   #  Discard the echo
        queryLine = Dall.sp.lineGet()
        while ( queryLine != '' ):
            if ( queryLine != '\r-->' ):
                self.parseQueryLine(queryLine)
            queryLine = Dall.sp.lineGet()
        Dall.lockBox.set( Dall.locked )

    # ----- status Query -----
    def statusQuery( self ):
        """ Fetch the Synthesizer's status and update the status bar """
        Dall.status1.set( "Status" )
        Dall.sp.writeline( "status" )
        Dall.sp.readAll()
        Dall.sp.lineGet()   # Discard the echo
        queryLine = Dall.sp.lineGet()
        # Display only the first line of the synthesizer's output
        lineCount = 1
        while( queryLine != '' ):
            if ( lineCount == 1 ):
                Dall.status2.set( queryLine )
            queryLine = Dall.sp.lineGet()
            lineCount += 1

    # ----- dallQuery -----
    def dallQuery( self ):
        """ This procedure issues the DALL command and
            calls parseQueryLine to update values in the widgets.
            parseQueryLine also determines the 'locked' state.
        """
        # As we write initial values to the widgets, don't let them
        #  send their "new" values back to the synthesizer!
        saveSuppressCommands = Dall.mainWindow.suppressCommands
        self.suppressCommands = True

        # Fetch the synthesizer's register values
        Dall.sp.writeline("DALL")
        Dall.sp.readAll()

        # Parse the register values and store them into our widgets
        Dall.sp.lineGet()   #Discard the echo

        queryLine = Dall.sp.lineGet()
        while ( queryLine != '' ):
            if ( queryLine != '\r-->' ):
                self.parseQueryLine(queryLine)
            queryLine = Dall.sp.lineGet()
        Dall.lockBox.set( Dall.locked )
        self.suppressCommands = saveSuppressCommands

    # ----- listQuery -----
    def listQueryCmd( self ):
        """ This procedure issues the LIST query and
            parses result to update values in the widgets.
            Sample output from 5015:
            seg 1   2  3    4     5
                LI  1 2401 MHz  10.00; // Act 2401 MHz
        """

        saveSuppressCommands = Dall.mainWindow.suppressCommands
        self.suppressCommands = True

        # Fetch the synthesizer's LIST values
        # Expect 32 lines of output
        Dall.sp.writeline( "LIST" )
        Dall.sp.readAll()

        # Discard the echo
        Dall.sp.lineGet()

        queryLine = Dall.sp.lineGet()
        while (queryLine != ''):
            if (queryLine == '\r-->'):
                queryLine = Dall.sp.lineGet()
                continue

            queryLine = queryLine.replace( ';', '' )
            seg = queryLine.split()
            seg0 = seg[ 0 ].upper()
            if (seg0 != 'LI'):
                print( "Unexpected LIST COMMAND output\b", seg0 )
                continue

            rowIndex = int( seg[ 1 ] )
            """ 
            if ( rowIndex == 32 ):  for debugging
                print( rowIndex )
            """
            freq = self.megahertz( seg[ 2 ], seg[ 3 ] )
            power = seg[ 4 ]

            listWidgets = Dall.listPanel.listWidgets[ rowIndex - 1 ]

            freqWidget, powerWidget = listWidgets

            freqWidget.Value.set( freq )
            powerWidget.Value.set( power )

            queryLine = Dall.sp.lineGet()

        self.suppressCommands = saveSuppressCommands
