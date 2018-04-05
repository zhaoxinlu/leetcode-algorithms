# -*- coding: utf-8 -*-
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        curP = head
        nextP = head.next

        while nextP and curP:
            if nextP.val == curP.val:
                curP.next = nextP.next
            else:
                curP = curP.next
            nextP = nextP.next

        return head