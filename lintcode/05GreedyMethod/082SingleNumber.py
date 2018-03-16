# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-04
算法思想： 落单的数--异或（位运算）
"""
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        result = A[0]

        for i in range(1, len(A)):
            result = result ^ A[i]

        return result

if __name__ == '__main__':
    A = [1, 2, 2, 3, 1, 4, 3]
    print Solution().singleNumber(A)