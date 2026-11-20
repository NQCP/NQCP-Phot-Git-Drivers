# Keithley 2450 driver

`Keithley2450_Driver.py`: SCPI over a LAN socket (port 5025). On Atto01 it runs inside the LabServer on
kk4labserver01 (`finder.get_driver("keithley")`): **a change here reaches the notebooks only after a push, a pull on
kk4labserver01 and a restart of its server.**

## Hardware-timed operation (added 2026-11-09, not yet tested on the instrument)

Why (the user, 2026-11-09: can the voltage switch e.g. -40 / +40 V at 100 Hz?): one SCPI command per level costs a
LAN round trip plus the LabServer call, with ms of jitter. The 2450 can step a list and read on its own clock.

| method | SCPI | note |
|---|---|---|
| `set_source_list(values)` | `:SOUR:LIST:VOLT v1, ...` then `:SOUR:LIST:VOLT:APP ...` | <= 100 values per command, <= 2500 per list; replaces the list `VoltCustomSweepList` |
| `get_source_list_points()` | `:SOUR:LIST:VOLT:POIN?` | |
| `configure_list_sweep(start, delay_s, count, fail_abort, buffer)` | `:SOUR:SWE:VOLT:LIST ...` | one reading per point; delay 0 or 50 us - 10000 s (added to the source delay); count 0 = until aborted; failAbort OFF to go on at the current limit |
| `load_duration_loop` / `load_simple_loop` (`syntax="named"` or `"legacy"`) | `:TRIG:LOAD "DurationLoop", ...` / `:TRIG:LOAD:LOOP:DUR ...` | readings at a fixed level; which syntax this unit's firmware takes is unknown (the manual rev B has the legacy one) |
| `initiate()`, `abort()`, `get_trigger_state()` | `:INIT`, `:ABOR`, `:TRIG:STAT?` (first field) | |
| `set_buffer_size`, `clear_buffer`, `get_buffer_count`, `get_buffer_data(start, end, elements)` | `:TRAC:POIN`, `:TRAC:CLE`, `:TRAC:ACT?`, `:TRAC:DATA? s, e, "buf", READ, SOUR, REL` | data read in pieces of 500 readings |
| `set_sense_function`, `set_measurement_nplc` (0.01-10), `set_measurement_autozero`, `set_measurement_autorange`, `set_source_readback`, `set_source_delay(_auto)`, `set_source_function` | `:SENS:FUNC "CURR"`, `:SENS:CURR:NPLC`, `:SENS:CURR:AZER`, `:SENS:CURR:RANG:AUTO`, `:SOUR:VOLT:READ:BACK`, `:SOUR:VOLT:DEL` | readback ON: the buffer's source value is the measured output |
| `get_next_error()` | `:SYST:ERR:NEXT?` | |

Sources: Model 2450 Reference Manual, section 6 (ManualsLib copy, rev B 2013: `:SOURce:LIST:<function>:APPend`
p. 6-80, `:SOURce:SWEep:<function>:LIST` p. 6-86, `:TRIGger:LOAD:LOOP:DURation` p. 6-163); buffer element names
as in QCoDeS' `Keithley_2450` driver. Tests: `photonicdrivers/tests/test_keithley2450_driver_hardware_timed.py`
(fake socket: the exact strings and the reply parsing).

### To check on the instrument (first use, low voltage, with the user's go)

1. `*IDN?` firmware; `:TRIG:LOAD "DurationLoop", 1, 0.01` accepted? (error queue) - else the legacy syntax.
2. A short list (0 / 1 / 0 V, 100 points, 10 ms delay) at the 10 nA limit: the readings, time stamps and source
   readback come back; the output is still ON after the sweep and rests at the last list value.
3. The time per point against NPLC (0.01 / 0.1 / 1) and delay: the 2450's own overhead per point.
4. The `:TRIG:STAT?` reply format.

## Physics limit to keep in mind

Charging the electrodes takes I = C dV/dt: a 80 V swing in time t needs C x 80 V / t (at 160 pF: 13 uA for 1 ms);
the controllers refuse current limits above 1 uA. The sample's relaxation (62 run 2: 0.84 s and 11.4 s) also limits
how fast the field at the emitter follows. Protocol 65 measures both.

Last updated 2026-11-09.
