# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-10
算法思想： 链表相加
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
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        # write your code here
        nhead = ListNode(0)
        tmp = nhead
        flag = 0

        while True:
            if l1:
                flag += l1.val
                l1 = l1.next

            if l2:
                flag += l2.val
                l2 = l2.next

            tmp.val = flag % 10
            flag = flag / 10

            if l1 or l2 or flag != 0:
                tmp.next = ListNode(0)
                tmp = tmp.next
            else:
                break

        return nhead