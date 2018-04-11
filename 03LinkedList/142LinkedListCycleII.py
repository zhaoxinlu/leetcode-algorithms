# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：快慢指针找链表环的入口,没有返回None
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next == None:
            return None

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if fast == None or fast.next == None:
            return None
        else:
            inner = slow
            tmp = head
            while tmp != inner:
                inner = inner.next
                tmp = tmp.next

            return tmp