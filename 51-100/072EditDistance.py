# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-27
算法思想：编辑距离--动态规划
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        length1 = len(word1)
        length2 = len(word2)
        if length1 == 0:
            return length2
        if length2 == 0:
            return length1

        dp = [[0] * (length2+1) for i in range(length1+1)]
        #dp[i][j]表示word1前i个字符与word2前j个字符的距离
        for i in range(length1+1):
            dp[i][0] = i

        for j in range(length2+1):
            dp[0][j] = j

        for i in range(1, length1+1):
            for j in range(1, length2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[length1][length2]

if __name__ == '__main__':
    s1 = 'word1'
    s2 = 'word2'
    print Solution().minDistance(s1, s2)