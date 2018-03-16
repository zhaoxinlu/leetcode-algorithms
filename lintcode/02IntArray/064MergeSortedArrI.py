# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-03
算法思想： 合并两个排序数组，B合入A
"""
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        total = m + n

        while m > 0 and n > 0:
            if A[m-1] > B[n-1]:
                A[total-1] = A[m-1]
                m -= 1
                total -= 1
            else:
                A[total-1] = B[n-1]
                n -= 1
                total -= 1

        while n > 0:
            A[total - 1] = B[n - 1]
            n -= 1
            total -= 1

        return A

if __name__ == '__main__':
    A = [1, 3, 5, 0, 0]
    B = [2, 4]
    print Solution().mergeSortedArray(A, 3, B, 2)