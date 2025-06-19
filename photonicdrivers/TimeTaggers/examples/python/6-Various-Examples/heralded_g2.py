# This example shows an implementation for a heralded g2 measurement, also called conditional g2 measurement
# because conditional on measuring a heralded photon, one can have a single photon source. In this example,
# we follow closely the review article [1] "On-chip heralded single photon sources" by Signorini and Pavesi,
# doi: 10.1116/5.0018594

# There is no point to run this example with test signals, so the focus is only on the implementation
# of a heralded g2 measurement with the Time Tagger 

import TimeTagger
import matplotlib.pyplot as plt

# Here we consider a pulsed experiment. To measure a meaningful second order coherence function (g2)
# in a pulsed experiment, it is necessary to adjust the binwidth so that each bin has on average the same number
# of photons. This means the binwidth must correspond to the inverse of the frequency of the laser pulse frequency.
# # compare Fig.3 in [1]

# So let us define the parameters
signal_1_ch = 1
signal_2_ch = 2
idler_ch = 3
pulse_freq = 10e6  # Hz
laser_sync_ch = 4
binwidth = int(1 / pulse_freq * 1e12)
bins = 10
meas_time = 1e12  # ps

# Setting up the tagger
tagger = TimeTagger.createTimeTagger()
# We use the software clock to ensure no timing drifts between "laser clock" and Time Tagger's clock, 
# such that the binwidth always corresponds to the pulse frequency.
tagger.setSoftwareClock(laser_sync_ch, pulse_freq)

# For a heralded g2 measurement, we need three Time Tagger measurement objects (two different measurement classes).
# So we have to use synchronizedMeasurements to ensure to operate on the same data in all the three measurements.
sm = TimeTagger.SynchronizedMeasurements(tagger)
sm_tagger = sm.getTagger()

# Make sure idler and signals are well aligned, see text between Eq(48) and Eq(49) in Ref.[1]
# -> tagger.setInputDelay(...)

# We calculate g2 according to Eq(51) with the rates. The numerator of Eq(51) shows a triple coincidence.
# We account for it with a virtual channel giving coincidence clicks of signal_1 and idler leading to t_i=t_1=t
# Then, this coincidence channel is fed into a correlation measurement with the signal_2 giving us the three-fold
# coincidence. (The coincidenceWindow has to be chosen according to your experimental conditions).
# We also need the correlation of signal_2 and idler as well as the rates for the idler and signal_1/idler coincidence
# Here, we assume R_i and R_si are constant.

# Setting up the Time Tagger measurements
s1i = TimeTagger.Coincidence(sm_tagger, [idler_ch, signal_1_ch], coincidenceWindow=100,
                             timestamp=TimeTagger.CoincidenceTimestamp_ListedFirst)
corr_ssi = TimeTagger.Correlation(sm_tagger, s1i.getChannel(), signal_2_ch, binwidth, n_bins=bins)
corr_s2i = TimeTagger.Correlation(sm_tagger, idler_ch, signal_2_ch, binwidth, n_bins=bins)
cnr = TimeTagger.Countrate(sm_tagger, [s1i.getChannel(), idler_ch])

sm.startFor(meas_time)
sm.waitUntilFinished()

Nssi_data = corr_ssi.getData()
Nssi_lag_times = corr_ssi.getIndex()
Ns2i_data = corr_s2i.getData()
Rs1i, Ri = cnr.getData()

# Now, we can use our measurements data to calculate the heralded g2.
# As both correlation measurements have the same binwidth, we can work with the number of clicks directly.
# (The binwidths cancel out)
heralded_g2 = Nssi_data * Ri / (Ns2i_data * Rs1i)

# Plotting
plt.plot(Nssi_lag_times, heralded_g2)
plt.ylabel('heralded g2')
plt.xlabel('lag time (ps)')
