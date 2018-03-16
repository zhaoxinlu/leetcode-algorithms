# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-04
算法思想： 寻找峰值--二分查找
"""
class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if len(A) < 3:
            return False

        start = 1
        end = len(A) - 2

        while start <= end:
            mid = (start + end) / 2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] > A[mid-1]:
                start = mid + 1
            else:
                end = mid - 1

        return start

if __name__ == '__main__':
    nums = [1, 2, 1, 3, 4, 5, 7, 6]
    print Solution().findPeak(nums)