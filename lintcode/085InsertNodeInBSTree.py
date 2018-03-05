# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-05
算法思想： 二叉搜索树中插入节点
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
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root == None:
            root = node
        elif root.val > node.val:
            root.left = self.insertNode(root.left, node)
        elif root.val < node.val:
            root.right = self.insertNode(root.right, node)

        return root