# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-09
算法思想：是否对称二叉树
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, root)

    def helper(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)