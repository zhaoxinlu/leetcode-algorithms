# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： 平衡二叉树
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        return self.treeDepth(root) != -1

    def treeDepth(self, root):
        if root == None:
            return 0

        left = self.treeDepth(root.left)
        right = self.treeDepth(root.right)

        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1

        return max(left, right) + 1