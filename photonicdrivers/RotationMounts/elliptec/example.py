from rotator import Rotator
from controller import Controller
controller =  Controller(port="COM8", debug=True)

rotator_A = Rotator(controller = controller, address="A", debug=True)
rotator_B = Rotator(controller = controller, address="B", debug=True)
rotator_C = Rotator(controller = controller, address="C", debug=True)
rotator_D = Rotator(controller = controller, address="D", debug=True)


rotator_A.home()
rotator_A.set_angle(45)
rotator_A.get_angle()
rotator_A.set_angle(0)
rotator_A.get_angle()
controller.close_connection()
