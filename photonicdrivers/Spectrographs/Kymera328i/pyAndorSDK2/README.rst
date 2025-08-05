***********
pyAndorSDK2
***********

===========
Information
===========
Python wrapper for Andor SDK2.

Contains wrapper interface and SDK2 libraries

Supported platforms: python 3.5.1 +

============
Installation
============
Installation depending on your python installation:

Open command console within the same directory as the setup.py:

- python3 –m pip install .

Also:

- pip3 install .
- pip3 list
- pip3 uninstall pyAndorSDK2

'sudo' as necessary for Linux

Any errors or suggestions, please report to row_productsupport@andor.com.

=========
Libraries
=========
Windows:

During installation the appropriate libraries (64/32 bit) are copied into the site-packages folder of your python installation.

When the pyAndorSDK2 module is imported the site-packages folder containing the libs is added to the systems PATH variable.

Linux:

The pyAndorSDK2 for Linux assumes the user has installed AndorSDK2 for Linux on their system. This will have correctly configured LD_LIBRARY_PATH as well as configuring the correct symbolic links.

The environment variable LD_LIBRARY_PATH controls the behaviour of the dynamic loader used to find and load the shared libraries needed by a program.


.. raw:: pdf

   PageBreak

======================
Example Initialization
======================

To be able to make use of the pyAndorSDK2, first the SDK must be installed by either using the above guide or an alternative method.
Once the SDK is properly installed it can be accessed via the atmcd object once it has been initialized as shown below.


Import and initialize SDK2 with default library location:
 
.. code-block:: python

    from pyAndorSDK2 import atmcd
    sdk = atmcd()
    ret = sdk.Initialize("")
    print(ret)

Import and initialize SDK2 with user defined library location:

.. code-block:: python

    from pyAndorSDK2 import atmcd
    sdk = atmcd()
    ret = sdk.Initialize("directory/to/files")
    print(ret)

For users with a standard installation of the Andor Linux SDK:

.. code-block:: python

    from pyAndorSDK2 import atmcd
    sdk = atmcd()
    ret = sdk.Initialize("/usr/local/etc/andor")
    print(ret)


.. raw:: pdf

    PageBreak


========================
Common Methods Available
========================

pyAndorSDK2 has many functions some of the most common functions are listed below.

Where sdk = atmcd library.

.. table::
    :widths: 30 40

    +-----------------------------------+-----------------------------------------------------------------------------------+
    | Example Code                      | Description                                                                       |
    +===================================+===================================================================================+
    | sdk.Initialize(dir)               | Initializes the pyAndorSDK2 object.                                               |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.SetTriggerMode(mode)          | Sets the device to the specified trigger mode.                                    |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.SetTemperature(temperature)   | Sets the target temperature of the of the detector.                               |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.CoolerON()                    | Starts the cooler.                                                                |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.SetAcquisitionMode(mode)      | Sets the acquisition mode to be used on next Start Acquisition.                   |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.SetExposureTime(time)         | Sets the time in second for how long the image exposure will last.                |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.SetReadMode(mode)             | Sets the readout mode for following acquisitions.                                 |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | | sdk.SetImage(hbin,              | | Sets the horizontal and vertical binning when taking a full resolution image.   |
    | |     vbin, hstart, hend,         | | Can also be used for configuring a sub image.                                   |
    | |     vstart, vend)               |                                                                                   |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.GetStatus()                   | Gets the current status of the device.                                            |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.GetImages16(first, last, size)| Gets any available images in the buffer. In 16 bit format                         |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.GetDetector()                 | Gets the dimension of the detector in pixels.                                     |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.StartAcquisition()            | The device begins its predefined acquisition cycle.                               |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.WaitForAcquisition()          | Puts calling thread to sleep until an acquisition event occurs.                   |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.ShutDown()                    | Closes the atmcd resource.                                                        |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    

    
.. raw:: pdf

    PageBreak
    
===========
Atmcd Codes
===========
Within pyAndorSDK2 there is a file atmcd_codes.py which contains a selection of user codes that make it easier to set up and configure your device.

Where codes = atmcd_codes.UserCodes & sdk = atmcd library


.. table::
    :widths: 30 40

    +---------------------------+-----------------------------------------------------------------------------------+
    | Enum                      | Description                                                                       |
    +===========================+===================================================================================+
    | codes.Read_Mode           | Contains codes for configuring sdk.SetReadMode()                                  |
    +---------------------------+-----------------------------------------------------------------------------------+
    | codes.Trigger_Mode        | Contains codes for configuring sdk.SetTriggerMode()                               |
    +---------------------------+-----------------------------------------------------------------------------------+
    | codes.Acquisition_Mode    | Contains codes for configuring sdk.SetAcquisitionMode()                           |
    +---------------------------+-----------------------------------------------------------------------------------+
    | codes.Spool_Mode          | Contains codes for configuring the method parameter for sdk.SetSpool()            |
    +---------------------------+-----------------------------------------------------------------------------------+
    | codes.Gate_Mode           | Contains codes for configuring sdk.SetGateMode()                                  |
    +---------------------------+-----------------------------------------------------------------------------------+
    | codes.Shutter_Mode        | Contains codes for configuring the mode parameter for sdk.SetShutter()            |
    +---------------------------+-----------------------------------------------------------------------------------+
    
There is also atmcd_errors which provides a way to search through error codes that may be returned by the atmcd object to aid in debugging. 


.. raw:: pdf

    PageBreak

========
Examples
========
This SDK contains a folder called examples. Which showcases different functionality available in the SDK.
The current list of examples is:


.. table::
    :widths: 30 40

    +---------------------------+-----------------------------------------------------------------------------------+
    | Example Name              | Description                                                                       |
    +===========================+===================================================================================+
    | AcquireSeries.py          | Details how to set up and configure a device to capture a series of 5 images.     |
    +---------------------------+-----------------------------------------------------------------------------------+
    | Cooling.py                | Shows how to properly configure cooling setting and how to turn on cooling.       |
    +---------------------------+-----------------------------------------------------------------------------------+
    | FVB.py                    | Acquires an image while Read mode is set to Full Vertical Binning.                |
    +---------------------------+-----------------------------------------------------------------------------------+
    | Image.py                  | Acquires an image while Read mode is set to Image.                                |
    +---------------------------+-----------------------------------------------------------------------------------+
    | SerialNumber.py           | | Initializes an atmcd object to uses a method to retrieve                        |
    |                           | | the serial number from the connected device.                                    |
    +---------------------------+-----------------------------------------------------------------------------------+
    | USBiStar.py               | | Displays an image acquisition while using an USB iStar                          |
    |                           | | device, and set the delay generator.                                            |
    +---------------------------+-----------------------------------------------------------------------------------+
    | SaveAsSIF.py              | Shows do a basic image save in .SIF format                                        |
    +---------------------------+-----------------------------------------------------------------------------------+
    | ReadOutRates.py           | Acquires the HSSpeed, VSSpeed and availabe amp modes                              |
    +---------------------------+-----------------------------------------------------------------------------------+
    | RunTillabort.py           | | Demonstrates the runtillabort readout mode by                                   |
    |                           | | showing the most recent image acquired.                                         |
    +---------------------------+-----------------------------------------------------------------------------------+
    | GetCapabilities.py        | Demonstrates how to use the CameraCapabilities class.                             |
    +---------------------------+-----------------------------------------------------------------------------------+
    

----

For SDK2 usage or feature specific information please refer to the manual Andor Software Development Kit.pdf