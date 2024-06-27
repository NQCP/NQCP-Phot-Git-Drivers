from autoProber_atto1000_01 import autoProber_atto1000_01
from autoProber_mpiProber import autoProber_mpiProber
from autoProber_protocol import autoProber_prot



# Creating an instance of the autoProber_atto1000_01.
# Checking the it fulfills the protocol (could be skipped, as all autopriber child classes inhereits from the same parent)
autoProber: autoProber_prot = autoProber_atto1000_01()
# autoProber: autoProber_prot = autoProber_mpiProber()


#################### GENERIC CODE BELOW HERE ############################

autoProber.connectToEquipment()
autoProber.roughAlignment()