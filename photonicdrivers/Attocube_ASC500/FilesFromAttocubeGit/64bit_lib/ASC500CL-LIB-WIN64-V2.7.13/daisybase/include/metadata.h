/******************************************************************************
 *
 *  Project:        Daisy Client Library
 *
 *  Filename:       metadata.h
 *
 *  Purpose:        Service Functions for Data Evaluation
 *
 *  Author:         NHands GmbH & Co KG
 */
/******************************************************************************/
/** @file metadata.h
 *  @brief Service Functions for Data Evaluation
 *
 *  Defines functions for the interpretation of data received from the
 *  NHands controller.
 *
 *  All measurement data received come together with a set of metadata
 *  that describes the encoding of independent and dependent variables and
 *  allows the conversion to physical units.
 *  The metadata reflect the configuration of the measurement but are strictly
 *  synchronized with the data. I.e. a set of meta data always belongs to the
 *  data block it is delivered with, no matter if the corresponding configuration
 *  has been delayed for some reason.
 *
 *  The metadata don't change during a measurement as long as no important
 *  parameters are changed.
 */
/******************************************************************************/
/* $Id: metadata.h,v 1.12.8.2 2021/02/09 12:24:01 trurl Exp $ */

#ifndef __METADATA_H
#define __METADATA_H

#include "daisydecl.h"


/** @brief Data Ordering
 *
 *  Ordering of the data, i.e. the kind of mapping of the data index to the
 *  physical independent variable(s). The variable(s) may
 *
 *  - be one (like time) or two (a scan),
 *
 *  - grow unlimited (like time) or may be cyclic (like a scan),
 *
 *  - have an absolutely defined origin (e.g. spectroscopy) or not
 *    (like time, again)
 *
 *  - perform a scan beginning with a line in forward or backward direction,
 *
 *  - have subsequent scan lines in the same direction only or alternating
 *    between forward and backward.
 *
 *  The first frame of a scan always runs bottom to top, the Y direction
 *  of subsequent frames alternate.
 */
typedef enum {
  DYB_Linear    = 0,   /**< 1 Variable, unlimited, no origin defined          */
  DYB_Triggered = 1,   /**< 1 Variable, unlimited, absolute origin defined    */
  DYB_Cyclic    = 2,   /**< 1 Variable, ranging from absolute origin to limit */
  DYB_FfScan    = 3,   /**< 2 Variables, forward-forward scan, origin defined */
  DYB_FbScan    = 4,   /**< 2 Variables, forward-backward scan, origin def    */
  DYB_BbScan    = 5,   /**< 2 Variables, backward-backward scan, origin def   */
  DYB_BfScan    = 6,   /**< 2 Variables, backward-forward scan, origin def    */
  DYB_BfNone           /**< Invalid order                                     */
} DYB_Order;


/** @brief Physical Unit
 *
 *  Possible physical units of independent and dependent variables.
 *  Note that lowest byte encodes a scaling factor.
 */
typedef enum {
  DYB_UnitNone = 0x0080,  /**< No unit, invalid                               */
  DYB_UnitM    = 0x0180,  /**< Meter                                          */
  DYB_UnitMm   = 0x017F,  /**< MilliMeter                                     */
  DYB_UnitUm   = 0x017E,  /**< MicroMeter                                     */
  DYB_UnitNm   = 0x017D,  /**< NanoMeter                                      */
  DYB_UnitPm   = 0x017C,  /**< PicoMeter                                      */
  DYB_UnitV    = 0x0280,  /**< Volt                                           */
  DYB_UnitMv   = 0x027F,  /**< MilliVolt                                      */
  DYB_UnitUv   = 0x027E,  /**< MicroVolt                                      */
  DYB_UnitNv   = 0x027D,  /**< NanoVolt                                       */
  DYB_UnitMhz  = 0x0382,  /**< MegaHertz                                      */
  DYB_UnitKhz  = 0x0381,  /**< KiloHertz                                      */
  DYB_UnitHz   = 0x0380,  /**< Hertz                                          */
  DYB_UnitIhz  = 0x037F,  /**< MilliHertz                                     */
  DYB_UnitKs   = 0x0481,  /**< KiloSecond                                     */
  DYB_UnitS    = 0x0480,  /**< Second                                         */
  DYB_UnitMs   = 0x047F,  /**< MilliSecond                                    */
  DYB_UnitUs   = 0x047E,  /**< MicroSecond                                    */
  DYB_UnitNs   = 0x047D,  /**< NanoSecond                                     */
  DYB_UnitPs   = 0x047C,  /**< PicoSecond                                     */
  DYB_UnitA    = 0x0580,  /**< Ampere                                         */
  DYB_UnitMa   = 0x057F,  /**< MilliAmpere                                    */
  DYB_UnitUa   = 0x057E,  /**< MicroAmpere                                    */
  DYB_UnitNa   = 0x057D,  /**< NanoAmpere                                     */
  DYB_UnitW    = 0x0680,  /**< Watt                                           */
  DYB_UnitMw   = 0x067F,  /**< MilliWatt                                      */
  DYB_UnitUw   = 0x067E,  /**< MicroWatt                                      */
  DYB_UnitNw   = 0x067D,  /**< NanoWatt                                       */
  DYB_UnitT    = 0x0780,  /**< Tesla                                          */
  DYB_UnitMt   = 0x077F,  /**< MilliTesla                                     */
  DYB_UnitUt   = 0x077E,  /**< MicroTesla                                     */
  DYB_UnitNt   = 0x077D,  /**< NanoTesla                                      */
  DYB_UnitK    = 0x0880,  /**< Kelvin                                         */
  DYB_UnitMk   = 0x087F,  /**< MilliKelvin                                    */
  DYB_UnitUk   = 0x087E,  /**< MicroKelvin                                    */
  DYB_UnitNk   = 0x087D,  /**< NanoKelvin                                     */
  DYB_UnitDeg  = 0x0980,  /**< Angular Degree                                 */
  DYB_UnitMdeg = 0x097F,  /**< MilliDegree                                    */
  DYB_UnitUdeg = 0x097E,  /**< MicroDegree                                    */
  DYB_UnitNdeg = 0x097D,  /**< NanoDegree                                     */
  DYB_UnitCos  = 0x0A80,  /**< Cosine                                         */
  DYB_UnitDB   = 0x0B80,  /**< dB                                             */
  DYB_UnitLSB  = 0x0C80   /**< LSB                                            */
} DYB_Unit;


/** @brief Metadata for measurement results
 *
 *  This struct contains a set of metadata describing the encoding of
 *  dependent and independent variables of the measurement results
 *  delivered by a data callback function.
 *
 *  Depending on the _order, some entries may be invalid.
 *
 *  The struct may be subject to change; as far as possible use the functions
 *  declared below instead of directly accessing the data fields.
 */
typedef struct {
  DYB_Order _order;    /**< Data order                                        */
  Int32     _pointsX;  /**< Number of data in a line                          */
  Int32     _pointsY;  /**< Number of lines (of a scan)                       */
  Flt32     _stepX;    /**< Distance of two data points in physical units     */
  Flt32     _stepY;    /**< Distance of two lines in physical units           */
  Flt32     _originX;  /**< Position (X) of the first point in physical units */
  Flt32     _originY;  /**< Position (Y) of the first point in physical units */
  Flt32     _rotation; /**< Rotation angle of scan area in rad                */
  DYB_Unit  _unitXY;   /**< Physical unit of independent variable(s)          */
  Flt32     _stepVal;  /**< Scale of data values, i.e. the number of physical
                            units correspoding to the LSB                     */
  Flt32     _stepValNum;/**< Scale numerator of data values, i.e. the LSB 
                            corresonding to physical units                    */
  Flt32    _offsetVal; /**< Offset to the data values in units                */
  DYB_Unit _unitVal;   /**< Physical unit of data values                      */
} DYB_Meta;



/** @brief Returncodes of the functions                                              */
typedef enum {
  DYB_MetaOk      = 0, /**< Function call was successful                      */
  DYB_MetaNotApp  = 1, /**< Function not applicable for current data order    */
  DYB_MetaInvalid = 2  /**< Meta data set is invalid                          */
} DYB_MRc;


/** @brief Extract Data Order
 *
 *  Extracts the data order from the meta data set.
 *  @param meta      Meta data set
 *  @return          Data order
 */
DYB_API DYB_Order DYB_CC DYB_getOrder( const DYB_Meta * meta );


/** @brief Data Points in a Line
 *
 *  Extract the number of data points in a row if applicable.
 *  @param meta      Meta data set
 *  @param pointsX   Output: Number of points
 *  @return          Success code
 */
DYB_API DYB_MRc DYB_CC DYB_getPointsX( const DYB_Meta * meta, Int32 * pointsX );


/** @brief Number of Lines
 *
 *  Extract the number of lines of a scan if applicable.
 *  @param meta      Meta data set
 *  @param pointsY   Output: Number of lines
 *  @return          Success code
 */
DYB_API DYB_MRc DYB_CC DYB_getPointsY( const DYB_Meta * meta, Int32 * pointsY );


/** @brief Unit of independent Variable(s)
 *
 *  Returns the common unit of all independent variables.
 *  @param meta      Meta data set
 *  @return          Unit
 */
DYB_API DYB_Unit DYB_CC DYB_getUnitXY( const DYB_Meta * meta );


/** @brief Unit of dependent Variable
 *
 *  Returns the unit of the data.
 *  @param meta      Meta data set
 *  @return          Unit
 */
DYB_API DYB_Unit DYB_CC DYB_getUnitVal( const DYB_Meta * meta );


/** @brief Scan Range Rotation
 *
 *  Returns the rotation angle of the scan area if the data originate
 *  from a scan.
 *  @param meta      Meta data set
 *  @param rotation  Output: Rotation angle [rad]
 *  @return          Success code
 */
DYB_API DYB_MRc DYB_CC DYB_getRotation( const DYB_Meta * meta, Flt32 * rotation );


/** @brief Physical Range X
 *
 *  Returns the physical length of a line of data for cyclic data order.
 *  The length is the distance between the first and the last point of the line.
 *  @param meta      Meta data set
 *  @param rangeX    Output: Line length
 *  @return          Success code
 */
DYB_API DYB_MRc DYB_CC DYB_getPhysRangeX( const DYB_Meta * meta, Flt32 * rangeX );


/** @brief Physical Range Y
 *
 *  Returns the physical height of the scan area if applicable.
 *  The height is the distance between the first and the last line of the frame.
 *  @param meta      Meta data set
 *  @param rangeY    Output: Column height
 *  @return          Success code
 */
DYB_API DYB_MRc DYB_CC DYB_getPhysRangeY( const DYB_Meta * meta, Flt32 * rangeY );


/** @brief Pixel Position from Data Index
 *
 *  Converts a data index to the pixel position (i.e. column and line number)
 *  if the data originate from a scan. The coordinate origin is bottom left.
 *  @param meta      Meta data set
 *  @param index     Data index
 *  @param x         Output: Horizontal pixel position (column number)
 *  @param y         Output: Vertical pixel position (line number)
 *  @return          Success code
 */
DYB_API DYB_MRc DYB_CC DYB_convIndex2Pixel( const DYB_Meta * meta, Int32 index,
                                            Int32 * x, Int32 * y );

/** @brief Scan Direction from Data Index
 *
 *  Calclulates the current scan direction corresponding to a particular index.
 *  The direction is seen from the coordinate origin which is bottom left.
 *  @param meta      Meta data set
 *  @param index     Data index
 *  @param forward   Output: If the current scan direction is forward
 *  @param upward    Output: If the current scan direction is upward
 *  @return          Success code
 */
DYB_API DYB_MRc DYB_CC DYB_convIndex2Direction( const DYB_Meta * meta, Int32 index,
                                                Bln32 * forward, Bln32 * upward );


/** @brief Physical Position from Data Index for one variable
 *
 *  Converts a data index to the physical coordinates of the data point
 *  if one independent variable exists. If the data order is @ref DYB_Linear,
 *  the absolute value is meaningless but differences are valid.
 *  The corresponding unit can be retreived by DYB_getUnitXY().
 *  @param meta      Meta data set
 *  @param index     Data index
 *  @param x         Output: independent variable
 *  @return          Success code
 */
DYB_API DYB_MRc DYB_CC DYB_convIndex2Phys1( const DYB_Meta * meta, Int32 index,
                                            Flt32 * x );


/** @brief Physical Position from Data Index for two variables
 *
 *  Converts a data index to the physical coordinates of the data point
 *  if the data originate from a scan. The origin is bottom left.
 *  The corresponding unit can be retreived by DYB_getUnitXY().
 *  @param meta      Meta data set
 *  @param index     Data index
 *  @param x         Output: Horizontal position
 *  @param y         Output: Vertical position
 *  @return          Success code
 */
DYB_API DYB_MRc DYB_CC DYB_convIndex2Phys2( const DYB_Meta * meta, Int32 index,
                                            Flt32 * x, Flt32 * y );


/** @brief Data Value
 *
 *  Converts a raw data value to the physical value.
 *  The unit can be retreived by DYB_getUnitVal().
 *  @param meta      Meta data set
 *  @param value     Raw data value
 *  @return          Physical value
 */
DYB_API Flt32 DYB_CC DYB_convValue2Phys( const DYB_Meta * meta, Int32 value );



/** @brief Make up Value for Printing
 *
 *  A physical value consisting of number and unit is rescaled for
 *  comfortable reading. The unit is prefixed with a magnitude prefix
 *  (like "k" or "n") so that the number ranges between 1 and 1000.
 *  Prefix and unit are provided as a printable string.
 *  If the unit is invalid, the number will be unchanged and the unit string
 *  will be "?".
 *  @param number    Number belonging to the physical value
 *  @param unit      Unit   belonging to the physical value
 *  @param unitStr   String buffer of at least 10 chars. On output it will
 *                   contain the prefixed unit after rescaling (encoded in Latin1)
 *  @return          Number after rescaling.
 */
DYB_API Flt32 DYB_CC DYB_convPhys2Print( Flt32 number, DYB_Unit unit, char * unitStr );


#endif
