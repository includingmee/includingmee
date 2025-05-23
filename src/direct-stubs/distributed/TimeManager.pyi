from _typeshed import Unused
from typing import ClassVar, Literal

from .DistributedObject import DistributedObject

class TimeManager(DistributedObject):
    updateFreq: ClassVar[float]
    minWait: ClassVar[float]
    maxUncertainty: ClassVar[float]
    maxAttempts: ClassVar[int]
    extraSkew: ClassVar[int]
    reportFrameRateInterval: ClassVar[float]
    thisContext: int
    nextContext: int
    attemptCount: int
    start: int
    lastAttempt: float
    def startTask(self) -> None: ...
    def stopTask(self) -> None: ...
    def doUpdate(self, task: Unused) -> Literal[0]: ...
    def handleClockError(self) -> None: ...
    def synchronize(self, description: str) -> bool: ...
    def serverTime(self, context: int, timestamp: int) -> None: ...
