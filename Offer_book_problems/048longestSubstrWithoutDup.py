# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-26
Function: 最长不含重复字符的子字符串
"""
def longestSubStrWithoutDuplication(str):
    curLength = 0
    maxLength = 0

    position = [-1] * 26

    for i in range(0, len(str)):
        preIndex = position[ord(str[i])-ord('a')]
        # ord(str[i])-ord('a') --> str[i]-'a'

        if preIndex < 0 or i - preIndex > curLength:
            curLength += 1
        else:
            if curLength > maxLength:
                maxLength = curLength

            curLength = i - preIndex

        position[ord(str[i])-ord('a')] = i

    if maxLength < curLength:
        maxLength = curLength

    return maxLength

if __name__ == '__main__':
    print longestSubStrWithoutDuplication('arabcacfr')