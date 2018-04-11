# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：链表节点值相加II
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

        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        while stack1 != [] and stack2 != []:
            add = stack1.pop() + stack2.pop() + carry
            tmp = ListNode(add % 10)
            carry = add / 10
            tmp.next = head
            head = tmp

        while stack1 != []:
            add = stack1.pop()+carry
            tmp = ListNode(add % 10)
            carry = add / 10
            tmp.next = head
            head = tmp

        while stack2 != []:
            add = stack2.pop() + carry
            tmp = ListNode(add % 10)
            carry = add / 10
            tmp.next = head
            head = tmp

        if carry == 1:
            tmp = ListNode(carry)
            tmp.next = head
            head = tmp

        return head