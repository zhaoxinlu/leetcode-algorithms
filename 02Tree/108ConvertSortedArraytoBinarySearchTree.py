# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-05
算法思想：排序数组转化为平衡二叉排序树
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) <= 0:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        root = TreeNode(nums[len(nums)/2])
        root.left = self.sortedArrayToBST(nums[:len(nums)/2])
        root.right = self.sortedArrayToBST(nums[len(nums)/2+1:])

        return root