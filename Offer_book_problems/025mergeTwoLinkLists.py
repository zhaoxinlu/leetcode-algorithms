# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-29
Function: 链表合并的递归实现
"""
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next_ = None

def Merge2LinkLists(lists1, lists2):
    """
    链表合并的递归实现
    :param lists1:
    :param lists2:
    :return:
    """
    if not lists1:
        return lists2
    if not lists2:
        return lists1

    l = None
    if lists1.val < lists2.val:
        l = lists1
        l.next_ = Merge2LinkLists(lists1.next_, lists2)
    else:
        l = lists2
        l.next_ = Merge2LinkLists(lists1, lists2.next_)

    return l

if __name__ == '__main__':
    pheadNode1 = ListNode(1)
    p1 = ListNode(3)
    p2 = ListNode(4)
    p3 = ListNode(7)
    pheadNode1.next_ = p1
    p1.next_ = p2
    p2.next_ = p3

    pheadNode2 = ListNode(2)
    p11 = ListNode(5)
    p22 = ListNode(6)
    p33 = ListNode(8)
    pheadNode2.next_ = p11
    p11.next_ = p22
    p22.next_ = p33

    p = Merge2LinkLists(pheadNode1, pheadNode2)
    while p:
        print p.val
        p = p.next_