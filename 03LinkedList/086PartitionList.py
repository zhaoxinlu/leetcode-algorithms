# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：划分链表
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head

        small = ListNode(0)
        s = small
        large = ListNode(0)
        l = large

        while head:
            if head.val < x:
                s.next = head
                s = s.next
            else:
                l.next = head
                l = l.next
            head = head.next

        s.next = large.next
        l.next = None

        return small.next