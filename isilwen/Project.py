#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from IsiBase import IsiBase, IsiBaseCtlContainer

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
        self._menu = QtGui.QMenu(parent)
        self._menu.addAction('Software', self.swTrigger)

    @QtCore.pyqtSlot()
    def swTrigger(self):
        """"""
        print "OK !"
    
    @property
    def menu(self):
        """"""
        return self._menu
        
    
if __name__ == '__main__':
    app = QApplication([])    
    root = Project('project')
    model = IsiBaseModel(root)
    dialog = QDialog()
    dialog.setMinimumSize(300, 150)
    layout = QVBoxLayout(dialog)
    tv = TrainingTree(dialog)
    tv.setModel(model)
    layout.addWidget(tv)
    dialog.exec_()
    app.closeAllWindows()
    SoundMgr.instance = None
