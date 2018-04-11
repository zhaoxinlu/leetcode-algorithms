# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：右看二叉树
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        rightVals = []
        curLevelNodes = [root]

        while curLevelNodes:
            nextLevelNodes = []

            for i in range(len(curLevelNodes)):
                if curLevelNodes[i].left:
                    nextLevelNodes.append(curLevelNodes[i].left)
                if curLevelNodes[i].right:
                    nextLevelNodes.append(curLevelNodes[i].right)
                if i == len(curLevelNodes)-1:
                    rightVals.append(curLevelNodes[i].val)

            curLevelNodes = nextLevelNodes

        return rightVals