// --------------------------------- lda_defintions.h -------------------------------------------
//
//  Include file for Linux LabBrick attenuator defintions
//
// (c) 2020-2021 by Vaunix Technology Corporation, all rights reserved
//
//  JA  Version 1.0 LDA Ethernet Driver Interface Definitions
//	NJB 5/18/2026	Incremented library version number to 1.1.0
//-----------------------------------------------------------------------------
#ifdef VNX_ATTEN_EXPORTS
#define VNX_ATTEN_API __declspec(dllexport)
#else
#define VNX_ATTEN_API __declspec(dllimport) 
#endif

/// ---------- Include headers ----------------

//*****************************************************************************
//
// If building with a C++ compiler, make all of the definitions in this header
// have a C binding.
//
//*****************************************************************************
#ifdef __cplusplus
extern "C"
{
#endif


/// ---------- Macros ----------------
#define MAX_MODELNAME   32
#define MAX_SWVERSION   7
#define MAX_NETBUFF     16

// ----------- Profile Control -----------
#define PROFILE_ONCE	1		// play the profile once
#define PROFILE_REPEAT	2		// play the profile repeatedly
#define PROFILE_OFF		0		// stop the profile

// Feature bits for the feature DWORD
#define DEFAULT_FEATURES	0x00000000
#define HAS_BIDIR_RAMPS		0x00000001
#define HAS_PROFILES		0x00000002
#define HAS_HIRES			0x00000004
#define HAS_4CHANNELS		0x00000008
#define HAS_8CHANNELS		0x00000010
#define HAS_LONG_PROFILE	0x00000020
#define HAS_MCHANNELS		0x00000040

// STATUS ENUM
#define STATUS_OK		0       // 0
#define STATUS_ERROR	1       // 1
#define LDASTATUS 		int


// LDA Device Response Data Structure
typedef struct
{
	//  Global device variables
	int serialnumber;
	char modelname[MAX_MODELNAME];
	char swversion[MAX_SWVERSION];
	int device_features;
	int ipmode;
	char ipaddress[MAX_NETBUFF];
	char netmask[MAX_NETBUFF];
	char gateway[MAX_NETBUFF];
	int minfrequency;
	int maxfrequency;
	int minattenuation;
	int maxattenuation;           // maximum attenuation in .05 db units
	int maxchannels;
	int rf_channel;                  // the current channel number
	int rf_current_frequency;
	int rf_attenuation;                // in .05db units
	int rf_on;
	int attenuationstep;
	int rampstart_attenuation;
	int rampstop_attenuation;
	int ramp_dwelltime;
	int ramp_idletime;
	int ramp_holdtime;
	int ramp_bidirectional_dwelltime;
	int attenuationsteptwo;
	int profile_maxlength;
	int profile_count;
	int profile_dwelltime;
	int profile_idletime;
	int profile_index;
} LDADEVICE_DATA_T;

// LDA Device Init
VNX_ATTEN_API void fnLDA_Init(void);

// Get Library Version as a string
VNX_ATTEN_API char* fnLDA_LibVersion(void);

// Get library version as an integer with one byte each for major and minor version (e.g. 0x0101 for version 1.1)
VNX_ATTEN_API int fnLDA_GetLibVersion(void);

// LDA Test mode
VNX_ATTEN_API void fnLDA_SetTestMode(bool testmode);

// InitDevice
VNX_ATTEN_API LDASTATUS fnLDA_InitDevice(char* deviceip);

// Close the Device Socket
VNX_ATTEN_API LDASTATUS fnLDA_CloseDevice(char* deviceip);

// Device Ready
VNX_ATTEN_API LDASTATUS fnLDA_CheckDeviceReady(char* deviceip);

// Get Number of Channels
VNX_ATTEN_API LDASTATUS fnLDA_GetMaxChannels(char* deviceip, int* respdata);

// Get Model Name
VNX_ATTEN_API LDASTATUS fnLDA_GetModelName(char* deviceip, char* respdata);

// Get Serial Number of the device
VNX_ATTEN_API LDASTATUS fnLDA_GetSerialNumber(char* deviceip, int* respdata);

// Get SW Version of the device
VNX_ATTEN_API LDASTATUS fnLDA_GetSoftwareVersion(char* deviceip, char* respdata);

// Get IP Mode of the device  0 - Static, 1 - DHCP
VNX_ATTEN_API LDASTATUS fnLDA_GetIPMode(char* deviceip, int* respdata);

// Get IP Address of the device
VNX_ATTEN_API LDASTATUS fnLDA_GetIPAddress(char* deviceip, char* respdata);

// Get Netmask of the device
VNX_ATTEN_API LDASTATUS fnLDA_GetNetmask(char* deviceip, char* respdata);

// Get Gateway of the device
VNX_ATTEN_API LDASTATUS fnLDA_GetGateway(char* deviceip, char* respdata);

// Get Current Frequency
VNX_ATTEN_API LDASTATUS fnLDA_GetWorkingFrequency(char* deviceip, int* respdata);

// Get Mininum Frequency
VNX_ATTEN_API LDASTATUS fnLDA_GetMinWorkingFrequency(char* deviceip, int* respdata);

// Get Maximum Frequency
VNX_ATTEN_API LDASTATUS fnLDA_GetMaxWorkingFrequency(char* deviceip, int* respdata);

// Get Channel
VNX_ATTEN_API LDASTATUS fnLDA_GetChannel(char* deviceip, int* respdata);

// Get Max Attenuation
VNX_ATTEN_API LDASTATUS fnLDA_GetMaxAttenuation(char* deviceip, int* respdata);

// Get Min Attenuation
VNX_ATTEN_API LDASTATUS fnLDA_GetMinAttenuation(char* deviceip, int* respdata);

// Get Attenuation Data
VNX_ATTEN_API LDASTATUS fnLDA_GetAttenuation(char* deviceip, int* respdata);

// Get Ramp Start Data
VNX_ATTEN_API LDASTATUS fnLDA_GetRampStart(char* deviceip, int* respdata);

// Get Ramp End Data
VNX_ATTEN_API LDASTATUS fnLDA_GetRampEnd(char* deviceip, int* respdata);

// Get Dwell Time
VNX_ATTEN_API LDASTATUS fnLDA_GetDwellTime(char* deviceip, int* respdata);
VNX_ATTEN_API LDASTATUS fnLDA_GetDwellTimeTwo(char* deviceip, int* respdata);

// Get Idle Time
VNX_ATTEN_API LDASTATUS fnLDA_GetIdleTime(char* deviceip, int* respdata);

// Get Hold Time
VNX_ATTEN_API LDASTATUS fnLDA_GetHoldTime(char* deviceip, int* respdata);

// Get Attenuation Step
VNX_ATTEN_API LDASTATUS fnLDA_GetAttenuationStep(char* deviceip, int* respdata);
VNX_ATTEN_API LDASTATUS fnLDA_GetAttenuationStepTwo(char* deviceip, int* respdata);

// Get RF On/Off State
VNX_ATTEN_API LDASTATUS fnLDA_GetRF_On(char* deviceip, int* respdata);

// Get Profile MaxLength
VNX_ATTEN_API LDASTATUS fnLDA_GetProfileMaxLength(char* deviceip, int* respdata);

// Get Profile Element
VNX_ATTEN_API LDASTATUS fnLDA_GetProfileElement(char* deviceip, int index, int* respdata);

// Get Profile Count
VNX_ATTEN_API LDASTATUS fnLDA_GetProfileCount(char* deviceip, int* respdata);

// Get Profile Dwell Time
VNX_ATTEN_API LDASTATUS fnLDA_GetProfileDwellTime(char* deviceip, int* respdata);

// Get Profile Idle Time
VNX_ATTEN_API LDASTATUS fnLDA_GetProfileIdleTime(char* deviceip, int* respdata);

// Get Profile Index (not currently supported over Ethernet)
VNX_ATTEN_API LDASTATUS fnLDA_GetProfileIndex(char* deviceip, int* respdata);

// Get Features
VNX_ATTEN_API LDASTATUS fnLDA_GetFeatures(char* deviceip, int* respdata);

// Set Frequency  --- Frequency in 100KHz Resolution
VNX_ATTEN_API LDASTATUS fnLDA_SetWorkingFrequency(char* deviceip, int frequency);

// Set Channel
VNX_ATTEN_API LDASTATUS fnLDA_SetChannel(char* deviceip, int channel);

// Set Attenuation  -- Attenuation in 0.05db Resolution
VNX_ATTEN_API LDASTATUS fnLDA_SetAttenuation(char* deviceip, int attenuation);

// Set Channel Attenuation -- Attenuation in 0.05db Resolution
VNX_ATTEN_API LDASTATUS fnLDA_SetAttenuationQ(char* deviceip, int attenuation, int channel);

// Set Attenuatuion Step 
VNX_ATTEN_API LDASTATUS fnLDA_SetAttenuationStep(char* deviceip, int attenuationstep);
VNX_ATTEN_API LDASTATUS fnLDA_SetAttenuationStepTwo(char* deviceip, int attenuationstep2);

// Set Ramp Start -- Attenuation in 0.05db Resolution
VNX_ATTEN_API LDASTATUS fnLDA_SetRampStart(char* deviceip, int rampstart);

// Set Ramp End -- Attenuation in 0.05db Resolution
VNX_ATTEN_API LDASTATUS fnLDA_SetRampEnd(char* deviceip, int rampstop);

// Set Dwell Time -- Time in millisecond Resolution
VNX_ATTEN_API LDASTATUS fnLDA_SetDwellTime(char* deviceip, int dwelltime);
VNX_ATTEN_API LDASTATUS fnLDA_SetDwellTimeTwo(char* deviceip, int dwelltime2);

// Set Idle Time -- Time in millisecond Resolution
VNX_ATTEN_API LDASTATUS fnLDA_SetIdleTime(char* deviceip, int idletime);

// Set Hold Time -- Time in millisecond Resolution
VNX_ATTEN_API LDASTATUS fnLDA_SetHoldTime(char* deviceip, int holdtime);

// Set Ramp Direction
VNX_ATTEN_API LDASTATUS fnLDA_SetRampDirection(char* deviceip, bool up);

// Set Ramp Mode
VNX_ATTEN_API LDASTATUS fnLDA_SetRampMode(char* deviceip, bool mode);

// Set Ramp Bidirectional
VNX_ATTEN_API LDASTATUS fnLDA_SetRampBidirectional(char* deviceip, bool bidir_enable);

// Start Ramp
VNX_ATTEN_API LDASTATUS fnLDA_StartRamp(char* deviceip, bool go);

// Set Profile Element
VNX_ATTEN_API LDASTATUS fnLDA_SetProfileElement(char* deviceip, int index, int attenuation);

// Set Profile Count
VNX_ATTEN_API LDASTATUS fnLDA_SetProfileCount(char* deviceip, int profilecount);

// Set Profile Idle Time
VNX_ATTEN_API LDASTATUS fnLDA_SetProfileIdleTime(char* deviceip, int idletime);

// Set Profile Dwell Time
VNX_ATTEN_API LDASTATUS fnLDA_SetProfileDwellTime(char* deviceip, int dwelltime);

// Set Profile Mode
VNX_ATTEN_API LDASTATUS fnLDA_StartProfile(char* deviceip, int mode);

// Set RF On
VNX_ATTEN_API LDASTATUS fnLDA_SetRFOn(char* deviceip, bool on);

// Save Setting Callback
VNX_ATTEN_API LDASTATUS fnLDA_SaveSettings(char* deviceip);


// ************** To Be Done

// Start RampMC
VNX_ATTEN_API LDASTATUS fnLDA_StartRampMC(char* deviceip, int mode, int chmask, bool deferred);

// Start ProfileMC
VNX_ATTEN_API LDASTATUS fnLDA_StartProfileMC(char* deviceip, int mode, int chmask, bool deferred);

//*****************************************************************************
//
// Mark the end of the C bindings section for C++ compilers.
//
//*****************************************************************************
#ifdef __cplusplus
}
#endif