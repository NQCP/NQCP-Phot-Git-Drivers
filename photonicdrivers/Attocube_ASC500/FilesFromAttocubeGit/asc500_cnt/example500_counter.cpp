#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>

#include "metadata.h"
#include "daisybase.h"
#include "daisydata.h"
#include "asc500.h"
#include <windows.h>

/** \brief Print error code if return is not "Ok".
 *
 * \param call const char* Name of function call.
 * \param rc const DYB_Rc Return value.
 * \return void
 *
 */
static void checkRc(const char *call, const DYB_Rc rc, const int line)
{
    if(rc != DYB_Ok)
        fprintf(stdout,
                "%s failed : %s, line %i\n",
                call,
                DYB_printRc(rc),
                line);
}


/** \brief Set parameter with error reporting.
 *
 * \param id const int32_t ID that identifies the parameter to set.
 * \param index const int32_t Sub ID for some parameters.
 * \param value const int32_t New value for the parameter.
 * \return void
 *
 */
static void setParameter(const int32_t id, const int32_t index, const int32_t value)
{
    DYB_Rc rc = DYB_setParameterAsync(id, index, value);
    if(rc != DYB_Ok)
        fprintf(stdout,
                "DYB_setParameterAsync failed for id %x,%x : %s\n",
                id, index, DYB_printRc(rc));
}


/** \brief Wait for the first full buffer and write it to a file.
 *
 * \param channel_no const int32_t Input channel number.
 * \param framesize const int32_t Size of the data frame.
 * \return DYB_Rc Checks for success or failure.
 *
 */
static DYB_Rc pollDataFull(const int32_t channel_no, const int32_t framesize)
{
    DYB_Rc rc = DYB_Ok;
    int32_t *frame = new int32_t[framesize];
    int32_t event = 0,
            index = 0,
            dataSize = framesize;
    DYB_Meta meta;

    /* Wait for full buffer and show progress */
    while(event == 0 /* means timeout */ && rc == DYB_Ok)
        event = DYB_waitForEvent(500, DYB_EVT_DATA_00, 0 /* not relevant */);

    /* Read and print data frame */
    assert(rc == DYB_Ok);

    fprintf(stdout,
            "Reading frame; buffer size = %d, frame size = %d\n",
            dataSize,
            DYB_getFrameSize(channel_no));

    rc = DYB_getDataBuffer(channel_no,
                           1,
                           NULL /* ignore */,
                           &index,
                           &dataSize,
                           frame,
                           &meta);
    checkRc("DYB_getDataBuffer", rc, __LINE__);

    rc = DYB_writeBuffer("data_output//demo_fwd", "ADC2", 0, 1, index, dataSize, frame, &meta);
    checkRc("DYB_writeBuffer", rc, __LINE__);
    rc = DYB_writeBuffer("data_output//demo_bwd", "ADC2", 0, 0, index, dataSize, frame, &meta);
    checkRc("DYB_writeBuffer", rc, __LINE__);

    delete[] frame;
    return rc;
}


/** \brief Polls data now without waiting for event.
 *
 * \param channel_no const int32_t Input channel number.
 * \param buffersize const int32_t Size of the data buffer.
 * \return DYB_Rc Checks for success or failure.
 *
 */
static DYB_Rc pollDataNow(const int32_t channel_no, const int32_t buffersize)
{
    int32_t framesize = DYB_getFrameSize(channel_no),
            index = 0;
    int32_t *buffer = new int32_t[buffersize],
            dataSize = buffersize;

    DYB_Rc rc = DYB_Ok;
    DYB_Meta meta;

    fprintf(stdout,
            "Reading data; buffer size = %d, frame size = %d\n",
            dataSize, framesize);


    rc = DYB_getDataBuffer(channel_no,
                           1, /* Get data only when buffer is full. */
                           0, /* Output: number of the frame, ignore. */
                           &index, /* Output: index of first element in buffer. */
                           &dataSize, /* In/Output: number of valid data in buffer. */
                           buffer, /* Allocated buffer. */
                           &meta);
    checkRc("DYB_getDataBuffer", rc, __LINE__);

    rc = DYB_writeBuffer("data_output//demo_fwd",
                         "Counter", /* Comment */
                         0, /* Ignore */
                         0, /* Fwd/Bwd direction, not relevant. */
                         index,
                         dataSize,
                         buffer,
                         &meta);
    checkRc("DYB_writeBuffer", rc, __LINE__);

    delete[] buffer;
    return rc;
}


/** \brief Cyclically read incomplete frame and write it to a file.
 *
 * \param channel_no const int32_t Input channel number.
 * \param framesize const int32_t Size of the data frame.
 * \return DYB_Rc Checks for success or failure.
 *
 */
static DYB_Rc pollDataPartial(const int32_t channel_no, const int32_t framesize)
{
    DYB_Rc rc = DYB_Ok;
    int loop = 0;

    while(rc == DYB_Ok && loop < 10)
    {
        int32_t *frame = new int32_t[framesize];
        DYB_Meta meta;
        int32_t index = 0,
                frameNo = 0,
                dataSize = framesize;
        char fn[128];

        Sleep(200);
        /* Read as much data as available */
        rc = DYB_getDataBuffer(channel_no,
                               0,
                               &frameNo,
                               &index,
                               &dataSize,
                               frame,
                               &meta);
        checkRc("DYB_getDataBuffer", rc, __LINE__);
        fprintf(stdout, "Data Read: loop %2d frame %d, index %d, size %d\n", loop, frameNo, index, dataSize);

        if(dataSize > 0)
        {
            /* Writing empty buffer ends up with error */
            sprintf(fn, "data_output//demo_fwd_%d", loop);
            rc = DYB_writeBuffer(fn, "ADC2", 0, 1, index, dataSize, frame, &meta);
            checkRc("DYB_writeBuffer", rc, __LINE__);
        }
        loop++;
        delete[] frame;
    }

    return rc;
}


int main(int argc, char **argv)
{

    std::string bin_path = "..\\Installer\\ASC500CL-V2.7.6",
                profile_path = bin_path + "\\afm.ngp";
    DYB_Rc ret = DYB_Ok;
    int32_t outActive = 0,
            variant = 10,
            buffer_size = 2048,
            channel_no = 0,
            columns = 100, /* Scanrange number of columns */
            lines = 150, /* Scanrange number of lines */
            pixelsize = 1000, /* Width of a column/line [10pm] */
            sampletime = 100, /* Scanner sample time in multiples of 2.5us */
            framesize = columns * lines * 2; /* Amount of data in a frame */


    if(argc > 1)
        variant = atoi(argv[1]); /* Selects data acquisition variant */

    /* Initialize & start */
    ret = DYB_init(nullptr, bin_path.c_str(), nullptr, ASC500_PORT_NUMBER);
    checkRc("DYB_Init", ret, __LINE__);
    ret = DYB_run();
    checkRc("DYB_Run", ret, __LINE__);

    /* Configure the scanner by sending a profile. */
    ret = DYB_sendProfile(profile_path.c_str());
    checkRc("DYB_sendProfile", ret, __LINE__);

    /* Configure data channel and source. */
    ret = DYB_configureChannel(channel_no,
                               CHANCONN_PERMANENT, /* Trigger by timer */
                               CHANADC_COUNTER, /* Source is counter */
                               0, /* Don't average */
                               sampletime); /* Time to samples are sent to PC */
    checkRc("DYB_configureChannel", ret, __LINE__);

    /* Configure buffer size, necessary when no natural size
     * (due to a scan) is defined.
     */
    ret = DYB_configureDataBuffering(channel_no, buffer_size);
    checkRc("DYB_configureDataBuffering", ret, __LINE__);

    /* Switch off annoying automatics that are useful only for GUI users */
    setParameter(ID_SCAN_X_EQ_Y,  0, 0);
    setParameter(ID_SCAN_GEOMODE, 0, 0);

    /* Adjust parameters */
    setParameter(ID_SCAN_PIXEL, 0, pixelsize);
    setParameter(ID_SCAN_COLUMNS, 0, columns);
    setParameter(ID_SCAN_LINES, 0, lines);
    setParameter(ID_SCAN_OFFSET_X, 0, 150 * pixelsize);
    setParameter(ID_SCAN_OFFSET_Y, 0, 150 * pixelsize);
    setParameter(ID_SCAN_MSPPX, 0, sampletime);
    setParameter(ID_CNT_EXP_TIME, 0, sampletime);

    /* Enable Outputs, wait for success (use polling for demonstration). */
    setParameter(ID_OUTPUT_ACTIVATE, 0, 1);

    while(!outActive && ret == DYB_Ok)
    {
        ret = DYB_getParameterSync(ID_OUTPUT_STATUS, 0, &outActive);
        checkRc("DYB_getParameterSync", ret, __LINE__);
        fprintf(stdout, "Output Status: %d\n", outActive);
        Sleep(50);
    }

    /* Acquire data using the selected method */
    switch(variant)
    {
    case 0:
        ret = pollDataFull(channel_no, framesize);
        break;
    case 1:
        ret = pollDataPartial(channel_no, framesize);
        break;
    default:
        ret = pollDataNow(channel_no, buffer_size);
    }

    /* Stop it and exit. This time use wait for event instead of polling */
    setParameter(ID_OUTPUT_ACTIVATE, 0, 0);
    DYB_waitForEvent(1000, DYB_EVT_CUSTOM, ID_OUTPUT_STATUS);
    DYB_getParameterSync(ID_OUTPUT_STATUS, 0, &outActive);
    if(outActive)
        fprintf(stdout, "Outputs are not deactivated!\n");

    DYB_stop();

    fprintf(stdout, ">>> Hit enter to proceed\n");
    getchar();

    return ret;
}
