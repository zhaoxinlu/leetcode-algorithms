# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-26
Function: 两个链表的第一个公共节点
"""
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next_ = None

def getListLength(headNode):
    length = 0
    pNode = headNode

    while pNode != None:
        length += 1
        pNode = pNode.next_

    return length

def findFirstCommonNode(headNode1, headNode2):
    nLength1 = getListLength(headNode1)
    nLength2 = getListLength(headNode2)

    nLengthDif = nLength1 - nLength2
    headLongList = headNode1
    headShortList = headNode2
    if nLength2 > nLength1:
        headLongList = headNode2
        headShortList = headNode1
        nLengthDif = nLength2 - nLength1
    # 先长链表走几步
    for i in range(nLengthDif):
        headLongList = headLongList.next_
    # 再两链表同时遍历
    while headLongList != None and headShortList != None and headLongList != headShortList:
        headLongList = headLongList.next_
        headShortList = headShortList.next_

    pFirstCommonNode = headLongList

    return pFirstCommonNode