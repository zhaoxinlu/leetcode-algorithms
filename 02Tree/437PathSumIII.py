# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：路径之和III
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.pathSumIIIDFS(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSumIIIDFS(self, root, sum):
        result = 0
        if not root:
            return result
        if sum == root.val:
            result += 1

        result += self.pathSumIIIDFS(root.left, sum-root.val)
        result += self.pathSumIIIDFS(root.right, sum-root.val)

        return result