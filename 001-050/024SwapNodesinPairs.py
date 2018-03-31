# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-24
算法思想：将链表中的节点两两交换
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        preNode, curNode = dummy, head

        while curNode and curNode.next:
            nextNode = curNode.next
            preNode.next = nextNode
            curNode.next = nextNode.next
            nextNode.next = curNode

            preNode = curNode
            curNode = curNode.next

        return dummy.next