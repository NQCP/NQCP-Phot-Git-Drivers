import TimeTagger
import time

tagger = TimeTagger.createTimeTagger()
#connect to the Time Tagger via USB

tagger.startServer(access_mode = TimeTagger.AccessMode.Control,port=41101)
# Start the Server. TimeTagger.AccessMode sets the access rights for clients. Port defines the network port to be used
# The server keeps running until the command tagger.stopServer() is called or until the program is terminated

while True:
    print("I am alive")
    time.sleep(5)