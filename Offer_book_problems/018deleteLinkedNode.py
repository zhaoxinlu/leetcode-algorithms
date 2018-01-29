# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-29
Function: 在O(1)时间内删除链表结点  && 删除排序链表中重复的节点(含重复值的节点全删除)
"""
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next_ = None

    def __del__(self):
        self.val = None
        self.next_ = None

def DeleteNode(pListHead, pToBeDeleted):
    """
    在O(1)时间内删除链表结点
    :param pListHead:
    :param pToBeDeleted:
    :return:
    """
    if not pListHead or not pToBeDeleted:
        return None

    if pToBeDeleted.next_ != None:
        # 要删除的节点后有节点
        pToBeDeleted.val = pToBeDeleted.next_.val
        pToBeDeleted.next_ = pToBeDeleted.next_.next_
        pToBeDeleted.next_.__del__()
    elif pToBeDeleted == pListHead:
        # 链表中只有一个节点
        pToBeDeleted.__del__()
        pListHead.__del__()
    else:
        # 要删除的节点后面没有节点
        tmpNode = pListHead
        while tmpNode.next_ != pToBeDeleted:
            tmpNode = tmpNode.next_
        tmpNode.next_ = None
        pToBeDeleted.__del__()

def DeleteDuplication(pListHead):
    """
    删除排序链表中重复的节点
    :param pListHead:
    :return:
    """
    if not pListHead or pListHead.next_ is None:
        return pListHead

    preNode = None
    curNode = pListHead
    while curNode != None:
        nextNode = curNode.next_
        flag = 0
        # flag=1表示重复节点
        if nextNode != None and nextNode.val == curNode.val:
            flag = 1

        if flag == 0:
            preNode = curNode
            curNode = nextNode
        else:
            value = curNode.val
            ToBeDeletedNode = curNode
            while ToBeDeletedNode != None and ToBeDeletedNode.val == value:
                nextNode = ToBeDeletedNode.next_
                ToBeDeletedNode.__del__()
                ToBeDeletedNode = nextNode
            if preNode == None:
                pListHead = nextNode
            else:
                preNode.next_ = nextNode
            curNode = nextNode