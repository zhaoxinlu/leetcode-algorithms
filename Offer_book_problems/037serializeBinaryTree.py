# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-12
Function: 序列化与反序列化二叉树
"""
class BTNode(object):
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None

def serializeBinaryTree(root):
    """
    前序遍历，序列化二叉树
    :param root:
    :return:
    """
    def preOrderBTree(root):
        if root:
            result.append(str(root.val))
            preOrderBTree(root.lchild)
            preOrderBTree(root.rchild)
        else:
            result.append('#')

    result = []
    preOrderBTree(root)
    return ','.join(result)

def deserializeBinaryTree(s):
    s = s.split(',')

if __name__ == '__main__':
    root = BTNode(1)
    node_2 = BTNode(2)
    node_3 = BTNode(3)
    node_4 = BTNode(4)
    node_5 = BTNode(5)
    node_6 = BTNode(6)
    root.lchild = node_2
    root.rchild = node_3
    node_2.lchild = node_4
    node_3.lchild = node_5
    node_3.rchild = node_6

    print serializeBinaryTree(root)