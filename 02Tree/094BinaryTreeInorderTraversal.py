# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-03
算法思想：二叉树的中序遍历--递归与非递归
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        inVal = [root.val]
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left+inVal+right

    def inOrder_nonDigui(self, root):
        """
            1. 使用一个栈保存结点（列表实现）；
            2. 如果结点存在，入栈，然后将当前指针指向左子树，直到为空；
            3. 当前结点不存在，则出栈栈顶元素，并把当前指针指向栈顶元素的右子树；
            4. 栈不为空，循环2、3部。
        :param root:
        :return:
        """
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        nodes = []
        inVals = []
        curNode = root

        while curNode or nodes:
            while curNode:
                nodes.append(curNode)
                curNode = curNode.left
            if nodes:
                node = nodes.pop()
                inVals.append(node.val)
                curNode = node.right

        return inVals

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

    print Solution().inorderTraversal(root)
    print Solution().inOrder_nonDigui(root)