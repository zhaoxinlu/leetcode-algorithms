# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-09
算法思想： 复制带随机指针的链表
"""
"""
Definition for singly-linked list with a random pointer.
"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        """
        1. 复制每个节点，位于其后;
        2. 复制对应节点的random指针
        3. 拆分链表，返回克隆链表的头节点
        :param head:
        :return:
        """
        head = self.cloneNodes(head)
        head = self.cloneNodeRandom(head)
        return self.resolveListNode(head)

    def cloneNodes(self, head):
        tmpNode = head
        while tmpNode:
            nNode = RandomListNode(tmpNode.label)
            nNode.next = tmpNode.next
            nNode.random = None

            tmpNode.next = nNode
            tmpNode = nNode.next

        return head

    def cloneNodeRandom(self, head):
        tmpNode = head
        while tmpNode:
            if tmpNode.random:
                tmpNode.next.random = tmpNode.random.next

            tmpNode = tmpNode.next.next

        return head

    def resolveListNode(self, head):
        dummy = RandomListNode(0)
        tmpNode = head
        copyNode = None

        if tmpNode != None:
            copyNode = tmpNode.next
            dummy.next = tmpNode.next
            tmpNode.next = copyNode.next
            tmpNode = tmpNode.next

        while tmpNode:
            copyNode.next = tmpNode.next
            copyNode = copyNode.next
            tmpNode.next = copyNode.next
            tmpNode = tmpNode.next

        return dummy.next