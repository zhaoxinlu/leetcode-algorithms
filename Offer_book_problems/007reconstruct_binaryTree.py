# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-23
Function: 重建二叉树
"""
class BTNode(object):
    def __init__(self, elem, lchild, rchild):
        """
        初始化树节点
        :param elem:
        :param lchild:
        :param rchild:
        """
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


def Reconstruct_BTree(preOrder, inOrder):
    """
    输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
        假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
    :param preOrder: 前序遍历list
    :param inOrder: 中序遍历list
    :return: tree root
    """
    if len(preOrder) <= 0 or len(inOrder) <= 0:
        return None

    root_elem = preOrder[0]
    for i in range(len(inOrder)):
        if inOrder[i] == root_elem:
            break
    # 递归构造左子树/右子树
    left = Reconstruct_BTree(preOrder[1:i+1], inOrder[:i])
    right = Reconstruct_BTree(preOrder[i+1:], inOrder[i+1:])
    return BTNode(root_elem, left, right)

if __name__ == '__main__':
    preOrder = [1, 2, 4, 7, 3, 5, 6, 8]
    inOrder = [4, 7, 2, 1, 5, 3, 8, 6]
    root = Reconstruct_BTree(preOrder=preOrder, inOrder=inOrder)
    print root.lchild.elem # 2
    print root.rchild.rchild.lchild.elem # 8