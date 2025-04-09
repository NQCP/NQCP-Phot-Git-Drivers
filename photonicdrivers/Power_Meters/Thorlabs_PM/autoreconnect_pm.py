import time

def auto_reconnect(method):
    """Recover gracefully from some Thorlabs PMs closing connection after 120 seconds"""
    def wrapper(self, *args, **kwargs):
        # Makes the reconnection + retry opt-in
        if self.auto_disconnecting is not True:
            return method(self, *args, **kwargs)

        if self.enabled is True:
            try:
                return method(self, *args, **kwargs)
            except:
                self.connect()
                time.sleep(0.2)
                return method(self, *args, **kwargs)
    return wrapper