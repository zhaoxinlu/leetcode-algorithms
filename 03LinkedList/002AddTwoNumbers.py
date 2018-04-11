# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：链表节点值相加
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0
        dummy = ListNode(0)
        tmp = dummy
        while l1 and l2:
            tmp.next = ListNode((l1.val+l2.val+carry) % 10)
            carry = (l1.val+l2.val+carry) / 10
            l1 = l1.next
            l2 = l2.next
            tmp = tmp.next

        while l1:
            tmp.next = ListNode((l1.val+carry) % 10)
            carry = (l1.val+carry) / 10
            l1 = l1.next
            tmp = tmp.next

        while l2:
            tmp.next = ListNode((l2.val+carry) % 10)
            carry = (l2.val+carry) / 10
            l2 = l2.next
            tmp = tmp.next

        if carry == 1:
            tmp.next = ListNode(carry)

        return dummy.next