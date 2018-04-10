# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-09
算法思想：层序遍历二叉树
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        levelVals = []
        curLevelNodes = [root]
        while curLevelNodes:
            nextLevelNodes = []
            curLevelVals = []

            for node in curLevelNodes:
                curLevelVals.append(node.val)
                if node.left:
                    nextLevelNodes.append(node.left)
                if node.right:
                    nextLevelNodes.append(node.right)

            levelVals.append(curLevelVals)
            curLevelNodes = nextLevelNodes

        return levelVals