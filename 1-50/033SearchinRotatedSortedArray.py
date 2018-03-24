# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-24
算法思想：在旋转排序数组中搜索
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right-left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[right]:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

if __name__ == '__main__':
    print Solution().search([3, 1], 1)