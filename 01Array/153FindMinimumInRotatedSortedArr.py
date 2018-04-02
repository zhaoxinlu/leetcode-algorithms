# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-02
算法思想：旋转数组的最小值
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

        while nums[left] > nums[right]:
            if left + 1 == right:
                return nums[right]

            mid = left + (right - left) / 2
            if nums[mid] > nums[left]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid

        return nums[left]

if __name__ == '__main__':
    nums = [3, 1, 2]
    print Solution().findMin(nums)