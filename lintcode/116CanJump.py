# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-07
算法思想： 跳跃游戏
"""
class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        i = 0
        curSum = 0

        while i <= curSum:
            curSum = max(curSum, i+A[i])
            i += 1
            if curSum >= len(A)-1:
                return True

        return False

if __name__ == '__main__':
    A = [2, 3, 1, 0, 4]
    print Solution().canJump(A)