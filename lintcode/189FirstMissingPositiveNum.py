# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： 寻找丢失的第一个正整数--桶排序
"""
class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """
    def firstMissingPositive(self, A):
        # write your code here
        i = 0
        while i < len(A):
            while A[i] != i + 1:
                if A[i] <= 0 or A[i] > len(A) or A[i] == A[A[i]-1]:
                    break
                tmp = A[i]
                A[i] = A[tmp-1]
                A[tmp-1] = tmp
            i += 1

        for i in range(len(A)):
            if A[i] != i + 1:
                return i+1

        return len(A)+1

if __name__ == '__main__':
    A = [3, 4, 2, 1]
    print Solution().firstMissingPositive(A)