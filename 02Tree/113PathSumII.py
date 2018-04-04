# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-04
算法思想：输出所有二叉树路径和等于某值--回溯
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
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        self.pathsumDFS(root, sum, [], result)
        return result

    def pathsumDFS(self, root, sum, tmp, result):
        tmp.append(root.val)
        sum -= root.val
        if not root.left and not root.right and sum == 0:
            result.append(tmp[:])
        if root.left:
            self.pathsumDFS(root.left, sum, tmp, result)
        if root.right:
            self.pathsumDFS(root.right, sum, tmp, result)
        tmp.pop()