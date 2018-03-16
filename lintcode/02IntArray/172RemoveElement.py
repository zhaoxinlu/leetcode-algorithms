# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： 删除元素
"""
class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        Alen = len(A)
        i = 0
        while i < Alen:
            if A[i] == elem:
                Alen -= 1
                del A[i]
            else:
                i += 1

        return Alen

if __name__ == '__main__':
    A = [0, 4, 4, 0, 0, 2, 4, 4]
    print Solution().removeElement(A, 4)