
class Console_Controller:
    __print_bool = True
    __instance = None

    def __init__(self):
        '''
        This class is a singleton and hence no instance should be created of this class. To emulate a private access
        modifier in Python code, I simply raise an exception when this class is instantiated.
        '''
        raise RuntimeError(
            "This class is a singleton and hence no instance should be created. Instead, invoke the class method get_instance().")

    @classmethod
    def create_instance(cls):
        '''
        The cls.__new__(cls) method does not invoke the __init__() method although it creates a new instance of the Console_Controller class
        :return: returns an instance of the singleton instance of the Console_Controller class
        '''
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)
        return cls.__instance

    @classmethod
    def print_message(cls, message, print_bool = True):
        if cls.__print_bool and print_bool == True:
            print(message)

    @classmethod
    def set_print_bool(cls, bool):
        cls.__print_bool = bool
