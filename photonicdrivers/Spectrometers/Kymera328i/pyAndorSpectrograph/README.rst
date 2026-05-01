*************************************
Andor Spectrograph SDK python wrapper
*************************************

===========
Information
===========
API wrapper for ATSpectrograph from Andor.
Supported platforms: python 3.7, python 3.8

----

Beta test python ATSpectrograph wrapper
Contains wrapper interface and latest SDK libraries
Note the new package name to use in an import; all other wrapper use should be the same. (You can alias the import if you absolutely have to.)

Tested on Win 10 32- and 64-bit

============
Installation
============
Installation depending on your python installation:

Open command console (Windows):

- pip3 install .
- python3 –m pip install .

Also

- pip3 list
- pip3 uninstall pyAndorSpectrograph

'sudo' as necessary for Linux

Any errors or suggestions, please report.


.. raw:: pdf

    PageBreak
    
======================
Example Initialization
======================

To be able to make use of the pyAndorSpectrograph, first the SDK must be installed by either using the above guide or an alternative method.
Once the SDK is properly installed it can be accessed via the ATSpectrograph object once it has been initialized as shown below.

Import and initialize pyAndorSpectrograph with default library location:
 
.. code-block:: python

    from pyAndorSpectrograph import ATSpectrograph
    sdk = ATSpectrograph()
    ret = sdk.ATSpectrographInitialize("")
    print(ret)

Import and initialize ATSpectrograph with user defined library location:
 

.. code-block:: python

    from pyAndorSpectrograph import ATSpectrograph
    sdk = ATSpectrograph()
    ret = sdk.ATSpectrographInitialize("directory/to/files")
    print(ret)



For users with a standard installation of the Andor Linux SDK:

.. code-block:: python

    from pyAndorSpectrograph import ATSpectrograph
    sdk = ATSpectrograph()
    ret = sdk.ATSpectrographInitialize("/usr/local/etc/andor")
    print(ret)


.. raw:: pdf

    PageBreak

================
Common Functions
================
pyAndorSpectrograph has many functions some of the most common functions are listed below.

Where sdk = ATSpectrograph library.


.. table::
    :widths: 30 40

    +-----------------------------------+-----------------------------------------------------------------------------------+
    | Example Code                      | Description                                                                       |
    +===================================+===================================================================================+
    | sdk.initialize(IniPath)           | Initializes the spectrograph driver.                                              |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.GetWavelength(device)         | Returns the current wavelength.                                                   |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.GetGrating(device)            | Returns the current grating.                                                      |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.GetGratingInfo(device,        | | Returns the grating information.                                                |
    | grating, maxBlazeStrLen)          | |                                                                                 |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.GetWavelengthlimits(device,   | | Returns the Grating wavelength limits.                                          |
    | grating)                          | |                                                                                 |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.GetCalibration(device,        | | Returns the wavelength calibration of each pixel on the attached sensor         |
    | numberPixels)                     | |                                                                                 |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.SetNumberPixels(device,       | | Set the number of pixels for the attached sensor.                               |
    | numberPixels)                     | |                                                                                 |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.SetPixelWidth(device, width)  | Sets the pixel width of the attached sensor. (In microns)                         |
    +-----------------------------------+-----------------------------------------------------------------------------------+
    | sdk.Close()                       | Closes the spectrograph driver.                                                   |
    +-----------------------------------+-----------------------------------------------------------------------------------+ 
    

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
    | Basic.py                  | Shows basic Initialization and displays basic device information.                 |
    +---------------------------+-----------------------------------------------------------------------------------+
    | FVB.py                    | Using pyAndorSpectrograph & pyAndorSdk2 to acquire a full vertically binned image.|
    +---------------------------+-----------------------------------------------------------------------------------+
    | Gating.py                 | Gets grating information from the Spectrograph.                                   |
    +---------------------------+-----------------------------------------------------------------------------------+
    | Wavelength.py             | Gets Wavelength information from the Spectrograph.                                |
    +---------------------------+-----------------------------------------------------------------------------------+
    | ShowImage.py              | Captures an single image and displays the acquired image                          |
    +---------------------------+-----------------------------------------------------------------------------------+
    | SaveAsCalibratedSif.py    | Saves an image as in the sif format and has appropriate calibrations              |
    +---------------------------+-----------------------------------------------------------------------------------+

 