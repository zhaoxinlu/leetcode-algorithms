# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：奇偶链表
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummyOdd = ListNode(0)
        dummyEven = ListNode(0)
        odd = dummyOdd
        even = dummyEven
        cur = head
        pos = 1

        while cur:
            if pos % 2 == 1:
                odd.next = cur
                odd = odd.next
                pos += 1
            else:
                even.next = cur
                even = even.next
                pos += 1
            cur = cur.next

        even.next = None
        odd.next = dummyEven.next
        return dummyOdd.next