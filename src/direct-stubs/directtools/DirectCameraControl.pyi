from _typeshed import Unused
from collections.abc import Sequence
from typing import Any, ClassVar, Final, Literal
from typing_extensions import TypeAlias

from direct.directnotify.Notifier import Notifier
from direct.interval.MetaInterval import MetaInterval
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
from panda3d.core import AsyncTask, CollisionEntry, LPoint3f, LVector3f, NodePath

CAM_MOVE_DURATION: Final = 1.2
COA_MARKER_SF: Final = 0.0075
Y_AXIS: Final[LVector3f]

_TaskCont: TypeAlias = Literal[1]

class DirectCameraControl(DirectObject):
    notify: ClassVar[Notifier]
    startT: float
    startF: int
    orthoViewRoll: float
    lastView: int
    coa: LPoint3f
    coaMarker: NodePath
    coaMarkerPos: LPoint3f
    coaMarkerColorIval: MetaInterval | None
    fLockCOA: bool
    nullHitPointCount: int
    cqEntries: list[CollisionEntry]
    coaMarkerRef: NodePath
    camManipRef: NodePath
    switchDirBelowZero: bool
    manipulateCameraTask: AsyncTask | None
    manipulateCameraInterval: MetaInterval | None
    actionEvents: list[list[Any]]
    keyEvents: list[list[Any]]
    lockRoll: bool
    useMayaCamControls: bool
    altDown: bool
    perspCollPlane: NodePath | None
    perspCOllPlane2: NodePath | None
    def __init__(self) -> None: ...
    def toggleMarkerVis(self) -> None: ...
    def mouseRotateStart(self, modifiers: int) -> None: ...
    def mouseDollyStart(self, modifiers: int) -> None: ...
    def mouseDollyStop(self) -> None: ...
    def mouseFlyStart(self, modifiers: int) -> None: ...
    def mouseFlyStop(self) -> None: ...
    def mouseFlyStartTopWin(self) -> None: ...
    def mouseFlyStopTopWin(self) -> None: ...
    def spawnXZTranslateOrHPanYZoom(self) -> None: ...
    def spawnXZTranslateOrHPPan(self) -> None: ...
    def spawnXZTranslate(self) -> None: ...
    def spawnOrthoTranslate(self) -> None: ...
    def spawnHPanYZoom(self) -> None: ...
    def spawnOrthoZoom(self) -> None: ...
    def spawnHPPan(self) -> None: ...
    def XZTranslateOrHPanYZoomTask(self, state: Task) -> _TaskCont: ...
    def XZTranslateOrHPPanTask(self, state: Unused) -> _TaskCont: ...
    def XZTranslateTask(self, state: Unused) -> _TaskCont: ...
    def OrthoTranslateTask(self, state: Task) -> _TaskCont: ...
    def HPanYZoomTask(self, state: Task) -> _TaskCont | None: ...
    def OrthoZoomTask(self, state: Unused) -> _TaskCont: ...
    def HPPanTask(self, state: Unused) -> _TaskCont: ...
    def spawnMouseRotateTask(self) -> None: ...
    def mouseRotateTask(self, state: Task) -> _TaskCont: ...
    def spawnMouseRollTask(self) -> None: ...
    def mouseRollTask(self, state: Task) -> _TaskCont: ...
    def lockCOA(self) -> None: ...
    def unlockCOA(self) -> None: ...
    def toggleCOALock(self) -> None: ...
    def pickNextCOA(self) -> None: ...
    def computeCOA(self, entry: CollisionEntry) -> None: ...
    def updateCoa(self, ref2point: Sequence[float], coaDist: float | None = None, ref: NodePath | None = None) -> None: ...
    def updateCoaMarkerSizeOnDeath(self) -> None: ...
    def updateCoaMarkerSize(self, coaDist: float | None = None) -> None: ...
    def homeCam(self) -> None: ...
    def uprightCam(self) -> None: ...
    def orbitUprightCam(self) -> None: ...
    def centerCam(self) -> None: ...
    def centerCamNow(self) -> None: ...
    def centerCamIn(self, t: Unused) -> None: ...
    def zoomCam(self, zoomFactor: float, t: Unused) -> None: ...
    def spawnMoveToView(self, view: int) -> None: ...
    def swingCamAboutWidget(self, degrees: float, t: Unused) -> None: ...
    def reparentCam(self, parent: NodePath) -> None: ...
    def fitOnWidget(self, nodePath: Unused = 'None Given') -> None: ...
    def moveToFit(self) -> None: ...
    def stickToWidgetTask(self, state: Unused) -> _TaskCont: ...
    def enableMouseFly(self, fKeyEvents: bool = ...) -> None: ...
    def disableMouseFly(self) -> None: ...
    def removeManipulateCameraTask(self) -> None: ...
