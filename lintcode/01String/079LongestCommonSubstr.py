# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-05
算法思想： 最长公共子串--动态规划
"""
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        # write your code here
        if len(A) == 0 or len(B) == 0:
            return 0

        maxLen = 0
        dp = [[0] * len(B) for i in range(len(A))]
        # dp[i][j]表示以i结尾的字符串str1[i]与j结尾的字符串str2[j]的公共连续子串的长度

        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                    maxLen = max(maxLen, dp[i][j])

        return maxLen

if __name__ == '__main__':
    A = 'ABCD'
    B = 'CBCEBCDG'
    print Solution().longestCommonSubstring(A, B)