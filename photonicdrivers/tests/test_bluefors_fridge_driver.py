from __future__ import annotations

from typing import Any, cast
from unittest.mock import patch

from photonicdrivers.BlueForsFridge.BlueForsFridge_Driver import BlueForsFridge_Driver


class _DummyResponse:
    def __init__(self, payload: dict[str, Any], status_code: int = 200):
        self._payload = payload
        self.status_code = status_code

    def json(self) -> dict[str, Any]:
        return self._payload


class _DummySession:
    def __init__(self):
        self.post_calls: list[tuple[str, dict[str, Any] | None]] = []

    def post(self, url: str, json: dict[str, Any] | None = None) -> _DummyResponse:
        self.post_calls.append((url, json))
        return _DummyResponse({"ok": True, "url": url, "json": json})


def _make_driver(session: _DummySession) -> BlueForsFridge_Driver:
    driver = BlueForsFridge_Driver()
    driver.session = cast(Any, session)
    return driver


def _assert_raises(call: Any, exception_type: type[BaseException], message_contains: str) -> None:
    try:
        call()
        raise AssertionError(f"Expected {exception_type.__name__} to be raised")
    except exception_type as exc:
        assert message_contains in str(exc)


def test_set_valve_forbidden_blocked_even_if_normalized_variant() -> None:
    session = _DummySession()
    driver = _make_driver(session)

    _assert_raises(lambda: driver.set_valve("  V15  ", True), ValueError, "forbidden")

    assert session.post_calls == []


def test_set_valve_non_common_prompts_and_can_abort() -> None:
    session = _DummySession()
    driver = _make_driver(session)

    with patch("builtins.input", return_value="n"):
        _assert_raises(lambda: driver.set_valve("v12", True), ValueError, "Aborting control")

    assert session.post_calls == []


def test_set_pump_posts_expected_values_payload() -> None:
    session = _DummySession()
    driver = _make_driver(session)

    response = driver.set_pump("scroll1", True)

    assert response["ok"] is True
    assert len(session.post_calls) == 1
    post_url, post_json = session.post_calls[0]
    assert post_url == "http://localhost:49099/values/?prettyprint=1&fields=name;value;status"
    assert post_json == {
        "data": {
            "mapper.bf.pumps.scroll1": {"content": {"value": 1}},
        }
    }


def test_configure_fse_pid_uses_hardcoded_fse_heater_and_never_recouples() -> None:
    session = _DummySession()
    driver = _make_driver(session)

    response = driver.configure_fse_temperature_pid_loop(
        setpoint=0.9,
        proportional=0.01,
        integral=50.0,
        derivative=0.0,
        max_power=0.1,
        resistance=120.0,
        active=True,
    )

    assert response["ok"] is True
    assert len(session.post_calls) == 1
    post_url, post_json = session.post_calls[0]
    assert post_url == "http://localhost:49099/heater/update"
    assert post_json is not None
    assert post_json["heater_nr"] == 4
    assert post_json["pid_mode"] == 1
    assert post_json["control_algorithm"] == 1
    assert all("channel/heater/update" not in call_url for call_url, _ in session.post_calls)


def test_disable_fse_pid_uses_hardcoded_fse_heater() -> None:
    session = _DummySession()
    driver = _make_driver(session)

    response = driver.disable_fse_temperature_pid_loop(keep_heater_active=False)

    assert response["ok"] is True
    assert len(session.post_calls) == 1
    post_url, post_json = session.post_calls[0]
    assert post_url == "http://localhost:49099/heater/update"
    assert post_json == {
        "heater_nr": 4,
        "pid_mode": 0,
        "active": False,
    }
