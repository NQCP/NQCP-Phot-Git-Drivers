/******************************************************************************
 *
 *  Project:        Daisy Client Library
 *
 *  Filename:       daisydata.h
 *
 *  Purpose:        Service functions for data handling on top of daisybase.h
 *
 *  Author:         NHands GmbH & Co KG
 */
/*****************************************************************************/
/** @file daisydata.h
 *  @brief Service functions for data handling on top of @ref daisybase.h
 *
 *  Defines functions that simplify the use of the daisybase library -
 *  primarily the data handling. They allow to avoid callback functions
 *  (@ref DYB_setDataCallback, @ref DYB_setEventCallback) (and thus the need of
 *  thread synchronisation) in application programs.
 *  
 *  These functions must not be called from the context of a daisybase
 *  callback function.
 */
/*****************************************************************************/
/* $Id: daisydata.h,v 1.4 2016/12/01 18:02:32 trurl Exp $ */

#ifndef __ASC500HELPERS_H
#define __ASC500HELPERS_H

#include "daisydecl.h"
#include "daisybase.h"


/** @name Event Types
 *
 *  @anchor EventTypes
 *  Event identifiers for @ref DYB_waitForEvent.
 *  Can be extended!
 *  @{
 */
#define DYB_EVT_DATA_00  0x00000001  /**< Event: Full buffer on data channel  0 */
#define DYB_EVT_DATA_01  0x00000002  /**< Event: Full buffer on data channel  1 */
#define DYB_EVT_DATA_02  0x00000004  /**< Event: Full buffer on data channel  2 */
#define DYB_EVT_DATA_03  0x00000008  /**< Event: Full buffer on data channel  3 */
#define DYB_EVT_DATA_04  0x00000010  /**< Event: Full buffer on data channel  4 */
#define DYB_EVT_DATA_05  0x00000020  /**< Event: Full buffer on data channel  5 */
#define DYB_EVT_DATA_06  0x00000040  /**< Event: Full buffer on data channel  6 */
#define DYB_EVT_DATA_07  0x00000080  /**< Event: Full buffer on data channel  7 */
#define DYB_EVT_DATA_08  0x00000100  /**< Event: Full buffer on data channel  8 */
#define DYB_EVT_DATA_09  0x00000200  /**< Event: Full buffer on data channel  9 */
#define DYB_EVT_DATA_10  0x00000400  /**< Event: Full buffer on data channel 10 */
#define DYB_EVT_DATA_11  0x00000800  /**< Event: Full buffer on data channel 11 */
#define DYB_EVT_DATA_12  0x00001000  /**< Event: Full buffer on data channel 12 */
#define DYB_EVT_DATA_13  0x00002000  /**< Event: Full buffer on data channel 13 */
#define DYB_EVT_HANDSHK  0x00004000  /**< Event: Path mode handshake request    */
#define DYB_EVT_CUSTOM   0x00008000  /**< Event: Custom parameter received      */
/* @} */


/** @brief Interpret return codes

 *  Returns a descriptive text for a given daisybase return code
 *  @param  rc       return code of a daisybase function
 *  @return          Error description (if any) or "Ok";
 *                   "????" indicates an invalid error code
 */
DYB_API const char * DYB_printRc( DYB_Rc rc );


/** @brief Interpret data units

 *  Returns the unit as an ASCII string (no greek letters).
 *  @param  unit     Unit encoding from a @ref DYB_Meta structure.
 *  @return          Unit as ASCII string.
 *                   "?" indicates an invalid unit code
 */
DYB_API const char * DYB_printUnit( DYB_Unit unit );


/** @brief Configure a Data Channel
 *
 *  Configures what kind of data is sent on a specific data channel.
 *
 *  @param  number   Number of the channel to be configured (0..13)
 *  @param  trigger  Trigger source for data output (one of CHANCONN_..)
 *  @param  source   Data source for the channel (one of CHANADC_..)
 *  @param  average  If data should be averaged over the sample time (boolean)
 *  @param  smpTime  Time per sample in [s]. Has no effect unless the
 *                   channel is timer triggered.
 *  @return
 *     @ref DYB_Ok           - Success
 *  @n @ref DYB_OutOfRange   - Invalid channel number
 *  @n @ref DYB_ServerLost   - Can't send - server not running?
 */
DYB_API DYB_Rc DYB_configureChannel( Int32  number,
                                     Int32  trigger,
                                     Int32  source,
                                     Bln32  average,
                                     double smpTime );


/** @brief Retrieve Data Channel Configuration
 *
 *  Reads out the channel configuration as set by @ref DYB_configureChannel.
 *  @param  number   Number of the channel of interest (0..13)
 *  @param  trigger  Output: Trigger source for data output (one of CHANCONN_..)
 *  @param  source   Output: Data source for the channel (one of CHANADC_..)
 *  @param  average  Output: If the data are averaged over the sample time (boolean)
 *  @param  smpTime  Output: Time per sample in [s]. The returned value is valid
 *                   even if the sample time is controlled by the trigger source.
 *  @return
 *     @ref DYB_Ok           - Success
 *  @n @ref DYB_OutOfRange   - Invalid channel number
 *  @n @ref DYB_ServerLost   - Can't send - server not running?
 */
DYB_API DYB_Rc DYB_getChannelConfig( Int32    number,
                                     Int32  * trigger,
                                     Int32  * source,
                                     Bln32  * average,
                                     double * smpTime );


/** @brief Configure Data Channel Buffering
 *
 *  The function configures if data arriving from a specific data channel are
 *  buffered and sets the default size of the buffer.
 *
 *  If the default size is set to 0, data are not buffered and data callback functions
 *  of daisybase (@ref DYB_setDataCallback) can be used.
 *
 *  If it is set to a positive value, the data are buffered and can be retreived with
 *  @ref DYB_getDataBuffer. The actual value of the size is relevant only for data
 *  channels that are triggered by timer; in all other cases the "native" buffer size
 *  is used. If size is too small (< 128), timer triggered data will not be buffered
 *  to avoid too mucht buffer-full events.
 *  
 *  If buffering is enabled, no data callback function can be used for the channel.
 *  @param   channel  Number of the channel of interest (0..13)
 *  @param   size     Buffer size [32 bit items]
 *  @return
 *     @ref DYB_Ok           - Success
 *  @n @ref DYB_OutOfRange   - size too big (> 1M) or negative
 */
DYB_API DYB_Rc DYB_configureDataBuffering( Int32 channel,
                                           Int32 size );

/** @brief Get Size of Data Frame
 *
 *  The function returns the size of a complete data frame for the channel.
 *  This is the buffer size required for a call to @ref DYB_getDataBuffer.
 *
 *  The size may vary when measurement parameters are changed. It is not valid
 *  before the data acquisition has started!
 *  @param   channel  Number of the channel of interest (0..13)
 *  @return           Frame size [32 bit items]; 0 if the channel number is
 *                    invalid or the channel is not active.
 */
DYB_API Int32 DYB_getFrameSize( Int32 channel );


/** @brief Retrieve Data Channel Buffer
 *
 *  If a data channel is configured for buffering with @ref DYB_configureDataBuffering,
 *  the next buffer can be retrieved with this function without using data callback functions.
 *
 *  Normally, only completely filled buffers are returned and an error @ref DYB_OutOfRange is
 *  signalled when no full buffer is available. No data will be returned twice.
 *  The user can change this behaviour by requesting also partially filled buffers with
 *  the parameter fullOnly = 0. The partially filled buffer may be returned multiple times
 *  until it is full. In the case of scanner triggered data, a frame is considered full when
 *  the upmost OR the lowermost line has been scanned.
 *
 *  A data frame is available when it is complete until it is retrieved or the next frame
 *  is complete. If it is not retrieved in time, the frame number may "jump".
 *  @param   channel    Number of the channel of interest (0..13)
 *  @param   fullOnly   If only completely filled buffers are requested.
 *  @param   frameNo    Output: Number of the frame. With fullOnly=0 the same frame can
 *                      be returned repeatedly.
 *  @param   index      Output: Index of the first element in the buffer.
 *  @param   dataSize   Input:  Size of the data buffer provided by the user.
 *                      If insufficient, @ref DYB_OutOfRange will be returned.
 *                      Output: Number of valid data (32-bit items) in the buffer.
 *  @param   data       Output: Pointer to an array to store the data. The array
 *                      must be provided by the caller and its size must be
 *                      at least one frame size (@ref DYB_getFrameSize).
 *  @param   meta       Output: Pointer to a space to copy the meta data.
 *                      The space must be provided by the caller.
 *  @return
 *     @ref DYB_Ok           - Success
 *  @n @ref DYB_OutOfRange   - No full buffer available
 */
DYB_API DYB_Rc DYB_getDataBuffer( Int32      channel,
                                  Bln32      fullOnly,
                                  Int32    * frameNo,
                                  Int32    * index,
                                  Int32    * dataSize,
                                  Int32    * data,
                                  DYB_Meta * meta );


/** @brief Write Buffer to file
 *
 *  Writes a buffer (as retrieved with @ref DYB_getDataBuffer) to a file of
 *  an appropriate ascii or binary format. The format is chosen automatically
 *  according to the meta data.
 *
 *  Available formats are "bcrf" (binary) and "asc" (ascii) for scanner triggered data
 *  and "csv" for all other data. The formats are "Daisy compatible".
 *  @param   fileName   Name of the file to write, without extension (selected automatically).
 *  @param   comment    Data or channel description for the file header. Can be left blank.
 *  @param   binary     If the desired format is binary.
 *                      Relevant only for scanner triggered data, ignored otherwise.
 *  @param   forward    If the forward scan (in X direction) is to be written.
 *                      Relevant only for scanner triggered data, ignored otherwise.
 *  @param   index      Index of the first element in the buffer.
 *  @param   dataSize   Number of valid data (32-bit items) in the buffer.
 *  @param   data       The data buffer.
 *  @param   meta       Meta data belonging to the buffer.
 *  @return
 *     @ref DYB_Ok           - Success
 *  @n @ref DYB_OutOfRange   - Desired format not available
 *  @n @ref DYB_OpenError    - Can't write to file
 */
DYB_API DYB_Rc DYB_writeBuffer( const char     * fileName,
                                const char     * comment,
                                Bln32            binary,
                                Bln32            forward,
                                Int32            index,
                                Int32            dataSize,
                                const Int32    * data,
                                const DYB_Meta * meta );


/** @brief Wait for Events
 *
 *  The function waits until one of the specified events occur or on timeout.
 *  Note that there is a danger of race conditions: the event may have been
 *  occured before you begin waiting for it. The function can't recognize this case.
 *  @param   timeout   wait timeout [ms]
 *  @param   eventMask Events to wait for: bitfield that combines some of the
 *                     @ref EventTypes "event types"
 *  @param   customId  Address of a parameter to wait for. Only relevant if the
 *                     corresponding eventMask flag is set.
 *  @return            Event that actually woke up the function:
 *                     bitfield of @ref EventTypes "event types"
 */
DYB_API Int32 DYB_waitForEvent( Int32   timeout,
                                Int32   eventMask,
                                Int32   customId );


#endif
