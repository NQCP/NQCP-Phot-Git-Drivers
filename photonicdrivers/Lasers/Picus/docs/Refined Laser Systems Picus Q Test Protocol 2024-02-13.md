Picus Q – NB 2024
Test Protocol
P/N: PICUS Q
S/N: 0X-LH-222-017 + 0X-PS-220-022
DATE: 13.2.2024
1

Picus Q – NB 2024
Contents
1. Introduction .................................................................................................................................... 3
2. Output Power ................................................................................................................................. 4
3. Pulse Durations ............................................................................................................................... 6
4. Output Spectra ............................................................................................................................... 7
5. Repetition frequency ...................................................................................................................... 9
6. Warm-up Time .............................................................................................................................. 10
2

Picus Q – NB 2024
1. Introduction
The measured values shown in this document were generated with the laser system intended for the
NBI during final inspection.
3

Picus Q – NB 2024
2. Output Power
The average power of the Signal and Idler fiber outputs depending on the wavelength settings is
shown in Figure 1. The output power varies across the tuning range. For this custom version of the
Picus Q, the Signal and the Idler is transported by a PM980 patch cord with FC/APC termination.
Figure 1: Average output power from the Signal and Idler fiber output depending on the central
wavelength setting.
The output power of the Idler fiber is shown in Figure 2, depending on its central wavelength.
Figure 2: Average output power from the Idler fiber output depending on the central wavelength of the
Idler.
4

Picus Q – NB 2024
|     |     |     |     |     |
| --- | --- | --- | --- | --- |

The tuning range of the filtered Signal output is narrower, than the output of the Signal. Engaging the
Wavelength Lock ensures a match between the filter setting and the actual output of the Signal, as
its central wavelength is depending on the ambient conditions. Figure 3 shows the output power of
the filtered Signal fiber, depending on the wavelength setting, with the Wavelength Lock engaged.

Figure 3: Average output power from the filtered Signal fiber output depending on the central
wavelength setting.
The accessible tuning range is summarized in Table 1. Setting values below or above the stated limits
results in a “bounds error”.
Table 1: Summary of the tuning limits.
|                         | Wavelength Signal  | Wavelength Idler  | Wavfilter  |       |
| ----------------------- | ------------------ | ----------------- | ---------- | ----- |
|                         | (nm)               | (nm)              | (bits)     |       |
| Upper wavelength limit  |                    | 991               | 1129       | 1300  |
| Upper Filter limit      |                    | 981               | 1141       | 1440  |
| Lower Filter limit      |                    | 911               | 1236       | 2455  |
| Lower wavelength limit  |                    | 762               | 1561       | 6200  |

5

Picus Q – NB 2024
3. Pulse Durations
The pulse duration has been measured with a home-built interferometric autocorrelator, calibrated
intrinsically by the distance of the interference fringes. The measured intensity autocorrelation shown
in Figure 4 was calculated from interferometric traces and is representative for the performance over
the tuning range (plotted in Figure 5).
Figure 4: Representative intensity autocorrelation trace of the fiber output.
Figure 5: Estimated pulse durations, retrieved from autocorrelation traces assuming a Gaussian pulse
shape, at wavelength settings across the tuning range.
6

Picus Q – NB 2024
4. Output Spectra
The output spectra in Figure 6 and Figure 7 were taken after the output fiber. The spectra are
exemplary representatives for the complete tuning range. Note the cascaded signals for longer
output wavelengths than 900 nm. These cascades are orders of magnitude weaker than the main
peak.
Figure 6: Signal output spectra at various wavelength settings.
Figure 7: Idler output spectra at various wavelength settings.
7

Picus Q – NB 2024
Figure 8 shows representative spectra of the filtered Signal output fiber.
Figure 8: Filtered Signal output spectra at various wavelength settings.
The spectral bandwidth of the output pulses is shown in Figure 9 as a function of the center
wavelength. The spectral bandwidth of the Signal increases for longer center wavelengths, while the
bandwidth of the Idler decreases.
Figure 9: Spectral bandwidth as a function of the center wavelength.
8

Picus Q – NB 2024
5. Repetition frequency
While tuning the center wavelength of the output pulses, the repetition frequency of the pulse train
changes accordingly. The dependency of the repetition frequency on the wavelength is depicted in
Figure 10.
Figure 10: Repetition frequency depending on the wavelength setting.
9

Picus Q – NB 2024
6. Warm-up Time
The system becomes operable and emits light within seconds after starting the system. A change of
5-10% of the output specifications over 2h is possible until stabilized. It is recommended to use the
Picus Wavelength Lock with the internal calibration during warm-up to account for wavelength drifts.
10