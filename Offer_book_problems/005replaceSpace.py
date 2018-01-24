# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-23
Function: 替换空格 ' ' -> '%20'
"""
def replaceSpace1(s):
    """
    创建新的字符串进行替换
    :param s:
    :return:
    """
    if type(s) != str:
        return False

    tmpS = ''
    for t in s:
        if t == ' ':
            tmpS += '%20'
        else:
            tmpS += t

    return tmpS

def replaceSpace2(s):
    """
    统计字符串中空格的个数, 利用指针插入字符串(从后插入)
    :param s:
    :return:
    """
    if not isinstance(s, str) or len(s) <= 0 or s == None:
        return False

    spaceNum = 0
    for st in s:
        if st == ' ':
            spaceNum += 1

    newStrLen = len(s) + spaceNum * 2
    newStr = [None] * newStrLen

    indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1
    while indexOfNew >= 0 and indexOfNew >= indexOfOriginal:
        if s[indexOfOriginal] == ' ':
            newStr[indexOfNew-2:indexOfNew+1] = ['%', '2', '0']
            indexOfNew -= 3
            indexOfOriginal -= 1
        else:
            newStr[indexOfNew] = s[indexOfOriginal]
            indexOfNew -= 1
            indexOfOriginal -= 1

    return ''.join(newStr)

if __name__ == '__main__':
    strs = 'We Are Happy!'
    print replaceSpace1(s=strs)
    print replaceSpace2(s=strs)