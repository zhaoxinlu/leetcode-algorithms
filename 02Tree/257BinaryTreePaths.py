# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-05
算法思想：打印二叉树路径
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        result = []
        self.binaryTreePathsDFS(root, [], result)
        return result

    def binaryTreePathsDFS(self, root, tmp, result):
        tmp.append(str(root.val))
        if not root.left and not root.right:
            result.append('->'.join(tmp))
        if root.left:
            self.binaryTreePathsDFS(root.left, tmp, result)
        if root.right:
            self.binaryTreePathsDFS(root.right, tmp, result)
        tmp.pop()