from __future__ import print_function
import sys
import serial
import serial.tools.list_ports
import time

class VSerialPort( serial.Serial ):

    portLines = []
    portLineCount = 0
    portLineIndex = 0
    
    def __init__( self, portParam=None ):
        # Call the base constructor
        serial.Serial.__init__( self )

        if ( portParam != None ):
            if ( self.isOpen() ):
                self.close()
            self.portList = [ portParam ]
        else:
            self.portList = []
            # serial.tools.list_ports.comports returns ListPortInfo objects
            # A ListPortInfo object contains port, dec, and hwid.
            for port, desc, hwid in serial.tools.list_ports.comports():
                print( 'Port: ', port, ' Desc: ', desc, ' HwId: ', hwid )

            for port, desc, hwid in serial.tools.list_ports.comports():
                if ( desc.find( "USB" ) != -1 ):
                    self.portList.append( port )

            if ( len( self.portList ) == 0 ):
                print( "No FTDI com ports are available" )
                return
        
        self.port = self.portList[ 0 ]
        self.timeout = 1.0
        self.baudrate = 9600
        self.open()

        print( "Trying 9600 Baud" )
        self.write( b'\r' )
        self.readAll()

        if ( len( self.portLines ) == 0 ):
            print( "No response.  Trying 115200")
            self.baudrate = 115200
            self.write( b'\r' )
            self.readAll()
            if ( len( self.portLines ) == 0 ):
                print( "Can't communicate with the synthesizer" )
                self.close()

        print( "Using " + self.port )
        self.changeBaudRate( 115200 )

        # ----- End of Constructor -----
                
    # -----------------------------------
    def writeline( self, text ):
        if ( not self.isOpen() ):
            return
        self.write( text.encode() + b'\r' )

    # -----------------------------------
    def readAll(self):
        del self.portLines[:]
        self.portLineCount = self.portLineIndex = 0

        if not self.isOpen():
            return

        text = self.readline()

        while True:
            sys.stdout.write(text.decode(errors='replace'))

            if not text:
                sys.stdout.flush()
                return

            self.portLines.append(text.decode(errors='replace'))
            self.portLineCount += 1

            if b'-->' in text:
                sys.stdout.flush()
                return

            text = self.readline()

    # -----------------------------------
    def lineGet( self ):
        """ Read from the array of previously-received lines of text """
        i = self.portLineIndex
        self.portLineIndex += 1
        if ( self.portLineIndex > self.portLineCount ):
            return ''
        return self.portLines[ i ]
    
    # -----------------------------------
    def changeBaudRate( self, rateParam ):
        if ( self.baudrate == rateParam ):
            return
        print( "Switching from ", self.baudrate, " to ", rateParam )
        oldRate = self.baudrate
        cmd = "Baud " + str( rateParam )
        print( cmd )
        self.writeline( cmd )
        # Read the echo of the Baud command
        self.readAll()

        # Now (we hope) we are communicating at the new rate
        self.baudrate = rateParam
        #time.sleep(1)
        self.write(b'\r')
        self.readAll()
        for ix in range( 3 ):
            if ( len(self.portLines) != 0 ):
                break
            time.sleep(0.2)
            self.readAll()
            print( "waiting..." )

        if (len(self.portLines) != 0):
            for line in self.portLines:
                print( line )
            print( 'Success at ', self.baudrate )
            return

        print( "Can't communicate at new baud rate" )
        print( "Trying " + str(oldRate) )
        self.baudrate = oldRate
        self.write(b'\r')
        self.readAll()
        if (len(self.portLines) != 0):
            for line in self.portLines:
                print( line )
            print( "Success at", self.baudrate )
            return

        print( "Can't communicate with the synthesizer" )
        self.close()

