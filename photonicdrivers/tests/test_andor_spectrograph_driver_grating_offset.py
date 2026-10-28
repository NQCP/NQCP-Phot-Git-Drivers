import pytest

from photonicdrivers.Spectrometers.Andor_Spectrograph_Driver import (
    AndorException,
    Andor_Spectrograph_Driver,
    errors,
)


class FakeATSpectrograph:
    """Answers like pyAndorSpectrograph.ATSpectrograph for the grating-offset calls."""

    def __init__(self, num_gratings=3):
        self.offsets = {grating: 0 for grating in range(1, num_gratings + 1)}

    def GetGratingOffset(self, device, Grating):
        if Grating not in self.offsets:
            return (errors.ATSPECTROGRAPH_P2INVALID, 0)
        return (errors.ATSPECTROGRAPH_SUCCESS, self.offsets[Grating])

    def SetGratingOffset(self, device, Grating, offset):
        if Grating not in self.offsets:
            return errors.ATSPECTROGRAPH_P2INVALID
        self.offsets[Grating] = offset
        return errors.ATSPECTROGRAPH_SUCCESS

    def GetFunctionReturnDescription(self, error, MaxDescStrLen):
        return (errors.ATSPECTROGRAPH_SUCCESS, errors(error).name)


@pytest.fixture
def driver():
    driver = Andor_Spectrograph_Driver()
    driver.spectrograph = FakeATSpectrograph()
    return driver


def test_set_and_get_grating_offset_per_grating(driver):
    driver.set_grating_offset(grating=2, offset=-150)

    assert driver.get_grating_offset(grating=2) == -150
    assert driver.get_grating_offset(grating=1) == 0


def test_invalid_grating_raises(driver):
    with pytest.raises(AndorException) as excinfo:
        driver.set_grating_offset(grating=7, offset=10)
    assert excinfo.value.error_number == errors.ATSPECTROGRAPH_P2INVALID

    with pytest.raises(AndorException):
        driver.get_grating_offset(grating=7)
