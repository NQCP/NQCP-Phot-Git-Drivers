from photonicdrivers.Mocks.Elliptec_Driver_Mock import Elliptec_Driver_Mock


def test_elliptec_driver_mock_tracks_position_per_address():
    driver = Elliptec_Driver_Mock(addresses=["A", "B"], initial_positions={"A": 10.0, "B": 20.0})

    driver.connect()

    assert driver.is_connected() is True
    assert driver.get_address() == ["A", "B"]
    assert driver.get_position("A") == 10.0
    assert driver.get_position("B") == 20.0

    driver.move_to(45.0, "A")
    driver.move_by(-5.0, "B")

    assert driver.get_position("A") == 45.0
    assert driver.get_position("B") == 15.0


def test_elliptec_driver_mock_homes_and_disconnects():
    driver = Elliptec_Driver_Mock(addresses=["A"], initial_positions={"A": 33.0}, home_position=2.5)

    driver.connect()
    driver.home("A")
    driver.disconnect()

    assert driver.get_position("A") == 2.5
    assert driver.is_connected() is False
