# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-09
算法思想： 右旋转链表--快慢指针
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
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        # write your code here
        if head == None or head.next == None or k <= 0:
            return head

        tmp = head
        length = 1
        while tmp.next:
            tmp = tmp.next
            length += 1

        k = k % length
        if k == 0:
            return head

        slow, fast = head, head
        for i in range(k):
            if fast.next:
                fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        nhead = slow.next
        slow.next = None
        fast.next = head

        return nhead

if __name__ == '__main__':
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print Solution().rotateRight(head, 5).val