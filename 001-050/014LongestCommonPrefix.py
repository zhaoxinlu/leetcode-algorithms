# -*- coding: utf-8 -*-
"""
Write a function to find the longest common prefix string amongst an array of strings.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        s = strs[0]

        for i in range(len(s)):
            for str in strs[1:]:
                if len(str) <= i or str[i] != s[i]:
                    return strs[0][:i]

        return s

if __name__ == '__main__':
    strs = ['leets', 'leetcode', 'leet', 'leetts']
    print Solution().longestCommonPrefix(strs)