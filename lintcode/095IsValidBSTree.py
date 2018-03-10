# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-10
算法思想： 验证二叉搜索树--利用中序遍历特点 OR
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
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        if not root:
            return True

        inOrderVal = self.inOrderHelper(root)

        for i in range(1, len(inOrderVal)):
            if inOrderVal[i] <= inOrderVal[i-1]:
                return False

        return True

    def inOrderHelper(self, root):
        if not root:
            return []

        inOrderVal = [root.val]
        lchild = self.inOrderHelper(root.left)
        rchild = self.inOrderHelper(root.right)

        return lchild+inOrderVal+rchild