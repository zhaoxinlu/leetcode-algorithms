# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-05
算法思想： 最长公共前缀--以第一个字符串做基准
"""
class Solution:
    """
    @param: strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs:
            return ""

        if len(strs) < 2:
            return strs[0]

        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if not strs[i]:
                    return ""
                elif strs[0][j] != strs[i][j]:
                    return strs[0][:j]

        return strs[0]

if __name__ == '__main__':
    strs = ["ABCD", "ABDE", "AB", "ABCEFG"]
    print Solution().longestCommonPrefix(strs)