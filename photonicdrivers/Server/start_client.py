import rpyc

# Connect to the server
conn = rpyc.connect("10.209.67.53", 12505)

# Get the object from the server
remote_object = conn.root.get_object()

# Use the object as if it were local
print(remote_object.exposed_get_data())  # Call the exposed method

# Close the connection when done
conn.close()
