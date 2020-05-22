""" Module for creating linked binary tree"""


class BinaryTree:
    """Class for representation tree for
     representing game actions"""

    def __init__(self, root):
        """ Create new Tree """
        self.key = root
        self.left = None
        self.right = None

    def insertLeft(self, node):
        """
        Insert node to the left.
        :return:
        """
        if self.left is None:
            self.left = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left = self.left
            self.left = t

    def insertRight(self, node):
        """
        Insert node to the right.
        :return:
        """
        if self.right is None:
            self.right = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right = self.right
            self.right = t

    def getLeft(self):
        """
        Return value of left node.
        :return:
        """
        return self.left

    def getRight(self):
        """
        Return value of right node.
        :return:
        """
        return self.right

    def preorder(self):
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key)

    def inorder(self, lst):
        if self.left:
            lst.append(self.left)
            self.left.inorder(lst)
        if self.right:
            lst.append(self.right)
            self.right.inorder(lst)
        return lst

    def getAllLeaves(self):
        """
        Return list with tree's leaves.
        :return:
        """
        newLst = []

        def _getAllLeaves(tree, lst_):
            if tree.getLeft() is not None and tree.getRight()\
                    is not None:
                if tree.getLeft() is not None:
                    _getAllLeaves(tree.left, lst_)
                if tree.getRight() is not None:
                    _getAllLeaves(tree.getRight(), lst_)
            elif tree.getLeft() is None and tree.getRight()\
                    is None:
                newLst.append(tree.key)

        _getAllLeaves(self, newLst)
        return newLst
