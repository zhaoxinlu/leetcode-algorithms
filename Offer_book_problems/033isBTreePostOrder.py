# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-30
Function: 判断序列是不是某二叉搜索树的后序遍历
"""
def isPostOrderOfBTree(lists):
    """
    判断序列是不是某二叉搜索树的后序遍历
    :param lists:
    :return: True or False
    """
    length = len(lists)
    if length <= 0 or lists == None:
        return False

    rootVal = lists[length-1]

    i = 0
    for i in range(length-1):
        if lists[i] > rootVal:
            break

    for j in range(i, length-1):
        if lists[j] < rootVal:
            return False

    left = True
    if i > 0:
        left = isPostOrderOfBTree(lists[0:i])

    right = True
    if i < length-1:
        right = isPostOrderOfBTree(lists[i:length-1])

    return left and right

if __name__ == '__main__':
    lists = [5, 7, 6, 9, 11, 10, 8]
    print isPostOrderOfBTree(lists)