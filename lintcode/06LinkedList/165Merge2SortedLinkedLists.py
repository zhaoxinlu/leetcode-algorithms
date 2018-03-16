# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-08
算法思想： 合并两个排序链表
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
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if not l1:
            return l2
        if not l2:
            return l1

        tmp = ListNode(0)
        l3 = tmp
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

        while l1:
            l3.next = l1
            l1 = l1.next
            l3 = l3.next

        while l2:
            l3.next = l2
            l2 = l2.next
            l3 = l3.next

        return tmp.next