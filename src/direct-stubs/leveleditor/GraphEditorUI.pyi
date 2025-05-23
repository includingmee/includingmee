from _typeshed import Unused
from collections.abc import Sequence
from typing import Any, SupportsFloat

import wx  # type: ignore
import wx.siplib as sip  # type: ignore
from direct._typing import Obj
from panda3d._typing import Vec2Like
from wx.lib.embeddedimage import PyEmbeddedImage  # type: ignore

from .LevelEditor import LevelEditor

property: list[str]
ZoomIn: PyEmbeddedImage
ZoomOut: PyEmbeddedImage
OneTangent: PyEmbeddedImage
TwoTangents: PyEmbeddedImage

class GraphEditorWindow(wx.Window, metaclass=sip.wrapper):
    w: int
    h: int
    zoom: float
    object: Obj
    curFrame: int
    property = ...
    zeroPos: tuple[float, float]
    zero: int
    unitWidth: float
    unitHeight: float
    X: list
    Y: list
    Z: list
    buffer: wx.Bitmap
    def __init__(
        self, parent: Any, windowSize, property, xRange: SupportsFloat, yRange: SupportsFloat, curFrame: int, object: Obj
    ) -> None: ...
    def refresh(self) -> None: ...
    def generateInfo(self) -> None: ...
    def generateHandler(self, item) -> list: ...
    def InitBuffer(self) -> None: ...
    def SetGraphEditorData(self, property, curFrame: int = 1) -> None: ...
    def OnPaint(self, evt: Unused) -> None: ...
    def DrawXCoord(self, dc) -> None: ...
    def DrawYCoord(self, dc) -> None: ...
    def drawXNumber(self, dc, st, pos: float) -> None: ...
    def drawYNumber(self, dc, st, pos: float) -> None: ...
    def DrawFrame(self, dc) -> None: ...
    def drawX(self, dc) -> None: ...
    def drawY(self, dc) -> None: ...
    def drawZ(self, dc) -> None: ...
    def DrawCurve(self, dc) -> None: ...
    def drawSingleCurve(self, list: Sequence, dc) -> None: ...
    def drawKeys(self, list: Sequence, dc) -> None: ...
    def drawHandler(self, list: Sequence, dc) -> None: ...
    def DrawSelectRec(self, dc) -> None: ...
    def OnSize(self, evt: Unused) -> None: ...
    def OnLeftDown(self, evt) -> None: ...
    def OnLeftUp(self, evt: Unused) -> None: ...
    def OnMiddleDown(self, evt) -> None: ...
    def OnMiddleUp(self, evt: Unused) -> None: ...
    def OnMotion(self, evt) -> None: ...
    def setExistKey(self, list: Sequence) -> bool: ...
    def setNewKey(self, list: Sequence) -> None: ...
    def setSelection(self) -> None: ...
    def setSelectionBase(self, list: Sequence) -> None: ...
    def inside(self, point0: Vec2Like, point1: Vec2Like, point: Vec2Like) -> bool: ...
    def recalculateSlope(self) -> None: ...
    def recalculateSlopeBase(self, list: Sequence) -> None: ...
    def selectHandler(self) -> None: ...
    def onAnimation(self) -> None: ...

class GraphEditorUI(wx.Dialog, metaclass=sip.wrapper):
    editor: LevelEditor
    object: Obj
    xRange: int
    yRange: int
    curFrame: int
    mainPanel1: wx.Panel
    buttonZoomIn: wx.BitmapButton
    buttonZoomOut: wx.BitmapButton
    buttonOneTangent: wx.BitmapButton
    buttonTwoTangents: wx.BitmapButton
    mainPanel2: wx.Panel
    tree: wx.TreeCtrl
    namestr: str
    root: wx.TreeItemId
    str: str
    graphEditorWindow: GraphEditorWindow
    dialogSizer: wx.BoxSizer
    def __init__(self, parent: Any, editor: LevelEditor, object: Obj) -> None: ...
    def SetProperties(self) -> None: ...
    def DoLayout(self) -> None: ...
    def AddTreeNodes(self, parentItem, items) -> None: ...
    def OnSelChanged(self, evt) -> None: ...
    def OnZoomIn(self, evt: Unused) -> None: ...
    def OnZoomOut(self, evt: Unused) -> None: ...
    def OnOneTangent(self, evt: Unused) -> None: ...
    def OnTwoTangents(self, evt: Unused) -> None: ...
    def curFrameChange(self) -> None: ...
    def OnExit(self, evt: Unused) -> None: ...
