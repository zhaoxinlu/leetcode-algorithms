# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-10
算法思想： 二叉树的最小深度
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
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if not root:
            return 0

        if root.left == None and root.right == None:
            return 1

        if root.left:
            left = self.minDepth(root.left)
        else:
            return self.minDepth(root.right) + 1

        if root.right:
            right = self.minDepth(root.right)
        else:
            return left + 1

        return min(left, right) + 1