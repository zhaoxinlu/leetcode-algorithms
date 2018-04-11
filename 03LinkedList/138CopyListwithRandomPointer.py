# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：复制复杂链表
"""
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        head = self.copyNodes(head)
        head = self.copyRandom(head)
        return self.resolveLists(head)

    def copyNodes(self, head):
        if not head:
            return

        cur = head

        while cur:
            cloneNode = RandomListNode(cur.label)
            cloneNode.next = cur.next
            cloneNode.random = None

            cur.next = cloneNode
            cur = cloneNode.next

        return head

    def copyRandom(self, head):
        if not head:
            return

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next

            cur = cur.next.next

        return head

    def resolveLists(self, head):
        nhead = None
        cur = head
        cloneNode = None

        if cur:
            cloneNode = cur.next
            nhead = cur.next
            cur.next = cloneNode.next
            cur = cur.next

        while cur:
            cloneNode.next = cur.next
            cloneNode = cloneNode.next
            cur.next = cloneNode.next
            cur = cur.next

        return nhead