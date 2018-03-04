# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-04
算法思想： 最长上升子序列--动态规划
"""
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if nums == None or len(nums) < 1:
            return 0

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

    def LIS_nLogn(self, nums):
        dp = [0] * (len(nums)+1)

        length = 1
        dp[1] = nums[0]

        for i in range(1, len(nums)):
            if dp[length] < nums[i]:
                length += 1
                dp[length] = nums[i]
            else:
                flag = self.LowerBound(dp, nums[i], 1, length+1)
                dp[flag] = nums[i]

        return length

    def LowerBound(self, nums, key, low, high):
        # 求最小下界的--nums中大于key的最小值
        while low < high:
            mid = (low + high) / 2
            if nums[mid] <= key:
                low = mid + 1
            else:
                high = mid

        return low

if __name__ == '__main__':
    nums = [4, 2, 4, 5, 3, 7]
    print Solution().longestIncreasingSubsequence(nums)
    print Solution().LIS_nLogn(nums)