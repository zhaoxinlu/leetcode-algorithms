# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：两个链表的公共节点
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headB or not headA:
            return None

        length1 = self.getLengthOfLists(headA)
        length2 = self.getLengthOfLists(headB)
        lenDiff = length1 - length2
        LongHead = headA
        ShortHead = headB
        if length1 < length2:
            lenDiff = length2 - length1
            LongHead = headB
            ShortHead = headA

        for i in range(lenDiff):
            LongHead = LongHead.next

        while LongHead and ShortHead and LongHead != ShortHead:
            LongHead = LongHead.next
            ShortHead = ShortHead.next

        return LongHead


    def getLengthOfLists(self, head):
        if not head:
            return 0
        if not head.next:
            return 1
        length = 0
        while head:
            length += 1
            head = head.next

        return length