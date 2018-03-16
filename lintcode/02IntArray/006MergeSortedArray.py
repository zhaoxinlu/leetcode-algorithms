# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-28
算法思想：
    合并排序数组
"""
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        C = []
        lenA = len(A)
        lenB = len(B)

        i = j = 0
        while i < lenA and j < lenB:
            if A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1

        while i < lenA:
            C.append(A[i])
            i += 1

        while j < lenB:
            C.append(B[j])
            j += 1

        return C

if __name__ == '__main__':
    A = [1, 2, 3, 4]
    B = [2, 4, 5, 6]
    print Solution().mergeSortedArray(A, B)