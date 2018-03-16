# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-08
算法思想： 删除链表中倒数第n个节点--利用双指针
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
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        nhead = ListNode(0)
        nhead.next = head
        tmp = nhead

        for i in range(n):
            head = head.next

        while head != None:
            head = head.next
            tmp = tmp.next

        tmp.next = tmp.next.next
        return nhead.next