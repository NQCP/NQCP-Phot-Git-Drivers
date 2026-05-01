import logging
import photonicdrivers._version
import os
import sys

__version__ = photonicdrivers._version.__version__


logger = logging.getLogger(__name__)
logger.info(f"Imported photonicdriversversion: {__version__}")

# Timetagger library needs this path
tt_path = r"C:\Program Files\Swabian Instruments\Time Tagger\driver\python"

if tt_path not in sys.path:
    sys.path.insert(0, tt_path)

try:
    os.add_dll_directory(tt_path)
except Exception:
    pass
