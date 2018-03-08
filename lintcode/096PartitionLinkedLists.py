# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-08
算法思想： 划分链表--利用两个新链表
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
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        lowHead, highHead = ListNode(0), ListNode(0)
        lowTail, highTail = lowHead, highHead

        while head != None:
            if head.val < x:
                lowTail.next = head
                lowTail = lowTail.next
            else:
                highTail.next = head
                highTail = highTail.next
            head = head.next

        highTail.next = None
        lowTail.next = highHead.next
        return lowHead.next

if __name__ == '__main__':
    head = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(5)
    node6 = ListNode(2)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    print Solution().partition(head, 3).next.val