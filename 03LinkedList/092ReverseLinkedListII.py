# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-11
算法思想：部分反转链表
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
            不妨拿出四本书，摞成一摞（自上而下为 A B C D），要让这四本书的位置完全颠倒过来（即自上而下为 D C B A）：
            盯住书A，每次操作把A下面的那本书放到最上面
            初始位置：自上而下为 A B C B
            第一次操作后：自上而下为 B A C D
            第二次操作后：自上而下为 C B A D
            第三次操作后：自上而下为 D C B A
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        for i in range(m-1):
            pre = pre.next

        cur = pre.next
        for i in range(n-m):
            nextNode = cur.next
            cur.next = nextNode.next
            nextNode.next = pre.next
            pre.next = nextNode

        return dummy.next

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

    print Solution().reverseBetween(head, 2, 4)