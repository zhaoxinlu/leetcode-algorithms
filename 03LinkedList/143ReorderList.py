# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：链表重排序
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        midNode = self.midOfList(head)
        behindHead = self.reverseList(midNode.next)
        midNode.next = None
        head = self.mergeList(head, behindHead)

    def midOfList(self, head):
        if not head:
            return head

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head):
        if not head or not head.next:
            return head

        pre = None
        cur = head
        nhead = None

        while cur:
            nextNode = cur.next

            if cur.next == None:
                nhead = cur

            cur.next = pre
            pre = cur
            cur = nextNode

        return nhead

    def mergeList(self, head1, head2):
        if not head2:
            return head1

        if not head1:
            return head2

        dummy = ListNode(0)
        l3 = dummy
        while head1 and head2:
            l3.next = head1
            head1 = head1.next
            l3 = l3.next

            l3.next = head2
            head2 = head2.next
            l3 = l3.next

        if head1:
            l3.next = head1

        if head2:
            l3.next = head2

        return dummy.next