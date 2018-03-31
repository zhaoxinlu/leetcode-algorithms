# -*- coding: utf-8 -*-
"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        tmp = ListNode(0)
        l3 = tmp
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

        if l1:
            l3.next = l1
        else:
            l3.next = l2

        return tmp.next

if __name__ == '__main__':
    a1 = [1, 2, 3]
    a2 = [5, 6, 7]
    l1 = ListNode(a1[0])
    p1 = l1
    l2 = ListNode(a2[0])
    p2 = l2
    for i in a1[1:]:
        p1.next = ListNode(i)
        p1 = p1.next
    for j in a2[1:]:
        p2.next = ListNode(j)
        p2 = p2.next
    s = Solution()
    p = s.mergeTwoLists(l1, l2)