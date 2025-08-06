# -*- coding: utf-8 -*-
"""
Network Time Tagger: Server example
See also: "client.py"
"""
import TimeTagger
import socket

print("""
*****************************
*    Time Tagger Network
*      Server example
*****************************
""")

# Connect to the Time Tagger and activate the internal test signal on four channels
tagger = TimeTagger.createTimeTagger()
tagger.setTestSignal([1, 2, 3, 4], True)

local_ip = socket.gethostbyname(socket.gethostname())
print("Local IP address:\n{}\n".format(local_ip))

# Start server with full control of the hardware by the connected clients.
tagger.startServer(TimeTagger.AccessMode.Control)
print('Time Tagger server started successfully on the default port 41101.\n')

print("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+  Now you can run the "client.py" in a the same or a separate Python process.
+  Or you can use any other client example from a different language.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")

# Keep the server alive until you press enter.
input('Press ENTER to stop the server...')

tagger.stopServer()
TimeTagger.freeTimeTagger(tagger)
del tagger
