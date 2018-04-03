# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-03
算法思想：二叉树的后序遍历--递归与非递归
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        效仿先序遍历的非递归实现：
            先根，后右，再左，逆序输出即为后序序列
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        postVal = []
        nodes = [root]

        while nodes:
            node = nodes.pop()
            postVal.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return postVal[::-1]

    def postOrder_Digui(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        postVal = [root.val]
        left = self.postOrder_Digui(root.left)
        right = self.postOrder_Digui(root.right)

        return left+right+postVal

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

    print Solution().postorderTraversal(root)
    print Solution().postOrder_Digui(root)