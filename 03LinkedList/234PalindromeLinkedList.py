# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：判断是不是回文链表
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
            判断回文主要是前半部分和后半部分的比较，将后半部分反转（仍然是单链表），则可以方便的判断回文。
            时间 O(n)，空间O(1).
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        mid = self.midOfLists(head)
        bhead = self.reverseList(mid.next)
        mid.next = None

        while bhead:
            if head.val != bhead.val:
                return False
            head = head.next
            bhead = bhead.next
        return True


    def midOfLists(self, head):
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
            nextN = cur.next
            if cur.next == None:
                nhead = cur

            cur.next = pre
            pre = cur
            cur = nextN

        return nhead