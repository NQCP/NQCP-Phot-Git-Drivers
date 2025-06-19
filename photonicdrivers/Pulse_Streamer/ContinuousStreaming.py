"""
This file shows how to use the continuous streaming mode of the Pulse Streamer 8/2.
With the release 2.x of the Pulse Streamer 8/2 firmware, we will introduce the feature of continuous streaming. 
With the preliminary release 2.0.0 Beta2, we give the opportunity to test the new feature while the complete 
firmware release is finished. The API will not change for the official release, and the feature is fully backwards 
compatible with the former firmware versions.

To be able to continuously stream sequence data, the Pulse Streamer 8/2 is charged with two independent memory slots. 
While streaming data from one slot, the data for the opposite one can be uploaded without stopping the current streaming. 
Several parameters can define the concrete transition process between the data slots in detail. So you can continuously stream 
into the newly uploaded sequence data or define that the device should continue with previously uploaded data. Furthermore, you 
can define that the device should wait in an idle state or repeat the current memory slot while it waits for the new data to arrive. 

For a detailed description of the Pulse Streamer API, please have a look at:
https://www.swabianinstruments.com/static/documentation/pulse-streamer/v2.0/

Before you can run this example, you need to install the pulsestreamer client package related to the Pulse Streamer 8/2 2.0.0 Beta2 firmware.
It is currently provided only for downloading from our website. 
Please visit https://www.swabianinstruments.com/pulse-streamer-8-2/downloads/ and download the pulsestreamer-2.0.*.whl-package. Then type: 

  > pip install pulsestreamer-2.0.*.whl

"""

# import JSON-RPC Pulse Streamer wrapper class; to use Google-RPC import from pulsestreamer.grpc
from pulsestreamer import PulseStreamer

#import the device detection
from pulsestreamer import findPulseStreamers

# import enum types
from pulsestreamer import TriggerStart, NextAction, When, OnNoData

# import class Sequence and OutputState for advanced sequence building
from pulsestreamer import Sequence, OutputState

# python module for scientific computing only used for creating the random pulse and merging signals
import numpy as np

import sys
import time

ip_hostname='pulsestreamer' # edit this line to use a specific Pulse Streamer IP address
HIGH = 1
LOW = 0

"""---------------- functions to create random pulse patterns on digital and analog outputs --------------"""
def random_digital(max_duration, min_pulse=20, max_pulse=256):
    """creates a random digital pattern with duration=max_duration (ns)"""
    channel_seq = []
    cum_sum=np.int64(0)
    t = np.random.randint(min_pulse, max_pulse, int(1E6)) 
    for i, ti in enumerate(t):
        state = i%2
        if (cum_sum+ti>max_duration):
            channel_seq.append((max_duration-cum_sum, state))
            break
        else:
            channel_seq.append((ti, state))
            cum_sum+=ti
    return channel_seq

def random_analog(max_duration, min_pulse=1, max_pulse=256):
    """creates a random analog pattern with duration=max_duration (ns)"""
    channel_seq = []
    cum_sum=np.int64(0)
    t = np.random.randint(min_pulse, max_pulse, int(1E6)) 
    for i, ti in enumerate(t):
        a = np.random.uniform(-1.0, 1.0)
        if (cum_sum+ti*8>max_duration):
            channel_seq.append((max_duration-cum_sum, a))
            break
        else:
            channel_seq.append((ti*8, a))
            cum_sum+=ti*8
    return channel_seq

def random_constant(digi_channels=8, ana_channels=2):
    """creates a random tuple for a constant OutputState of the Pulse Streamer 8/2"""
    ch_list=[]
    for i in range(1, digi_channels):
        if np.random.randint(0,2,1)==1:
            ch_list.append(i)

    ana_1 = np.random.uniform(-1.0, 1.0)
    ana_2 = np.random.uniform(-1.0, 1.0)

    output=(ch_list, ana_1, ana_2)

    return output

"""------------------ functions to setup continuos streaming scenarios --------------------"""

def stream_continuously_and_stop(pulser):
    """Streaming continuously a continuous pattern on ch_0 and a signal with a shifting period on ch_1"""
    
    ref_period=100000 #10kHz
    shifting_period_0=10000 #100kHz
    t_delay=25000000
    gate_width=100
    ref_ch=0
    shift_ch=1
    duration=int(10E9)
    
    #generate patterns for constant frequency and shifting square waves
    reference_pattern=duration//ref_period*[(10,HIGH),(ref_period-10,LOW)] #10s reference pattern
    shifting_pattern=[(t_delay,0)]
    i=1
    cumsum_total=0
    while (True):
        shifting_period=np.append(np.linspace(shifting_period_0, i*shifting_period_0//10, num=int(i* 9*shifting_period_0//10), endpoint=False),np.linspace(i*shifting_period_0//10, i*2*shifting_period_0, num=int(19*shifting_period_0//10), endpoint=False))
        cumsum_total+=shifting_period.cumsum()[-1]
        if cumsum_total>=duration:
            break
        else:
            [shifting_pattern.extend([(gate_width,HIGH),(j-gate_width,LOW)]) for j in shifting_period]
            i+=1

    #set total sequence, which has many more sequence steps as the Pulse Streamer can accept at once
    seq_total=pulser.createSequence()
    seq_total.setDigital(ref_ch,reference_pattern)
    seq_total.setDigital(shift_ch, shifting_pattern)
    
    #split the total sequence
    seq_list=Sequence.split(seq_total,list(range(int(1E9), duration, int(1E9))))
    
    pulser.reset()
    i=0
    for seq in seq_list:
        if i==1:
            pulser.upload(slot_nr=pulser.AUTO, data=seq, n_runs=1, next_action=NextAction.SWITCH_SLOT_EXPECT_NEW_DATA, when=When.IMMEDIATE) #upload and switch to other memory slot afterwards
            input("Press <ENTER> to start streaming")
            pulser.start(slot_nr=pulser.AUTO, slots_to_run=-1) #start streaming process
            print("Start streaming data continuosly...")
        elif i==(len(seq_list)-1):
            while(not pulser.isReadyForData(pulser.AUTO)):
                time.sleep(0.001)
            pulser.upload(slot_nr=pulser.AUTO, data=seq, n_runs=1, next_action=NextAction.STOP) #upload and stop streaming afterwards
            print("Uploading last data slot and stop streaming")
        else:
            while(not pulser.isReadyForData(pulser.AUTO)):
                time.sleep(0.01)
            pulser.upload(slot_nr=pulser.AUTO, data=seq, n_runs=1, next_action=NextAction.SWITCH_SLOT_EXPECT_NEW_DATA, when=When.IMMEDIATE) #upload and switch to other memory slot afterwards
            print("Uploading new data...")
        i+=1

    while(pulser.isStreaming()):
        time.sleep(0.001)
    print('Pulse Streamer has finished all sequence slots: '+str(pulser.hasFinished()))


def stream_continuously_and_repeat(pulser):
    """Streaming three data slots with patterns for setup, measurement and sync-pulses and repeat the last data slot afterwards"""
    seq0=pulser.createSequence()
    seq1=pulser.createSequence()
    seq2=pulser.createSequence()

    period=80
    laser_pulse_width=15
    reference_delay=10
    reference_signal_width=20
    
    laser_ch=0
    reference_ch=1
    mw_ch=2
    final_slot_trigger_ch=3

    #mw_pattern
    mw_pattern=[]
    [mw_pattern.extend([((period-mw_pulse_width)//2,LOW),(mw_pulse_width, HIGH),((period-mw_pulse_width)//2,LOW)]) for mw_pulse_width in range(40, 80, 10)]
    

    #setting up initialisation sequence
    seq0.setDigital(laser_ch,[(laser_pulse_width,HIGH),(period-laser_pulse_width,LOW)]) #Laser pulses
    seq0.setDigital(reference_ch,[(reference_delay,LOW),(reference_signal_width,HIGH),(period-reference_signal_width-reference_delay,LOW)]) #Setup reference signal on channel 1

    #setting up measurement sequence
    seq1.setDigital(laser_ch,8*[(laser_pulse_width,HIGH),(period-laser_pulse_width,LOW)]) #Laser pulses
    seq1.setDigital(reference_ch,8*[(reference_delay,LOW),(reference_signal_width,HIGH),(period-reference_signal_width-reference_delay,LOW)]) #Setup reference signal on channel 1
    seq1.setDigital(mw_ch,mw_pattern)
    
    #setting up sequence with only reference signal
    seq2.setDigital(reference_ch,[(reference_delay,LOW),(reference_signal_width,HIGH),(period-reference_signal_width-reference_delay,LOW)]) #Setup reference signal on channel 1
    seq2.setDigital(final_slot_trigger_ch,[(8,HIGH)]) #signal to trigger on final memory slot
    
    pulser.reset()
    #configure software trigger
    pulser.setTrigger(TriggerStart.SOFTWARE)
    
    #upload data for both memory slots (setup and seq1)
    pulser.upload(slot_nr=pulser.AUTO, data=seq0, n_runs=1, next_action=NextAction.SWITCH_SLOT_EXPECT_NEW_DATA, when=When.IMMEDIATE) #upload initial sequence data
    pulser.upload(slot_nr=pulser.AUTO, data=seq1, n_runs=int(1E6),next_action=NextAction.SWITCH_SLOT_EXPECT_NEW_DATA, when=When.IMMEDIATE) #upload measurement sequence with n_runs=1E6
    
    #start internal data processing only as extra software trigger option is set (memory slots cannot be overwritten anymore)
    pulser.start(pulser.AUTO, 10) # run 10 slots, so the last slot with the reference signal is played once and repeated 7 times afterwards
    
    input("Press <ENTER> to start streaming")
    pulser.startNow()
    print("Pulse Streamer is streaming: " +str(pulser.isStreaming()))
    #check if next memory slot is writable
    while(not pulser.isReadyForData(pulser.AUTO)):
        time.sleep(0.001)
    #upload further data to memory
    print("Uploading new data...")
    pulser.upload(slot_nr=pulser.AUTO, data=seq2, n_runs=1,next_action=NextAction.REPEAT_SLOT, when=When.IMMEDIATE) #upload last memory slot and with next_action=REPEAT_SLOT

    while(pulser.isStreaming()):
        time.sleep(0.01)

    print('Pulse Streamer has finished all three sequence slots: '+str(pulser.hasFinished()))


def stream_continuously_and_wait_idling(pulser):
    """Stream 20 data slots with random patterns continuously and wait in an idle state till new data arrives"""
    seq0=pulser.createSequence()
    slots_to_run=20

    #creating pulse pattern for each digital channel
    seq0.setDigital(0, [(8, HIGH),(8, LOW)]) # trigger on channel 0
    for ch_digi in range(1,8):
        seq0.setDigital(ch_digi, random_digital(10000))
    #creating pulse pattern for each analog channel
    for ch_ana in range(2):
        seq0.setAnalog(ch_ana, random_analog(10000))

    pulser.reset()
    pulser.upload(slot_nr=pulser.AUTO, data=seq0, n_runs=1, idle_state=([0,2,4,6],0,0), next_action=NextAction.SWITCH_SLOT_EXPECT_NEW_DATA, when=When.IMMEDIATE, on_nodata=OnNoData.WAIT_IDLING) #upload and switch to the other memory slot to wait idling

    input("Press <ENTER> to start streaming")
    pulser.start(slot_nr=pulser.AUTO, slots_to_run=slots_to_run) # start and run a specific number of memory slots

    i=0
    while(i<slots_to_run):
        if(i==10):
            input("Press <ENTER> to generate and upload the data for the last 10 memory slots and quit afterwards")

        #creating pulse pattern for each digital channel
        seq0.setDigital(0, [(8, HIGH),(8, LOW)]) # trigger on channel 0
        for ch_digi in range(1,8):
            seq0.setDigital(ch_digi, random_digital(10000,2,255))
        #creating pulse pattern for each analog channel
        for ch_ana in range(2):
            seq0.setAnalog(ch_ana, random_analog(10000,2,255))

        output_state=random_constant() #create output state to wait idling

        print("Uploading new data...")
        pulser.upload(slot_nr=pulser.AUTO, data=seq0, n_runs=1,idle_state=output_state, next_action=NextAction.SWITCH_SLOT_EXPECT_NEW_DATA, when=When.IMMEDIATE, on_nodata=OnNoData.WAIT_IDLING) #upload and switch to the other memory slot to wait idling
        i+=1

    while(pulser.isStreaming()):
        time.sleep(0.01)

    print('Pulse Streamer has finished all five sequence slots: '+str(pulser.hasFinished()))

    
    
def stream_continuously_and_wait_repeating(pulser):
    """Stream random patterns continuously and repeat trigger and  1MHz frequency on digital channels as nested loop while waiting for new data"""
    seq_idling=pulser.createSequence()
    seq_random=pulser.createSequence()
    #creating pulse pattern for each digital channel
    seq_idling.setDigital(0, [(8, HIGH),(8, LOW)]) # trigger on channel 0
    for ch_digi in range(1,8):
        seq_idling.setDigital(ch_digi, 8* [(500,HIGH),(500,LOW)])

    #create idle statepulser.createOutputState(OutputState.ZERO())
    constant_zero=OutputState.ZERO()

    pulser.reset()
    pulser.upload(slot_nr=pulser.AUTO, data=seq_idling, n_runs=1, idle_state=constant_zero, next_action=NextAction.SWITCH_SLOT_EXPECT_NEW_DATA, when=When.IMMEDIATE, on_nodata=OnNoData.WAIT_REPEATING) #stream and switch to other memory slot afterwards
    input("Press <ENTER> to start streaming")
    pulser.start(slot_nr=pulser.AUTO, slots_to_run=-1)
    print("Pulse Streamer is streaming: " +str(pulser.isStreaming()))

    while(True):
        choice = None
        choice = input("Press <ENTER> to generate and upload next sequence, press q + <ENTER> if you want to quit afterwards (setting the next_action=NextAction.STOP)")

        #creating pulse pattern for each digital channel
        seq_random.setDigital(0, [(8, HIGH),(8, LOW)]) # trigger on channel 0
        for ch_digi in range(1,8):
            seq_random.setDigital(ch_digi, random_digital(1E6,2,256))
        #creating pulse pattern for each analog channel
        for ch_ana in range(2):
            seq_random.setAnalog(ch_ana, random_analog(1E6,2,256))

        if choice=='q':
            print("Uploading new data...")
            pulser.upload(slot_nr=pulser.AUTO, data=seq_random, n_runs=1,idle_state=constant_zero, next_action=NextAction.STOP)
            while(pulser.isStreaming()):
                time.sleep(0.01)
            print('Pulse Streamer has finished: '+str(pulser.hasFinished()))
            break
        else:
            print("Uploading new data...")
            pulser.upload(slot_nr=pulser.AUTO, data=seq_random, n_runs=1000, idle_state=constant_zero,next_action=NextAction.SWITCH_SLOT, when=When.IMMEDIATE, on_nodata=OnNoData.ERROR)


if __name__=='__main__':
    #create Pulsestreamer
    """To set the IP-Address of the Pulse Streamer, see
    https://www.swabianinstruments.com/static/documentation/PulseStreamer/sections/network.html
    """
    try:
        pulser = PulseStreamer(ip_hostname)
    except AssertionError:
        print("No Pulse Streamer found with ip_hostname: " + ip_hostname)
        print("")
        print("Pulse Streamer 8/2 found in the network:")
        print(findPulseStreamers())
        print("Use one of the devices shown above, or visit https://www.swabianinstruments.com for more information")
        input("Press <ENTER> to end program")
        sys.exit()

    print ("******************************************")
    print ("****** Streaming data continuously ******")
    print ("******************************************")
    print ("")
    print ("Stream data continuously and stop afterwards")
    print ("")
    stream_continuously_and_stop(pulser)

    input("\nFor next example press <ENTER>")

    print ("**********************************************************************")
    print ("****** Streaming three data slots with data block as nested loop******")
    print ("**********************************************************************")
    print ("")
    print ("Stream three data slots and repeat last memory slot")
    print ("")
    stream_continuously_and_repeat(pulser)

    input("\nFor next example press <ENTER>")

    print ("********************************************************")
    print ("****** Streaming data continuously and wait idling ******")
    print ("********************************************************")
    print ("")
    print ("Stream random data continuously and wait idling for new data after each slot")
    print ("")
    stream_continuously_and_wait_idling(pulser)

    input("\nFor next example press <ENTER>")

    print ("***********************************************************")
    print ("****** Streaming data continuously and wait repeating ******")
    print ("***********************************************************")
    print ("")
    print ("Stream random data continuously and repeat one slot as nested loop while waiting for new data")
    print ("User creates and uploads new data with <ENTER>")
    print ("")
    stream_continuously_and_wait_repeating(pulser)


