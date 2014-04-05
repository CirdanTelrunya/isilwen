#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from TreeNode import TreeNode
import pickle
import string

class TreeNodeItemModel(QtCore.QAbstractItemModel):

    def __init__(self, rootNode=None, parent=None):
        super(TreeNodeItemModel, self).__init__(parent)
        # add the virtual root with name for header
        self._rootNode = TreeNode('Tree')
        if rootNode is None:
            self._rootNode.insert_child(TreeNode(name='Untitled',
                    parent=rootNode))
        else:
            self._rootNode.insert_child(rootNode)


    def columnCount(self, index):
        return 1

    def data(self, index, role):
        if not index.isValid():
            return None
        if role != QtCore.Qt.DisplayRole:
            return None
        node = self.getNode(index)
        return QtCore.QString(node.name())

    def dropMimeData(self, mimedata, action, row, column, parent):
        if not parent.isValid():
            return False
        node = self.getNode(parent)
        newNode = pickle.loads(str(mimedata.text()))
        
        if action != QtCore.Qt.MoveAction:
            return False

        if node.can_be_inserted(newNode):
            return self.insertNode(parent, newNode, row)
        else:
            return False

    def flags(self, index):
        defaultFlags = QtCore.QAbstractItemModel.flags(self, index)
        if index.isValid():
            return QtCore.Qt.ItemIsDragEnabled | \
                    QtCore.Qt.ItemIsDropEnabled | defaultFlags
        else:
            return QtCore.Qt.ItemIsDropEnabled | defaultFlags

    def getNode(self, index):
        if index.isValid():
            node = index.internalPointer()
            if node:
                return node
        return self._rootNode

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal \
           and role == QtCore.Qt.DisplayRole:
            return self._rootNode.name()
        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()
        
        parentNode = self.getNode(parent)
        childNode = parentNode.child(row)
        if childNode:
            return self.createIndex(row, column, childNode)
        else:
            return QtCore.QModelIndex()

    def insertNode(self, parent, node, row = None):
        if not parent.isValid():
            return False
        parentNode = self.getNode(parent)

        if row is None or row < 0 :
            row = parentNode.child_count()
        # Insert the Node
        self.beginInsertRows(parent, row, row)
        parentNode.insert_child(node, row)
        self.endInsertRows()
        return True

    def mimeTypes(self):
        types = QtCore.QStringList()
        types.append('text/plain')
        return types

    def mimeData(self, index):
        node = index[0].internalPointer()
        data = pickle.dumps(node)
        mimeData = QtCore.QMimeData()
        mimeData.setText(data)
        return mimeData 

    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()
        childItem = self.getNode(index)
        parentNode = childItem.parent()
        if parentNode == self._rootNode:
            return QtCore.QModelIndex()
        return self.createIndex(parentNode.row(), 0, parentNode)

    def removeRows(self, row, count, parent):        
        if not parent.isValid():
            return False
        parentNode = self.getNode(parent)
        self.beginRemoveRows(parent, row, row)
        parentNode.remove_child(row)
        self.endRemoveRows()
        return True

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0
        parentNode = self.getNode(parent)
        return parentNode.child_count()

    def supportedDropActions(self):
        return QtCore.Qt.MoveAction 

if __name__ == '__main__':
    app = QtGui.QApplication([])
    root = TreeNode('Root')
    root.insert_child(TreeNode('Plup'))
    
    model = TreeNodeItemModel(root)
    dialog = QtGui.QDialog()
    dialog.setMinimumSize(300, 150)
    layout = QtGui.QVBoxLayout(dialog)
    tv = QtGui.QTreeView(dialog)
    tv.setModel(model)
    tv.dragEnabled()
    tv.acceptDrops()
    tv.showDropIndicator()
    tv.setDragDropMode(QtGui.QAbstractItemView.InternalMove) 
    

    layout.addWidget(tv)
    index = model.index(0, 0, QtCore.QModelIndex())
    model.insertNode(index, TreeNode('Plop'))
    # model.insertNode(index, TreeNode('Plip'))
    dialog.exec_()
    app.closeAllWindows()
