import pyvisa

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