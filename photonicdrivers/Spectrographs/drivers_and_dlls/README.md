# OceanDirect Sample Code
```
from oceandirect.od_logger import od_logger
from oceandirect.OceanDirectAPI import OceanDirectAPI, OceanDirectError

logger = od_logger()

def get_spec_formatted(device, sn):
    try:
        #device.set_electric_dark_correction_usage(False);
        #device.set_nonlinearity_correction_usage(False);

        #10ms
        device.set_integration_time(10000);

        print("Reading spectra for dev s/n = %s" % sn, flush=True)
        for i in range(10):
            spectra = device.get_formatted_spectrum()
            print("spectra[100,200,300,400]: %d, %d, %d, %d" % (spectra[100], spectra[200], spectra[300], spectra[400]), flush=True)
    except OceanDirectError as e:
        logger.error(e.get_error_details())

if __name__ == '__main__':
    od = OceanDirectAPI()
    device_count = od.find_usb_devices()
    device_ids = od.get_device_ids()

    device_count = len(device_ids)
    (major, minor, point) = od.get_api_version_numbers()

    print("API Version  : %d.%d.%d " % (major, minor, point))
    print("Total Device : %d     \n" % device_count)

    if device_count == 0:
        print("No device found.")
    else:
        for id in device_ids:
            device       = od.open_device(id)
            serialNumber = device.get_serial_number()

            print("First Device : %d       " % id)
            print("Serial Number: %s     \n" % serialNumber)

            get_spec_formatted(device, serialNumber)

            print("Closing device!\n")
            od.close_device(id)

    print("**** exiting program ****")
    
```

