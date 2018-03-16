# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-04
算法思想： 前序/中序重建二叉树
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
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if len(preorder) <= 0 or len(inorder) <= 0:
            return None
        root = TreeNode(preorder[0])

        for i in range(len(inorder)):
            if inorder[i] == root.val:
                break

        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return root

if __name__ == '__main__':
    preorder = [2, 1, 3]
    inorder = [1, 2, 3]

    print Solution().buildTree(preorder, inorder).left.val