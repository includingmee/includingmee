from _typeshed import Unused
from typing import Any

import wx  # type: ignore
import wx.siplib as sip  # type: ignore

from .LevelEditor import LevelEditor
from .PaletteTreeCtrl import PaletteTreeCtrl

class ObjectPaletteUI(wx.Panel, metaclass=sip.wrapper):
    editor: LevelEditor
    palette: Any
    tree: PaletteTreeCtrl
    opSortAlpha: str
    opSortOrig: str
    opSort: str
    menuItems: list[str]
    popupmenu: wx.Menu
    def __init__(self, parent: Any, editor: LevelEditor) -> None: ...
    def populate(self) -> None: ...
    def onSelected(self, event: Unused) -> None: ...
    def onShowPopup(self, event) -> None: ...
    def onPopupItemSelected(self, event) -> None: ...
    def compareItems(self, item1, item2): ...
    def getSelected(self): ...
