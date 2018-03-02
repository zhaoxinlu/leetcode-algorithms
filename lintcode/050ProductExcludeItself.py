# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-02
算法思想： 数组剔除元素后的乘积
"""
class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # write your code here
        if nums == None or len(nums) <= 1:
            B = [1]
            return B
        # result[i] = left[i] * right[i] ,left[i] = A[0]*A[1]***A[i-1]，right[i] = A[i+1]*A[i+2]***A[len(A)-1]
        left = [1] * len(nums)
        right = [1] * len(nums)
        B = []

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        for i in range(0, len(nums)):
            k = left[i] * right[i]
            B.append(k)

        return B

if __name__ == '__main__':
    nums = [1, 2, 3]
    print Solution().productExcludeItself(nums)