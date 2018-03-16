# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-08
算法思想： 删除数字--贪心，若前面数>后面数，删除前面数
"""
class Solution:
    """
    @param: A: A positive integer which has N digits, A is a string
    @param: l: Remove k digits
    @return: A string
    """
    def DeleteDigits(self, A, l):
        # write your code here
        A = list(A)
        for i in range(l):
            flag = 1
            for j in range(len(A)-1):
                if A[j] > A[j+1]:
                    del A[j]
                    flag = 0
                    break

            if flag == 1 and len(A)>1:
                A.pop(-1)

        while len(A) > 1 and A[0] == '0':
            del A[0]

        return ''.join(A)

if __name__ == '__main__':
    print Solution().DeleteDigits('1557768', 1)