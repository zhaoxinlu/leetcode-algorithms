# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：链表插入排序
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        cur = head
        while cur:
            pre = dummy
            while pre.next and pre.next.val < cur.val:
                pre = pre.next

            tmp = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = tmp

        return dummy.next