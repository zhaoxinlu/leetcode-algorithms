# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-04
算法思想：平铺二叉树（按先序遍历顺序）
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                curNode = root.left
                while curNode.right:
                    curNode = curNode.right

                curNode.right = root.right
                root.right = root.left
                root.left = None
            root = root.right