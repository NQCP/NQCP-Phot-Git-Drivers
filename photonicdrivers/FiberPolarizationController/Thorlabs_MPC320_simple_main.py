

from Thorlabs_MPC320 import Thorlabs_MPC320
serial_number = "38449564"
polarization_controller = Thorlabs_MPC320(serial_number)
polarization_controller.connect()
new_positions = [60, 20, 60]
polarization_controller.move_to(*new_positions)
polarization_controller.home()
polarization_controller.disconnect()