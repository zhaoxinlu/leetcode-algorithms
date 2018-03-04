# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-04
算法思想： 二叉树的前序遍历
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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if root == None:
            return []

        result = [root.val]
        lchild = self.preorderTraversal(root.left)
        rchild = self.preorderTraversal(root.right)

        return result+lchild+rchild

    def preOrder_no_digui(self, root):
        if root == None:
            return []

        nodes = [root]
        preVal = []

        while nodes:
            curNode = nodes.pop()
            preVal.append(curNode.val)

            if curNode.right:
                nodes.append(curNode.right)

            if curNode.left:
                nodes.append(curNode.left)

        return preVal

if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root.right = node2
    node2.left = node3

    print Solution().preorderTraversal(root)
    print Solution().preOrder_no_digui(root)