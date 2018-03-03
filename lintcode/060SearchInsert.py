# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-03
算法思想： 搜索插入位置
"""
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        left = 0

        while left < len(A):
            if A[left] >= target:
                return left
            else:
                left += 1

        return left

if __name__ == '__main__':
    A = [2, 3, 5, 7]
    target = 8
    print Solution().searchInsert(A, target)