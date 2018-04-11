# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：链表排序--归并思想O(nlogn)
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        mid = self.midOfLists(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)

        return self.mergeLists(left, right)

    def midOfLists(self, head):
        if not head:
            return head

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode(0)
        l3 = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
                l3 = l3.next
            else:
                l3.next = l2
                l2 = l2.next
                l3 = l3.next

        if l1:
            l3.next = l1
        if l2:
            l3.next = l2

        return dummy.next