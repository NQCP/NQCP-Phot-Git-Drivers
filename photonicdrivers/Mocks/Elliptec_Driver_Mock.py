from __future__ import annotations

from collections.abc import Iterable

from photonicdrivers.Abstract.Connectable import Connectable


class Elliptec_Driver_Mock(Connectable):
    def __init__(
        self,
        addresses: Iterable[str | int],
        initial_positions: dict[str | int, float] | None = None,
        home_position: float = 0.0,
    ):
        self.addresses = [str(address) for address in addresses]
        self._positions = {
            str(address): float(initial_positions.get(address, initial_positions.get(str(address), home_position)))
            for address in self.addresses
        } if initial_positions is not None else {
            str(address): float(home_position) for address in self.addresses
        }
        self.home_position = float(home_position)
        self.connected = False
        self.command_history: list[tuple[str, str, float | None]] = []

    def _normalize_address(self, address: str | int | None) -> str:
        if address is None:
            if len(self.addresses) != 1:
                raise ValueError("address must be provided when the mock controls multiple mounts")
            return self.addresses[0]

        normalized = str(address)
        if normalized not in self._positions:
            raise ValueError(f"Unknown Elliptec mock address {address!r}")
        return normalized

    def connect(self) -> None:
        self.connected = True

    def disconnect(self) -> None:
        self.connected = False

    def is_connected(self) -> bool:
        return self.connected

    def get_address(self) -> list[str]:
        return list(self.addresses)

    def get_position(self, address) -> float:
        normalized = self._normalize_address(address)
        return float(self._positions[normalized])

    def move_to(self, position: int | float, address) -> None:
        normalized = self._normalize_address(address)
        self._positions[normalized] = float(position)
        self.command_history.append(("move_to", normalized, float(position)))

    def move_by(self, angle: float, address) -> None:
        normalized = self._normalize_address(address)
        self._positions[normalized] += float(angle)
        self.command_history.append(("move_by", normalized, float(angle)))

    def home(self, address=None) -> None:
        normalized = self._normalize_address(address)
        self._positions[normalized] = self.home_position
        self.command_history.append(("home", normalized, None))
