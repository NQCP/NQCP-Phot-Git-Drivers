import pyvisa


print("hello")
# Open a VISA resource manager
rm = pyvisa.ResourceManager()

# List available VISA resources (instruments)
available_resources = rm.list_resources()
if not available_resources:
    print("No available VISA resources found.")


# Print the list of available resources
print("Available VISA resources:")
for idx, resource in enumerate(available_resources, start=1):
    print(f"{idx}. {resource}")

# Open a VISA instrument connection
instrument = rm.open_resource("USB0::0x1313::0x8078::P0041989::INSTR")

# Send an IDN query using SCPI
idn_query = "*IDN?"
response = instrument.query(idn_query)
print("Device Identification:", response.strip())

# Close the instrument connection
instrument.close()
rm.close()


