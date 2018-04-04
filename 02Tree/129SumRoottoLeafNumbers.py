# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-04
算法思想：二叉树路径总和
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
            使用一个preSum变量来记录从根节点到节点父亲的路径.
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)

    def helper(self, root, preSum):
        if not root:
            return 0
        preSum = preSum * 10 + root.val
        if not root.left and not root.right:
            return preSum
        return self.helper(root.left, preSum) + self.helper(root.right, preSum)