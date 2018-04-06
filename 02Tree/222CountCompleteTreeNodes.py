# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-06
算法思想：完全二叉树的节点个数
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
            利用完全二叉树的性质
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        leftDepth = self.getLeftDepth(root)+1
        rightDepth = self.getRightDepth(root)+1

        count = 0

        if leftDepth == rightDepth:
            count = pow(2, leftDepth) - 1
        else:
            count = self.countNodes(root.left) + self.countNodes(root.right) + 1

        return count

    def getLeftDepth(self, root):
        depth = 0

        while root.left:
            depth += 1
            root = root.left

        return depth

    def getRightDepth(self, root):
        depth = 0

        while root.right:
            depth += 1
            root = root.right

        return depth