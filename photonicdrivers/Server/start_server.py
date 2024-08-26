import rpyc

# The object you want to distribute
class MyObject:
    def __init__(self, data):
        self.data = data
    
    def exposed_get_data(self):  # Rename method to be accessible remotely
        return self.data

# The service class which will be exposed to the client
class MyService(rpyc.Service):
    def on_connect(self, conn):
        pass
    
    def on_disconnect(self, conn):
        pass
    
    def exposed_get_object(self):
        # This method will be exposed to the client
        return MyObject("Hello from the server!")

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(MyService, port=12505)
    print("Server is running...")
    server.start()