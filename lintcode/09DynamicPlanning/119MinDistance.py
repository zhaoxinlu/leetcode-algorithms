# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-16
算法思想： 编辑距离--动态规划
"""
class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        if word1 == None or word2 == None:
            return None

        length1 = len(word1)
        length2 = len(word2)
        dp = [[0] * (length2+1) for i in range(length1+1)]

        for i in range(1, length1+1):
            dp[i][0] = i

        for j in range(1, length2+1):
            dp[0][j] = j

        for i in range(1, length1+1):
            for j in range(1, length2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[length1][length2]

if __name__ == '__main__':
    w1 = 'mart'
    w2 = 'karma'
    print Solution().minDistance(w1, w2)