# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： 两个字符串是变位词
"""
class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        sDict = {}
        for i in range(len(s)):
            if s[i] in sDict:
                sDict[s[i]] += 1
            else:
                sDict[s[i]] = 1

        for j in range(len(t)):
            if t[j] in sDict:
                sDict[t[j]] -= 1
                if sDict[t[j]] < 0:
                    return False
            else:
                return False

        for k in sDict.values():
            if k != 0:
                return False

        return True

if __name__ == '__main__':
    s = 'abcd'
    t = 'ab'
    print Solution().anagram(s, t)