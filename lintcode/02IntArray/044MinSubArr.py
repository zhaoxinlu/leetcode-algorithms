# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-02
算法思想： 最小子数组
"""
class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        curSum = 0
        minSum = sum(nums)

        for i in range(len(nums)):
            curSum += nums[i]
            if curSum < minSum:
                minSum = curSum
            # 所以如果前面加起来的值大于0了，则舍弃前面的和，从下一位开始继续求和
            if curSum > 0:
                curSum = 0

        return minSum

if __name__ == '__main__':
    nums = [1, -1, -2, 2, -5]
    print Solution().minSubArray(nums)