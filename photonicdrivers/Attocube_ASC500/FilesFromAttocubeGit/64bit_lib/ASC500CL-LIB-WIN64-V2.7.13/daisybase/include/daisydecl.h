/******************************************************************************
 *
 *  Project:        Daisy Client Library
 *
 *  Filename:       daisydecl.h
 *
 *  Purpose:        Variants of Interface Declarations, Base Types
 *
 *  Author:         NHands GmbH & Co KG
 *
 */
/******************************************************************************/
/** @file daisydecl.h
 *  Variants of Interface Declarations, Base Types
 *
 *  Declaration of macros required for use with C and C++ and for the Windows
 *  DLL interface. Basic types.
 */
/******************************************************************************/
/* $Id: daisydecl.h,v 1.7 2017/11/28 15:01:40 trurl Exp $ */

#ifndef __DAISYDECL_H
#define __DAISYDECL_H

#ifdef __cplusplus
#define EXTC extern "C"                          /**< For use with C++        */
#else
#define EXTC extern                              /**< For use with C          */
#endif

#ifdef unix
#define DYB_API EXTC                             /**< Not required for Unix   */
#define DYB_CC                                   /**< Not required for Unix   */
#else
#define DYB_CC     /*  __stdcall */              /**< Calling conv. removed   */
#ifdef  DYB_EXPORTS
#define DYB_API EXTC __declspec(dllexport)       /**< For internal use        */
#else
#ifndef DYB_NO_DLL
#define DYB_API EXTC __declspec(dllimport)       /**< For external use        */
#else
#define DYB_API                                  /**< For non-DLL use         */
#endif
#endif
#endif

#ifdef _MSC_VER
typedef __int32 Int32;                           /**< 32 bit signed integer   */
#else
#include <inttypes.h>
typedef int32_t Int32;                           /**< 32 bit signed integer   */
#endif

typedef float  Flt32;                            /**< Single precision float  */
typedef int    Bln32;                            /**< Boolean (documentation) */
typedef Int32  DYB_Address;                      /**< Control parameter id    */

#endif
