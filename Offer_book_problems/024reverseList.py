# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-29
Function: 反转单链表
"""
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next_ = None

def ReverseList_nonrecurse(pListHead):
    """
    非递归反转链表，三个指针 pre/cur/next.
    :param pListHead:
    :return:
    """
    if pListHead == None or pListHead.next_ == None:
        return pListHead

    preNode = None
    curNode = pListHead
    reverseListHead = None

    while curNode != None:
        nextNode = curNode.next_

        if nextNode == None:
            reverseListHead = curNode

        curNode.next_ = preNode

        preNode = curNode
        curNode = nextNode

    return reverseListHead

def ReverseList_recurse(head):
    """
    :param head:
    :return:
    """
    if head == None or head.next_ == None:
        return head
    else:
        newHead = ReverseList_recurse(head.next_)
        head.next_.next_ = head
        head.next_ = None

        return newHead

if __name__ == '__main__':
    pheadNode = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3)
    p3 = ListNode(4)
    pheadNode.next_ = p1
    p1.next_ = p2
    p2.next_ = p3

    print "原始链表如下："
    p = pheadNode
    while p:
        print p.val
        p = p.next_

    print "非递归反转链表后如下："
    pNode = ReverseList_nonrecurse(pheadNode)
    while pNode:
        print pNode.val
        pNode = pNode.next_