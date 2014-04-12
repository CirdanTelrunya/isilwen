#!/usr/bin/python
# -*- coding: utf-8 -*-


class TreeNode(object):

    def __init__(self, name='', parent=None):
        # Contents
        self._name = name
        # Structure
        self._parent = parent
        self._children = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name='Untitled'):
        self._name = name
    @property
    def parent(self):
        return self._parent
    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def child(self, row):
        if(len(self._children) == 0):
            return None
        return self._children[row]

    def insert_child(self, node, row=None):
        node._parent = self
        if row is None or row < 0:
            self._children.append(node)
        else:
            self._children.insert(row, node)

    def remove_child(self, row=None):
        if row is None:
            self._children.pop()
        else:
            self._children.pop(row)
    @property
    def children(self):
        return self._children

    def child_count(self):
        return len(self._children)

    def row(self):
        if self._parent:
            return self._parent._children.index(self)
        else:
            raise IndexError('No parent')
        return 0

    def can_be_inserted(self, node):
        return True

if __name__ == '__main__':
    test = TreeNode()
    test.insert_child(TreeNode('pop'))
    test.name = 'Plop'
    print test.child(0)
    print test.child(0).row()
    print test.name
