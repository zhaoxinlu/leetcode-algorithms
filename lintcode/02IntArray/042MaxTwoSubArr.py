# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-02
算法思想： 最大子数组II
"""
class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        length = len(nums)
        left = [0] * length
        right = [0] * length

        result = nums[0]
        Tsum = 0
        for i in range(0, length):
            Tsum += nums[i]
            result = max(Tsum, result)
            Tsum = max(Tsum, 0)
            left[i] = result

        result = nums[length-1]
        Tsum = 0
        for i in range(length-1, 0, -1):
            Tsum += nums[i]
            result = max(Tsum, result)
            Tsum = max(Tsum, 0)
            right[i] = result

        result = -2147483648
        for i in range(0, length-1):
            result = max(result, left[i]+right[i+1])

        return result

if __name__ == '__main__':
    nums = [1, 3, -1, 2, -1, 2]
    print Solution().maxTwoSubArrays(nums)