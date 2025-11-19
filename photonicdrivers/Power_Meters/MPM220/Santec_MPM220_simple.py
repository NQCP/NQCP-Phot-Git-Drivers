from photonicdrivers.Power_Meters.MPM220.Santec_MPM220_driver import santec_MPM220_driver

mpm220 = santec_MPM220_driver(address="ASRL5::INSTR")
mpm220.connect()
print(mpm220.get_id())
print(f"module info: {mpm220.get_module_information(0)}")
print(f"module info: {mpm220.get_module_information(1)}")

# set measurement mode
mpm220.set_measurement_mode(mode="SWEEP1")

# get measurement mode
mode = mpm220.get_measurement_mode()
print(f"Current measurement mode: {mode}")

mpm220.disconnect()