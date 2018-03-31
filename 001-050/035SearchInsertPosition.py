# -*- coding: utf-8 -*-
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        二分查找的变形
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left

if __name__ == '__main__':
    print Solution().searchInsert([1, 3, 4, 5], 6)