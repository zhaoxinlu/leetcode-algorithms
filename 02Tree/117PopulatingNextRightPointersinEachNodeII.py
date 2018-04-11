# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：普通二叉树层结点连接
"""
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        """
            建立一个dummy结点来指向每层的首结点的前一个结点，然后指针t用来遍历这一层，实际上是遍历一层，然后连下一层的next;
            首先从根结点开始，如果左子结点存在，那么t的next连上左子结点，然后t指向其next指针；如果root的右子结点存在，那么t的next连上右子结点，然后t指向其next指针.
            此时root的左右子结点都连上了，此时root向右平移一位，指向其next指针，如果此时root不存在了，说明当前层已经遍历完了;
            重置t为dummy结点，root此时为dummy->next，即下一层的首结点，然后dummy的next指针晴空
        :param root:
        :return:
        """
        if not root:
            return
        dummy = TreeLinkNode(0)
        tmp = dummy
        while root:
            if root.left:
                tmp.next = root.left
                tmp = tmp.next
            if root.right:
                tmp.next = root.right
                tmp = tmp.next
            root = root.next
            if not root:
                root = dummy.next
                dummy.next = None
                tmp = dummy