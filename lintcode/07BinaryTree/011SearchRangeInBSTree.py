# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-01
算法思想： 二叉搜索树中的搜索区间
    借助带list的辅助函数
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
    @param: root: param root: The root of the binary search tree
    @param: k1: An integer
    @param: k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        result = []

        self.helper(root, k1, k2, result)

        return result

    def helper(self, root, k1, k2, result):
        if root == None:
            return
        elif root.val >= k1 and root.val <= k2:
            self.helper(root.left, k1, k2, result)
            result.append(root.val)
            self.helper(root.right, k1, k2, result)
        elif root.val < k1:
            self.helper(root.right, k1, k2, result)
        else:
            self.helper(root.left, k1, k2, result)

    def searchRange_2(self, root, k1, k2):
        if root == None:
            return []
        elif root.val >= k1 and root.val <= k2:
            left = self.searchRange_2(root.left, k1, k2)
            result = [root.val]
            right = self.searchRange_2(root.right, k1, k2)
            return left+result+right
        elif root.val < k1:
            right = self.searchRange_2(root.right, k1, k2)
            return right
        else:
            left = self.searchRange_2(root.left, k1, k2)
            return left

if __name__ == '__main__':
    root = TreeNode(20)
    node8 = TreeNode(8)
    node22 = TreeNode(22)
    root.left = node8
    root.right = node22
    node4 = TreeNode(4)
    node12 = TreeNode(12)
    node8.left = node4
    node8.right = node12

    print Solution().searchRange(root, 10, 22)
    print Solution().searchRange_2(root, 10, 22)