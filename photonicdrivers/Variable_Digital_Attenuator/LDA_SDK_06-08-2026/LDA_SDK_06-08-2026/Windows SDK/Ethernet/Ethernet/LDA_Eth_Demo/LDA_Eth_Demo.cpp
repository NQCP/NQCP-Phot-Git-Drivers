// LDA_Eth_Demo.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "stdafx.h"
#include "ldadrvr.h"

using namespace std;


#define THIS_FILE_DATE "5-20-2026"

const char* ldadevices[] = {"192.168.100.5"};
#define DEBUG_LEVEL 1
#define LDA_DEVICES  (sizeof(ldadevices)/sizeof(ldadevices[0]))

// IP Address Validator
#define DELIM "."

// ------------------------------ - Equates-----------------------------------------------
#define CL_SWP_DIRECTION		0x04	// MASK: bit = 0 for ramp up, 1 for ramp down 
#define CL_SWP_CONTINUOUS		0x02	// MASK: bit = 1 for continuous ramping
#define CL_SWP_ONCE				0x01	// MASK: bit = 1 for single ramp
#define CL_SWP_BIDIRECTIONALLY	0x10	// MASK: bit = 1 for bidirectional ramps (V2 LDA's only)

// --------------------------- Variables -------------------------------------------------
static char *ndeviceip;
static int IdleTime = 1;			// default idle time is 1 ms
static int HoldTime = 1;			// default hold time is 1 ms
static float AStart = 0;				// default atten start level is 0 db.
static float AStop = 252;				// default atten stop, for most devices this is 63 db so we use that.
static int Dwell = 1000;			// default dwell time is 1 second for first ramp phase
static int Dwell2 = 1000;			// default dwell time is 1 second for second ramp phase (V2 LDA's only)
static float AStep = 2;				// default step size is .5db, some LDA's have larger minimum steps
static float AStep2 = 2;				// default second phase step size for LDA's that support bidirectional ramps

static int WorkingFrequency = 0;	// working frequency for the HiRes attenuators
static float Attenuation = 0;		// default attenuation is 0db, entered as a floating point value

static int ScaledAttenuation = 0;	// temporary storage for scaled attenuation values
static int SerialNumber = 0;		// used to hold the serial number for the get serial number command

static int RFOnOff = 1;				// really used as a bool -- if non zero, turn on the RF output

static int Sweep_mode = 0;			// used to control the sweep mode
static int GetParam = 0;			// the low byte is the GET command byte

static int ProfileIndex = 0;		// the element in the profile we want to set
static int ProfileLength = 0;		// the length of the profile
static int ProfileValue = 0;		// the profile element's value

static int Channel = 1;				// we just default to the first channel
static int RampChannelList[8] = { 0, 0, 0, 0, 0, 0, 0, 0 };
static int RampChMask = 0;
static int NumToRamp = 0;			// number of channels we should ramp (also used as an index -- post increment!)
static int RampMode = 0;
static char gldadevicesip[16];       // devices ip address

bool gbDeviceOpen = FALSE;
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
bool gbWantSetRFOnOff = FALSE;
bool gbQuietMode = FALSE;
bool gbWantSetProfileElement = FALSE;
bool gbWantSetProfileLength = FALSE;
bool gbWantChannel = FALSE;
bool gbWantMCRamp = FALSE;


//***************************************************************************
//
// Validate netconfig digits and return 1 if string contain only digits, else return 0
//
//*****************************************************************************
static int valid_digit(char *ip_str){
    while (*ip_str) {
        if (*ip_str >= '0' && *ip_str <= '9')
            ++ip_str;
        else
            return 0;
    }
    return 1;
}

//***************************************************************************
//
// Validate IP Configuration -return 1 if IP string is valid, else return 0
//
//*****************************************************************************
static int is_valid_ip(char *ip_str){
    int num, dots = 0;
    char *ptr;
    char lstr[16];
    char* next_token;

	strcpy_s(lstr,ip_str);

    if (lstr == NULL)
        return 0;

    ptr = strtok_s(lstr, DELIM, &next_token);

    if (ptr == NULL)
        return 0;

    while (ptr) {

        /* after parsing string, it must contain only digits */
        if (!valid_digit(ptr))
            return 0;

        num = atoi(ptr);

        /* check for valid IP */
        if (num >= 0 && num <= 255) {
            /* parse remaining string */
            ptr = strtok_s(NULL, DELIM, &next_token);
            if (ptr != NULL)
                ++dots;
        } else
            return 0;
    }

    /* valid IP string must contain 3 dots */
    if (dots != 3)
        return 0;
    return 1;
}

void PrintHelp()
{
	printf("Vaunix Attenuator Demonstration\n");
	printf("\n");
	printf("Hit CTRL+C to exit\n");
	printf("\n");

	printf(" --- Overall modes and device selection based on ip address ---\n");
	printf("  -d i 		Select the device to work with, i is the device ip address (192.168.100.11)\n");
	printf("  -r  		Read the current information of the device\n");
	printf("  -y		Save the current settings in the device.\n");
	printf("\n");
	printf("  -b		Batch mode, exit immediately after sending commands to the Lab Bricks.\n");
	printf("  -q		Quiet mode, skip most outputs.\n");
	printf("\n");

	printf(" --- Commands to set parameters and start ramp --- \n");
	printf("  -c n      Set the active channel\n");
	printf("  -f nn     Set working frequency, nn is working frequency in MHz\n");
	printf("  -a nn     Set attenuation, nn is attenuation in db units\n");
	printf("  -w nn     Set idle time between attenuator ramps, nn is time in ms.\n");
	printf("  -h nn     Set hold time between ramp phases\n");
	printf("  -s nn     Set ramp start value, nn is start value in db units\n");
	printf("  -e nn     Set ramp end value, nn is end value in db units\n");
	printf("  -t p nn   Set time to dwell on each attenuation value, nn is time in ms., p is ramp phase 1 or 2\n");
	printf("  -i p nn   Set attenuation ramp increment, nn is the increment\n");
	printf("            in db units. p is ramp phase 1 or 2\n");
	printf("  -g n      Start a ramp, 1 = once upwards, 2 = continuous upwards\n");
	printf("            5 = once down, 6 = continuous down, 17 = bidirectional once,\n");
	printf("            18 = continuous bidirectional ramps, 0 to stop\n");
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

// a helper function that converts a single channel to a mask in the format used
// by the fnLDA_StartRampMC and fnLDA_StartRampMC and fnLDA_StartProfileMC functions
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
	int RampPhase;
	char devipstr[16];
	size_t icount;
	int iActiveChannel = 0;

	enum {
		wantDash, wantIdle, wantAStart, wantAStop, wantDwell, wantAStep,
		wantAtten, wantSetRFOnOff, wantSweep, wantGetParam, wantDevID,
		wantDwell2, wantAStep2, wantHold, wantDwellPhase, wantStepPhase, wantWorkingFrequency,
		wantChannel, wantNumToRamp, wantRampCmd, wantActiveChannel
	} state = wantDash;

	for (int i = 1; i < argc; ++i) {
		// Convert each argument to lowercase
		wstring thisParam(argv[i]);
		for_each(thisParam.begin(), thisParam.end(), MakeLowerW);

		printf("string:%ls\n",thisParam.c_str());

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
			else if (L"r" == thisParam) {
				gbWantGetParam = TRUE;
				state = wantDash;
			}
			else if (L"w" == thisParam) {
				gbWantSetIdle  = TRUE;
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
			else if (L"g" == thisParam) {
				gbWantStartSweep = TRUE;
				state = wantSweep;
			}
			else if (L"r" == thisParam) {
				gbWantSetRFOnOff = TRUE;
				state = wantSetRFOnOff;
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
			else if ('x' == thisParam[0]) {
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

			switch (state){

			case wantDevID:
				wcstombs_s(&icount, devipstr, sizeof(devipstr), thisParam.c_str(), sizeof(devipstr));
				if(is_valid_ip(devipstr))
				{
					strcpy_s(gldadevicesip, devipstr);
//					printf("Device IP Address:%s\n",gldadevicesip);
					gbDeviceOpen = TRUE;
				}
				else
					printf("Invalid IP Address\n");
				state = wantDash;
				break;

			case wantDwellPhase:
				RampPhase = _wtoi(thisParam.c_str());
				if (RampPhase == 1){
					gbWantSetDwell = TRUE;
					state = wantDwell;
				}
				else if (RampPhase == 2){
					gbWantSetDwell2 = TRUE;
					state = wantDwell2;
				}
				else state = wantDash;		// phase value is wrong, not much we can do about it...
				break;

			case wantStepPhase:
				RampPhase = _wtoi(thisParam.c_str());
				if (RampPhase == 1){
					gbWantSetAStep = TRUE;
					state = wantAStep;
				}
				else if (RampPhase == 2){
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

			case wantChannel:
				Channel = _wtoi(thisParam.c_str());
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
				AStep =  (float)_wtof(thisParam.c_str());
				state = wantDash;
				break;

			case wantAStep2:
				AStep2 =  (float)_wtof(thisParam.c_str());
				state = wantDash;
				break;

			case wantAtten:
				Attenuation = (float)_wtof(thisParam.c_str());	// cast to a float, _wtof actually returns a double
				state = wantDash;
				break;

			case wantWorkingFrequency:
				WorkingFrequency = (int)_wtof(thisParam.c_str());	// cast to a float, _wtof actually returns a double
				state = wantDash;
				break;

			case wantSetRFOnOff:
				RFOnOff = _wtoi(thisParam.c_str());
				state = wantDash;
				break;

			case wantSweep:
				Sweep_mode = _wtoi(thisParam.c_str());
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


int _tmain(int argc, _TCHAR* argv[])
{
    bool realhardware;
    unsigned int index=0;
    float fdata;
	bool bTemp;
	int i;
	int TestMask;
    LDADEVICE_DATA_T  ldadevicedata[LDA_DEVICES]; // MAX DEVICES list

	if (!ParseCommandLine(argc, argv))
		return 0;

	// LDA Data Structure Initialization
    fnLDA_Init();
	
    /* If you have actual hardware attached, set this to TRUE. Setting to FALSE will run in test mode */
    realhardware = TRUE;
    fnLDA_SetTestMode(!realhardware);

	// Initialize the LDA Device
	if(gbDeviceOpen)
	{
	    if (fnLDA_InitDevice((char *)gldadevicesip))
	        printf("Device Connection Error:%s\n", gldadevicesip);
		else
			printf("Device Connection Success:%s\n", gldadevicesip);		
	}

	//Set channel
	if (gbWantChannel)
	{
		if (!gbQuietMode) printf("Setting the channel for device %s to %d\n", gldadevicesip, Channel);
		fnLDA_SetChannel((char *)gldadevicesip, Channel);
	}

	// Set Frequency
	if(gbWantSetWorkingFrequency)
	{
		if (!gbQuietMode) printf("Working Frequency set to %d Mhz\n", WorkingFrequency);
		fnLDA_SetWorkingFrequency((char *)gldadevicesip, WorkingFrequency*10);
	}

	// Set Attenuation
	if(gbWantSetAttenuation)
	{
		// using the HiRes API function with .05db units
		ScaledAttenuation = (int)(Attenuation * 20);
		
		// Set the selected channel with the attenuation
		if (!gbQuietMode) printf("Setting the attenuation for device %s to %.2f db\n", gldadevicesip, Attenuation);
		fnLDA_SetAttenuation((char *)gldadevicesip, ScaledAttenuation);
	}

	
	// Idle time
	if(gbWantSetIdle)
	{
		if (!gbQuietMode) printf("Setting the idle time between ramps for device %s to %d ms\n", gldadevicesip, IdleTime);
		fnLDA_SetIdleTime((char *)gldadevicesip, IdleTime);
	}

	// Hold time
	if(gbWantSetHold)
	{
		if (!gbQuietMode) printf("Setting the hold time between ramp phases for device %s to %d ms\n", gldadevicesip, HoldTime);
		fnLDA_SetHoldTime((char *)gldadevicesip, HoldTime);
	}

	// DWell time
	if (gbWantSetDwell){
	
		if (!gbQuietMode) printf("Setting the first phase dwell time for device %s to %d ms\n", gldadevicesip, Dwell);
		fnLDA_SetDwellTime((char *)gldadevicesip, Dwell);
	}

	// Dwell time2
	if (gbWantSetDwell2)
	{
		if (!gbQuietMode) printf("Setting the second phase dwell time for device %s to %d ms\n", gldadevicesip, Dwell2);
		fnLDA_SetDwellTimeTwo((char *)gldadevicesip, Dwell2);
	}

	// Ramp Start
	if (gbWantSetAStart){
	
		if (!gbQuietMode) printf("Setting the ramp start for device %s to %.2f db\n", gldadevicesip, AStart);
		fnLDA_SetRampStart((char *)gldadevicesip, (int)(AStart*20.0));
	}

	// Ramp Stop
	if (gbWantSetAStop){
	
		if (!gbQuietMode) printf("Setting ramp end for device %s to %.2f db\n", gldadevicesip, AStop);
		fnLDA_SetRampEnd((char *)gldadevicesip, (int)(AStop*20.0));
	}


	if (gbWantSetAStep){
		if (!gbQuietMode) printf("Setting the first phase attenuation step for device %s to %.2f db\n",gldadevicesip, AStep);
		fnLDA_SetAttenuationStep((char *)gldadevicesip,(int)(AStep*20.0));
	}


	if (gbWantSetAStep2){
		if (!gbQuietMode) printf("Setting the second phase attenuation step for device %s to %.2f db\n",gldadevicesip, AStep2);
		fnLDA_SetAttenuationStepTwo((char *)gldadevicesip,(int)(AStep2*20.0));
	}

	// Ramp Mode and Direction
	if (gbWantStartSweep)
	{
		if (Sweep_mode == 0)
		{
			if (!gbQuietMode) printf("Stopping the Attenuation Ramp\n");
			fnLDA_StartRamp((char*)gldadevicesip, FALSE);

		}
		else
		{

			// --- The user wants to start some kind of an attenuation ramp ---
			if (Sweep_mode & CL_SWP_DIRECTION)
			{
				bTemp = FALSE;
			}
			else
			{
				bTemp = TRUE;
			}	// NB -- the flag is TRUE for "up" in the Set...Direction call.
			// but the old test program uses a 0 bit for up, and a 1 bit for down...

			fnLDA_SetRampDirection((char*)gldadevicesip, bTemp);

			// --- and now we'll do the mode - one time or repeated ---
			if (Sweep_mode & CL_SWP_ONCE)
			{
				bTemp = FALSE;
			}
			else
			{
				bTemp = TRUE;
			}	// NB -- the flag is TRUE for "repeated" in the SetSweepMode call.
			// but the old test program encodes the modes differently

			fnLDA_SetRampMode((char*)gldadevicesip, bTemp);

			if (Sweep_mode & CL_SWP_BIDIRECTIONALLY)
			{
				bTemp = TRUE;
			}							// the command line has true for bidirectional 
			else						// as does the actual HW command...
			{
				bTemp = FALSE;
			}

			printf("Bidirection mode set to %x \n", bTemp);
			fnLDA_SetRampBidirectional((char*)gldadevicesip, bTemp);

			if (!gbQuietMode) printf("Starting an attenuation ramp for device %s\n", gldadevicesip);
			fnLDA_StartRamp((char*)gldadevicesip, TRUE);

		}
	}

	if (gbWantMCRamp)
	{
		// --- Now we will handle the case of multi-channel ramps, controlled by the channel list ---
		// -- For multi channel ramps we first set the parameters, then send the actual commands to start the ramps
		//	  grouping these commands reduces the latency between the ramps on each attenuator
		//	  Note that this command uses the same per channel settings for each device
		// --- then we loop over the selected channels, generating a channel mask from our active channel list
		for (i = 0; i < NumToRamp; i++) {
			RampChMask |= ChannelToMask(RampChannelList[i]);		// add a bit to our mask for each active channel
		}

		// --- first we'll get the number of channels for this device
		fnLDA_GetMaxChannels((char*)gldadevicesip, &ldadevicedata[index].maxchannels);
		if ((ldadevicedata[index].maxchannels <= 0) || (ldadevicedata[index].maxchannels > 64)) ldadevicedata[index].maxchannels = 1;	// defend against bad values

		// --- then we loop over the channels, setting the ramp parameters from our array
		//     for each channel in our channel selection mask (and therefore in the channel selection list)
		TestMask = 1;
		for (int ch = 1; ch <= ldadevicedata[index].maxchannels; ch++)
		{
			if (TestMask & RampChMask)
			{
				fnLDA_SetChannel((char*)gldadevicesip, ch);	// the channel argument runs from 1 to N channels
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

					fnLDA_SetRampDirection((char*)gldadevicesip, bTemp);

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

					fnLDA_SetRampMode((char*)gldadevicesip, bTemp);

					// --- and then the bidirectional ramp control if the device is a V2 device
					fnLDA_GetFeatures((char*)gldadevicesip, &ldadevicedata[index].device_features);
					if (ldadevicedata[index].device_features > 0)
					{
						if (RampMode & CL_SWP_BIDIRECTIONALLY)
						{
							bTemp = TRUE;
						}							// the command line has true for bidirectional 
						else						// as does the actual HW command...
						{
							bTemp = FALSE;
						}

						fnLDA_SetRampBidirectional((char*)gldadevicesip, bTemp);
					}

				}
			}

			TestMask <<= 1;		// move to the next channel
		}

		// start or stop the ramps for the selected channels 
		if (RampMode == 0)
		{
			if (!gbQuietMode) printf("Stopping the selected attenuation ramps for channel in RampChMask %x for device %s\n", RampChMask, (char*)gldadevicesip);
			fnLDA_StartRampMC((char*)gldadevicesip, FALSE, RampChMask, FALSE);
		}
		else
		{
			if (!gbQuietMode) printf("Starting the selected attenuation ramp for channel in RampChMask %x for device %s\n", RampChMask, (char*)gldadevicesip);
			fnLDA_StartRampMC((char*)gldadevicesip, RampMode, RampChMask, FALSE);
		}
	}
	
	// Save settings
	if (gbWantSaveSettings)
	{
		if (!gbQuietMode) printf("Saving the settings for device %s\n", gldadevicesip);
		fnLDA_SaveSettings((char *)gldadevicesip);
	}

	if (gbWantGetParam)
	{
		if (fnLDA_CheckDeviceReady((char*)gldadevicesip) == STATUS_OK)
		{
			// Device IP
			printf("Device IP:%s\n", gldadevicesip);
			printf("----------------------------------------------\n");

			// Device Name
			fnLDA_GetModelName((char*)gldadevicesip, ldadevicedata[index].modelname);
			printf("Model Name:%s\n", ldadevicedata[index].modelname);

			// Serial#
			fnLDA_GetSerialNumber((char*)gldadevicesip, &ldadevicedata[index].serialnumber);
			printf("Serial Number:%d\n", ldadevicedata[index].serialnumber);

			// Sw Version #
			fnLDA_GetSoftwareVersion((char*)gldadevicesip, ldadevicedata[index].swversion);
			printf("SW Version:%s\n", ldadevicedata[index].swversion);

			// Device Features
			fnLDA_GetFeatures((char*)gldadevicesip, &ldadevicedata[index].device_features);
			printf("Device Features:0b");
			for (int i = 8; i >= 0; i--)
			{
				printf("%d", (ldadevicedata[index].device_features >> i) & 1);
			}
			printf("\n");

			// IP Mode
			fnLDA_GetIPMode((char*)gldadevicesip, &ldadevicedata[index].ipmode);
			printf("IP Mode:%d\n", ldadevicedata[index].ipmode);

			// IP Address
			fnLDA_GetIPAddress((char*)gldadevicesip, ldadevicedata[index].ipaddress);
			printf("IP Address:%s\n", ldadevicedata[index].ipaddress);

			// Netmask
			fnLDA_GetNetmask((char*)gldadevicesip, ldadevicedata[index].netmask);
			printf("Subnet Mask:%s\n", ldadevicedata[index].netmask);

			// Gateway
			fnLDA_GetGateway((char*)gldadevicesip, (char*)ldadevicedata[index].gateway);
			printf("Gateway:%s\n", ldadevicedata[index].gateway);

			// Min Frequency
			fnLDA_GetMinWorkingFrequency((char*)gldadevicesip, &ldadevicedata[index].minfrequency);
			printf("Min Frequency:%d\n", (ldadevicedata[index].minfrequency / 10));

			// Max Frequency
			fnLDA_GetMaxWorkingFrequency((char*)gldadevicesip, &ldadevicedata[index].maxfrequency);
			printf("Max Frequency:%d\n", (ldadevicedata[index].maxfrequency / 10));

			// Min Attenuation
			fnLDA_GetMinAttenuation((char*)gldadevicesip, &ldadevicedata[index].minattenuation);
			fdata = (float)(ldadevicedata[index].minattenuation / 20.0);
			printf("Min Attenuation:%f\n", fdata);

			// Max Attenuation
			fnLDA_GetMaxAttenuation((char*)gldadevicesip, &ldadevicedata[index].maxattenuation);
			fdata = (float)(ldadevicedata[index].maxattenuation / 20.0);
			printf("Max Attenuation:%f\n", fdata);

			// Channel #
			fnLDA_GetChannel((char*)gldadevicesip, &ldadevicedata[index].rf_channel);
			printf("Channel:%d\n", ldadevicedata[index].rf_channel);

			// Current Frequency
			fnLDA_GetWorkingFrequency((char*)gldadevicesip, &ldadevicedata[index].rf_current_frequency);
			printf("Frequency:%d\n", (ldadevicedata[index].rf_current_frequency / 10));

			// Current Attenuation
			fnLDA_GetAttenuation((char*)gldadevicesip, &ldadevicedata[index].rf_attenuation);
			fdata = (float)(ldadevicedata[index].rf_attenuation / 20.0);
			printf("Attenuation:%f\n", fdata);

			// RF On/Off State
			fnLDA_GetRF_On((char*)gldadevicesip, &ldadevicedata[index].rf_on);
			printf("RF On/Off State:%d\n", (ldadevicedata[index].rf_on));

			// Ramp Start
			fnLDA_GetRampStart((char*)gldadevicesip, &ldadevicedata[index].rampstart_attenuation);
			fdata = (float)(ldadevicedata[index].rampstart_attenuation / 20.0);
			printf("Ramp Start:%f\n", fdata);

			// Ramp End
			fnLDA_GetRampEnd((char*)gldadevicesip, &ldadevicedata[index].rampstop_attenuation);
			fdata = (float)(ldadevicedata[index].rampstop_attenuation / 20.0);
			printf("Ramp Stop:%f\n", fdata);

			// Attenuation Step
			fnLDA_GetAttenuationStep((char*)gldadevicesip, &ldadevicedata[index].attenuationstep);
			fdata = (float)(ldadevicedata[index].attenuationstep / 20.0);
			printf("Attenuation Step:%.2f\n", fdata);

			// Attenuation Step Two
			fnLDA_GetAttenuationStepTwo((char*)gldadevicesip, &ldadevicedata[index].attenuationsteptwo);
			fdata = (float)(ldadevicedata[index].attenuationsteptwo / 20.0);
			printf("Attenuation Step Two:%.2f\n", fdata);

			// Dwell Time
			fnLDA_GetDwellTime((char*)gldadevicesip, &ldadevicedata[index].ramp_dwelltime);
			printf("Dwell Time:%d\n", (ldadevicedata[index].ramp_dwelltime));

			// Dwell Time2
			fnLDA_GetDwellTimeTwo((char*)gldadevicesip, &ldadevicedata[index].ramp_bidirectional_dwelltime);
			printf("Bi-directional Dwell Time:%d\n", (ldadevicedata[index].ramp_bidirectional_dwelltime));

			// Idle Time
			fnLDA_GetIdleTime((char*)gldadevicesip, &ldadevicedata[index].ramp_idletime);
			printf("Idle Time:%d\n", (ldadevicedata[index].ramp_idletime));

			// Hold Time
			fnLDA_GetHoldTime((char*)gldadevicesip, &ldadevicedata[index].ramp_holdtime);
			printf("Hold Time:%d\n", (ldadevicedata[index].ramp_holdtime));

			// Get Profile Count
			fnLDA_GetProfileCount((char*)gldadevicesip, &ldadevicedata[index].profile_count);
			printf("Profile Count:%d\n", (ldadevicedata[index].profile_count));

			// Get Profile Max Length
			fnLDA_GetProfileMaxLength((char*)gldadevicesip, &ldadevicedata[index].profile_maxlength);
			printf("Profile Max Length:%d\n", (ldadevicedata[index].profile_maxlength));

			// Get Profile Dwell Time
			fnLDA_GetProfileDwellTime((char*)gldadevicesip, &ldadevicedata[index].profile_dwelltime);
			printf("Profile Dwell Time:%d\n", (ldadevicedata[index].profile_dwelltime));

			// Get Profile Idle Time
			fnLDA_GetProfileIdleTime((char*)gldadevicesip, &ldadevicedata[index].profile_idletime);
			printf("Profile Idle Time:%d\n", (ldadevicedata[index].profile_idletime));
		}
		gbWantGetParam = FALSE;
	}

	// Close the device socket at the end of the process
	if(gbDeviceOpen)
	{
		fnLDA_CloseDevice((char *)gldadevicesip);
		gbDeviceOpen = FALSE;
	}

   
}

