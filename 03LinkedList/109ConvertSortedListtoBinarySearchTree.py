# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：转换排序链表/数组到二叉搜索树
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        midPre = self.midPreOfLists(head)
        mid = midPre.next
        right = midPre.next.next
        midPre.next = None
        mid.next = None

        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right)
        return root

    def midPreOfLists(self, head):
        """
            qiu中间节点的前一个节点
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sortedArrayToBST(self, array):
        """
            排序数组-->BST
        :param array:
        :return:
        """
        if not array or len(array) < 1:
            return None
        if len(array) == 1:
            return TreeNode(array[0])

        length = len(array)
        root = TreeNode(array[length/2])
        root.left = self.sortedArrayToBST(array[:length/2])
        root.right = self.sortedArrayToBST(array[length/2+1:])

        return root

    def sortedListToBSTII(self, head):
        """
            先转换为数组
        :param head:
        :return:
        """
        if not head:
            return None
        array = []
        tmp = head
        while tmp:
            array.append(tmp.val)
            tmp = tmp.next
        return self.sortedArrayToBST(array)