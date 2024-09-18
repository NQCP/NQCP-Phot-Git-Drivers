/******************************************************************************
 *
 *  Project:        Daisy Client Library
 *
 *  Filename:       daisybase.h
 *
 *  Purpose:        Controller High Level API
 *
 *  Author:         NHands GmbH & Co KG
 */
/*****************************************************************************/
/** @file daisybase.h
 *  @brief Controller High Level API
 *
 *  Defines functions for the control of the controller via the
 *  application server: boot, configure, get data.
 *
 *  The communication doesn't take place directly with the controller but via
 *  an application server connected over TCP. Only "high level" control with
 *  product specific semantics is possible; the server manages the
 *  translation to "low level" commands to the controller.
 *
 *  An application using this library is referred to as "client".
 *  Several clients can be run at the same time.
 *  The server is started automatically if required.
 *
 *  The control functions are generic; a product specific list of actual
 *  parameters is provided by a separate header file.
 *
 *  @warning The functions are not thread safe.
 *  Most of them (exceptions are explicitly marked) may be called from the
 *  librarie's callback functions as long as no other thread is accessing at
 *  the same time. But note that no receiving is possible as long as a callback
 *  function is running.
 */
/*****************************************************************************/
/* $Id: daisybase.h,v 1.13 2016/10/24 17:55:23 trurl Exp $ */

#ifndef __DAISYBASE_H
#define __DAISYBASE_H

#include "daisydecl.h"
#include "metadata.h"


/**  @brief Return codes of the functions                                     */
typedef enum {
  DYB_Ok,                                /**< No error                        */
  DYB_Error,                             /**< Unknown / other error           */
  DYB_Timeout,                           /**< Communication timeout           */
  DYB_NotConnected,                      /**< No contact to controller via USB*/
  DYB_DriverError,                       /**< Error when calling USB driver   */
  DYB_FileNotFound,                      /**< Controller boot image not found */
  DYB_SrvNotFound,                       /**< Server executable not found     */
  DYB_ServerLost,                        /**< No contact to the server        */
  DYB_OutOfRange,                        /**< Invalid parameter in fct call   */
  DYB_WrongContext,                      /**< Call in invalid thread context  */
  DYB_XmlError,                          /**< Invalid format of profile file  */
  DYB_OpenError                          /**< Can't open specified file       */
} DYB_Rc;


/** @brief Data Callback Function
 *
 *  Functions of this type can be registered as callback functions for data
 *  channels. They will be called by the event loop as soon as data for the
 *  specified channel arrive. The data are always transferred in 32 bit items
 *  but the encoding depends on the product and the channel.
 *  The meta data buffer contains information required to interpret the data.
 *  See @ref metadata.h for details.
 *
 *  The index counts the data since the begin of the measurement, i.e. it is
 *  incremented from call to call by length. It also counts data that have been
 *  lost due to performance problems of the control PC. To avoid overflow, the
 *  index is resetted from time to time in a way that doesn't affect the
 *  calculation of the independent variables. When data stem from a scan,
 *  every frame begins with a new data packet with an index of 0.
 *
 *  The buffer that contains the data is static and will be overwritten in
 *  the next call. It must not be free()'d or used by the application to
 *  store data.
 * 
 *  To use the data channels they must be enabled by using @ref ID_DATA_EN
 *
 *  @param  channel  Data channel that has sent the data
 *  @param  length   Length of the packet (number of Int32 items)
 *  @param  index    Number of the first item of the packet
 *  @param  buffer   Pointer to the data buffer
 *  @param  meta     Pointer to the corresponding meta data
 */
typedef void (* DYB_DataCallback) ( Int32 channel,
                                    Int32 length,
                                    Int32 index,
                                    const Int32 * data,
                                    const DYB_Meta * meta );


/** @brief Event Callback Function
 *
 *  Functions of this type can be registered as callback functions for events.
 *  They will be called by the event loop as soon as the specified parameter
 *  arrives.
 *
 *  "Event" here means the notification about the change of a parameter
 *  caused by the client itself, by another client, or autonomously by the
 *  server. Also the event may be the answer to a parameter inquiry to the
 *  server.
 *
 *  Note that changing one parameter by the client may in turn cause the
 *  change of several others. Sometimes the events may be redundant, i.e.
 *  the value of the parameter hasn't changed since the last call.
 *
 *  @param  address  Address of the parameter that has been changed
 *  @param  index    If defined for the parameter: subaddress, 0 otherwise
 *  @param  value    New value of the parameter
 */
typedef void (* DYB_EventCallback) ( DYB_Address address,
                                     Int32 index,
                                     Int32 value );

/** @brief Configure Library
 *
 *  This function makes some basic settings for the library and has to be
 *  called before all other functions.
 *
 *  The path to the application server must be specified to allow automatic
 *  starting. If the server resides on another computer and should be
 *  accessed via network, its network address must be specified. Obviously
 *  it can't be started automatically in this case.
 *
 *  The @em binPath is required for automatic starting of the server and
 *  booting the controller. It points to the directory where the executable
 *  of the application server daisysrv(.exe) resides.
 *  Usually this is the daisy program directory.
 *
 *  @param unused      Unused Parameter, left for backward compatibility only.
 *                     Use NULL or empty string.
 *  @param binPath     Path to the server executables. Can be left empty if
 *                     the server resides on another computer or automatic
 *                     start is not required.
 *  @param serverHost  Hostname or IP address in "dotted decimal" notation
 *                     for the host where the application server resides.
 *                     NULL or empty if the server should run locally.
 *  @param serverPort  TCP port number of the server, required in any case.
 *                     The number is product specific and can be found in
 *                     the product specific header file.
 *  @return
 *     @ref DYB_Ok           - Successfull
 *  @n @ref DYB_OutOfRange   - Invalid parameters
 */
DYB_API DYB_Rc DYB_CC DYB_init( const char * unused,
                                const char * binPath,
                                const char * serverHost,
                                unsigned short serverPort );


/** @brief Start Event Loop and boot Controller if necessary
 *
 *  If an already running server is found, a connection is made up and the
 *  event loop is started.
 *  
 *  If no server is present, it is started automatically. In turn, it
 *  initializes the USB communication to the controller and tries to boot it.
 *  The controller ignores booting if it is already running. To force a
 *  reboot, DYB_reset() must be called.
 *
 *  Callback functions may be registered before this call, control functions
 *  must be called later.
 *
 *  If a server is to be started, the function requires to find its executable
 *  and the boot images of the controller at the binPath configured by
 *  DYB_init().
 *
 *  @return
 *     @ref DYB_Ok           - Successfully started or already running
 *  @n @ref DYB_DriverError  - Driver problem - driver not installed?
 *  @n @ref DYB_NotConnected - No contact to controller - USB-Wiring? DC-Power?
 *  @n @ref DYB_SrvNotFound  - Server executable not found
 *  @n @ref DYB_FileNotFound - One of the boot images has not been found
 *  @n @ref DYB_ServerLost   - Could not connect to the server
 *  @n @ref DYB_Error        - Unknown error
 */
DYB_API DYB_Rc DYB_CC DYB_run( void );


/** @brief Terminate Event Loop
 *
 *  Terminates the event loop without any commands to the controller.
 *  The connection to the server is closed; in turn the server will
 *  shut down if no other client is connected to it.
 *
 *  @return @ref DYB_Ok (always ok)
 */
DYB_API DYB_Rc DYB_CC DYB_stop( void );


/** @brief Controller Reset
 *
 *  Performs a reset of the controller, shuts down the server and terminates
 *  the event loop. This call is necessary to reboot the controller.
 *  It takes a few seconds.
 *
 *  @return @ref DYB_Ok (always ok)
 */
DYB_API DYB_Rc DYB_CC DYB_reset( void );


/** @brief Register Data Callback Function
 *
 *  Registers a callback function for a data channel. That function will be
 *  called when new data arrive on the channel. A callback function registered
 *  previously is unregistered.
 *
 *  The function is called in the context of a thread that serves the
 *  event loop. If it is not processed fast enough, events or data may be lost.
 *
 *  To use the data channels they must be enabled by using @ref ID_DATA_EN
 *
 *  @param  channel    Number of the data channel. Numbers begin with 0,
 *                     the maximum is product specifc.
 *  @param  callback   Callback function for that channel,
 *                     use NULL to unregister a function
 *  @return
 *     @ref DYB_Ok           - Successful
 *  @n @ref DYB_ServerLost   - Data request failed - server not running?
 */
DYB_API DYB_Rc DYB_CC DYB_setDataCallback( Int32 channel,
                                           DYB_DataCallback callback );


/** @brief Register Event Callback Function
 *
 *  Registers a callback function for an event. That function will be called
 *  when the event is recognized.  A callback function registered previously
 *  is unregistered.
 *
 *  The function is called in the context of a thread that serves the
 *  event loop. If it is not processed fast enough, events or data may be lost.
 *
 *  It is possible to register a "catchall" callback for all events not
 *  explicitly handled by using the invalid address -1.
 *
 *  @param  address    Identification of the parameter that is observed,
 *                     -1 for catchall
 *  @param  callback   Callback function for that event
 *  @return @ref DYB_Ok (always ok)
 */
DYB_API DYB_Rc DYB_CC DYB_setEventCallback( DYB_Address address,
                                            DYB_EventCallback callback );


/** @brief Set a Parameter
 *
 *  Generic function that sends a single parameter value to the server.
 *  It may be accepted, rejected or limited by the server, which
 *  returns an event with the value actually in place.
 *  The answer may be caught by a matching event callback; the function
 *  doesn't wait for it.
 *
 *  The semantics depends on the address and the index (if applicable).
 *
 *  @param  address  Identification of the parameter
 *  @param  index    If defined for the parameter: subaddress, 0 otherwise
 *  @param  value    New parameter value
 *  @return
 *     @ref DYB_Ok           - Success
 *  @n @ref DYB_ServerLost   - Can't send - server not running?
 */
DYB_API DYB_Rc DYB_CC DYB_setParameterAsync( DYB_Address address,
                                             Int32 index,
                                             Int32 value );


/** @brief Set a Parameter and wait for Acknowledgement
 *
 *  Generic function that sends a single parameter value to the server
 *  and waits for the acknowledgement. The acknowledged value is returned.
 *  The semantics depends on the address and the index (if applicable).
 *
 *  The function must not be called in the context of a data or event callback.
 *
 *  @param  address  Identification of the parameter
 *  @param  index    If defined for the parameter: subaddress, 0 otherwise
 *  @param  value    New parameter value
 *  @param  returned  Output: The parameter value as returned from the server.
 *  @return
 *     @ref DYB_Ok           - Success
 *  @n @ref DYB_ServerLost   - Can't send - server not running?
 *  @n @ref DYB_WrongContext - Forbidden call from a callback function
 */
DYB_API DYB_Rc DYB_CC DYB_setParameterSync( DYB_Address address,
                                            Int32 index,
                                            Int32 value,
                                            Int32 * returned );


/** @brief Asynchronous Inquiry about a Parameter
 *
 *  The function sends an inquiry about a single parameter value to the server
 *  and returns immediately. The answer must be received by a matching
 *  event callback.
 *
 *  @param  address  Identification of the parameter
 *  @param  index    If defined for the parameter: subaddress, 0 otherwise
 *  @return
 *     @ref DYB_Ok           - Success
 *  @n @ref DYB_ServerLost   - Can't send - server not running?
 *  @n @ref DYB_Timeout      - No answer from the server
 */
DYB_API DYB_Rc DYB_CC DYB_getParameterAsync( DYB_Address address,
                                             Int32 index );


/** @brief Synchronous Inquiry about a Parameter
 *
 *  The function sends an inquiry about a single parameter value to the server
 *  and waits for the answer. This may take a few ms at most.
 *
 *  The function must not be called in the context of a data or event callback.
 *
 *  @param  address  Identification of the parameter
 *  @param  index    If defined for the parameter: subaddress, 0 otherwise
 *  @param  data     Output: Parameter value
 *  @return
 *     @ref DYB_Ok           - Success
 *  @n @ref DYB_ServerLost   - Can't send - server not running?
 *  @n @ref DYB_Timeout      - No answer from the server
 *  @n @ref DYB_WrongContext - Forbidden call from a callback function
 */
DYB_API DYB_Rc DYB_CC DYB_getParameterSync( DYB_Address address,
                                            Int32 index,
                                            Int32 * data );


/** @brief Send a Parameter Set
 *
 *  Reads a daisy profile file (NHands GUI Profile, usually *.ngp) and sends
 *  the parameter values contained in it to the application server.
 *  All other (GUI specific) stuff in that file is ignored.
 *
 *  The function may run several seconds. Note that a whole lot of parameter
 *  change notifications may be sent back during that time. It may be useful
 *  to deactivate the event callback functions temporarily.
 *
 *  The function must not be called in the context of a data or event callback.
 *
 *  @param  profile  Filename of the profile file
 *  @return
 *     @ref DYB_Ok           - Success
 *  @n @ref DYB_ServerLost   - Can't send - server not running?
 *  @n @ref DYB_OpenError    - Can't open profile file
 *  @n @ref DYB_XmlError     - Wrong format of profile file
 *  @n @ref DYB_WrongContext - Forbidden call from a callback function
 */
DYB_API DYB_Rc DYB_CC DYB_sendProfile( const char * profile );


#endif
