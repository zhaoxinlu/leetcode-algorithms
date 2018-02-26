# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-26
Function: 第一个只出现一次的字符
"""
def FirstNotRepeatingChar(s):
    numDic = {}

    for i in range(0, len(s)):
        if s[i] in numDic:
            numDic[s[i]] += 1
        else:
            numDic[s[i]] = 1

    for i in range(len(s)):
        if numDic[s[i]] == 1:
            return s[i]

if __name__ == '__main__':
    print FirstNotRepeatingChar('abaccdeff')