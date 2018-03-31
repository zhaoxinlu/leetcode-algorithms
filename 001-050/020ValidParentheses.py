# -*- coding: utf-8 -*-
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = [None]
        par = {')': '(', '}': '{', ']': '['}
        for p in s:
            if p in par:
                if par[p] != tmp.pop():
                    return False
            else:
                tmp.append(p)
        return len(tmp) == 1

if __name__ == '__main__':
    print Solution().isValid('({}){}[]')