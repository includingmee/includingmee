from _typeshed import Incomplete, Unused
from collections.abc import Container, Iterable, Sequence
from types import CodeType
from typing import Any, ClassVar, Literal, NoReturn
from typing_extensions import TypeAlias

from direct.directnotify.Notifier import Notifier
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from direct.showbase.DirectObject import DirectObject
from panda3d._typing import Vec3Like, Vec4Like
from panda3d.core import (
    Connection,
    ConnectionWriter,
    DatagramIterator,
    LVecBase2f,
    LVector3f,
    NetDatagram,
    NodePath,
    QueuedConnectionManager,
    QueuedConnectionReader,
)

from .ClusterMsgs import ClusterMsgHandler

_NamedMovement: TypeAlias = tuple[
    str, float, float, float, float, float, float, float, float, float, float, float, float, float, bool
]
_TaskCont: TypeAlias = Literal[1]

class ClusterClient(DirectObject):
    notify: ClassVar[Notifier]
    MGR_NUM: ClassVar[int]
    __name__: str
    daemon: Any
    qcm: QueuedConnectionManager
    serverList: list[DisplayConnection]
    serverQueues: list[list[tuple[Incomplete, Incomplete, Incomplete]]]
    msgHandler: ClusterMsgHandler
    objectMappings: dict[str, NodePath]
    objectHasColor: dict[str, bool]
    controlMappings: dict[str, tuple[str, Sequence[int]]]
    controlOffsets: dict[str, LVector3f]
    taggedObjects: dict[str, dict[str, Any]]
    controlPriorities: dict[str, int]
    sortedControlMappings: list[tuple[int, str]]
    def __init__(self, configList: Iterable[ClusterConfigItem], clusterSyncFlag: int) -> None: ...
    def startReaderPollTask(self) -> None: ...
    def startControlObjectTask(self) -> None: ...
    def startSynchronizeTimeTask(self) -> None: ...
    def synchronizeTimeTask(self, task: Unused) -> _TaskCont: ...
    def startMoveCamTask(self) -> None: ...
    def controlObjectTask(self, task: Unused) -> _TaskCont: ...
    def sendNamedMovementDone(self, serverList: Sequence[int] | None = None) -> None: ...
    def redoSortedPriorities(self) -> None: ...
    def moveObject(
        self, nodePath: NodePath, object: str, serverList: Iterable[int], offset: Vec3Like, hasColor: bool = True
    ) -> None: ...
    def moveCameraTask(self, task: Unused) -> _TaskCont: ...
    def moveCamera(self, xyz: Vec3Like, hpr: Vec3Like) -> None: ...
    def startMoveSelectedTask(self) -> None: ...
    def moveSelectedTask(self, state: Unused) -> _TaskCont: ...
    def addNamedObjectMapping(self, object: NodePath, name: str, hasColor: bool = True) -> None: ...
    def removeObjectMapping(self, name: str) -> None: ...
    def addControlMapping(
        self,
        objectName: str,
        controlledName: str,
        serverList: Sequence[int] | None = None,
        offset: LVector3f | None = None,
        priority: int = 0,
    ) -> None: ...
    def setControlMappingOffset(self, objectName: str, offset: LVector3f) -> None: ...
    def removeControlMapping(self, name: str, serverList: Container[int] | None = None) -> None: ...
    def getNodePathFindCmd(self, nodePath: NodePath) -> str: ...
    def getNodePathName(self, nodePath: NodePath) -> str: ...
    def addObjectTag(
        self, object: str, selectFunction: Any, deselectFunction: Any, selectArgs: Any, deselectArgs: Any
    ) -> None: ...
    def removeObjectTag(self, object: str) -> None: ...
    def selectNodePath(self, nodePath: NodePath) -> None: ...
    def deselectNodePath(self, nodePath: NodePath) -> None: ...
    def sendCamFrustum(
        self, focalLength: float, filmSize: LVecBase2f, filmOffset: LVecBase2f, indexList: Iterable[int] = []
    ) -> None: ...
    def loadModel(self, nodePath: Unused) -> None: ...
    def __call__(self, commandString: str, fLocally: bool = ..., serverList: Iterable[int] = []) -> None: ...
    def handleDatagram(self, dgi: DatagramIterator, type: int, server: int) -> int: ...
    def handleMessageQueue(self, server: int) -> None: ...
    def handleNamedMovement(self, data: _NamedMovement) -> None: ...
    def exit(self) -> NoReturn: ...

class ClusterClientSync(ClusterClient):
    waitForSwap: bool
    ready: bool
    def startSwapCoordinatorTask(self) -> None: ...
    def swapCoordinator(self, task: Unused) -> _TaskCont: ...

class DisplayConnection:
    msgHandler: ClusterMsgHandler
    tcpConn: Connection
    qcr: QueuedConnectionReader
    cw: ConnectionWriter
    def __init__(self, qcm: QueuedConnectionManager, serverName: str, port: int, msgHandler: ClusterMsgHandler) -> None: ...
    def poll(self) -> list[tuple[NetDatagram, PyDatagramIterator, str]]: ...
    def sendCamOffset(self, xyz: Vec3Like, hpr: Vec3Like) -> None: ...
    def sendCamFrustum(self, focalLength: float, filmSize: LVecBase2f, filmOffset: LVecBase2f) -> None: ...
    def sendNamedMovementDone(self) -> None: ...
    def sendMoveNamedObject(
        self, xyz: Vec3Like, hpr: Vec3Like, scale: Vec3Like, color: Vec4Like, hidden: bool, name: str
    ) -> None: ...
    def sendMoveCam(self, xyz: Vec3Like, hpr: Vec3Like) -> None: ...
    def sendMoveSelected(self, xyz: Vec3Like, hpr: Vec3Like, scale: Vec3Like) -> None: ...
    def getSwapReady(self) -> None: ...
    def sendSwapNow(self) -> None: ...
    def sendCommandString(self, commandString: str) -> None: ...
    def sendExit(self) -> None: ...
    def sendTimeData(self, frameCount: int, frameTime: float, dt: float) -> None: ...

class ClusterConfigItem:
    serverConfigName: str
    serverName: str
    serverDaemonPort: int
    serverMsgPort: int
    xyz: LVector3f
    hpr: LVector3f
    fFrustum: bool
    focalLength: float
    filmSize: LVecBase2f
    filmOffset: LVecBase2f
    def __init__(self, serverConfigName: str, serverName: str, serverDaemonPort: int, serverMsgPort: int) -> None: ...
    def setCamOffset(self, xyz: LVector3f, hpr: LVector3f) -> None: ...
    def setCamFrustum(self, focalLength: float, filmSize: LVecBase2f, filmOffset: LVecBase2f) -> None: ...

def createClusterClient() -> ClusterClient | ClusterClientSync: ...

class DummyClusterClient(DirectObject):
    notify: ClassVar[Notifier]
    def __init__(self) -> None: ...
    def __call__(self, commandString: str | bytes | CodeType, fLocally: bool = ..., serverList: Unused = None) -> None: ...
