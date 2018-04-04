# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-04
算法思想：是否平衡二叉树
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if abs(self.depth(root.left)-self.depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

        return False

    def depth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        return max(self.depth(root.left), self.depth(root.right)) + 1