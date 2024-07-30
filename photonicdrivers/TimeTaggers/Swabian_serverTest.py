import TimeTagger
import time


# Connecting to time tagger
serialNumber = "23010013V4"
print("Connecting to timetagger with serial number " + serialNumber)
tagger = TimeTagger.createTimeTagger(serialNumber)


# Start the Server. TimeTagger.AccessMode sets the access rights for clients. Port defines the network port to be used
# The server keeps running until the command tagger.stopServer() is called or until the program is terminated
print("Starts the server")
tagger.startServer(access_mode = TimeTagger.AccessMode.Control,port=41101)


# Keep this process running
run = True
print("Server is now running")
while run == True:
    user_input = input("Type 'close' in the terminal followed by ENTER to stop the server: ")
    if user_input.lower() == 'close':
        run = False
    time.sleep(0.1)


tagger.stopServer()
print("Server stopped")


print("Free up timetagger")
TimeTagger.freeTimeTagger(tagger)


print("Script completed")