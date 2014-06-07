#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from IsiBase import IsiBase, IsiBaseModel, IsiBaseCtlContainer
from Project import Project, ProjectCtl

class IsiTreeView(QtGui.QTreeView):

    """"""

    def __init__(self, parent=None):
        """"""
        super(IsiTreeView, self).__init__(parent)
        self.dragEnabled()
        self.acceptDrops()
        self.showDropIndicator()
        self.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.setIconSize(QtCore.QSize(32, 32))
        self.customContextMenuRequested.connect(self._ctxMenu)
        self._controllers = dict()
        self._controllers["Project"] = ProjectCtl(self)
        
    @QtCore.pyqtSlot(QtCore.QPoint)
    def _ctxMenu(self, point):
        """"""
        indices = self.selectedIndexes()
        assert len(indices) == 1
        node = indices[0].internalPointer()
        if node.type in self._controllers:
            ctl = self._controllers[node.type]
            ctl.node = node
            if isinstance(ctl, IsiBaseCtlContainer):
                ctl.model = self.model()
                ctl.index = indices[0]
            ctl.menu.exec_(self.mapToGlobal(point))

if __name__ == '__main__':
    app = QtGui.QApplication([])

    dialog = QtGui.QDialog()
    dialog.setMinimumSize(300, 150)
    layout = QtGui.QVBoxLayout(dialog)
    tv = IsiTreeView(dialog)

    root = Project('RootMMM')
    model = IsiBaseModel(rootNode=root)

    tv.setModel(model)
    layout.addWidget(tv)
    dialog.exec_()
    app.closeAllWindows()
