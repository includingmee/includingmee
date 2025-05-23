__all__ = ['DirectButton']

from _typeshed import Unused
from typing import Any

from panda3d.core import NodePath

from .DirectFrame import DirectFrame

class DirectButton(DirectFrame):
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
    def setCommandButtons(self) -> None: ...
    def commandFunc(self, event: Unused) -> None: ...
    def setClickSound(self) -> None: ...
    def setRolloverSound(self) -> None: ...
