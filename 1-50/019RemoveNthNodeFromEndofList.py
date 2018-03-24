# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-24
算法思想：双指针
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next

        if fast == None:
            return head.next

        while fast.next != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head