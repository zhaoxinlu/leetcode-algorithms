# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-04
算法思想： 二叉树的后序遍历
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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []

        postVal = [root.val]
        lchildVal = self.postorderTraversal(root.left)
        rchildVal = self.postorderTraversal(root.right)

        return lchildVal+rchildVal+postVal

if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root.right = node2
    node2.left = node3

    print Solution().postorderTraversal(root)