# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-02
算法思想：最大连续乘积--动态规划
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or nums == []:
            return 0

        if len(nums) == 1:
            return nums[0]

        maxLast = nums[0] # 连乘到上个元素的最大乘积
        minLast = nums[0] # 连乘到上个元素的最小乘积
        maxPro = nums[0] # 记录最大乘积，不断更新
        maxCur = 0 # 连乘到当前元素的最大乘积
        minCur = 0 # 连乘到当前元素的最小乘积

        for i in range(1, len(nums)):
            maxCur = max(nums[i], max(maxLast * nums[i], minLast * nums[i]))
            minCur = min(nums[i], min(maxLast * nums[i], minLast * nums[i]))
            maxLast = maxCur
            minLast = minCur
            maxPro = max(maxCur, maxPro)

        return maxPro

    def maxProduct_(self, nums):
        """
        Time Limit Exceeded
        :param nums:
        :return:
        """
        maxPro = -32768

        for i in range(len(nums)):
            tmp = 0
            for j in range(i, len(nums)):
                if j == i:
                    tmp = nums[i]
                else:
                    tmp *= nums[j]

                if tmp > maxPro:
                    maxPro = tmp

        return maxPro

if __name__ == '__main__':
    nums = [2, 3, -2, -8]
    print Solution().maxProduct(nums)