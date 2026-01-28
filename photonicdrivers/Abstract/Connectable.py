'''
For explanation of this type checking "Abstract class" look up wikipage:

    DevOps --> Wiki --> NQCP-teams --> Characterization-team --> Onboarding-to-Characterization --> Photonic Characterization Structures

'''

'''
In order to avoid race conditions, concurrent hardware access etc.
running a Connectable method will ALWAYS be exclusive access.
All other callers will be blocked until the method finishes (or timeout after 60s).
If a hardware call blocks indefinitely, the hardware *will* be locked.
This implementation hides the locking from Driver code, at the cost of a fair bit of Python 'magic'
'''

import functools
import inspect
import threading
from abc import ABC

def _wrap_with_lock(func):
    if getattr(func, "__connectable_wrapped__", False):
        return func

    @functools.wraps(func)
    def wrapped(self, *args, **kwargs):
        # RLock makes nested self-calls safe (A -> B -> C).
        acquired = False
        try:
            acquired = self._connectable_lock.acquire(timeout=60)
            if not acquired:
                raise TimeoutError(
                    f"Connectable method '{func.__qualname__}' lock acquisition timed out after 60s"
                )
            return func(self, *args, **kwargs)
        finally:
            if acquired:
                self._connectable_lock.release()

    wrapped.__connectable_wrapped__ = True
    return wrapped


class Connectable(ABC):
    def connect(self) -> None:
        ...

    def disconnect(self) -> None:
        ...

    def is_connected(self) -> bool:
        ...

    __slots__ = ("_connectable_lock",)

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        # Created even if subclasses override __init__ and forget super().__init__().
        self._connectable_lock = threading.RLock()
        return self

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        for name, attr in list(cls.__dict__.items()):
            # Skip dunder methods by default.
            if name.startswith("__") and name.endswith("__"):
                continue

            # Wrap properties
            if isinstance(attr, property):
                fget = _wrap_with_lock(attr.fget) if attr.fget else None
                fset = _wrap_with_lock(attr.fset) if attr.fset else None
                fdel = _wrap_with_lock(attr.fdel) if attr.fdel else None
                setattr(cls, name, property(fget, fset, fdel, attr.__doc__))
                continue

            # Wrap normal instance methods.
            if inspect.isfunction(attr):
                setattr(cls, name, _wrap_with_lock(attr))
                continue

            # Leave staticmethod and classmethod alone
            if isinstance(attr, (classmethod, staticmethod)):
                continue
