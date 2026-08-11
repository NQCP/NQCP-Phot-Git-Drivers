//
//  ProfileTest.cpp
//
//  This program is an example of how to use and create attenuator profiles
//
// 
//  NB 10/28/2025	changed user input from .05 db units to db units for consistency with other demo programs
//

#include "stdafx.h"
#include "vnx_LDA_api.h"
#define _USE_MATH_DEFINES
#include <math.h>

using namespace std;


#define THIS_FILE_DATE "10-28-2025"

// ------------------------------ - Equates-----------------------------------------------
#define CL_SWP_DIRECTION		0x04	// MASK: bit = 0 for ramp up, 1 for ramp down 
#define CL_SWP_CONTINUOUS		0x02	// MASK: bit = 1 for continuous ramping
#define CL_SWP_ONCE				0x01	// MASK: bit = 1 for single ramp
#define CL_SWP_BIDIRECTIONALLY	0x10	// MASK: bit = 1 for bidirectional ramps (V2 LDA's only)


// ------------------------------- Allocations -------------------------------------------

static DEVID MyDevices[MAXDEVICES];				// I have statically allocated this array for convenience
												// It holds a list of device IDs for the connected devices
												// They are stored starting at MyDevices[0]

static char MyDeviceNameA[MAX_MODELNAME];		// NB -- this is a single byte char array for testing the ASCII name function
static wchar_t MyDeviceNameW[MAX_MODELNAME];	// NB -- this is a WCHAR array for testing the Unicode name function

static wchar_t errmsg[32];						// For the status->string converter
static char cModelName[32];						// buffer for the model name

static string sDevName = "ATN-001";				// device name string
static bool gbWantOneDevice = FALSE;

static int DevNum = 0;				// the device we should work with.
static int DevRange = 1;			// the number of devices we'll send the command to
static int NumDevices = 0;			// used to store the actual number of devices found


// --------------------------- Variables -------------------------------------------------

static int IdleTime = 1;			// default idle time is 1 ms
static int Dwell = 1000;			// default dwell time is 1 second for first ramp phase
static int WorkingFrequency = 0;	// working frequency for the HiRes attenuators
static float Attenuation = 0;		// default attenuation is 0db, entered as a floating point value
static int ScaledAttenuation = 0;	// temporary storage for scaled attenuation values
static int SerialNumber = 0;		// used to hold the serial number for the get serial number command

static int Profile_mode = 0;		// used to control the profile mode, (off, single, repeat)

static int ProfileIndex = 0;		// the element in the profile we want to set
static int ProfileLength = 0;		// the length of the profile
static int ProfileValue = 0;		// the profile element's value

static int Channel = 1;				// we just default to the first channel
static int NumToPlay = 0;			// number of channels for multiple channel profile command  (also used as an index -- post increment!)
static int ChannelList[8] = { 0, 0, 0, 0, 0, 0, 0, 0 };
static int ChMask = 0;				// mask of active channel bits for MC profile play command

int Test_Type = 1;					// sine function test pattern
int Test_Frequency = 1;
float Test_Range = 60;
float Test_Baseline = 60;			// default values for a test profile				

bool gbWantSetIdle = FALSE;
bool gbWantSetDwell = FALSE;

bool gbWantStartSweep = FALSE;
bool gbWantSetWorkingFrequency = FALSE;
bool gbWantSetAttenuation = FALSE;

bool gbBatchMode = FALSE;
bool gbQuietMode = FALSE;
bool gbPrintProfile = FALSE;
bool gbWantTestProfile = FALSE;
bool gbWantSetProfileElement = FALSE;
bool gbWantSetProfileLength = FALSE;
bool gbWantChannel = FALSE;
bool gbWantMCProfile = FALSE;

// our profile array for generated profiles

int TestProfile[1000];

// ------------------------------- Support Routines --------------------------------------

void PrintHelp()
{
	printf("Vaunix Profile Demonstration\n");
	printf("\n");
	printf("Hit CTRL+C to exit\n");
	printf("\n");

	printf(" --- Overall modes and device selection. Defaults to first device ---\n");
	printf("  -d i n 	Select the devices to work with, i is the device number (1,2,3, etc.)\n");
	printf("			and n is the number of devices to apply the command to.\n");
	printf("			-d 1 2 applies the commands to attenuators 1 and 2.\n");
	printf("			-d 2 3 applies the commands to attenuators 2, 3 and 4.\n");
	printf("\n");
	printf("  -b		Batch mode, exit immediately after sending commands to the Lab Bricks.\n");
	printf("  -q		Quiet mode, skip most outputs.\n");
	printf("  -r		Print Profile contents\n");
	printf("\n");

	printf(" --- Commands to set parameters --- \n");
	printf("  -c n		Set the active channel\n");
	printf("  -f nn		Set working frequency, nn is working frequency in MHz\n");
	printf("  -a nn		Set attenuation, nn is attenuation in db units\n");
	printf("  -i nn		Set idle time between repeated profiles, nn is time in ms.\n");
	printf("  -l nn		Set the profile length, nn is the number of elements\n");
	printf("  -t nn		Set time to dwell on each profile value, nn is time in ms.\n");
	printf("  -p t nc nr nb		Generate a test profile of type t, with nn as a type specific parameter\n");
	printf("			t = 1 for a sine function, nc is the number of cycles in the profile from 1 to 100\n");
	printf("			nr is the range for sin = 1, nb is the baseline, both db units.\n");
	printf("\n");
	printf(" --- Commands to start multiple profiles --- \n");
	printf("  -x m n c c...	Start multiple profiles, m is the mode:\n");
	printf("			1 = play the profiles once, 2 = play the profiles repeatedly,\n");
	printf("			0 to stop the profiles\n");
	printf("			n = number of profiles, for each one c is the channel number");
	printf("			(only for channel numbers 1-8, separate from earlier channel selection)\n");
	printf("\n");


}

// -------------------- - MakeLower------------------------------

wchar_t MakeLowerW(wchar_t &wc)
{
	return wc = towlower(wc);
}

// --------------------------------------------------------------

#define MAX_MSG 32

/* A function to display an error status as a Unicode string */
wchar_t* fnLDA_perror(LVSTATUS status) {
	wcscpy_s(errmsg, MAX_MSG, L"STATUS_OK");
	if (BAD_PARAMETER == status) wcscpy_s(errmsg, MAX_MSG, L"BAD_PARAMETER");
	if (BAD_HID_IO == status) wcscpy_s(errmsg, MAX_MSG, L"BAD_HID_IO");
	if (DEVICE_NOT_READY == status) wcscpy_s(errmsg, MAX_MSG, L"DEVICE_NOT_READY");
	if (FEATURE_NOT_SUPPORTED == status) wcscpy_s(errmsg, MAX_MSG, L"FEATURE_NOT_SUPPORTED");
	if (INVALID_DEVID == status) wcscpy_s(errmsg, MAX_MSG, L"INVALID_DEVID");

	return errmsg;
}

// -- one way to check for errors --
void CheckAPISet(LVSTATUS status)
{
	if (status & 0x80000000)
	{
		wprintf(L"*** Error: LDA API returned status = %x, %s ***\n", status, fnLDA_perror(status));
	}

}

/* A function to display the status as a Unicode string */
wchar_t* fnLDA_pstatus(LVSTATUS status) {
	wcscpy_s(errmsg, MAX_MSG, L"STATUS_OK");

	// Status returns for DevStatus
	if (INVALID_DEVID == status) wcscpy_s(errmsg, MAX_MSG, L"INVALID_DEVID");
	if (DEV_CONNECTED == status) wcscpy_s(errmsg, MAX_MSG, L"DEV_CONNECTED");
	if (DEV_OPENED == status) wcscpy_s(errmsg, MAX_MSG, L"DEV_OPENED");
	if (SWP_ACTIVE == status) wcscpy_s(errmsg, MAX_MSG, L"SWP_ACTIVE");
	if (SWP_UP == status) wcscpy_s(errmsg, MAX_MSG, L"SWP_UP");
	if (SWP_REPEAT == status) wcscpy_s(errmsg, MAX_MSG, L"SWP_REPEAT");
	if (SWP_BIDIRECTIONAL == status) wcscpy_s(errmsg, MAX_MSG, L"SWP_BIDIRECTIONAL");
	if (PROFILE_ACTIVE == status) wcscpy_s(errmsg, MAX_MSG, L"PROFILE_ACTIVE");

	return errmsg;
}


// --- routines to generate a sample profile ---
// 
// frequency is in Hz from 1 to 100 Hz
// range is the maximum amplitude of the sine wave in .05 db units around a baseline level also in .05 db units
// The function limits profile elements to 120 db attenuation, but it is up to the user to ensure that the range
// of the profile corresponds to the range of the device
//

void SineProfile(int frequency, float range, float baseline)
{
	int i;
	float attenuation;
	double angle;

	// -- just clip any bad arguments to something reasonable -- 
	if (frequency < 1) frequency = 1;
	if (frequency > 100) frequency = 100;

	if (range < 0) range = 0;
	if (range > 120) range = 120;

	if (baseline < 0) baseline = 0;
	if (baseline > 120) baseline = 120;

	// -- we fill our 1000 element RAM profile buffer with a sine running from 0 degrees --
	// There can be from 1 to 100 cycles of the sin function in the 1000 element profile
	// At the shortest 1ms dwell time this corresponds to a frequency from 1 Hz to 100 Hz.

	for (i = 0; i < 1000; i++)
	{
		angle = i * frequency * (M_PI) / 500;				// instead of 2*pi / 1000,  I factored out the 2
		attenuation = baseline + (float)sin(angle) * range;
		TestProfile[i] = (int)(attenuation * 20);
		if (TestProfile[i] < 0) TestProfile[i] = 0;
		if (TestProfile[i] > 2400) TestProfile[i] = 2400;	// clip to 0 to 120 db in HR units
	}
}


int ChannelToMask(int channel)
{
	int mask = 1;
	if (channel < 1) channel = Channel;		// channel 0 signifies the current global channel
	return mask << (channel - 1);			// channel runs from 1 to 8
}


// ParseCommandLine() will return FALSE to indicate that we received an invalid
// command or should abort for another reason.
bool ParseCommandLine(int argc, _TCHAR *argv[])
{
	int iActiveChannel = 0;

	enum {
		wantDash, wantDevSubstring, wantIdle, wantDwell, wantPRType,
		wantAtten, wantSweep, wantDevID, wantDevRange, wantNumToPlay,
		wantProfileLength, wantDwellPhase, wantStepPhase, wantWorkingFrequency,
		wantChannel, wantProfileMode, wantActiveChannel, wantCycles, wantTestRange, wantTestBaseline
	} state = wantDash;

	for (int i = 1; i < argc; ++i) {
		// Convert each argument to lowercase
		wstring thisParam(argv[i]);
		for_each(thisParam.begin(), thisParam.end(), MakeLowerW);

		if (state == wantDash)
		{
			if ('-' != thisParam[0])
			{
				printf("\n *** Error in command line syntax *** \n");
				PrintHelp();
				return FALSE;
			}
			// remove the dash from the front of the string
			thisParam = wstring(thisParam.begin() + 1, thisParam.end());

			// Identify the command line arguments
			if (L"d" == thisParam) {
				state = wantDevID;
			}
			else if (L"q" == thisParam) {
				gbQuietMode = TRUE;
				state = wantDash;
			}
			else if (L"r" == thisParam) {
				gbPrintProfile = TRUE;
				state = wantDash;
			}
			else if (L"b" == thisParam) {
				gbBatchMode = TRUE;
				state = wantDash;
			}
			else if (L"c" == thisParam) {
				gbWantChannel = TRUE;
				state = wantChannel;
			}
			else if (L"f" == thisParam) {
				gbWantSetWorkingFrequency = TRUE;
				state = wantWorkingFrequency;
			}
			else if (L"a" == thisParam) {
				gbWantSetAttenuation = TRUE;
				state = wantAtten;
			}
			else if (L"i" == thisParam) {
				gbWantSetIdle = TRUE;
				state = wantIdle;
			}
			else if (L"l" == thisParam) {
				gbWantSetProfileLength = TRUE;
				state = wantProfileLength;
			}
			else if (L"t" == thisParam) {
				gbWantSetDwell = TRUE;
				state = wantDwell;
			}
			else if (L"p" == thisParam) {
				gbWantTestProfile = TRUE;
				state = wantPRType;
			}

			else if (L"x" == thisParam) {
				gbWantMCProfile = TRUE;
				NumToPlay = 0;
				Profile_mode = 0;
				state = wantProfileMode;
			}
			else {
				// this case is for "-?" and any argument we don't recognize
				PrintHelp();
				return FALSE;	// don't continue
			}
		}

		else {

			// save the whole substring and do conversions for each argument type

			switch (state) {

			case wantIdle:
				IdleTime = _wtoi(thisParam.c_str());		// convert to a int
				state = wantDash;
				break;

			case wantProfileLength:
				ProfileLength = _wtoi(thisParam.c_str());
				state = wantDash;
				break;

			case wantDevID:
				DevNum = _wtoi(thisParam.c_str());
				state = wantDevRange;
				break;

			case wantChannel:
				Channel = _wtoi(thisParam.c_str());
				state = wantDash;
				break;

			case wantDevRange:
				DevRange = _wtoi(thisParam.c_str());
				state = wantDash;
				break;

			case wantDwell:
				Dwell = _wtoi(thisParam.c_str());
				state = wantDash;
				break;

			case wantAtten:
				Attenuation = (float)_wtof(thisParam.c_str());	// cast to a float, _wtof actually returns a double
				state = wantDash;
				break;

			case wantWorkingFrequency:
				WorkingFrequency = (int) (10 * _wtof(thisParam.c_str()));	// _wtof actually returns a double in MHz
																			// internally we use 100 Khz units
				state = wantDash;
				break;

			case wantPRType:
				Test_Type = _wtoi(thisParam.c_str());						// as of now we only support type 1, a sin function
				state = wantCycles;
				break;

			case wantCycles:
				Test_Frequency = _wtoi(thisParam.c_str());					// "frequency" is in units of cycles per buffer
				state = wantTestRange;
				break;

			case wantTestRange:
				Test_Range = (float)_wtof(thisParam.c_str());					// the range is the amplitude in .05 db units of sin = 1.
				state = wantTestBaseline;
				break;

			case wantTestBaseline:
				Test_Baseline = (float)_wtof(thisParam.c_str());				// the baseline is the "DC" level of the sin function in .05 db units
				state = wantDash;
				break;

			case wantProfileMode:
				Profile_mode = _wtoi(thisParam.c_str());
				state = wantNumToPlay;
				break;

			case wantNumToPlay:
				NumToPlay = _wtoi(thisParam.c_str());
				if (NumToPlay < 0) NumToPlay = 0;
				if (NumToPlay > 8) NumToPlay = 8;
				state = wantActiveChannel;
				break;

			case wantActiveChannel:
				ChannelList[iActiveChannel] = _wtoi(thisParam.c_str());
				iActiveChannel++;
				if (iActiveChannel < NumToPlay) state = wantActiveChannel;
				else state = wantDash;
				break;
			}
		}
	}

	if (state != wantDash) {
		// we are expecting an argument, if we didn't get one then print the help message
		PrintHelp();
		return FALSE;
	}

	// It's OK to continue
	return TRUE;
}

int _tmain(int argc, _TCHAR* argv[])
{
	//std::cout << "Hello World!\n";

	int i, j, k;
	int iDev;
	int itemp;
	float ftemp;
	int NumChannels;		// temporary storage for the number of channels in a device
	int NumProfileElements;	// temporary storage for the number of profile elements in a device  (per channel, always the same for each channel)


	if (!ParseCommandLine(argc, argv))
		return 0;

	if (!gbQuietMode) printf("Lab Brick Multi Attenuator Demonstration Program\n");

	//	 -- convert the user's device number to our internal MyDevices array index and check our device range --

	DevNum = DevNum - 1;

	if (DevNum < 0) DevNum = 0;
	if (DevRange < 1) DevRange = 1;
	if (DevRange > MAXDEVICES) DevRange = MAXDEVICES;

	if (DevNum > MAXDEVICES - 1) DevNum = MAXDEVICES - 1;
	if ((DevNum + DevRange) > MAXDEVICES) DevRange = MAXDEVICES - DevNum;

	// at this point our device starting index and number of devices should be reasonable...
	if (!gbQuietMode) printf("Starting device number = %d, using %d device[s]\n", DevNum + 1, DevRange);

	// --- if TestMode = TRUE then the dll will fake the hardware ---
	fnLDA_SetTestMode(FALSE);


	// --- Use the tracing control function to turn on debug messages
	fnLDA_SetTraceLevel(0, 0, false);
	//fnLDA_SetTraceLevel(3, 3, true);


	i = fnLDA_GetNumDevices();

	if (i == 0) {
		printf("No device found\n");
	}

	if (i == 1) {
		if (!gbQuietMode) printf("Found %d Device\n", i);

	}
	else {
		if (!gbQuietMode) printf("Found %d Devices\n", i);
	}

	// -- warn the user if he or she expects more devices than we have --
	if (DevRange > i) {
		printf(" Warning - not enough attenuators are connected\n");
	}

	NumDevices = fnLDA_GetDevInfo(MyDevices);

	if (!gbQuietMode) printf("Got Device Info for %d Device[s]\n", NumDevices);


	if (NumDevices > 0)	// do we have a device?
	{
		for (j = 0; j < NumDevices; j++) {

			// --- print out the first device's name ---
			if (!gbQuietMode) {
				itemp = fnLDA_GetModelNameA(MyDevices[j], MyDeviceNameA);
				printf("Device %d is an %s \n", j + 1, MyDeviceNameA);
			}

			// --- print out the device's serial number ---
			if (!gbQuietMode) {
				itemp = fnLDA_GetSerialNumber(MyDevices[j]);
				if (itemp >= 0)
					printf("Device %d has serial number %d \n", j + 1, itemp);
			}


			// --- We need to init the device (open it) before we can do anything else ---
			itemp = fnLDA_InitDevice(MyDevices[j]);

			if (itemp) {
				printf("InitDevice returned error code %x\n", itemp);
			}

			// --- Lets see if we got the device's parameters ---
			if (!gbQuietMode) {

				// Display the number of channels for this device
				NumChannels = fnLDA_GetNumChannels(MyDevices[j]);
				if (NumChannels >= 0) {
					if (NumChannels == 1) printf("Single Channel Device\n");
					else printf("Device has %d Channels\n", NumChannels);
				}
				else
					CheckAPISet(NumChannels);

				// show device wide parameters
				printf("Attenuation Range:\n");
				itemp = fnLDA_GetMinAttenuation(MyDevices[j]);
				ftemp = (float) (itemp * .25);
				if (itemp >= 0)
					printf("Minimum Attenuation = %.2f db\n", ftemp);
				else
					CheckAPISet(itemp);

				itemp = fnLDA_GetMaxAttenuation(MyDevices[j]);
				ftemp = (float) (itemp * .25);
				if (itemp >= 0)
					printf("Maximum Attenuation = %.2f db\n", ftemp);
				else
					CheckAPISet(itemp);

				if (fnLDA_GetFeatures(MyDevices[j]) & HAS_HIRES)
				{
					printf("Working Frequency Range:\n");
					itemp = fnLDA_GetMinWorkingFrequency(MyDevices[j]);
					ftemp = ((float)itemp) / 10;		// frequency is in 100KHz units
					if (itemp >= 0)
						printf("Minimum Frequency = %.2f Mhz\n", ftemp);
					else
						CheckAPISet(itemp);

					itemp = fnLDA_GetMaxWorkingFrequency(MyDevices[j]);
					ftemp = ((float)itemp) / 10;		// frequency is in 100KHz units
					if (itemp >= 0)
						printf("Maximum Frequency = %.2f Mhz\n", ftemp);
					else
						CheckAPISet(itemp);
				}

				// if we have more than one channel, show the parameters for each channel
				for (i = 0; i < NumChannels; i++)
				{
					if (NumChannels > 1)
					{
						printf("\nParameters for device %d channel %d\n", j + 1, i + 1);
						fnLDA_SetChannel(MyDevices[j], i + 1);	// the channel argument runs from 1 to N channels
						CheckAPISet(itemp);
					}

					if (fnLDA_GetFeatures(MyDevices[j]) & HAS_HIRES)
					{
						// Display the frequency related parameters
						itemp = fnLDA_GetWorkingFrequency(MyDevices[j]);
						ftemp = ((float)itemp) / 10;	// working frequency is in 100KHz units
						if (itemp >= 0)
							printf("Working Frequency = %.2f Mhz\n", ftemp);
						else
							CheckAPISet(itemp);
					}

					itemp = fnLDA_GetAttenuationHR(MyDevices[j]);
					ftemp = (float)itemp / 20;
					if (itemp >= 0)
						printf("Attenuation = %.2f db\n", ftemp);
					else
						CheckAPISet(itemp);

					itemp = fnLDA_GetRampStart(MyDevices[j]);
					ftemp = (float)(itemp * .25);
					if (itemp >= 0)
						printf("Ramp Start Level = %.2f db\n", ftemp);
					else
						CheckAPISet(itemp);

					itemp = fnLDA_GetRampEnd(MyDevices[j]);
					ftemp = (float)(itemp * .25);
					if (itemp >= 0)
						printf("Ramp End Level = %.2f db\n", ftemp);
					else
						CheckAPISet(itemp);

					itemp = fnLDA_GetAttenuationStep(MyDevices[j]);
					ftemp = (float)(itemp * .25);
					if (itemp >= 0)
						printf("First Phase Ramp Attenuation Step Size = %.2f db\n", ftemp);
					else
						CheckAPISet(itemp);

					if (fnLDA_GetFeatures(MyDevices[j]) > 0)
					{
						itemp = fnLDA_GetAttenuationStepTwo(MyDevices[j]);
						ftemp = (float)(itemp * .25);
						if (itemp >= 0)
							printf("Second Phase Ramp Attenuation Step Size = %.2f db\n", ftemp);
						else
							CheckAPISet(itemp);
					}

					itemp = fnLDA_GetDwellTime(MyDevices[j]);
					if (itemp >= 0)
						printf("First Phase Ramp Dwell Time = %d\n", itemp);
					else
						CheckAPISet(itemp);


					itemp = fnLDA_GetIdleTime(MyDevices[j]);
					if (itemp >= 0)
						printf("Ramp Idle Time = %d\n", itemp);
					else
						CheckAPISet(itemp);

					if (fnLDA_GetFeatures(MyDevices[j]) > 0)
					{
						itemp = fnLDA_GetHoldTime(MyDevices[j]);
						if (itemp >= 0)
							printf("Ramp Hold Time = %d\n", itemp);
						else
							CheckAPISet(itemp);
					}

					// show the profile values for this channel
					if (fnLDA_GetFeatures(MyDevices[j]) > 0 && gbPrintProfile)
					{
						NumProfileElements = fnLDA_GetProfileMaxLength(MyDevices[j]);
						printf("Maximum Profile Length = %d\n", NumProfileElements);

						itemp = fnLDA_GetProfileCount(MyDevices[j]);
						if (itemp >= 0)
							printf("Active Profile Length = %d\n", itemp);
						else
							CheckAPISet(itemp);

						if (NumProfileElements >= 0)
						{
							for (k = 0; k < NumProfileElements; k++)
							{
								itemp = fnLDA_GetProfileElementHR(MyDevices[j], k);
								if (itemp >= 0)
								{
									ftemp = (float)itemp / 20;		// Convert profile element attenuation to db 
									printf("  Profile Element %d =  %.1f db \n", k, ftemp);
								}
								else CheckAPISet(itemp);
							}
						}
					}
					printf("\n");

				} // end of our loop over channels
			} // end of our quiet mode case
		} // end of the for loop over the devices

		// if the user is trying to control a device we don't have, then quit now

		if (DevNum > NumDevices - 1) {
			for (j = 0; j < NumDevices; j++)
			{
				itemp = fnLDA_CloseDevice(MyDevices[j]);
			}
			printf("First selected device is not attached, exiting.\n");
			return 0;			// quit - nothing else to do
		}

		// if the user is trying to control more devices than we have, reduce the number of devices in the group
		if ((DevNum + DevRange) > NumDevices) {
			DevRange = NumDevices - DevNum;
			printf("Not enough attenuators connected, using %d devices.\n", DevRange);
		}

		// ------------- Now we'll set the requested device or devices with new parameters -------------
		if (!gbQuietMode)printf("Setting the attenuator parameters..\n");

		for (iDev = DevNum; iDev < DevNum + DevRange; iDev++)
		{
			// --- warn the user if they have an old LDA ---
			if (fnLDA_GetFeatures(MyDevices[iDev]) == 0) {
				printf(" *** Warning - device %d does not support all functions\n", iDev);
			}

			NumChannels = fnLDA_GetNumChannels(MyDevices[iDev]);

			if (NumChannels < 1 || NumChannels > 8) {
				continue;	// skip over this device, we don't have a valid channel count...
			}

			if (gbWantChannel)
			{
				if (!gbQuietMode) printf("Setting the channel for device %d to %d", MyDevices[iDev], Channel);
				itemp = fnLDA_SetChannel(MyDevices[iDev], Channel);
				CheckAPISet(itemp);
			}

			// -- Set the working frequency --
			if (gbWantSetWorkingFrequency) {

				if (fnLDA_GetFeatures(MyDevices[iDev]) & HAS_HIRES) {

					itemp = fnLDA_SetWorkingFrequency(MyDevices[iDev], WorkingFrequency);
					
					if (!gbQuietMode) {
						if (itemp == 0) {
							ftemp = (float)WorkingFrequency;
							ftemp = ftemp / 10;
							printf("Working Frequency set to  = %.2f Mhz\n", ftemp);
						}
						else
							CheckAPISet(itemp);
					}
				}
			}
			
			// --- Lets set the attenuation for the channel next ---
			if (gbWantSetAttenuation) {
				// using the HiRes API function with .05db units
				ScaledAttenuation = (int)(Attenuation * 20);

				// Set the selected channel with the attenuation
				if (!gbQuietMode) printf("Setting the attenuation for Channel %d to %.2f db\n", Channel, Attenuation);
				itemp = fnLDA_SetAttenuationHR(MyDevices[iDev], ScaledAttenuation);
				CheckAPISet(itemp);
			}

			// --- and then do whatever else the user requested ---
			if (gbWantSetDwell) {
				if (!gbQuietMode) printf("Setting the profile dwell time for device %d to %d ms\n", MyDevices[iDev], Dwell);
				itemp = fnLDA_SetProfileDwellTime(MyDevices[iDev], Dwell);
				CheckAPISet(itemp);
			}

			if (gbWantSetIdle) {
				if (!gbQuietMode) printf("Setting the idle time between repeating profiles for device %d to %d ms\n", MyDevices[iDev], IdleTime);
				itemp = fnLDA_SetProfileIdleTime(MyDevices[iDev], IdleTime);
				CheckAPISet(itemp);
			}

			if (gbWantSetProfileLength) {
				if (!gbQuietMode) printf("Setting profile length for device %d, channel %d to %d\n", MyDevices[iDev], Channel, ProfileLength);
					itemp = fnLDA_SetProfileCount(MyDevices[iDev], ProfileLength);
					CheckAPISet(itemp);
				}
			
			if (gbWantTestProfile) {

				// -- compute a sample profile --
				SineProfile(Test_Frequency, Test_Range, Test_Baseline);

				// -- download it to the device --
				NumProfileElements = fnLDA_GetProfileMaxLength(MyDevices[iDev]);
				if (NumProfileElements >= 0)
				{
					for (k = 0; k < NumProfileElements; k++)
					{
						itemp = fnLDA_SetProfileElementHR(MyDevices[iDev], k, TestProfile[k]);
						CheckAPISet(itemp);
					}
				}

			}
			
		}	// this is the end of our for loop over devices for the general commands

		// We will handle the case of multi-channel profiles separately

		// -- For multi channel profiles we first set the parameters, then send the actual command or commands to start the profiles
		//	  grouping these commands reduces the latency between the profiles on each attenuator
		//	  this code will work for devices with 1, 4 or 8 channels
		//	  Note that this command uses the same per channel settings for each device

		for (iDev = DevNum; iDev < DevNum + DevRange; iDev++)
		{
			if (gbWantMCProfile)
			{
				// --- first we'll get the number of channels for this device
				NumChannels = fnLDA_GetNumChannels(MyDevices[iDev]);

				if ((NumChannels <= 0) || (NumChannels > 8)) NumChannels = 1;	// defend against bad values

				// --- then we loop over the selected channels, generating a channel mask from our active channel list
				for (i = 0; i < NumToPlay; i++) {
					ChMask |= ChannelToMask(ChannelList[i]);		// add a bit to our mask for each active channel
				}

				// --- launch the set of selected profiles for this device ---
				if (!gbQuietMode) printf("Starting profiles for device %d\n", MyDevices[iDev]);
				itemp = fnLDA_StartProfileMC(MyDevices[iDev], Profile_mode, ChMask, FALSE);		// start the profiles immediately
				CheckAPISet(itemp);
			}
		} // this is the end of our for loop over selected devices for the multi channel profile command

		// -- Lets report on the device's operation for a little while, unless we are in batch mode
		if (!gbBatchMode)
		{
			j = 0;
			while (j < 10)
			{
				for (iDev = DevNum; iDev < DevNum + DevRange; iDev++)
				{
					// use the HiRes function and show all the channels for the device
					NumChannels = fnLDA_GetNumChannels(MyDevices[iDev]);
					if ((NumChannels <= 0) || (NumChannels > 64)) NumChannels = 1;	// defend against bad values

					for (k = 1; k <= NumChannels; k++)
					{
						fnLDA_SetChannel(MyDevices[iDev], k);
						ftemp = ((float)fnLDA_GetAttenuationHR(MyDevices[iDev])) / 20;
						printf("Attenuation = %.2f db for device %d, channel %d\n", ftemp, MyDevices[iDev], k);
					}
				}
				printf("\n");
				Sleep(200);		// wait for 1/5 second
				j++;
			}

		} // end of if not batch mode

		// -- we've done whatever the user wanted, time to close the devices
		for (j = 0; j < i; j++)
		{
			itemp = fnLDA_CloseDevice(MyDevices[j]);
		}

	} // end of if ( i > 0 ) -- "we have a device"

	return 0;
}