# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-10
算法思想： 删除二叉查找树的节点 -- !!!!
"""
"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        """
        一、删除的节点无左右节点，直接return NULL；
        二、删除的节点只有一个左节点或者右节点，return delNode->left 或者return delNode->right;
        三、删除的节点即有左节点也有右节点，则需要：
            1、将delNode备份，temp = delNode；
            2、delNode指向后继右节点的最小节点，即delNode = minNode（delNode->right）;
            3、将delNode的right链接到removeNode（temp->right）上；
            4、将delNode的left连接点temp的left上；
        :param root:
        :param value:
        :return:
        """
        if not root:
            return None

        if root.val > value:
            root.left = self.removeNode(root.left, value)
        elif root.val < value:
            root.right = self.removeNode(root.right, value)
        else:
            if root.right == None:
                return root.left
            if root.left == None:
                return root.right

            tmpNode = root
            root = self.minNode(root.right)
            root.right = self.delminNode(tmpNode.right)
            root.left = tmpNode.left

        return root

    def minNode(self, root):
        if root.left == None:
            return root

        return self.minNode(root.left)

    def delminNode(self, root):
        if root.left == None:
            return root.right

        root.left = self.delminNode(root.left)

        return root