# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：链表反转
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre = None
        cur = head
        nhead = None

        while cur:
            net = cur.next
            if not net:
                nhead = cur

            cur.next = pre

            pre = cur
            cur = net

        return nhead