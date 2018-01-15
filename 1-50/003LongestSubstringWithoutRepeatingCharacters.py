# -*- coding: utf-8 -*-
"""
Given a string, find the length of the longest substring without repeating characters.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        numsDic = {}
        for i in range(len(s)):
            if s[i] in numsDic and start <= numsDic[s[i]]:
                start = numsDic[s[i]] + 1
            else:
                maxLength = max(maxLength, i-start+1)
            numsDic[s[i]] = i

        return maxLength

if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring('abcabcbb')