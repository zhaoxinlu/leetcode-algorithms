# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-03
算法思想： 比较字符串
"""
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        # write your code here
        dictA = {}
        for i in range(len(A)):
            if A[i] in dictA:
                dictA[A[i]] += 1
            else:
                dictA[A[i]] = 1

        for j in range(len(B)):
            if B[j] in dictA:
                dictA[B[j]] -= 1
                if dictA[B[j]] < 0:
                    return False
            else:
                return False

        return True

if __name__ == '__main__':
    A = 'ABCD'
    B = 'AACD'
    print Solution().compareStrings(A, B)