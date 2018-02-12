# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-12
Function: 二叉搜索树转换成一个排序的双向链表.
         要求不能创建任何新的结点，只能调整树中结点指针的指向。

         非递归版--解题思路：
            1.核心是中序遍历的非递归算法。
            2.修改当前遍历节点与前一遍历节点的指针指向。
"""
class BTNode(object):
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None

def convertBSTreeToDouLList(root):
    """
    递归版（左/根/右）--算法思路：
        1.将左子树构造成双链表，并返回链表头节点。
        2.定位至左子树双链表最后一个节点。
        3.如果左子树链表不为空的话，将当前root追加到左子树链表。
        4.将右子树构造成双链表，并返回链表头节点。
        5.如果右子树链表不为空的话，将该链表追加到root节点之后。
        6.根据左子树链表是否为空确定返回的节点。
    :param root:
    :return:
    """
    if root == None:
        return None

    if root.lchild == None and root.rchild == None:
        return root

    left = convertBSTreeToDouLList(root.lchild)
    tmp = left

    while tmp != None and tmp.rchild != None:
        tmp = tmp.rchild

    if left != None:
        tmp.rchild = root
        root.lchild = tmp

    right = convertBSTreeToDouLList(root.rchild)

    if right != None:
        right.lchild = root
        root.rchild = right

    if left != None:
        return left
    else:
        return root

if __name__ == '__main__':
    # Create a BinarySearchTree
    root = BTNode(10)
    node_6 = BTNode(6)
    node_14 = BTNode(14)
    node_4 = BTNode(4)
    node_8 = BTNode(8)
    node_12 = BTNode(12)
    node_16 = BTNode(16)
    root.lchild = node_6
    root.rchild = node_14
    node_6.lchild = node_4
    node_6.rchild = node_8
    node_14.lchild = node_12
    node_14.rchild = node_16

    # Check function correct or not
    print convertBSTreeToDouLList(root).rchild.rchild.rchild.rchild.lchild.val