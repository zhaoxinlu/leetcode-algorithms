# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-29
Function: 输入一个链表，输出该链表中倒数第k个结点。
"""
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next_ = None

def FindKthToTail(pListHead, k):
    """
    遍历链表一次，前后两个指针
    :param pListHead:
    :param k:
    :return:
    """
    if pListHead == None or k <= 0:
        return None

    fontNode = pListHead
    behindNode = None

    for i in range(0, k-1):
        if fontNode.next_ != None:
            fontNode = fontNode.next_
        else:
            return None

    behindNode = pListHead
    while fontNode.next_ != None:
        fontNode = fontNode.next_
        behindNode = behindNode.next_

    return behindNode