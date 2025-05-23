from _typeshed import Unused
from collections.abc import Callable, Iterable, Mapping
from typing import Any, Final, NoReturn

TIMEOUT_MAX: Final[float]

def force_yield() -> None: ...
def consider_yield() -> None: ...

forceYield = force_yield
considerYield = consider_yield

class error(Exception): ...

class LockType:
    def __init__(self) -> None: ...
    def release(self) -> None: ...
    def locked(self) -> bool: ...
    def __enter__(self, waitflag: bool = ..., timeout: float = -1) -> bool: ...
    def __exit__(self, t: Unused, v: Unused, tb: Unused) -> None: ...  # noqa: Y036
    acquire = __enter__

def start_new_thread(
    function: Callable[..., object], args: Iterable[Any], kwargs: Mapping[str, Any] = {}, name: str | None = None
) -> int: ...
def interrupt_main() -> None: ...
def exit() -> NoReturn: ...
def allocate_lock() -> LockType: ...
def get_ident() -> int: ...
def stack_size(size: Unused = 0) -> NoReturn: ...
