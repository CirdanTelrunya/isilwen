#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from string import Template

from tree.TreeNode import TreeNode
from tree.TreeNodeItemModel import TreeNodeItemModel

class IsiTemplate(Template):
    """"""
    idpattern = r'[a-z][\.\-_a-z0-9]*'
    
class IsiBase(TreeNode):

    """The base for all generator"""

    def __init__(self, name='', parent=None):
        """"""
        super(IsiBase, self).__init__(name, parent)
        self._is_deleted = False
        self._icon = None
        self._deleted_icon = None
        self._properties = {}
        self._type = self.__class__.__name__

    @property
    def is_deleted(self):
        """"""
        return self._is_deleted
    @is_deleted.setter
    def is_deleted(self, deleted):
        self._is_deleted = deleted

    @property
    def icon(self):
        if self._is_deleted is True:
            return self._deleted_icon
        else:
            return self._icon
    @icon.setter
    def icon(self, icon):
        self._icon = icon

    @property
    def deleted_icon(self):
        return icon

    @deleted_icon.setter
    def deleted_icon(self, icon):
        self._deleted_icon = icon

    @property
    def properties(self):
        """"""
        return self._properties

    def append_properties(self, prop):
        self._properties.update(prop)

    @property
    def type(self):
        """"""
        return self._type

    @type.setter
    def type(self, type):
        """"""
        self._type = type
        
    def __getstate__(self):
        """Never record self and children if deleted"""
        odict = self.__dict__.copy()
        for child in self._children:
            if child.is_deleted:
                odict["_children"].remove(child)
        return odict


class IsiBaseModel(TreeNodeItemModel):

    """"""

    def __init__(self, rootNode=None, parent=None):
        """"""
        super(IsiBaseModel, self).__init__(rootNode, parent)

    def data(self, index, role):
        """"""
        if not index.isValid():
            return None
        node = self.getNode(index)
        if role == QtCore.Qt.DisplayRole:
            return QtCore.QString(node.name)
        elif role == QtCore.Qt.DecorationRole and node.icon:
            return QtGui.QIcon(node.icon)
        elif role == QtCore.Qt.FontRole and node.is_deleted:
            font = QtGui.QFont()
            font.setStrikeOut(True)
            return font
        elif role == QtCore.Qt.SizeHintRole:
            return QtCore.QSize(32, 32)

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal \
           and role == QtCore.Qt.DisplayRole:
            return 'Project View'
        return None

class IsiBaseCtl(QtCore.QObject):
    """"""
    def __init__(self, parent=None):
        """"""
        super(IsiBaseCtl, self).__init__(parent)
        self._node = None

    @property
    def node(self):
        """"""
        return self._node
    @node.setter
    def node(self, node):
        """"""
        self._node = node

class IsiBaseCtlContainer(IsiBaseCtl):
    """"""
    def __init__(self, parent=None):
        """"""
        super(IsiBaseCtlContainer, self).__init__(parent)
        self._index = None
        self._model = None

    @property
    def index(self):
        """"""
        return self._index
        
    @index.setter
    def index(self, index):
        """"""
        self._index = index

    @property
    def model(self):
        """"""
        return self._model

    @model.setter
    def model(self, model):
        """"""
        self._model = model
        
        
        
        
    
