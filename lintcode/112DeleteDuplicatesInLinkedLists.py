# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-08
算法思想： 删除链表重复元素
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
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        curNode = head

        while curNode != None and curNode.next != None:
            if curNode.val != curNode.next.val:
                curNode = curNode.next
            else:
                curNode.next = curNode.next.next

        return head
