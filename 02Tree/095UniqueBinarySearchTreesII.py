# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-03
算法思想：所有符合的二叉查找树--回溯
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.genTreeDFS(1, n)

    def genTreeDFS(self, start, end):
        if start > end:
            return [None]
        result = []
        for rootVal in range(start, end+1):
            leftTree = self.genTreeDFS(start, rootVal-1)
            rightTree = self.genTreeDFS(rootVal+1, end)
            for i in leftTree:
                for j in rightTree:
                    root = TreeNode(rootVal)
                    root.left = i
                    root.right = j
                    result.append(root)
        return result

if __name__ == '__main__':
    print Solution().generateTrees(3)