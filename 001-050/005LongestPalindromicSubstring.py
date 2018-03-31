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
        lenS = len(s)
        self.maxLen = 0 # 记录最长子回文串的长度
        self.start = 0 # 记录最长子回文串的起始位置
        if lenS < 2:
            return s
        for i in range(lenS):
            self.searchPalindromic(s, i, i) # 回文子串是奇数的情况 bab
            self.searchPalindromic(s, i, i+1) # 回文子串是偶数的情况 baab

        return s[self.start:self.start+self.maxLen]

    def searchPalindromic(self, s, i, j):
        while i>=0 and j<len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        if self.maxLen < j-i-1:
            self.maxLen = j-i-1
            self.start = i+1

if __name__ == '__main__':
    print Solution().longestPalindrome("babad")