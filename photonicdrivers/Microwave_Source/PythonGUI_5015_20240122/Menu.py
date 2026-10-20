# ----- Menu -----
#   Contains a row of labels at the top
#   Mode Selector
#   More to come

import tkinter as tk
from tkinter import messagebox as tkMessageBox


class ValonMenu( tk.Menu ):

    # ----- Constructor -----
    def __init__( self, parent ):
        tk.Menu.__init__( self, parent )
        # The parent is the Main procedure, which is the Top-Level window.
        self.parent = parent
        self.Name = "Menu"

        self.mainWindow = None  # Needed to call sendCommand()
        self.sp = parent.sp     # Needed by the constructor

        self.fileMenu = None
        self.synthMenu = None
        self.helpMenu = None


        # Shipman: You must use the .add_cascade() method to attach each
        # sub-menu (eg. 'file' 'view', etc.) to the top menu bar

        # ----- File Menu -----
        self.fileMenu = tk.Menu( self )
        self.add_cascade( label='File', menu=self.fileMenu )

        self.fileMenu.add_command( label='Load Config', command=self.parent.fileLoadConfig )
        self.fileMenu.add_command( label='Save Config', command=self.parent.fileSaveConfig )
        #self.fileMenu.add_command( label='Telnet', command=self.parent.fileTelnet )
        self.fileMenu.add_command( label='Exit', command=self.quit)  # exit the mainloop

        # ----- Synthesizer Menu -----
        self.synthMenu = tk.Menu(self, tearoff=0)
        self.add_cascade( label = 'Synthesizer', menu = self.synthMenu )

        self.synthMenu.add_command( label='Read Registers', command=self.parent.synthReadRegisters )
        self.synthMenu.add_command( label='Write Registers', command=self.parent.synthWriteRegisters )
        self.synthMenu.add_command( label='Reset',
                                    command=lambda : self.mainWindow.sendTextCommand( "RST" ) )
        self.synthMenu.add_command( label='Save to Flash',
                                    command=lambda : self.mainWindow.sendTextCommand( "SAVE" ) )
        self.synthMenu.add_command( label='Recall from Flash',
                                    command=lambda : self.mainWindow.sendTextCommand( "RCL" ) )
        self.synthMenu.add_command( label='Cleanse', command=lambda : self.mainWindow.sendTextCommand( "CLE" ) )

        # ---------- Select Synthesizer submenu ----------
        self.synthChoiceMenu = tk.Menu( self )
        self.synthMenu.add_cascade( label="Select", menu=self.synthChoiceMenu )

        # Instantiate the "variable" that is common to all radio buttons in this group
        self.synthSelection = tk.StringVar()

        # Create a list to hold the StringVar "value" variables; one for each RadioButton.
        #self.portList = []

        for portName in self.sp.portList:
            #self.portName = tk.StringVar()
            #self.portList.append( self.portName )
            #self.portName.set( portName )
            self.synthChoiceMenu.add_radiobutton( label = portName,
                                                  variable = self.synthSelection,
                                                  value = portName
                                                )
        self.synthSelection.trace( "w", self.parent.synthSelectEH )
        #                           lambda name1, name2, op, index=i, var=var : self.parent.selectSynthesizer( self.synthSelection.get()) )

        # The menu bar is on the root window, so panelSelectEH is in V5015CM.py
        self.add_command( label='Main', command=lambda : self.parent.panelSelectEH( 'CW') )
        self.add_command( label='Sweep', command=lambda: self.parent.panelSelectEH( 'Sweep' ) )
        self.add_command( label='List', command=lambda: self.parent.panelSelectEH( 'List' ) )

        # ----- Help Menu -----
        self.helpMenu = tk.Menu( self, tearoff=0 )
        self.add_cascade( label='Help', menu=self.helpMenu )
        self.helpMenu.add_command( label='About', command = helpAbout )

        # ----- end of constructor -----

    def setMainWindowAddress( self, addr ):
        self.mainWindow = addr

def helpAbout():
    text = 'Author Peter Mckone\n' \
           'Valon Technology\n' \
           'Sample 5015 GUI code\n' \
           'Version 2.0\n' \
           'No Copyright'
    tkMessageBox.showinfo( 'Help About V5015CM', text )

