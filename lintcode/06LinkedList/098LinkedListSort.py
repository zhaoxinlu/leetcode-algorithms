# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-08
算法思想： 链表排序--归并排序（O(logn)）&&快速排序
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
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        """
        归并排序思想
        :param head:
        :return:
        """
        # write your code here
        if head == None or head.next == None:
            return head

        midNode = self.middleList(head)
        right = self.sortList(midNode.next)
        midNode.next = None
        left = self.sortList(head)

        return self.mergeList(left, right)

    def middleList(self, head):
        """
        快慢指针寻链表中间值
        :param head:
        :return:
        """
        if head == None:
            return None
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeList(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        tmp = ListNode(0)
        l3 = tmp

        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

        if l1:
            l3.next = l1
        if l2:
            l3.next = l2

        return tmp.next

if __name__ == '__main__':
    head = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(6)
    node5 = ListNode(5)
    node6 = ListNode(2)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    print Solution().sortList(head=head).next.next.val