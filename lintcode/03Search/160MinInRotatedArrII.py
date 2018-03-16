# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： 寻找旋转排序数组的最小值II--可能存在重复元素
"""
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        left = 0
        right = len(nums) - 1
        mid = left

        while nums[left] >= nums[right]:
            if right-left == 1:
                mid = right
                break

            mid = left + (right-left) / 2
            if nums[mid] == nums[left] and nums[mid] == nums[left]:
                return self.minOrder(nums)
            if nums[mid] >= nums[left]:
                left = mid
            else:
                right = mid

        return nums[mid]

    def minOrder(self, nums):
        curMin = nums[0]

        for i in range(1, len(nums)):
            curMin = min(curMin, nums[i])

        return curMin

if __name__ == '__main__':
    nums = [1, 0, 1, 1, 1]
    print Solution().findMin(nums)
    print Solution().minOrder(nums)