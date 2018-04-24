# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-24
Function: 房屋抢劫--动态规划
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 0:
            return 0

        length = len(nums)

        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        else:
            dp = [0] * length
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, length):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])

            return dp[length-1]

if __name__ == '__main__':
    nums = [4, 3, 1, 3, 2]
    print Solution().rob(nums)