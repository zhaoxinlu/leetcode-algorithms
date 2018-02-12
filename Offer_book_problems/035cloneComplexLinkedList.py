# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-31
Function: 复杂链表的复制，不用辅助空间的情况下O(n)的时间效率
"""
class LLNode(object):
    def __init__(self, val):
        self.val = val
        self.next_ = None
        self.sibling = None

def cloneNodes(headNode):
    """
    第一步，复制链表所有节点，其中N'链接与N后面
    :param headNode:
    :return:
    """
    tmpNode = headNode

    while tmpNode != None:
        cloneNode = LLNode(tmpNode.val)
        cloneNode.next_ = tmpNode.next_
        cloneNode.sibling = None

        tmpNode.next_ = cloneNode
        tmpNode = cloneNode.next_

def cloneNodesSibling(headNode):
    """
    第二步，遍历链表，复制对应节点的sibling
    :param headNode:
    :return:
    """
    tmpNode = headNode

    while tmpNode != None:
        cloneNode = tmpNode.next_

        if tmpNode.sibling != None:
            cloneNode.sibling = tmpNode.sibling.next_

        tmpNode = cloneNode.next_

def resolveLinkedList(headNode):
    """
    第三步，拆分链表，奇数位置原链表，偶数位置为复制的链表
    :param headNode:
    :return:
    """
    tmpNode = headNode
    cloneHeadNd = None
    cloneNode = None

    if tmpNode != None:
        cloneHeadNd = cloneNode = tmpNode.next_
        tmpNode.next_ = cloneNode.next_
        tmpNode = tmpNode.next_

    while tmpNode != None:
        cloneNode.next_ = tmpNode.next_
        cloneNode = cloneNode.next_
        tmpNode.next_ = cloneNode.next_
        tmpNode = tmpNode.next_

    return cloneHeadNd

def cloneComplexLinkedList(headNode):
    """
    整合三个函数，复制复杂链表
    :param headNode:
    :return:
    """
    cloneNodes(headNode)
    cloneNodesSibling(headNode)

    return resolveLinkedList(headNode)