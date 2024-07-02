import ACS
from about import About
from access import Access
from amcids import Amcids
from control import Control
from description import Description
from diagnostic import Diagnostic
from functions import Functions
from move import Move
from network import Network
from res import Res
from rotcomp import Rotcomp
from rtin import Rtin
from rtout import Rtout
from status import Status
from system_service import System_service
from update import Update


class Device(ACS.Device):

    def __init__ (self, address):
    
        super().__init__(address)
        
        self.about = About(self)
        self.access = Access(self)
        self.amcids = Amcids(self)
        self.control = Control(self)
        self.description = Description(self)
        self.diagnostic = Diagnostic(self)
        self.functions = Functions(self)
        self.move = Move(self)
        self.network = Network(self)
        self.res = Res(self)
        self.rotcomp = Rotcomp(self)
        self.rtin = Rtin(self)
        self.rtout = Rtout(self)
        self.status = Status(self)
        self.system_service = System_service(self)
        self.update = Update(self)

def discover():
    return Device.discover("amc")