from _typeshed import Unused
from collections.abc import Callable
from typing import Any, ClassVar, Literal

from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject
from panda3d.core import (
    BitMask32,
    CollisionHandlerFloor,
    CollisionHandlerQueue,
    CollisionNode,
    CollisionRay,
    CollisionSphere,
    CollisionTraverser,
    ConfigVariableBool,
    LVector3f,
    NodePath,
)
from panda3d.physics import ActorNode, PhysicsCollisionHandler, PhysicsManager

class PhysicsWalker(DirectObject):
    notify: ClassVar[Notifier]
    wantDebugIndicator: ClassVar[ConfigVariableBool]
    useLifter: ClassVar[bool]
    useHeightRay: ClassVar[bool]
    needToDeltaPos: bool
    physVelocityIndicator: NodePath
    avatarControlForwardSpeed: float
    avatarControlJumpForce: float
    avatarControlReverseSpeed: float
    avatarControlRotateSpeed: float
    getAirborneHeight: Callable[[], float] | None
    collisionsActive: bool
    isAirborne: bool
    highMark: float
    cRay: CollisionRay
    cRayNodePath: NodePath[CollisionNode]
    cRayBitMask: BitMask32
    lifter: CollisionHandlerFloor
    cRayQueue: CollisionHandlerQueue
    avatarRadius: float
    cSphere: CollisionSphere
    cSphereNodePath: NodePath[CollisionNode]
    cSphereBitMask: BitMask32
    pusher: PhysicsCollisionHandler
    actorNode: ActorNode
    phys: PhysicsManager
    cTrav: CollisionTraverser
    floorOffset: float
    avatarNodePath: NodePath[ActorNode]
    physContactIndicator: NodePath
    def __init__(self, gravity: float = -32.174, standableGround: float = 0.707, hardLandingForce: float = 16.0) -> None: ...
    def setWalkSpeed(self, forward: float, jump: float, reverse: float, rotate: float) -> None: ...
    def getSpeeds(self) -> tuple[float, float]: ...
    def setAvatar(self, avatar: Any) -> None: ...
    def setupRay(self, floorBitmask: BitMask32, floorOffset: float) -> None: ...
    def determineHeight(self) -> float: ...
    def setupSphere(self, bitmask: BitMask32, avatarRadius: float) -> None: ...
    def setupPhysics(self, avatarNodePath: NodePath[ActorNode]) -> NodePath[ActorNode]: ...
    def initializeCollisions(
        self,
        collisionTraverser: CollisionTraverser,
        avatarNodePath: NodePath[ActorNode],
        wallBitmask: BitMask32,
        floorBitmask: BitMask32,
        avatarRadius: float = 1.4,
        floorOffset: float = 1.0,
        reach: float = 1.0,
    ) -> None: ...
    def setAirborneHeightFunc(self, getAirborneHeight: Callable[[], float]) -> None: ...
    def setAvatarPhysicsIndicator(self, indicator: NodePath) -> None: ...
    def avatarPhysicsIndicator(self, task: Unused) -> Literal[1]: ...
    def deleteCollisions(self) -> None: ...
    def setCollisionsActive(self, active: bool = ...) -> None: ...
    def getCollisionsActive(self) -> bool: ...
    def placeOnFloor(self) -> None: ...
    def oneTimeCollide(self) -> None: ...
    def addBlastForce(self, vector: Unused) -> None: ...
    def displayDebugInfo(self) -> None: ...
    def handleAvatarControls(self, task: Unused) -> Literal[1]: ...
    def doDeltaPos(self) -> None: ...
    def setPriorParentVector(self) -> None: ...
    def reset(self) -> None: ...
    def getVelocity(self) -> LVector3f: ...
    def enableAvatarControls(self) -> None: ...
    def disableAvatarControls(self) -> None: ...
    def flushEventHandlers(self) -> None: ...
