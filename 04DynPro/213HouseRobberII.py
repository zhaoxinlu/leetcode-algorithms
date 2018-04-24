# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-24
Function: 房屋抢劫II--动态规划
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(self.robsub(nums, 0, len(nums)-2), self.robsub(nums, 1, len(nums)-1))

    def robsub(self, nums, left, right):
        dp = [0] * (right-left+1)
        dp[0] = nums[left]
        dp[1] = max(nums[left], nums[left+1])
        for i in range(2, right-left+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[left+i])
        return dp[right-left]

if __name__ == '__main__':
    nums = [4, 3, 1, 1, 1]
    print Solution().rob(nums)