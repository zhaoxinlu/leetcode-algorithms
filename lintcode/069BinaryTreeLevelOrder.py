# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-04
算法思想： 二叉树的层序遍历--按层次打印Tree OR 底层打印s
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
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if root == None:
            return []

        curLevelnodes = [root]
        leVals = []

        while curLevelnodes:
            leVals.append([pNode.val for pNode in curLevelnodes])
            # leVals.insert(0, [pNode.val for pNode in curLevelnodes]) 从底层打印
            nextLevelnodes = []

            for curNode in curLevelnodes:
                if curNode.left:
                    nextLevelnodes.append(curNode.left)
                if curNode.right:
                    nextLevelnodes.append(curNode.right)
            curLevelnodes = nextLevelnodes

        return leVals

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

    print Solution().levelOrder(root)