# code for communicating with the PicoMotor from NewFocus model 8742 via USB


from classPicoMotor import PicoMotor

pico = PicoMotor(0x104d, 0x4000)
print(pico.getProductID())
pico.closeConnection()