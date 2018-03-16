# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-04
算法思想： 二叉树的之字形打印
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
    @param: root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if root == None:
            return []

        zigzagVals = []
        curlevelNodes = [root]
        flag = 1

        while curlevelNodes:
            nextlevelNodes = []
            curVals = []

            for pNode in curlevelNodes:
                if pNode.left:
                    nextlevelNodes.append(pNode.left)
                if pNode.right:
                    nextlevelNodes.append(pNode.right)
                curVals.append(pNode.val)

            if flag == 0:
                zigzagVals.append(curVals[::-1])
                flag = 1
            else:
                zigzagVals.append(curVals)
                flag = 0

            curlevelNodes = nextlevelNodes

        return zigzagVals

if __name__ == '__main__':
    root = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    root.left = node9
    root.right = node20
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node20.left = node15
    node20.right = node7

    print Solution().zigzagLevelOrder(root)