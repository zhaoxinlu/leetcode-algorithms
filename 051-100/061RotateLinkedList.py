# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-27
算法思想：链表右移k位
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1
        k %= length

        if k == 0:
            return head

        tmp = head
        for i in range(length-k-1):
            tmp = tmp.next

        nhead = tmp.next
        tmp.next = None
        last.next = head

        return nhead

if __name__ == '__main__':
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print Solution().rotateRight(head, 7).val