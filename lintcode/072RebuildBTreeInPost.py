# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-04
算法思想： 后序/中序重建二叉树
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
    @param: inorder: A list of integers that inorder traversal of a tree
    @param: postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        if len(inorder) <= 0 or len(postorder) <= 0:
            return None

        root = TreeNode(postorder[len(postorder)-1])

        for i in range(len(inorder)):
            if inorder[i] == root.val:
                break

        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])

        return root

if __name__ == '__main__':
    inOrder = [9, 3, 15, 20, 7]
    postOrder = [9, 15, 7, 20, 3]

    print Solution().buildTree(inOrder, postOrder).right.val