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
            frameno = 0,
            event = 0,
            index = 0;
    int32_t *buffer = new int32_t[buffersize],
            dataSize = buffersize;

    memset(buffer, 0xDEAD, sizeof(int32_t));

    DYB_Rc rc = DYB_Ok;
    DYB_Meta meta;

    fprintf(stdout,
            "Reading data; buffer size = %d, frame size = %d\n",
            dataSize, framesize);

    /* Wait for full buffer and show progress */
    while(event == 0 /* means timeout */)
        event = DYB_waitForEvent(500, /* Timeout in ms */
                                 DYB_EVT_DATA_00, /* Buffer full */
                                 0 /* custom ID: ignore */);

    rc = DYB_getDataBuffer(channel_no,
                           0, /* Get data only when buffer is full. */
                           &frameno, /* Output: number of the frame, ignore. */
                           &index, /* Output: index of first element in buffer. */
                           &dataSize, /* In/Output: number of valid data in buffer. */
                           buffer, /* Allocated buffer. */
                           &meta);
    checkRc("DYB_getDataBuffer", rc, __LINE__);

    fprintf(stdout,
            "Output buffer size = %d\n",
            dataSize);

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


int main(int argc, char **argv)
{
    std::string bin_path = "..\\Installer\\ASC500CL-V2.7.6";
    DYB_Rc ret = DYB_Ok;
    int32_t buffer_size = 256,
            channel_no = 0,
            exp_time = 1; /* Scanner sample time in multiples of 2.5 us */
    double sampletime = 1e-3;

    /* Initialize & start */
    ret = DYB_init(nullptr, bin_path.c_str(), nullptr, ASC500_PORT_NUMBER);
    checkRc("DYB_Init", ret, __LINE__);
    ret = DYB_run();
    checkRc("DYB_Run", ret, __LINE__);

    setParameter(ID_DATA_EN, 0, 1);

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

    /* Adjust parameters */
    setParameter(ID_CNT_EXP_TIME, 0, exp_time);

    ret = pollDataNow(channel_no, buffer_size);

    /* Stop it and exit. This time use wait for event instead of polling */
    int32_t outActive = 0;
    setParameter(ID_OUTPUT_ACTIVATE, 0, 0);
    DYB_waitForEvent(500, DYB_EVT_CUSTOM, ID_OUTPUT_STATUS);
    DYB_getParameterSync(ID_OUTPUT_STATUS, 0, &outActive);
    if(outActive)
        fprintf(stdout, "Outputs are not deactivated!\n");

    DYB_stop();

    fprintf(stdout, ">>> Hit enter to proceed\n");
    getchar();

    return ret;
}
