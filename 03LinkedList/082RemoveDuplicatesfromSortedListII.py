# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-27
算法思想：排序链表去重复元素II
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        preNode = dummy
        curNode = head
        while curNode:
            while curNode.next and curNode.next.val == preNode.next.val:
                curNode = curNode.next

            if preNode.next == curNode:
                preNode = preNode.next
            else:
                preNode.next = curNode.next
            curNode = curNode.next

        return dummy.next