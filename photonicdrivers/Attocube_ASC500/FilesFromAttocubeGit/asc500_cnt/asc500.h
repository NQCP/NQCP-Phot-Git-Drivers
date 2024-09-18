/*******************************************************************************
 *
 *  Project:        Daisy Client Library
 *
 *  Filename:       asc500.h
 *
 *  Purpose:        Parameter IDs and enum values to use with daisybase.h
 *
 *  Author:         NHands GmbH & Co KG
 */
/******************************************************************************/
/** @file asc500.h
 *  @brief Parameter IDs and enum values to use with daisybase.h
 *
 *  Defines constants to be used as parameters, enum values, or parameter limits for the
 *  functions defined in @ref daisybase.h . Those parameters control functions of the
 *  Attocube ASC500 SPM controller.
 */
/******************************************************************************/
/* $Id: asc500.h,v 1.24.2.5 2019/08/22 16:48:25 trurl Exp $ */

#ifndef __ASC500_H
#define __ASC500_H


/** @brief Server Port Number
 *
 *  The TCP port number of the ASC500 application server.
 *  Parameter serverPort of @ref DYB_init .
 */
#define ASC500_PORT_NUMBER    7000

/** @brief Number of Channels
 *
 *  Number of data channels available in ASC500. The parameter channel of
 *  @ref DYB_setDataCallback has to be smaller.
 */
#define ASC500_DATA_CHANNELS  14


/** @name Overall State Control
 *
 *  These parameters control global states of the ASC500 that affect all functions of the device.
 *  @{
 */

/** Output Activation
 *
 *  All electrical outputs of the ASC500 can be enabled / disabled at the same time using this
 *  parameter as a command (1=activate, 0=deactivate). It may take some time to reach the
 *  target state, therefore an additional status variable is provided. By default, outputs
 *  are disabled. Index is 0.
 */
#define ID_OUTPUT_ACTIVATE    0x0141

/** Output Status
 *
 *  State of the electrical outputs as controlled by @ref ID_OUTPUT_ACTIVATE
 *  (read only, 1=activated, 0=deactivated). Index is 0.
 */
#define ID_OUTPUT_STATUS      0x0140

/** Data Enable
 *
 *  Data channels can be enabled / disabled all at once. By default the channels are disabled.
 *  Using a XML profile with @ref DYB_sendProfile will automatically enable the data channels.
 *  Only index 0 is allowed.
 */
#define ID_DATA_EN            0x0146
/* @} */


/** @name Configuration of Data Channels
 *
 *  The controller provides a number of data channels (@ref ASC500_DATA_CHANNELS).
 *  The four ID_CHAN_ addresses are used to configure the data that are sent on a specific channel:
 *  data source, triggering, and sampling. The ID_... constants are for "address" in control
 *  functions, CHANCONN_... and CHANADC_... are valid enumeration values for
 *  @ref ID_CHAN_CONNECT and @ref ID_CHAN_ADC telegrams, respectively.
 *
 *  The index is valid and transports the channel number of the channel
 *  to be configured.
 *  @{
 */
#define ID_CHAN_CONNECT       0x0030  /**< Data channel trigger (one of CHANCONN_..)              */
#define ID_CHAN_ADC           0x0031  /**< Data channel source (one of CHANADC_..)                */
#define ID_CHAN_AVG_MAX       0x0035  /**< Data channel average over sample time (boolean)        */

/** Data channel sample time
 *
 *  The sample time can be adjusted for timer triggered channels only
 *  (@ref CHANCONN_PERMANENT). In all other cases, it is given by the
 *  trigger source and overwritten automatically.
 *  The unit is 2.5us.
 */
#define ID_CHAN_POINTS        0x0032

/* Data Triggers (for ID_CHAN_CONNECT)                                                            */
#define CHANCONN_DISABLED     0x00    /**< Data trigger: none (channel is disabled)               */
#define CHANCONN_SCANNER      0x01    /**< Data trigger: scanner                                  */
#define CHANCONN_PERMANENT    0x02    /**< Data trigger: timer with sample time                   */
#define CHANCONN_SPEC_0       0x03    /**< Data trigger: spectroscopy engine 1                    */
#define CHANCONN_SPEC_1       0x04    /**< Data trigger: spectroscopy engine 2                    */
#define CHANCONN_SPEC_2       0x05    /**< Data trigger: spectroscopy engine 3                    */
#define CHANCONN_SPEC_3       0x06    /**< Data trigger: spectroscopy engine 4 (Resonance)        */
#define CHANCONN_EVERY        0x08    /**< Data trigger: data source                              */
#define CHANCONN_COMMAND      0x09    /**< Data trigger: command ("soft spectroscopy")            */
#define CHANCONN_DUALPATH     0x0D    /**< Data trigger: 2nd scan of Dual path mode               */

/* Data Sources (for ID_CHAN_ADC)                                                                 */
#define CHANADC_ADC_MIN        0      /**< Data source: first physical AD converter               */
#define CHANADC_ADC_MAX        5      /**< Data source: last  physical AD converter               */
#define CHANADC_AFMAEXC        7      /**< Data source: HF 1 Out                                  */
#define CHANADC_AFMFEXC        8      /**< Data source: HF 1 df                                   */
#define CHANADC_ZOUT           9      /**< Data source: SPM Z Out                                 */
#define CHANADC_AFMSIGNAL     12      /**< Data source: HF 1                                      */
#define CHANADC_AFMAMPL       13      /**< Data source: HF 1 Amplitude / X                        */
#define CHANADC_AFMPHASE      14      /**< Data source: HF 1 Phase / Y                            */
#define CHANADC_AFMMAMPL      16      /**< Data source: LF Lockin Amplitude                       */
#define CHANADC_AFMMPHASE     17      /**< Data source: LF Lockin Phase                           */
#define CHANADC_ZOUTINV       18      /**< Data source: SPM Z Out inverted                        */
#define CHANADC_CROSSLINK_1   29      /**< Data source: crosslink 1                               */
#define CHANADC_CROSSLINK_2   30      /**< Data source: crosslink 2                               */
#define CHANADC_SENSOR_POS_X  31      /**< Data source: Position sensor X (raw) (if available)    */
#define CHANADC_SENSOR_POS_Y  32      /**< Data source: Position sensor Y (raw) (if available)    */
#define CHANADC_COUNTER       23
/* @} */


/** @name Data Output Scaling
 *
 *  ADC data can be passed through a linear output transfer function after the transfer
 *  via a data channel in order to allow for external wiring.
 *  The transfer function depends on the data source, therefore the index has to be
 *  between @ref CHANADC_ADC_MIN and @ref CHANADC_ADC_MAX.
 *  @{
 */
#define ID_ADC_ECAL_FACT      0x1042  /**< Transfer function: Gain [output_unit/uV]               */
#define ID_ADC_ECAL_OFFS      0x1043  /**< Transfer function: Offset [uV]                         */
#define ID_ADC_ECAL_UNIT      0x1044  /**< Transfer function: Unit, see @ref DUnits "Data Units"  */
/* @} */


/** @name Voltage and Deflection Limits
 *
 *  The voltage limits for X/Y and Z have always to be set to the limits of the piezo actuators
 *  to avoid damage. The deflection limits have to be set to their corresponding deflections
 *  for proper calibration of metric parameters.
 *
 *  All those values are stored as an arrays of two elements for room temperature (index 0)
 *  and low temperature (index 1). @ref ID_PIEZO_T_LIM holds the two temperature values themselves.
 *  With @ref ID_PIEZO_TEMP the actual temperature can be set. It controls the interpolation of
 *  the actual voltage and deflection limits between the two fixed points.
 *
 *  The actual (i.e. interpolated) limits can be read back at separate adresses.
 *  @{
 */
#define ID_PIEZO_VOLTLIM_X    0x1024  /**< Scanner maximum output voltage X [305.2 uV] (array)    */
#define ID_PIEZO_VOLTLIM_Y    0x1025  /**< Scanner maximum output voltage Y [305.2 uV] (array)    */
#define ID_REG_ZABS_LIM_A     0x1011  /**< Z maximum output voltage [19.07 uV] (array)            */
#define ID_PIEZO_RANGE_X      0x1026  /**< Scanner maximum deflection X [10pm] (array)            */
#define ID_PIEZO_RANGE_Y      0x1027  /**< Scanner maximum deflection Y [10pm] (array)            */
#define ID_REG_ZABS_LIMM_A    0x1012  /**< Z maximum deflection [pm] (array)                      */
#define ID_PIEZO_T_LIM        0x1034  /**< Temperature values for room and low temp [mK] (array)  */
#define ID_PIEZO_TEMP         0x1031  /**< Actual temperature for interplation of the limits [mK] */

#define ID_PIEZO_ACTVOLT_HX   0x1022  /**< Scanner actual voltage maximum X [305.2 uV] (read only)*/
#define ID_PIEZO_ACTVOLT_HY   0x1023  /**< Scanner actual voltage maximum Y [305.2 uV] (read only)*/
#define ID_REG_ZABS_LIM       0x1019  /**< Z actual maximum output voltage [19.07 uV] (read only) */
#define ID_PIEZO_ACTRG_X      0x1032  /**< Scanner actual maximum deflection X [10pm] (read only) */
#define ID_PIEZO_ACTRG_Y      0x1033  /**< Scanner actual maximum deflection Y [10pm] (read only) */
#define ID_REG_ZABS_LIMM      0x101A  /**< Z actual maximum deflection [pm] (read only)           */
/* @} */


/** @name Scanner Coordinates
 *
 *  There are two relevant coordinate systems for the X,Y (scanner) coordinates:
 *  An "absolute" system with an arbitrary origin that can be set by the user to match different
 *  scans, and a system relative to the voltage origin. The voltage origin is the position
 *  the scanner would have at zero output voltage.
 *
 *  The addresses can be used to read out the voltage origin in absolute coordinates and to
 *  move the absolute coordinate system. To perform a move, the new coordinate origin has to be
 *  followed by an explicit move command.
 *  @{
 */
#define ID_SCAN_COORD_ZERO_X  0x02FE  /**< Scanner voltage origin X [10pm] (read only)            */
#define ID_SCAN_COORD_ZERO_Y  0x02FF  /**< Scanner voltage origin Y [10pm] (read only)            */
#define ID_SCAN_COORD_MOVE_X  0x02FB  /**< Scanner new origin of absolute coordinates X [10pm]    */
#define ID_SCAN_COORD_MOVE_Y  0x02FC  /**< Scanner new origin of absolute coordinates X [10pm]    */
#define ID_SCAN_COORD_MOVE    0x02FD  /**< Scanner apply new origin coordinates (command)         */
/* @} */


/** @name Scanner Setup
 *
 *  The addresses are used to configure the scan range and sampling and to control the scanner
 *  operation. Positions are relative to the @ref ID_SCAN_COORD_ZERO_X "voltage origin".
 *  The index must always be 0.
 *  @{
 */
#define ID_SCAN_ONCE          0x002F  /**< Scanner single scan; stop after first run (boolean)    */
#define ID_SCAN_X_EQ_Y        0x1006  /**< Scanner fix lines=cols (boolean, for manual control)   */
#define ID_SCAN_GEOMODE       0x1009  /**< Scanner fix aspect ratio (boolean, for manual control) */
#define ID_SCAN_OFFSET_X      0x0010  /**< Scanner relative center of the scanfield X [10pm]      */
#define ID_SCAN_OFFSET_Y      0x0011  /**< Scanner relative center of the scanfield Y [10pm]      */
#define ID_SCAN_COLUMNS       0x1003  /**< Scanner number of scan columns                         */
#define ID_SCAN_LINES         0x001D  /**< Scanner number of scan lines                           */
#define ID_SCAN_PIXEL         0x1021  /**< Scanner size of a column/line [10pm]                   */
#define ID_SCAN_ROTATION      0x0018  /**< Scanner scanfeld rotation [360/65536 deg]              */
#define ID_SCAN_MSPPX         0x1020  /**< Scanner sample time [2.5us]                            */
#define ID_SCAN_COMMAND       0x0100  /**< Scanner command (SCANRUN_ constants)                   */
#define ID_SCAN_PSPEED        0x100B  /**< Scanner positioning speed [nm/s]                       */
#define ID_SCAN_ACCEL         0x0052  /**< Scanner maximum accelleration (0=unlimited) [um/s^2]   */
#define ID_SCAN_ACCEL_PRC     0x0053  /**< Scanner share of accel distance outside scanrange [%]  */
#define ID_CL_USESENPOS       0x01FE  /**< Scanner use sensor position for closed loop (bool)     */
#define ID_CL_RESTORE         0x02F8  /**< Scanner clear saturation error (command)               */

#define ID_POSI_TARGET_X      0x0027  /**< Scanner absolute target position X [10pm]              */
#define ID_POSI_TARGET_Y      0x0028  /**< Scanner absolute target position Y [10pm]              */
#define ID_POSI_GOTO          0x003A  /**< Scanner move to absolute target position (command)     */

#define ID_SCAN_DUALLINE      0x0210  /**< Dual line mode on (boolean)                            */
#define ID_REG_MFM_EN         0x005D  /**< Dual line mode feedback: 0=feedback, 1=1st line profile*/
#define ID_REG_MFM_OFF_M      0x10B7  /**< Dual line mode lift offset [pm]                        */
#define ID_REG_MFM_SLEW_M     0x10BB  /**< Dual line mode lift offset slew rate [pm/s]            */
#define ID_DUALLINE_WAIT      0x0216  /**< Dual line mode wait time [ms]                          */
#define ID_DUALLINE_SP_EN     0x0211  /**< Dual line mode enable alternative setpoint             */
#define ID_DUALLINE_SP_DISP   0x0213  /**< Dual line mode alternative setpoint value              */
#define ID_DUALLINE_DAC_EN    0x0215  /**< Dual line mode enable alt DAC output (Index= DAC No)   */
#define ID_DUALLINE_DAC       0x0214  /**< Dual line mode alternative DAC output value [305.2 uV] */
#define ID_DUALLINE_FEXC_EN   0x021C  /**< Dual line mode enable alternative F-excitation         */
#define ID_DUALLINE_FEXC      0x021B  /**< Dual line mode alternative F-excitation value [mHz]    */

/* Scanner commands (for ID_SCAN_COMMAND)                                                         */
#define SCANRUN_OFF           0x00    /**< Scanner command: off                                   */
#define SCANRUN_ON            0x01    /**< Scanner command: run                                   */
#define SCANRUN_PAUSE         0x02    /**< Scanner command: pause                                 */
/* @} */


/** @name Scanner Current State
 *
 *  Current state and position of the scanner. The scanner state is a collection of flags that
 *  represent the running state of the scan engine - see SCANSTATE_ constants for bit masks.
 *  The saturation warning is set when the closed loop controller is running out of range; the
 *  value provides its current direction. The scanner position is relative to the voltage origin.
 *
 *  All messages are sent autonomously by the ASC500 and can be retreived with DYB_get
 *  functions as well as by setting up an event callback. They are read only; index is 0.
 *  @{
 */
#define ID_SCAN_STATUS        0x0101  /**< Scanner running state, see SCANSTATE_ masks            */
#define ID_CL_SATSTATUS       0x02D5  /**< Scanner saturation; 1=left, 2=right, 4=top, 8=bottom   */
#define ID_SCAN_CURR_X        0x002A  /**< Scanner position relative to voltage origin Y [10pm]   */
#define ID_SCAN_CURR_Y        0x002B  /**< Scanner position relative to voltage origin Y [10pm]   */

/* Scanner state bit masks for @ref ID_SCAN_STATUS                                                */
#define SCANSTATE_PAUSE       0x01   /**< Scanner state flag pause                                */
#define SCANSTATE_MOVING      0x02   /**< Scanner state flag moving                               */
#define SCANSTATE_SCAN        0x04   /**< Scanner state flag scanning                             */
#define SCANSTATE_IDLE        0x08   /**< Scanner state flag idle                                 */
#define SCANSTATE_LOOP        0x10   /**< Scanner state flag closed loop                          */
/* @} */


/** @name Z Control and Z Feedback
 *
 *  The adresses are used to access Z and the z feedback controller. Index is always 0.
 *  @{
 */
#define ID_REG_LOOP_ON        0x0060  /**< Feedback on/off (boolean)                              */
#define ID_REG_INPUT          0x0062  /**< Feedback controller input (one of CHANADC_...)         */
#define ID_REG_LIM_MINUSR_M   0x10B9  /**< Feedback limit minimum [pm]                            */
#define ID_REG_LIM_MAXUSR_M   0x10BA  /**< Feedback limit maximum [pm]                            */
#define ID_REG_KI_DISP        0x10A3  /**< Feedback controller integral part I [mHz]              */
#define ID_REG_KP_DISP        0x10A4  /**< Feedback controller proportional part P [10^-6]        */
#define ID_REG_PI_CONST       0x10B0  /**< Feedback controller force constant P/I                 */
#define ID_REG_POLARITY       0x0068  /**< Feedback invert output polarity (boolean)              */
#define ID_REG_SLOPE_REQUEST  0x01E9  /**< Slope compensation enable (boolean)                    */
#define ID_REG_SLOPE_STATUS   0x01E8  /**< Slope compensation state (0=off, 1=on, other=adjusting)*/
#define ID_REG_SLOPE_X        0x006b  /**< Slope compensation slope X [6.104 * 10^-4 %]           */
#define ID_REG_SLOPE_Y        0x006c  /**< Slope compensation slope Y [6.104 * 10^-4 %]           */
#define ID_DAC_FB_STEP        0x0087  /**< Z output slewrate [466 uV/s]                           */
#define ID_REG_SET_Z_M        0x1035  /**< Direct Z output value [pm]                             */

/** Z Readback
 *
 *  Current Z position [pm]. The position is sent periodically by the ASC500 and can be retreived
 *  with DYB_get functions as well as by setting up an event callback. It is read only; index is 0.
 */
#define ID_REG_GET_Z_M        0x1038

/** Z Feedback Setpoint
 *
 *  The setpoint is given in the units of the input signal, but multiplied by 10000 for better
 *  resolution. The unit can be retrieved by @ref ID_GUI_UNIT_ZREG at index 0.
 */
#define ID_REG_SETP_DISP      0x007A

/** Unit of setpoint
 *
 *  The parameter is read only, DYB_set functions will fail. It reflects the unit of the input
 *  signal (@ref ID_REG_GEN_INPUT) and the setpoint. See @ref DUnits "Data Units".
 */
#define ID_GUI_UNIT_ZREG      0x1051
/* @} */


/** @name Coarse Parameters
 *
 *  The adresses control the coarse step generator. Index is the coarse device (0...6).
 *  Note that not all coarse control commands work with all posslible power amplifiers.
 *  @{
 */
#define ID_CRS_AXIS_MODE      0x0284  /**< Coarse Axis Enable (1=step, 2=ground, 0=reserved!)     */
#define ID_CRS_AXIS_UP        0x0285  /**< Coarse axis up by n steps                              */
#define ID_CRS_AXIS_DN        0x0286  /**< Coarse axis down by n steps                            */
#define ID_CRS_AXIS_CUP       0x0287  /**< Coarse axis continously up (boolean)                   */
#define ID_CRS_AXIS_CDN       0x0288  /**< Coarse axis continously down (boolean)                 */
#define ID_CRS_FREQUENCY      0x0280  /**< Coarse axis frequency [Hz] (1...8000)                  */
#define ID_CRS_VOLTAGE        0x0281  /**< Coarse axis voltage [V] (0...70)                       */
/* @} */


/** @name Auto Approach
 *
 *  The adresses control the auto approach feature. Index is always 0.
 *  Note that not all coarse control commands work with all posslible power amplifiers.
 *  @{
 */
#define ID_AAP_CTRL           0x0090  /**< Auto approach on/off (boolean)                         */
#define ID_AAP_SPEED          0x0092  /**< Auto approach speed [976.6 uV/s]                       */
#define ID_AAP_AXIS           0x009B  /**< Coarse axis selection (0..2 or 0..7, depending on HW)  */
#define ID_AAP_DELAY          0x009C  /**< Coarse delay after step [us]                           */
#define ID_AAP_MODE           0x009D  /**< Controller mode after approach (0=on, 1=retract, 2=off)*/
#define ID_AAP_THRCOND        0x009E  /**< AAP stop condition (0="> threshold", 1="< threshold")  */
#define ID_AAP_STEPSAPR       0x00A0  /**< AAP number of steps per approach                       */
#define ID_AAP_GNDWHILEAP     0x00A1  /**< AAP switch amplifier to gnd between approaches         */
#define ID_AAP_APR_MODE       0x00A2  /**< AAP mode: 0=Ramp, 1=Loop                               */
#define ID_AAP_CRS_DIR        0x00A3  /**< AAP direction of a coarse step (0=forward, 1=backward) */
#define ID_AAP_CRS_DEV        0x00A8  /**< Coarse device selection (one of AAP_DEVICE_...)        */
#define ID_AAP_CRS_POL        0x00A9  /**< Coarse trigger polarity (0=high active, 1=low active)  */
#define ID_AAP_CRS_HLDTIME    0x00AA  /**< Coarse trigger hold time [us]                          */

/** AAP Stop Threshold
 *
 *  The threshold is given in the units of the Z feedback input signal, but multiplied by 10000
 *  for better resolution. The unit can be retrieved by @ref ID_GUI_UNIT_ZREG at index 0.
 */
#define ID_AAP_THR_DISP       0x00AD

#define CRS_DEVICE_ANC        0x00    /**< Coarse device ANC300 / ANC350                          */
#define CRS_DEVICE_TTL        0x01    /**< Coarse device TTL via DAC2                             */
#define CRS_DEVICE_LVTTL      0x02    /**< Coarse device LVTTL via DAC2                           */
#define CRS_DEVICE_ANC_NSL    0x03    /**< Coarse device ANC350 via NSL                           */
#define CRS_DEVICE_ATTOSTM    0x04    /**< Coarse device AttoSTM                                  */
/* @} */


/** @name Generic Feedback Control
 *
 *  The addresses are used to configure the two generic feedback loops (crosslink 1 and 2).
 *  Index 0 is used to access crosslink 1, index 1 for crosslink 2.
 *  @{
 */
#define ID_REG_GEN_CTL        0x01C6  /**< Crosslink On/off (boolean)                             */
#define ID_REG_GEN_POL        0x01C7  /**< Crosslink invert polarity (boolean)                    */
#define ID_REG_GEN_INPUT      0x01C8  /**< Crosslink controller input (one of CHANADC_...)        */
#define ID_REG_GEN_DAC        0x01CD  /**< Crosslink controller output (0..3 for DAC1..DAC4)      */
#define ID_REG_GEN_MIN_DISP   0x10D7  /**< Crosslink output minimum [uV]                          */
#define ID_REG_GEN_MAX_DISP   0x10D8  /**< Crosslink output maximum [uV]                          */
#define ID_REG_GEN_OUT_DISP   0x10D6  /**< Crosslink current output value [uV]                    */
#define ID_REG_GEN_RESET      0x01CB  /**< Crosslink reset (command)                              */
#define ID_REG_GEN_KI_DISP    0x10D0  /**< Crosslink controller integral part I [mHz]             */
#define ID_REG_GEN_KP_DISP    0x10D1  /**< Crosslink controller proportional part P [10^-6]       */
#define ID_REG_GEN_PI_CONST   0x10D4  /**< Crosslink force constant P/I (boolean)                 */

/** Generic Feedback Setpoint
 *
 *  The setpoint is given in the units of the input Signal, but multiplied by 10000 for better
 *  resolution. The unit can be retrieved by @ref ID_GUI_UNIT_GENREG at index 0.
 */
#define ID_REG_GEN_SP_DISP    0x10D2

/** Unit of setpoint
 *
 *  The parameter is read only, DYB_set functions will fail. It reflects the unit of the input
 *  signal (@ref ID_REG_GEN_INPUT) and the setpoint. See @ref DUnits "Data Units".
 */
#define ID_GUI_UNIT_GENREG    0x10D5
/* @} */


/** @name AFM
 *
 *  These parameters control the AFM measurement method and related features. Index is always 0.
 *  @{
 */
#define ID_AFM_F_IN           0x00C8  /**< AFM lever excitation frequency [mHz]                   */
#define ID_AFM_R_AMP_OUT      0x00F9  /**< AFM lever excitation amplitude [19.074 uV]             */
#define ID_AFM_L_AMPL         0x00E0  /**< AFM lever detection sensitivity range [305.2 uV]       */
#define ID_AFM_L_PHASE        0x00E1  /**< AFM lever detection phase shift [1.463 nRad]           */
#define ID_AFM_AUTO_PHASE     0x00D9  /**< AFM lever detection auto phase command                 */
#define ID_AFM_L_SMPLTM       0x102D  /**< AFM lever detection sample time [20 ns]                */
#define ID_QCONTROL_EN        0x0230  /**< AFM Q control enable (boolean)                         */
#define ID_QCONTROL_PHASE     0x0231  /**< AFM Q control phase [mdeg]                             */
#define ID_QCONTROL_FEEDBACK  0x0232  /**< AFM Q control feedback [10^-3]                         */

#define ID_AFM_R_AMP_CTRL     0x00E7  /**< AFM amplitude controller loop on (boolean)             */
#define ID_AFM_R_AMPMIN_DISP  0x10F1  /**< AFM amplitude controller minimum [19.074 uV]           */
#define ID_AFM_R_AMPMAX_DISP  0x10F0  /**< AFM amplitude controller maximum [19.074 uV]           */
#define ID_AFM_R_AMP_POL      0x00F7  /**< AFM amplitude controller invert polarity (boolean)     */
#define ID_REG_A_KI_DISP      0x10A7  /**< AFM amplitude controller I [mHz]                       */
#define ID_REG_A_KP_DISP      0x10A8  /**< AFM amplitude controller P [10^-6]                     */

#define ID_AFM_R_FRQ_CTRL     0x00EB  /**< AFM frequency controller loop on (boolean)             */
#define ID_AFM_L_DF_DISP      0x10AD  /**< AFM frequency controller df [mHz]                 */
#define ID_AFM_R_FRQMIN       0x00C7  /**< AFM frequency controller minimum [mHz]                 */
#define ID_AFM_R_FRQMAX       0x00DB  /**< AFM frequency controller maximum [mHz]                 */
#define ID_REG_F_KI_DISP      0x10A5  /**< AFM frequency controller I [uHz]                       */
#define ID_REG_F_KP_DISP      0x10A6  /**< AFM frequency controller P [10^-9]                     */
#define ID_AFM_R_FRQ_ACTVAL   0x00FA  /**< AFM frequency controller input (one of CHANADC_...)    */
#define ID_AFM_R_FRQ_POL      0x00F6  /**< AFM frequency controller invert polarity (boolean)     */

#define ID_AFM_M_AMP          0x00C9  /**< AFM lockin modulation amplitude [305.2 uV]             */
#define ID_AFM_M_FREQ         0x00CA  /**< AFM lockin modulation frequency [mHz]                  */
#define ID_AFM_M_SHIFT        0x00CB  /**< AFM lockin phase shift [1.463 nRad]                    */
#define ID_AFM_M_DA           0x00D0  /**< AFM lockin output connector
                                           (0=Off, 1=DAC1, 2=DAC2, 3=DAC1+DAC2)                   */
#define ID_AFM_M_AD           0x00D1  /**< AFM lockin input connector (one of CHANADC_...)        */
#define ID_AFM_M_DEMAMP       0x00D4  /**< AFM lockin sensitivity range [305.2 uV]                */
#define ID_AFM_M_SMPLTM       0x102E  /**< AFM lockin sample time [20ns]                          */


/** Amplitude Feedback Setpoint
 *
 *  The setpoint is given in the units of the feedback input signal, but multiplied by 10000
 *  for better resolution. The unit can be retrieved by @ref ID_GUI_UNIT_AREG at index 0.
 */
#define ID_AFM_R_AMP_DISP     0x00F4

/** Unit of Amplitude Feedback Setpoint
 *
 *  The parameter is read only, DYB_set functions will fail. It reflects the unit of the input
 *  signal and the setpoint. See @ref DUnits "Data Units".
 */
#define ID_GUI_UNIT_AREG      0x1052

/** Frequency Feedback Setpoint
 *
 *  The setpoint is given in the units of the feedback input signal, but multiplied by 10000
 *  for better resolution. The unit can be retrieved by @ref ID_GUI_UNIT_PREG at index 0.
 */
#define ID_AFM_R_FRQ_DISP     0x00F5


/** Unit of Amplitude Feedback Setpoint
 *
 *  The parameter is read only, DYB_set functions will fail. It reflects the unit of the input
 *  signal and the setpoint. See @ref DUnits "Data Units".
 */
#define ID_GUI_UNIT_PREG      0x1053

/* @} */


/** @name Spectroscopy
 *
 *  These parameters control the built-in spectroscopy machines. The index is used to address
 *  the spectroscopy number (0-2). Spectroscopy engine 3 is reserved for resonance measurement.
 *  @{
 */
#define ID_SPEC_DAC_NO        0x0257  /**< Spectroscopy actuator (0..3=DAC1..4, 26=Z, 27=Low Freq)*/
#define ID_SPEC_START_DISP    0x1500  /**< Spectroscopy start value (unit actuator specific)      */
#define ID_SPEC_END_DISP      0x1501  /**< Spectroscopy end value (unit actuator specific)        */
#define ID_SPEC_UNIT_DISP     0x1502  /**< Spectroscopy start/end unit (read only)                */
#define ID_SPEC_COUNT         0x0252  /**< Spectroscopy number of steps                           */
#define ID_SPEC_MSPOINTS      0x0253  /**< Spectroscopy averaging time per step [2.5 us]          */
#define ID_SPEC_WAIT          0x0255  /**< Spectroscopy delay time before measurement [2.5 us]    */
#define ID_SPEC_STATUS        0x0256  /**< Spectroscopy run command and status (0=stop, 1=run)    */
#define ID_SPEC_RUNCOUNT      0x0258  /**< Spectroscopy number of runs                            */
#define ID_SPEC_FORBACK       0x0259  /**< Spectroscopy forward/backward (boolean)                */
#define ID_SPEC_COMP_EN       0x025D  /**< Spectroscopy limiter on (boolean)                      */
#define ID_SPEC_COMP_CH       0x025A  /**< Spectroscopy limiter input (one of CHANADC_...)        */
#define ID_SPEC_COMP_SGN      0x025C  /**< Spectroscopy limiter condition (0=">", 1="<" threshold)*/
#define ID_SPEC_COMP_VAL_DISP 0x025E  /**< Spectroscopy limiter threshold (actuator units)        */
#define ID_SPEC_LOOP_OFF      0x026A  /**< Spectroscopy Z loop off while running                  */
/* @} */


/** @name Path Mode
 *
 *  Parameters for selection and configuration of a scanner path. The index has to be 0
 *  except for @ref ID_PATH_GUI_X, @ref ID_PATH_GUI_Y, and @ref ID_PATH_ACTION
 *  @{
 */
#define ID_SPEC_PATHPREP      0x0264  /**< Pathmode preparation, used before starting with value=1*/
#define ID_SPEC_PATHCTRL      0x0263  /**< Pathmode start cmd: 0=stop, -1=grid, >1=no of points   */
#define ID_PATH_RUNNING       0x026F  /**< Pathmode activity status (readonly, boolean)           */
#define ID_SPEC_PATHPROCEED   0x0265  /**< Pathmode handshake acknowledgement                     */
#define ID_SPEC_PATHMANSTAT   0x0267  /**< Pathmode handshake request (read only)                 */
#define ID_PATH_GRIDP_X       0x026D  /**< Pathmode number of grid points X                       */
#define ID_PATH_GRIDP_Y       0x026E  /**< Pathmode number of grid points Y                       */
#define ID_EXTTRG_HS          0x0277  /**< Pathmode ext handshake enable (boolean)                */
#define ID_EXTTRG_COUNT       0x0276  /**< Pathmode ext handshake number of triggers, default=1   */
#define ID_EXTTRG_TIMEOUT     0x0278  /**< Pathmode ext handshake timeout [ms]                    */
#define ID_EXTTRG_STATUS      0x0275  /**< Pathmode ext handshake waiting (boolean, read only)    */
#define ID_EXTTRG_TIME        0x0271  /**< Pathmode ext handshake pulse duration [us]             */
#define ID_EXTTRG_EDGE        0x0272  /**< Pathmode ext handshake edge (0=rising, 1=falling)      */
#define ID_REG_Z_HOME_M       0x10F2  /**< Pathmode Z home position for "move home" action [pm]   */

/** Path Points
 *
 *  The index of the path points parameters is used as a point address. The point coordinates
 *  are relative to the scan center and encoded in [10pm]. When using in path mode
 *  (@ref ID_SPEC_PATHCTRL > 1), the parameters contain every single point. In grid mode
 *  (@ref ID_SPEC_PATHCTRL = -1), only the top left and bottom right points are stored.
 */
#define ID_PATH_GUI_X         0x1302  /**< Pathmode path points X                                 */
#define ID_PATH_GUI_Y         0x1303  /**< Pathmode path points Y                                 */

/** Path Actions
 *
 *  This parameter encodes a list of actions that have to be performed at every path point.
 *  At index 0, the number of actions is stored; the actions themselves follow.
 *  Defined actions are:
 *  0=manual handshake, 1..3=spectroscopy 1..3, 4=ext. handshake, 5=move Z home, 6=auto approach
 */
#define ID_PATH_ACTION        0x026C  /**< Pathmode list of path actions                          */
/* @} */


/** @name ADC Values
 *
 *  The following addresses are read only, DYB_set functions will fail. They provide information
 *  about the current voltage measured by the ADC selected by the index. Index=0 relates to ADC 1,
 *  Index=1 relates to ADC 2 and so on. The appropriate unit to a given ADC value is supplied
 *  by @ref ID_ADC_VAL_UNIT, see @ref DUnits "Data Units" for details.
 *  The ADC value itself is multiplied with 1.000.000 to provide sufficent accuracy.
 *  The values can be retreived with DYB_get functions or by setting up an event callback.
 *  @{
 */
#define ID_ADC_VALUE          0x0037  /**< ADC value                                              */
#define ID_ADC_VAL_UNIT       0x0038  /**< Unit of ADC value                                      */
/* @} */


/** @name DAC Values
 *
 *  The DAC outputs can be configured with the following addresses. The index identifies the
 *  accessed DAC.
 *  @{
 */
#define ID_GENDAC_LIMIT_RT    0x10DD  /**< Limitation of DAC output at room temperature [uV]      */
#define ID_GENDAC_LIMIT_LT    0x10F5  /**< Limitation of DAC output at low temperature [uV]       */
#define ID_GENDAC_LIMIT_CT    0x10F6  /**< Limitation at current temperature [uV] (read only)     */
#define ID_DAC_VALUE          0x0080  /**< DAC output voltage [305,19 uV]                         */
#define ID_DAC_GEN_STEP       0x0089  /**< DAC output slewrate [466 uV/s]                         */
/* @} */


/** @name Counter Parameters
 *
 *  Parameters for the pulse counter feature. Index is always 0.
 *  @{
 */
#define ID_CNT_EXP_TIME       0x0310  /**< Counter exposure time [2.5us] (0...65535)              */
/* @} */


/** @name Server Control
 *
 *  The server's built in tracing can be controlled with these flags. By default, the tracing
 *  goes to stdout. The TRACE_... constants are flags that may be or'ed together as value
 *  for the telegram @ref ID_SRV_TRACEFLG (with index 0).
 *  @{
 */
#define TRACE_FULL            0x0001 /**< Trace full length of data                               */
#define TRACE_GLOBAL          0x0004 /**< Trace warnings and infos                                */
#define TRACE_CS_IN           0x0008 /**< Trace telegrams from clients                            */
#define TRACE_CS_OUT          0x0010 /**< Trace telegrams to clients                              */
#define TRACE_UC_IN           0x0020 /**< Trace telegrams from controller                         */
#define TRACE_UC_OUT          0x0040 /**< Trace telegrams to controller                           */
#define TRACE_DATA            0x0080 /**< Include data telegrams in trace                         */
#define TRACE_EVT             0x0100 /**< Include event telegrams in trace                        */
#define ID_SRV_TRACEFLG       0x10A0 /**< Enable server tracing features                          */
/* @} */


/** @name Data Units
 *
 *  @anchor DUnits
 *  Constants used by e.g. @ref ID_GUI_UNIT_GENREG to inform about
 *  the unit of a parameter.
 *  @{
 */
#define DATA_UNIT_MM          0x0000  /**< [mm]                                                   */
#define DATA_UNIT_UM          0x0001  /**< [um]                                                   */
#define DATA_UNIT_NM          0x0002  /**< [nm]                                                   */
#define DATA_UNIT_PM          0x0003  /**< [pm]                                                   */
#define DATA_UNIT_V           0x0004  /**< [V]                                                    */
#define DATA_UNIT_MV          0x0005  /**< [mV]                                                   */
#define DATA_UNIT_UV          0x0006  /**< [uV]                                                   */
#define DATA_UNIT_NV          0x0007  /**< [nV]                                                   */
#define DATA_UNIT_MHZ         0x0008  /**< [MHz]                                                  */
#define DATA_UNIT_KHZ         0x0009  /**< [kHz]                                                  */
#define DATA_UNIT_HZ          0x000A  /**< [Hz]                                                   */
#define DATA_UNIT_IHZ         0x000B  /**< [mHz]                                                  */
#define DATA_UNIT_S           0x000C  /**< [s]                                                    */
#define DATA_UNIT_MS          0x000D  /**< [ms]                                                   */
#define DATA_UNIT_US          0x000E  /**< [us]                                                   */
#define DATA_UNIT_NS          0x000F  /**< [ns]                                                   */
#define DATA_UNIT_A           0x0010  /**< [A]                                                    */
#define DATA_UNIT_MA          0x0011  /**< [mA]                                                   */
#define DATA_UNIT_UA          0x0012  /**< [uA]                                                   */
#define DATA_UNIT_NA          0x0013  /**< [nA]                                                   */
#define DATA_UNIT_DEG         0x0014  /**< [deg]                                                  */
#define DATA_UNIT_COS         0x0018  /**< [cos]                                                  */
#define DATA_UNIT_DB          0x001C  /**< [dB]                                                   */
#define DATA_UNIT_W           0x0020  /**< [W]                                                    */
#define DATA_UNIT_MW          0x0021  /**< [mW]                                                   */
#define DATA_UNIT_UW          0x0022  /**< [uW]                                                   */
#define DATA_UNIT_NW          0x0023  /**< [nW]                                                   */
/* @} */


#endif
