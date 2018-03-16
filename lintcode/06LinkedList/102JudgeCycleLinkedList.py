# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-09
算法思想： 是否带环链表--快慢指针
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
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if not head or head.next == None:
            return False

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False

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
    # node5.next = node2

    print Solution().hasCycle(head)