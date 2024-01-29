import logging
import photonicdrivers._version


__version__ = photonicdrivers._version.__version__


logger = logging.getLogger(__name__)
logger.info(f"Imported photonicdriversversion: {__version__}")
