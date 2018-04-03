# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-03
算法思想：二叉树的Z字形遍历
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        zigzagVals = []
        currentNodes = [root]
        flag = 1

        while currentNodes:
            nextlevelNodes = []
            curVals = []

            for node in currentNodes:
                curVals.append(node.val)
                if node.left:
                    nextlevelNodes.append(node.left)
                if node.right:
                    nextlevelNodes.append(node.right)

            if flag == 1:
                zigzagVals.append(curVals)
                flag = 0
            elif flag == 0:
                zigzagVals.append(curVals[::-1])
                flag = 1

            currentNodes = nextlevelNodes

        return zigzagVals

if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    root.right = node2
    root.left = node4
    node2.left = node3
    node4.right = node5

    print Solution().zigzagLevelOrder(root)