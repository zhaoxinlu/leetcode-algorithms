# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-20
算法思想： 单词拆分--动态规划
"""
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if len(dict) == 0:
            return len(s) == 0

        lenS = len(s)
        dp = [False] * (lenS+1)
        dp[0] = True

        maxLength = max([len(w) for w in dict])
        for i in range(1, lenS+1):
            for j in range(1, min(i, maxLength) + 1):
                if not dp[i-j]:
                    continue
                if s[i-j:i] in dict:
                    dp[i] = True
                    break

        return dp[lenS]

    def wordBreak_nn(self, s, dict):
        # 超时解法
        if len(dict) == 0:
            return len(s) == 0

        lenS = len(s)
        dp = [False] * (lenS+1)
        dp[0] = True

        for i in range(1, lenS+1):
            for j in range(i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
                    break

        return dp[lenS]

if __name__ == '__main__':
    s = 'lintcode'
    dict = ['lint', 'code']
    print Solution().wordBreak(s, dict)