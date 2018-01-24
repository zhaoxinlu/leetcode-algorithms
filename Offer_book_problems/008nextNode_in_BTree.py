# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-23
Function: 二叉树的下一节点
"""
class BTLinkNode(object):
    def __init__(self, elem, lchild=None, rchild=None, parent=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild
        self.parent = parent

def getBTreeNextNode(pNode):
    """
    给定一棵二叉树和其中一个节点，找出中序遍历序列的下一个节点
    :param pNode: 给定节点
    :return: 该节点下一个节点
    """
    if pNode == None:
        return None
    if pNode.rchild != None:
        tmpNode = pNode.rchild
        while tmpNode.lchild:
            tmpNode = tmpNode.lchild
        return tmpNode
    else:
        if pNode.parent == None:
            return
        elif pNode.parent.lchild == pNode:
            return pNode.parent
        else:
            while pNode.parent:
                if pNode.parent.lchild and pNode.parent.lchild == pNode:
                    return pNode.parent
                pNode = pNode.parent

            return None