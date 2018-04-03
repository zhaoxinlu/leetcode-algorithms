# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-03
算法思想：二叉树的前序遍历--递归与非递归
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        preVals = []
        nodes = [root]

        while nodes != []:
            node = nodes.pop()
            preVals.append(node.val)
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)

        return preVals

    def preOrder_Digui(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        preVals = [root.val]
        left = self.preOrder_Digui(root.left)
        right = self.preOrder_Digui(root.right)

        return preVals+left+right

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

    print Solution().preorderTraversal(root)
    print Solution().preOrder_Digui(root)