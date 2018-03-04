# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-04
算法思想： 二叉树的中序遍历
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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []

        inVal = [root.val]
        lchildVal = self.inorderTraversal(root.left)
        rchildVal = self.inorderTraversal(root.right)

        return lchildVal+inVal+rchildVal

    def inOrder_no_digui(self, root):
        if not root:
            return []

        nodes = []
        inVals = []
        curNode = root

        while nodes or curNode:
            while curNode:
                nodes.append(curNode)
                curNode = curNode.left

            curNode = nodes.pop()
            inVals.append(curNode.val)
            curNode = curNode.right

        return inVals

if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root.right = node2
    node2.left = node3

    print Solution().inorderTraversal(root)
    print Solution().inOrder_no_digui(root)