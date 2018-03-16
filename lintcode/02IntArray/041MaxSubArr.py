# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-02
算法思想： 最大子数组、动态规划
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        result = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            if maxSum > 0:
                maxSum += nums[i]
            else:
                maxSum = nums[i]

            if result < maxSum:
                result = maxSum

        return result

if __name__ == '__main__':
    nums = [-2, 2, -3, 4, 2, -1, -5, 3]
    print Solution().maxSubArray(nums)