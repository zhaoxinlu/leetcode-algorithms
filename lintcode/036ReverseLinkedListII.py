# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-02
算法思想： 翻转链表II，引入区间
"""
"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param: head: ListNode head is the head of the linked list
    @param: m: An integer
    @param: n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        preNode = dummy

        for i in range(1, m):
            preNode = preNode.next

        curNode = preNode.next
        for i in range(0, n-m):
            nextNode = curNode.next
            curNode.next = nextNode.next
            nextNode.next = preNode.next
            preNode.next = nextNode

        return dummy.next