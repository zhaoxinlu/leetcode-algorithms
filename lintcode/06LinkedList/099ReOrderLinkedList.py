# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-09
算法思想： 重排链表，1-->n-->2-->n-1...
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
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        """
        1. 获取中间节点;
        2. 后半段链表逆序;
        3. 合并前后半段链表。
        :param head:
        :return:
        """
        if not head or head.next == None:
            return head

        midNode = self.middleList(head)
        nheadNode = self.reverseList(midNode.next)
        midNode.next = None
        dummy = self.mergeList(head, nheadNode)

        return dummy

    def middleList(self, head):
        if not head:
            return head

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head):
        if not head or head.next == None:
            return head

        preNode = None
        curNode = head
        nhead = None

        while curNode:
            nextNode = curNode.next

            if nextNode == None:
                nhead = curNode

            curNode.next = preNode

            preNode = curNode
            curNode = nextNode

        return nhead

    def mergeList(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        l3 = ListNode(0)
        tmp = l3

        while l1 and l2:
            tmp.next = l1
            l1 = l1.next
            tmp = tmp.next

            tmp.next = l2
            l2 = l2.next
            tmp = tmp.next

        if l1:
            tmp.next = l1

        if l2:
            tmp.next = l2

        return l3.next

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

    print Solution().reorderList(head).next.next.val