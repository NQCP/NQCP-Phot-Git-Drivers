import time

def auto_reconnect(method):
    """Recover from Thorlabs PM closing connection after 120 seconds -- the simple way"""
    def wrapper(self, *args, **kwargs):
        if self.enabled is True:
            try:
                return method(self, *args, **kwargs)
            except:
                self.connect()
                time.sleep(0.2)
                return method(self, *args, **kwargs)
    return wrapper