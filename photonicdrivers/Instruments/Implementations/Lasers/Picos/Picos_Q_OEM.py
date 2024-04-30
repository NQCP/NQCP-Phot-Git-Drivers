from photonicdrivers.Instruments.Abstract.Abstract import Instrument


class Picos_Q_OEM(Instrument):

    def load_settings(self) -> dict:
        pass

    def save_settings(self, settings: dict) -> None:
        pass

    def get_id(self, settings: dict) -> None:
        pass

    def __init__(self, resource_manager, port):
        self.port = port
        self.resource_manager = resource_manager

    def connect(self):
       try:
            self.laser = self.resource_manager.open_resource(self.port)  # use the correct COM port
            Console_Controller.print_message("Successfully connected to Picos laser")
       except:
            Console_Controller.print_message("Unable to connect to picos")


    def disconnect(self):
        try:
            self.laser.close()  # use the correct COM port
            Console_Controller.print_message("Successfully disconnected to Picos laser")
        except:
            Console_Controller.print_message("Unable to disconnect to picos")

    def turn_on_emission(self):
        try:
            self.laser.write('Laser:Enable 1')
            Console_Controller.print_message("Successfully turned Picos on emission")
        except:
            Console_Controller.print_message("Emission turn on was unsuccessful")

    def turn_off_emission(self):
        try:
            Console_Controller.print_message(self.laser.write('Laser:Enable 0'))
            Console_Controller.print_message("Successfully turned off Picos emission")
        except:
            Console_Controller.print_message("Emission turn off was unsuccessful")