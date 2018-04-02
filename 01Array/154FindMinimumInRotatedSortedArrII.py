# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-02
算法思想：旋转数组的最小值II
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 0:
            return 0

        left = 0
        right = len(nums)-1

        while nums[left] >= nums[right]:
            if left+1==right:
                return nums[right]

            mid = left + (right-left) / 2
            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                return min(nums)

            if nums[mid] <= nums[right]:
                right = mid
            elif nums[mid] >= nums[left]:
                left = mid

        return nums[left]