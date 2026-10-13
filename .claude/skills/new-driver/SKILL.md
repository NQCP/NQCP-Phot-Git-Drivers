---
name: new-driver
description: Write or extend a device driver in the Drivers repo (photonicdrivers/) - one device, its protocol (SCPI, socket, DLL, serial), no physics, Connectable, a mock and a mock-based test, backward-compatible changes. Use when the user wants a driver for a new device or new functions on an existing driver.
---

# New driver

The layers: **driver (one device)** -> instrument (an abstract interface) -> controllers ->
notebook (`NQCP-Phot-Git-Controllers/controllers/documentation/general_controller_guide.md`).

1. **Read the device's manual / programming guide** and an existing driver of the same kind
   (`photonicdrivers/<Kind>/`); copy its style. Do not assume command syntax - quote the manual.
2. **The driver**: `photonicdrivers/<Kind>/<Vendor_Model>_Driver.py`, implementing `Connectable`
   (`connect()`, `disconnect()`, `is_connected()`; `photonicdrivers/Abstract/Connectable.py`).
   One method per device function, named after what it does, with units in the names; raw values
   in and out - **no physics, no measurement logic, no retries that hide errors** (raise, with the
   device's error text).
3. **Changes to an existing driver**: keep every method name and signature; new behaviour behind
   new parameters whose defaults keep the old (e.g. `OPX_Driver(..., timeout=None)`). Drivers are
   used by every notebook of every station.
4. **A mock** (`photonicdrivers/Mocks/`) that answers like the device, and a test
   `photonicdrivers/tests/test_<name>_driver_mock.py` against it. Run
   `python -m pytest photonicdrivers/tests/test_<name>_driver_mock.py -q`.
5. **Never talk to a real device** from a test or a check, and never send commands to lab hardware,
   without the user's explicit OK. Hand the first real connection to the user (a short notebook or
   cell they run).
6. Register the driver where the lab finds it (LabServer's `DriverFinder` configuration) only with
   the user. Commit locally.
