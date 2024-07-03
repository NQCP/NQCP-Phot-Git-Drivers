import pyvisa

def main():
    print("hello")
    # Open a VISA resource manager
    rm = pyvisa.ResourceManager()

    # List available VISA resources (instruments)
    available_resources = rm.list_resources()
    if not available_resources:
        print("No available VISA resources found.")
        return

    # Print the list of available resources
    print("Available VISA resources:")
    for idx, resource in enumerate(available_resources, start=1):
        print(f"{idx}. {resource}")

    # Select a resource (instrument) to communicate with
    selected_idx = int(input("Enter the index of the desired resource: ")) - 1
    selected_resource = available_resources[selected_idx]

    try:
        # Open a VISA instrument connection
        instrument = rm.open_resource(selected_resource)

        # Send an IDN query using SCPI
        idn_query = "*IDN?"
        response = instrument.query(idn_query)
        print("Device Identification:", response.strip())

    except pyvisa.VisaIOError as e:
        print("An error occurred:", e)

    finally:
        # Close the instrument connection
        instrument.close()
        rm.close()

if __name__ == "__main__":
    main()
