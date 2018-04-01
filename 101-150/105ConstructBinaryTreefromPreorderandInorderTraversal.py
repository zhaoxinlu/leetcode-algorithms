# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-01
算法思想：先序序列与中序序列重构二叉树--递归
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) <= 0 or len(inorder) <= 0:
            return None

        root = TreeNode(preorder[0])
        for idx in range(len(inorder)):
            if inorder[idx] == root.val:
                break

        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])

        return root

if __name__ == '__main__':
    preOrder = [3, 9, 20, 15, 7]
    inOrder = [9, 3, 15, 20, 7]
    print Solution().buildTree(preOrder, inOrder).right.val