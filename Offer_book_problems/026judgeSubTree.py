# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-29
Function: 判断二叉树B是不是二叉树A的子结构
"""
class BTNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def Equal(num1, num2):
    """
    两个小数是否相等的判断方法
    :param num1:
    :param num2:
    :return:
    """
    if num1 - num2 > -0.0000001 and num1 - num2 < 0.0000001:
        return True
    else:
        return False

def HasSubtree(root1, root2):
    """
    查找根值相同的节点
    :param root1:
    :param root2:
    :return:
    """
    result = False

    if root1 != None and root2 != None:
        if Equal(root1.val, root2.val):
            result = DoesTree1HaveTree2(root1, root2)
        if not result:
            result = HasSubtree(root1.left, root2)
        if not result:
            result = HasSubtree(root1.right, root2)

    return result

def DoesTree1HaveTree2(root1, root2):
    """
    判断AB左右子树是否结构相同
    :param root1:
    :param root2:
    :return:
    """
    if root2 == None:
        return True

    if root1 == None:
        return False

    if not Equal(root1.val, root2.val):
        return False

    return DoesTree1HaveTree2(root1.left, root2.left) and DoesTree1HaveTree2(root1.right, root2.right)