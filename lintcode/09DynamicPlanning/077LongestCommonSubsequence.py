# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-04
算法思想： 最长公共子序列LCS--动态规划
"""
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        Alen = len(A)
        Blen = len(B)

        if A == None or B == None or Alen == 0 or Blen == 0:
            return 0

        dp = [[0] * (Blen+1) for i in range(Alen+1)]

        for i in range(Alen):
            for j in range(Blen):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return dp[Alen][Blen]

if __name__ == '__main__':
    StrA = 'ABCD'
    StrB = 'EACB'
    print Solution().longestCommonSubsequence(StrA, StrB)