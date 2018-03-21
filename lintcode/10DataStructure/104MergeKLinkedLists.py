# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-21
算法思想： 合并k个排序链表--分治,时间复杂度为O(nklogk)
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
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if lists == None or len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        start = 0
        end = len(lists)-1
        # 将lists的头和尾进行归并，然后将结果存放在头，头向后移动，尾向前移动，直到begin=end,则已经归并了一半，此时将begin=0,继续归并
        while end > 0:
            start = 0
            while start < end:
                lists[start] = self.merge2Lists(lists[start], lists[end])
                start += 1
                end -= 1

        return lists[0]

    def merge2Lists(self, head1, head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1

        dummy = ListNode(0)
        head3 = dummy

        while head1 and head2:
            if head1.val <= head2.val:
                head3.next = head1
                head1 = head1.next
            else:
                head3.next = head2
                head2 = head2.next
            head3 = head3.next

        while head1:
            head3.next = head1
            head1 = head1.next
            head3 = head3.next

        while head2:
            head3.next = head2
            head2 = head2.next
            head3 = head3.next

        return dummy.next