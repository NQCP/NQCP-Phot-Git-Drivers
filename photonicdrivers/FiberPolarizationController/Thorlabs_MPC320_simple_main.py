

from photonicdrivers.FiberPolarizationController.Thorlabs_MPC320_driver import Thorlabs_MPC320_Serial
serial_number = "38449564"
polarization_controller = Thorlabs_MPC320_Serial(serial_number)
polarization_controller.connect()
polarization_controller.set_position_0(100)
polarization_controller.set_position_1(90)
polarization_controller.set_position_2(160)
polarization_controller.disconnect()
polarization_controller.connect()
polarization_controller.set_position_0(40)
polarization_controller.set_position_1(20)
polarization_controller.set_position_2(160)
polarization_controller.disconnect()

from 