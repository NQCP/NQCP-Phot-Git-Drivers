//
//  Mulit_Channel_Demo.cpp
//
//  This program is an example of how to use the multiple channel SetAttenuation and StartRamp functions
//
// 
//  RD 1/15/2025	derived from LDA_Demo.cpp
//  NB 10/28/2025	changed name from LDA_Demo.cpp to Multi_Channel_Demo.cpp. Small updates to be consistent with other LDA example programs
//

#include "stdafx.h"
#include "vnx_LDA_api.h"

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
static int HoldTime = 1;			// default hold time is 1 ms
static float AStart = 0.0;			// default atten start level is 0 db.
static float AStop = 63.0;			// default atten stop, for most devices this is 63 db so we use that.
static int Dwell = 1000;			// default dwell time is 1 second for first ramp phase
static int Dwell2 = 1000;			// default dwell time is 1 second for second ramp phase (V2 LDA's only)
static float AStep = 1.0;			// default step size is 1.0 db, some LDA's have larger minimum steps
static float AStep2 = 1.0;			// default second phase step size for LDA's that support bidirectional ramps

static float WorkingFrequency = 0;	// working frequency for the HiRes attenuators in MHz
static float Attenuation = 0;		// default attenuation is 0db, entered as a floating point value

static int ScaledAttenuation = 0;	// temporary storage for scaled attenuation values
static int ScaledStart = 0;			// temporary storage for scaled start values
static int ScaledStop = 0;			// temporary storage for scaled stop values
static int ScaledStep = 0;			// temporary storage for scaled step values
static int ScaledStep2 = 0;			// temporary storage for scaled step2 values

static int SerialNumber = 0;		// used to hold the serial number for the get serial number command

static int GetParam = 0;			// the low byte is the GET command byte

static int ProfileIndex = 0;		// the element in the profile we want to set
static int ProfileLength = 0;		// the length of the profile
static int ProfileValue = 0;		// the profile element's value

static wchar_t ChannelList[65];	// the string listing channel numbers, ranges, or "all"
static int RampChannelList[8] = { 0, 0, 0, 0, 0, 0, 0, 0 };
static int RampChMask = 0;				// mask of active channel bits for MC profile play command
static int Channel = 1;				// temporary place holder for a single channel
static int NumToRamp = 0;			// number of channels we should ramp
static int RampMode = 0;

bool gbWantSetIdle = FALSE;
bool gbWantSetHold = FALSE;
bool gbWantSetAStart = FALSE;
bool gbWantSetAStop = FALSE;
bool gbWantSetDwell = FALSE;
bool gbWantSetDwell2 = FALSE;
bool gbWantStartSweep = FALSE;
bool gbWantSetAStep = FALSE;
bool gbWantSetAStep2 = FALSE;
bool gbWantSetWorkingFrequency = FALSE;
bool gbWantSetAttenuation = FALSE;
bool gbWantSaveSettings = FALSE;
bool gbWantGetParam = FALSE;
bool gbBatchMode = FALSE;
bool gbQuietMode = FALSE;
bool gbWantSetProfileElement = FALSE;
bool gbWantSetProfileLength = FALSE;
bool gbWantChannel = FALSE;
bool gbWantMCRamp = FALSE;
bool gbWantReadSettings = FALSE;




// ------------------------------- Support Routines --------------------------------------

void PrintHelp()
{
	printf("Vaunix Multiple Channel Attenuator Demonstration\n");
	printf("\n");
	printf("Hit CTRL+C to exit\n");
	printf("\n");

	printf(" --- Overall modes and device selection. Defaults to first device ---\n");
	printf("  -d i n	Select the devices to work with, i is the device number (1,2,3, etc.)\n");
	printf("			and n is the number of devices to apply the command to.\n");
	printf("			-d 1 2 applies the commands to attenuators 1 and 2.\n");
	printf("			-d 2 3 applies the commands to attenuators 2, 3 and 4.\n");
	printf("  -y		Save the current settings in the device for the selected channels.\n");
	printf("\n");
	printf("  -b		Batch mode, exit immediately after sending commands to the Lab Bricks.\n");
	printf("  -q		Quiet mode, skip most outputs.\n");
	printf("  -r		Display information about the device.\n");
	printf("\n");

	printf(" --- Commands to set parameters --- \n");
	printf("  -c <list> Set the active channels '1,2,4,5,8-15' or 'all'\n");
	printf("  -f nn		Set working frequency, nn is working frequency in MHz\n");
	printf("  -a nn		Set attenuation, nn is attenuation in db units\n");
	printf("  -w nn		Set idle time between attenuator ramps, nn is time in ms.\n");
	printf("  -h nn		Set hold time between ramp phases\n");
	printf("  -s nn		Set ramp start value, nn is start value in db units\n");
	printf("  -e nn		Set ramp end value, nn is end value in db units, p is ramp phase\n");
	printf("  -t p nn	Set time to dwell on each attenuation value, nn is time in ms., p is ramp phase 1 or 2\n");
	printf("  -i p nn	Set attenuation ramp increment, nn is the increment\n");
	printf("			in db units. p is ramp phase 1 or 2\n");
	printf("\n");
	printf(" --- Commands to start multiple ramps --- \n");
	printf("  -x m n c c...	Start multiple ramps, m is the mode: \n");
	printf("			1 = once upwards, 2 = continuous upwards,\n");
	printf("			5 = once down, 6 = continuous down,\n");
	printf("			17 = bidirectional once, 18 = continuous bidirectional ramps,\n");
	printf("			0 to stop the ramps\n");
	printf("			n = number of ramps, for each one c is the channel number\n");
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

// a helper function that converts a single channel to a mask in the format used
// by the fnLDA_StartRampMC and fnLDA_StartRampMC and fnLDA_StartProfileMC functions
int ChannelToMask(int channel)
{
	int mask = 1;
	if (channel < 1) channel = Channel;		// channel 0 signifies the current global channel
	return mask << (channel - 1);			// channel runs from 1 to 8
}

// a helper function that converts a list of channel numbers to a mask in the format used
// by the fnLDA_SetAttenuationMCHR function.
// The channel mask has 1 bits for every channel selected. Its LSB is channel 1, its MSB is channel 64
// The channel list is a string with channel numbers or ranges separated by commas (the function also accepts spaces as delimiters
// but the string from the command line will not have embedded spaces)
// For example, the string 1,3,7 would select channels 1, 3 and 7
// The channel list can also include ranges, the string 1-8 would select channels 1 through 8 inclusive
// If the channel list consists of the word all, then all channels are selected
void ChannelListToMask(unsigned long long * channelmask, wchar_t * channellist)
{
	unsigned long long cmask = 0;
	unsigned long long sel_mask;
	int i;
	int istart, iend;
	wchar_t * p_token;
	wchar_t * p_state;
	wchar_t * p_tmp;

	// change the input string to all lower case
	for (i = 0; i < wcslen(channellist); i++)
	{
		channellist[i] = towlower(channellist[i]);
	}

	// if the user entered "all" select all 64 channels
	// the SetAttenuationMCHR function ignores bits in the mask corresponding to channels it does not have
	if (wcscmp(channellist, L"all") == 0)
	{
		cmask = 0xFFFFFFFFFFFFFFFF;
		*channelmask = cmask;
		return;
	}

	// parse through the string, separating out each entry
	//p_token = wcstok(channellist, L", ", &p_state);
	p_token = wcstok_s(channellist, L", ", &p_state);
	while (p_token != NULL)
	{
		// lets look for a dash to see if we have a range
		p_tmp = wcspbrk(p_token, L"-");
		if (p_tmp != NULL)
		{
			// we have a dash in this token, so it is a range
			*p_tmp = 0;		// by replacing the "-" with a null character we split the token into two strings
			istart = _wtoi(p_token);
			p_tmp++;
			iend = _wtoi(p_tmp);

			// RD -- I don't ignore range inputs where _wtoi returns 0. They are probably typos, but a user
			//		 entering 0 for the first channel accidentally could occur.

			// clip the range start and stop values
			if (istart > 63) istart = 63;
			if (istart < 1) istart = 1;
			if (iend > 64) iend = 64;
			if (iend < 2) iend = 2;

			// add the bits for the selected range to the channel mask
			for (i = istart; i <= iend; i++)
			{
				sel_mask = 1i64 << (i - 1);	// generate the mask bit for this channel number
				cmask |= sel_mask;			// merge it into the channel mask
			}

		}

		// handle a token which is just a channel number
		i = _wtoi(p_token);
		
		if (i != 0)						// ignore any invalid tokens, probably a user typo
		{
			if (i > 64) i = 64;
			if (i < 1) i = 1;			// not really possible due to the filtering of - chars by the range parsing code...
			sel_mask = 1i64 << (i - 1);	// generate the mask bit for this channel number
			cmask |= sel_mask;			// merge it into the channel mask
		}
		p_token = wcstok_s(NULL, L", ", &p_state);
	}

	// return the mask
	*channelmask = cmask;
	return;
}


// ParseCommandLine() will return FALSE to indicate that we received an invalid
// command or should abort for another reason.
bool ParseCommandLine(int argc, _TCHAR *argv[])
{
	int RampPhase;
	int iActiveChannel = 0;

	enum {
		wantDash, wantDevSubstring, wantIdle, wantAStart, wantAStop, wantDwell, wantAStep,
		wantAtten, wantGetParam, wantDevID, wantDevRange, wantDwell2, wantAStep2,
		wantHold, wantDwellPhase, wantStepPhase, wantWorkingFrequency, wantChannel, 
		wantNumToRamp, wantRampCmd, wantActiveChannel
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
			else if (L"w" == thisParam) {
				gbWantSetIdle = TRUE;
				state = wantIdle;
			}
			else if (L"s" == thisParam) {
				gbWantSetAStart = TRUE;
				state = wantAStart;
			}
			else if (L"e" == thisParam) {
				gbWantSetAStop = TRUE;
				state = wantAStop;
			}
			else if (L"t" == thisParam) {
				state = wantDwellPhase;
			}
			else if (L"i" == thisParam) {
				state = wantStepPhase;
			}
			else if (L"a" == thisParam) {
				gbWantSetAttenuation = TRUE;
				state = wantAtten;
			}
			else if (L"y" == thisParam) {
				gbWantSaveSettings = TRUE;
				state = wantDash;
			}
			else if (L"b" == thisParam) {
				gbBatchMode = TRUE;
				state = wantDash;
			}
			else if (L"q" == thisParam) {
				gbQuietMode = TRUE;
				state = wantDash;
			}
			else if (L"r" == thisParam) {
				gbWantReadSettings = TRUE;
				state = wantDash;
			}
			else if (L"h" == thisParam) {
				gbWantSetHold = TRUE;
				state = wantHold;
			}
			else if (L"f" == thisParam) {
				gbWantSetWorkingFrequency = TRUE;
				state = wantWorkingFrequency;
			}
			else if (L"c" == thisParam) {
				gbWantChannel = TRUE;
				state = wantChannel;
			}
			else if (L"x" == thisParam) {
				gbWantMCRamp = TRUE;
				NumToRamp = 0;
				RampMode = 0;
				state = wantRampCmd;
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

			case wantDwellPhase:
				RampPhase = _wtoi(thisParam.c_str());
				if (RampPhase == 1) {
					gbWantSetDwell = TRUE;
					state = wantDwell;
				}
				else if (RampPhase == 2) {
					gbWantSetDwell2 = TRUE;
					state = wantDwell2;
				}
				else state = wantDash;		// phase value is wrong, not much we can do about it...
				break;

			case wantStepPhase:
				RampPhase = _wtoi(thisParam.c_str());
				if (RampPhase == 1) {
					gbWantSetAStep = TRUE;
					state = wantAStep;
				}
				else if (RampPhase == 2) {
					gbWantSetAStep2 = TRUE;
					state = wantAStep2;
				}
				else state = wantDash;		// phase value is wrong, not much we can do about it...
				break;

			case wantIdle:
				IdleTime = _wtoi(thisParam.c_str());		// convert to a int
				state = wantDash;
				break;

			case wantHold:
				HoldTime = _wtoi(thisParam.c_str());
				state = wantDash;
				break;

			case wantDevID:
				DevNum = _wtoi(thisParam.c_str());
				state = wantDevRange;
				break;

			case wantChannel:
				ChannelList[64] = 0;	// ensure the ChannelList string is null terminated
				wcsncpy_s(ChannelList, thisParam.c_str(), 64);	// copy limited to buffer size
				state = wantDash;
				break;

			case wantDevRange:
				DevRange = _wtoi(thisParam.c_str());
				state = wantDash;
				break;

			case wantAStart:
				AStart = (float)_wtof(thisParam.c_str());
				state = wantDash;
				break;

			case wantAStop:
				AStop = (float)_wtof(thisParam.c_str());
				state = wantDash;
				break;

			case wantDwell:
				Dwell = _wtoi(thisParam.c_str());
				state = wantDash;
				break;

			case wantDwell2:
				Dwell2 = _wtoi(thisParam.c_str());
				state = wantDash;
				break;

			case wantAStep:
				AStep = (float)_wtof(thisParam.c_str());
				state = wantDash;
				break;

			case wantAStep2:
				AStep2 = (float)_wtof(thisParam.c_str());
				state = wantDash;
				break;

			case wantAtten:
				Attenuation = (float)_wtof(thisParam.c_str());	// cast to a float, _wtof actually returns a double
				state = wantDash;
				break;

			case wantWorkingFrequency:
				WorkingFrequency = (float)_wtof(thisParam.c_str());	// cast to a float, _wtof actually returns a double
				state = wantDash;
				break;

			case wantRampCmd:
				RampMode = _wtoi(thisParam.c_str());
				state = wantNumToRamp;
				break;

			case wantNumToRamp:
				NumToRamp = _wtoi(thisParam.c_str());
				if (NumToRamp < 0) NumToRamp = 0;
				if (NumToRamp > 8) NumToRamp = 8;
				state = wantActiveChannel;
				break;

			case wantActiveChannel:
				RampChannelList[iActiveChannel] = _wtoi(thisParam.c_str());
				iActiveChannel++;
				if (iActiveChannel < NumToRamp) state = wantActiveChannel;
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
// ------------- Command Line Main ---------------------------------------------------

int _tmain(int argc, _TCHAR* argv[])
{
	int i, j, k;
	int iDev;
	int itemp;
	int itemp2;
	bool bTemp;
	float ftemp;
	int NumChannels;					// temporary storage for the number of channels in a device
	unsigned long long ExChannelMask;	// the mask of selected channels
	unsigned long long TestMask;		// used to test for selected channels in the ExChannelMask
	int ch;

	if (!ParseCommandLine(argc, argv))
		return 0;

	if (!gbQuietMode) printf("Lab Brick Attenuator Multiple Channel Demonstration Program\n");

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
	// fnLDA_SetTraceLevel(3, 3, false);

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
			fnLDA_SetTraceLevel(3, 3, false);
			itemp = fnLDA_InitDevice(MyDevices[j]);

			if (itemp) {
				printf("InitDevice returned error code %x\n", itemp);
			}

			fnLDA_SetTraceLevel(0, 0, false);

			// --- Lets see if we got the device's parameters ---
			if (!gbQuietMode && gbWantReadSettings) {

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
				ftemp = (float)(itemp * .25);
				if (itemp >= 0)
					printf("Minimum Attenuation = %.2f db\n", ftemp);
				else
					CheckAPISet(itemp);

				itemp = fnLDA_GetMaxAttenuation(MyDevices[j]);
				ftemp = (float)(itemp * .25);
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
					ftemp = (float)itemp / (float)20.0;
					if (itemp >= 0)
						printf("Attenuation = %.2f db\n", ftemp);
					else
						CheckAPISet(itemp);

					itemp = fnLDA_GetRampStartHR(MyDevices[j]);
					ftemp = (float)itemp / (float)20.0;
					if (itemp >= 0)
						printf("Ramp Start Level = %.2f db\n", ftemp);
					else
						CheckAPISet(itemp);

					itemp = fnLDA_GetRampEndHR(MyDevices[j]);
					ftemp = (float)(itemp * .05);
					if (itemp >= 0)
						printf("Ramp End Level = %.2f db\n", ftemp);
					else
						CheckAPISet(itemp);

					itemp = fnLDA_GetAttenuationStepHR(MyDevices[j]);
					ftemp = (float)(itemp * .05);
					if (itemp >= 0)
						printf("First Phase Ramp Attenuation Step Size = %.2f db\n", ftemp);
					else
						CheckAPISet(itemp);

					if (fnLDA_GetFeatures(MyDevices[j]) > 0)
					{
						itemp = fnLDA_GetAttenuationStepTwoHR(MyDevices[j]);
						ftemp = (float)(itemp * .05);
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

					if (fnLDA_GetFeatures(MyDevices[j]) > 0)
					{
						itemp = fnLDA_GetDwellTimeTwo(MyDevices[j]);
						if (itemp >= 0)
							printf("Second Phase Ramp Dwell Time = %d\n", itemp);
						else
							CheckAPISet(itemp);
					}

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

					printf("\n");

				} // end of our loop over channels

			} // end of our quiet mode read the settings case

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

		for (iDev = DevNum; iDev < DevNum + DevRange; iDev++) {

			// For this example we generate a 64 bit wide mask with a 1 bit for each channel
			// that the set attenuation command should change

			ExChannelMask = 0;
			if (gbWantChannel)
			{
				ChannelListToMask(&ExChannelMask, ChannelList);

				if (!gbQuietMode) printf("ExtendedChannelMask is %llx \n", ExChannelMask);
			}

			// --- Lets set the attenuation first using the multiple channel API function ---
			if (gbWantSetAttenuation) {

				// using the HiRes API function with .05db units
				ScaledAttenuation = (int)(Attenuation * 20);

				// Set the selected channels with the attenuation
				if (!gbQuietMode) printf("Setting the attenuation for channel in ExtendedChannelMask %llx to %.2f db\n", ExChannelMask, ((float)(ScaledAttenuation) / 20));
				itemp = fnLDA_SetAttenuationMCHR(MyDevices[iDev], ScaledAttenuation, ExChannelMask);

			}

			// --- and then do whatever else the user requested, looping over the selected channels
			TestMask = 1;

			// --- first we'll get the number of channels for this device
			NumChannels = fnLDA_GetNumChannels(MyDevices[iDev]);

			if ((NumChannels <= 0) || (NumChannels > 64)) NumChannels = 1;	// defend against bad values

			for (ch = 1; ch <= NumChannels; ch++)
			{
				if (TestMask & ExChannelMask)
				{
					// set the channel
					fnLDA_SetChannel(MyDevices[iDev], ch);	// the channel argument runs from 1 to N channels

					if (gbWantSetDwell) {

						if (!gbQuietMode) printf("Setting the first phase dwell time for device %d channel %d to %d\n", MyDevices[iDev], ch, Dwell);
						itemp = fnLDA_SetDwellTime(MyDevices[iDev], Dwell);
						CheckAPISet(itemp);
					}

					if (gbWantSetAStart) {

						// using the HiRes API function with .05db units
						ScaledAttenuation = (int)(AStart * 20);
						if (!gbQuietMode) printf("Setting the ramp start for device %d channel %d to %.2f db\n", MyDevices[iDev], ch, AStart);
						itemp = fnLDA_SetRampStartHR(MyDevices[iDev], ScaledAttenuation);
						CheckAPISet(itemp);
					}

					if (gbWantSetAStop) {

						// using the HiRes API function with .05db units
						ScaledStop = (int)(AStop * 20);
						if (!gbQuietMode) printf("Setting ramp end for device %d channel %d to %.2f db\n", MyDevices[iDev], ch, AStop);
						itemp = fnLDA_SetRampEndHR(MyDevices[iDev], ScaledStop);
						CheckAPISet(itemp);
					}

					if (gbWantSetAStep) {

						// using the HiRes API function with .05db units
						ScaledStep = (int)(AStep * 20);
						if (!gbQuietMode) printf("Setting the first phase attenuation step for device %d channel %d to %.2f db\n", MyDevices[iDev], ch, AStep);
						itemp = fnLDA_SetAttenuationStepHR(MyDevices[iDev], ScaledStep);
						CheckAPISet(itemp);
					}

					if (gbWantSetIdle) {

						if (!gbQuietMode) printf("Setting the idle time between ramps for device %d channel %d to %d ms\n", MyDevices[iDev], ch, IdleTime);
						itemp = fnLDA_SetIdleTime(MyDevices[iDev], IdleTime);
						CheckAPISet(itemp);
					}


					// if we have a V2 Lab Brick, send it the additional commands
					if (fnLDA_GetFeatures(MyDevices[iDev]) > 0)
					{
						if (gbWantSetAStep2)
						{
							// using the HiRes API function with .05db units
							ScaledStep2 = (int)(AStep2 * 20);
							if (!gbQuietMode) printf("Setting the second phase attenuation step for device %d channel %d to %.2f db\n", MyDevices[iDev], ch, AStep2);
							itemp = fnLDA_SetAttenuationStepTwoHR(MyDevices[iDev], ScaledStep2);
							CheckAPISet(itemp);
						}
						if (gbWantSetDwell2)
						{
							if (!gbQuietMode) printf("Setting the second phase dwell time for device %d channel %d to %d ms\n", MyDevices[iDev], ch, Dwell2);
							itemp = fnLDA_SetDwellTimeTwo(MyDevices[iDev], Dwell2);
							CheckAPISet(itemp);
						}
						if (gbWantSetHold)
						{
							if (!gbQuietMode) printf("Setting the hold time between ramp phases for device %d channel %d to %d ms\n", MyDevices[iDev], ch, HoldTime);
							itemp = fnLDA_SetHoldTime(MyDevices[iDev], HoldTime);
							CheckAPISet(itemp);
						}

						if (fnLDA_GetFeatures(MyDevices[iDev]) & HAS_HIRES)
						{
							// RD 1-14-25 cleaning up a needless message..
							if (gbWantSetWorkingFrequency)
							{
								// make sure the desired working frequency is in range for this device
								itemp = fnLDA_GetMinWorkingFrequency(MyDevices[iDev]);
								CheckAPISet(itemp);
								itemp2 = (int)(WorkingFrequency * 10);					// converting from Mhz to 100KHz integer units

								// clip the min value for this device and let the user know
								if ((itemp >= 0) && (itemp2 < itemp))
								{
									if (!gbQuietMode) printf("Working frequency for device %d of %.2f Mhz too low\n", MyDevices[iDev], WorkingFrequency);
									itemp2 = itemp;
								}

								itemp = fnLDA_GetMaxWorkingFrequency(MyDevices[iDev]);
								CheckAPISet(itemp);

								// clip the max value for this device and let the user know
								if ((itemp >= 0) && (itemp2 > itemp))
								{
									if (!gbQuietMode) printf("Working frequency for device %d of %.2f Mhz too high\n", MyDevices[iDev], WorkingFrequency);
									itemp2 = itemp;
								}

								ftemp = (float)(itemp2) / 10;

								if (!gbQuietMode) printf("Setting the working frequency for device %d channel %d to %.2f Mhz\n", MyDevices[iDev], Channel, ftemp);

								itemp = fnLDA_SetWorkingFrequency(MyDevices[iDev], itemp2);
								CheckAPISet(itemp);

							}
						}
					}

					if (gbWantSaveSettings)
					{
						if (!gbQuietMode) printf("Saving the settings for device %d channel %d\n", MyDevices[iDev], ch);
						itemp = fnLDA_SaveSettings(MyDevices[iDev]);
						CheckAPISet(itemp);
						Sleep(100);
					}

				}	// end of if active channel bit test

				TestMask <<= 1;		// move our test bit over to test the next channel's selection bit

			}	// end of loop over NumChannels for this device
		}	// this is the end of our for loop over devices for the general commands
		
		if (!gbQuietMode) printf("\n");
		// --- Now we will handle the case of multi-channel ramps, controlled by the channel list ---
		// -- For multi channel ramps we first set the parameters, then send the actual commands to start the ramps
		//	  grouping these commands reduces the latency between the ramps on each attenuator
		//	  Note that this command uses the same per channel settings for each device
		// --- then we loop over the selected channels, generating a channel mask from our active channel list
		for (i = 0; i < NumToRamp; i++) {
			RampChMask |= ChannelToMask(RampChannelList[i]);		// add a bit to our mask for each active channel
		}

		for (iDev = DevNum; iDev < DevNum + DevRange; iDev++)
		{
			if (gbWantMCRamp)
			{
				// --- first we'll get the number of channels for this device
				NumChannels = fnLDA_GetNumChannels(MyDevices[iDev]);
				if ((NumChannels <= 0) || (NumChannels > 64)) NumChannels = 1;	// defend against bad values

				// --- then we loop over the channels, setting the ramp parameters from our array
				//     for each channel in our channel selection mask (and therefore in the channel selection list)
				TestMask = 1;
				for (ch = 1; ch <= NumChannels; ch++)
				{
					if (TestMask & RampChMask)
					{
						fnLDA_SetChannel(MyDevices[iDev], ch);	// the channel argument runs from 1 to N channels
						i = ch - 1;

						if (RampMode != 0)
						{
							// --- The user wants to start some kind of an attenuation ramp ---
							if (RampMode & CL_SWP_DIRECTION)
							{
								bTemp = FALSE;
							}
							else
							{
								bTemp = TRUE;
							}	// NB -- the flag is TRUE for "up" in the Set...Direction call.
								// but the old test program uses a 0 bit for up, and a 1 bit for down...

							itemp = fnLDA_SetRampDirection(MyDevices[iDev], bTemp);
							CheckAPISet(itemp);

							// --- and now we'll do the mode - one time or repeated ---
							if (RampMode & CL_SWP_ONCE)
							{
								bTemp = FALSE;
							}
							else
							{
								bTemp = TRUE;
							}	// NB -- the flag is TRUE for "repeated" in the SetSweepMode call.
							// but the old test program encodes the modes differently

							itemp = fnLDA_SetRampMode(MyDevices[iDev], bTemp);
							CheckAPISet(itemp);

							// --- and then the bidirectional ramp control if the device is a V2 device
							if (fnLDA_GetFeatures(MyDevices[iDev]) > 0)
							{
								if (RampMode & CL_SWP_BIDIRECTIONALLY)
								{
									bTemp = TRUE;
								}							// the command line has true for bidirectional 
								else						// as does the actual HW command...
								{
									bTemp = FALSE;
								}

								itemp = fnLDA_SetRampBidirectional(MyDevices[iDev], bTemp);
								CheckAPISet(itemp);
							}

						}
					}

					TestMask <<= 1;		// move to the next channel
				}

				// start or stop the ramps for the selected channels 
				if (RampMode == 0)
				{
					if (!gbQuietMode) printf("Stopping the selected attenuation ramps for channel in RampChMask %x for device %d\n", RampChMask, MyDevices[iDev]);
					itemp = fnLDA_StartRampMC(MyDevices[iDev], FALSE, RampChMask, FALSE);
					CheckAPISet(itemp);
				}
				else
				{
					if (!gbQuietMode) printf("Starting the selected attenuation ramp for channel in RampChMask %x for device %d\n", RampChMask, MyDevices[iDev]);
					itemp = fnLDA_StartRampMC(MyDevices[iDev], RampMode, RampChMask, FALSE);
					CheckAPISet(itemp);
				}
			}
		} // this is the end of our for loop over selected devices for the multi channel ramp command


		// -- Lets report on the device's operation for a little while, unless we are in batch mode
		if (!gbBatchMode)
		{

			j = 0;
			while (j < 400)
			{
				for (iDev = DevNum; iDev < DevNum + DevRange; iDev++)
				{
					// use the HiRes function and show all the channels for the device
					NumChannels = fnLDA_GetNumChannels(MyDevices[iDev]);
					if ((NumChannels <= 0) || (NumChannels > 64)) NumChannels = 1;	// defend against bad values

					for (k = 1; k <= NumChannels; k++)
					{
						fnLDA_SetChannel(MyDevices[iDev], k);

						// show the per channel status for ramps and profiles
						itemp = fnLDA_GetDeviceStatus(MyDevices[iDev]);
						//printf("GetDeviceStatus returned: %x ", itemp);

						if (itemp & SWP_ACTIVE)
						{
							printf("Ramp in progress on channel %d\n", k);
						}
						if (itemp & PROFILE_ACTIVE)
						{
							printf("Profile in progress on channel %d\n", k);
						}

						ftemp = ((float)fnLDA_GetAttenuationHR(MyDevices[iDev])) / 20;
						printf("Attenuation = %.2f db for device %d, channel %d\n", ftemp, MyDevices[iDev], k);

					}
				}
				printf("\n");
				Sleep(100);		// wait for 0.1  second
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

// ===================== end of main ======================================
