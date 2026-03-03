'''
For explanation of this type checking "Abstract class" look up wikipage:

    DevOps --> Wiki --> NQCP-teams --> Characterization-team --> Onboarding-to-Characterization --> Photonic Characterization Structures

'''

from typing import Protocol, runtime_checkable

@runtime_checkable
class Connectable(Protocol):
    def connect(self) -> None:
        ...

    def disconnect(self) -> None:
        ...

    def is_connected(self) -> bool:
        ...

