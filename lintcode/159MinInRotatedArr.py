# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： 寻找旋转排序数组的最小值--不存在重复元素
"""
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        left = 0
        right = len(nums)-1
        # mid = left

        while nums[left] >= nums[right]:
            if right-left == 1:
                #mid = right
                #break
                return nums[right]

            mid = left + (right-left) / 2
            if nums[mid] >= nums[left]:
                left = mid
            else:
                right = mid

        return nums[left]

if __name__ == '__main__':
    print Solution().findMin([4, 5, 6, 7])