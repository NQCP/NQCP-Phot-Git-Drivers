import pyvisa, math, sys
import numpy as np
import time


class Powermeter(object):
    """
    Class for interfacing with Thorlab powermeters.
    Supported models: N7747A; PM100D; PM100USB; THORLABS PM101A TMC  (e.g. model='PM100USB')
    Supported units: {'W', 'mW', 'dBm'}
    """
    def __init__(self, model, serial=None, unit=None, wavelength=None, averages=None):

        # Defaults
        self.read_timeout = 0.
        self.unit = 'mW'  # {'W', 'mW', 'dBm'}
        self.model = None  # This is populated with the powermeter model, for handling different interfaces. Case sensitive

        # Find instrument corresponding to model and serial numbers
        rm = pyvisa.ResourceManager()
        serial_names = rm.list_resources()

        pm_serial = None
        instrs = []
        for serial_name in serial_names:
            instr = rm.open_resource(serial_name)

            instr.timeout = 2

            try:
                
                mn = instr.model_name
                sn = instr.serial_number
                instrs.append({'port': serial_name, 'model': mn, 'num': sn})

                if mn == model and (sn == serial or serial is None):
                    pm_serial = serial_name
                    break

            except: 
                print('One non-usb serial was discarded, might have been a powermeter')

            instr.close()



        # If we didn't find any matchin instrument, raise an error
        if pm_serial is None:
            raise ValueError('Unable to find device '+str(model)+ str(serial) + '. Found devices' + str(instrs))

        self.instr = rm.open_resource(pm_serial)
        self.model = self.instr.model_name

        # Set up default and initialisation values
        if wavelength is not None:
            self.set_wavelength(wavelength)
        if averages is not None:
            self.set_averages(averages)
        if unit is not None:
            self.unit = unit

    def close(self):
        print("closing device")
        self.instr.close()

    def __del__(self):
        self.close()

    def measure(self, channel=1):

        if self.model == 'PM100D' or 'PM100USB' or 'THORLABS PM101A TMC':

            result_W = -float('inf')
            n_tries = 5
            for iter in range(n_tries):
                try:
                    result_W = float(self.instr.query('read?', delay=self.read_timeout))
                except pyvisa.errors.VisaIOError:
                    print("Caught error during powermeter read '{:}'. Tries remaining: {:}.".format(sys.exc_info()[0],
                                                                                                    n_tries - iter + 1))
                    continue
                break
            if iter == n_tries - 1:
                try:
                    print('Trying to reinitialise powermeter.')
                    self.close()
                    self.__init__(self.model)
                    result_W = float(self.instr.query('read?', delay=self.read_timeout))
                except:
                    raise RuntimeError(
                        'Error:Powermeter:measure: Tried {:} times to read powermeter, failed. Tried to reinitialise powermeter, failed.'.format(
                            n_tries))

        elif self.model == 'N7747A':
            if channel not in [1, 2]:
                raise AttributeError(
                    'Channel number for model {0} must be in [1,2]. Specified channel {1} is invalid.'.format(
                        self.model, channel))
            result_W = float(self.instr.query('read{ch}:pow?'.format(ch=channel), delay=self.read_timeout))
        else:
            raise AttributeError('Unknown model "{0}".'.format(self.model))

        if self.unit == 'W':
            return result_W
        elif self.unit == 'mW':
            return result_W * 1000
        elif self.unit == 'dBm':
            return 10 * math.log(result_W * 1000, 10) if (result_W > 0) else (-float('Inf'))
        else:
            raise AttributeError('Measurement unit, {0}, unrecognised.'.format(self.unit))

    def query(self, command):
        return float(self.instr.query(command))

    def set_wavelength(self, wl_nm):
        self.instr.write('CORR:WAV {0}\n'.format(wl_nm))

    def set_averages(self, n_averages):
        self.instr.write('sens:aver {0}\n'.format(n_averages))

    def measure_average(self, n_averages=10):
        memo = np.zeros(n_averages)
        for j in range(n_averages):
            memo[j] = self.measure()
        return np.mean(memo)
