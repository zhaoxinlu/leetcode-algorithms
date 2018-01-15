# -*-coding: utf-8 -*-
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length == 1:
            return s
        if length == 2:
            if s[0] == s[1]:
                return s
            return s[0]
        i = 0
        result = s[0]
        maxLength = 1
        while i < length:
            j = i + 1
            while j < length:
                if s[j] == s[i]:
                    j += 1
                else:
                    break
            k = 0



if __name__ == '__main__':
    print Solution().longestPalindrome()