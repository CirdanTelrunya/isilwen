#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from IsiBase import IsiBase, IsiBaseCtlContainer
from ClassView import DlgClassView


class Project(IsiBase):

    """"""

    def __init__(self, name='', parent=None):
        """"""
        super(Project, self).__init__(name, parent)
        self._properties['path'] = ''


class ProjectCtl(IsiBaseCtlContainer):

    """"""

    def __init__(self, parent=None):
        """"""
        super(ProjectCtl, self).__init__(parent)
        self.__initMenu()

    def __initMenu(self):
        """"""
        self._menu = QtGui.QMenu(self.parent())
        self._menu.addAction('[project]')
        self._menu.addSeparator()
        self._menu.addAction('new class view...', self.__newClassView)

    @QtCore.pyqtSlot()
    def __newClassView(self):
        """"""
        dlg = DlgClassView(self.parent())
        if dlg.exec_():
            self._model.insertNode(self._index, dlg.classViewNode)

    @property
    def menu(self):
        """"""
        if self._node is not None:
            actions = self._menu.actions()
            actions[0].setText('[project] '+QtCore.QString(self._node.name))
        return self._menu
