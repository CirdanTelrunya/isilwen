#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from IsiBase import IsiBase, IsiBaseCtlContainer
from gui.ClassViewUi import Ui_ClassView

class ClassView(IsiBase):
    """"""
    def __init__(self, name='', parent=None):
        """"""
        super(ClassView, self).__init__(name, parent)
    def can_be_inserted(self, node):
        """"""
        return False
            

class DlgClassView(QtGui.QDialog):
    """"""
    def __init__(self, parent=None, classView=None):
        """"""
        super(DlgClassView, self).__init__(parent)
        self.ui = Ui_ClassView()
        self.ui.setupUi(self)
        if classView is None:
            self._classViewNode = ClassView(name='ClassView')
        else:
            self._classViewNode = classView

    def accept(self):
        """"""
        self._classViewNode.name = unicode(self.ui.ldtName.text())
        QtGui.QDialog.accept(self)
        
    @property
    def classViewNode(self):
        """"""
        return self._classViewNode
    
