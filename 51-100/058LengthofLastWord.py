# -*- coding: utf-8 -*-
"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip() #去除两边空格

        if s == '':
            return 0
        if ' ' not in s:
            return len(s)

        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                return len(s)-1-i

if __name__ == '__main__':
    print Solution().lengthOfLastWord(' a b ')