# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-01
算法思想： 查找字符串
    对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。
"""
class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        # write your code here
        if source == None or target == None or len(source) < len(target):
            return -1

        if target == "":
            return 0

        for i in range(len(source)):
            if source[i] == target[0]:
                if len(source) - i < len(target):
                    return -1
                else:
                    l = 0
                    for j in range(len(target)):
                        if target[j] == source[i+j]:
                            l += 1
                        else:
                            break

                    if l == len(target):
                        return i

        return -1

if __name__ == '__main__':
    print Solution().strStr("abcdabcdefg", "bcd")