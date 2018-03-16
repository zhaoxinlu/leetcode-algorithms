# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-02
算法思想： 交叉字符串
    动态规划，dp[i][j]表示s1前i个字符与s2前j个字符能否组成s3前i+j个字符
"""
class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        len_1 = len(s1)
        len_2 = len(s2)
        len_3 = len(s3)

        if len_1 + len_2 != len_3:
            return False

        dp = [[False for i in range(len_2+1)] for j in range(len_1+1)]
        dp[0][0] = True
        # dp[i][j]表示s1前i个字符与s2前j个字符能否组成s3前i+j个字符
        # s1前i个与s2前0个能否构成s3前i个
        for i in range(1, len_1+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = True
        # s1前0个与s2前j个能否构成s3前j个
        for j in range(1, len_2+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = True
        # s1前i个与s2前j个能否构成s3前i+j个（i>=1,j>=1）
        for i in range(1, len_1+1):
            for j in range(1, len_2+1):
                if s3[i+j-1] == s1[i-1] and s3[i+j-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif s3[i+j-1] == s1[i-1]:
                    dp[i][j] = dp[i-1][j]
                elif s3[i+j-1] == s2[j-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = False

        return dp[len_1][len_2]

if __name__ == '__main__':
    s1 = 'aabcc'
    s2 = 'dbbca'
    s3 = 'aadbbcbcac'
    print Solution().isInterleave(s1, s2, s3)