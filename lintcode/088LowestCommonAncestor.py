# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-05
算法思想： 二叉树最低公共祖先
    从根节点开始遍历，如果node1和node2中的任一个和root匹配，那么root就是最低公共祖先。
    如果都不匹配，则分别递归左、右子树，如果有一个 节点出现在左子树，并且另一个节点出现在右子树，则root就是最低公共祖先.
    如果两个节点都出现在左子树，则说明最低公共祖先在左子树中，否则在右子树。
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root == None:
            return None

        if root is A or root is B:
            return root

        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)

        if left != None and right != None:
            return root
        if left != None:
            return left
        return right