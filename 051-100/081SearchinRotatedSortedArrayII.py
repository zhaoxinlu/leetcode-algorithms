# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-01
算法思想：Search in Rotated Sorted Array II
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left) / 2
            if nums[mid] == target:
                return True
            elif nums[mid] < nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > nums[left]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[left] == target or nums[right] == target:
                    return True
                else:
                    left += 1
                    right -= 1

        return False

if __name__ == '__main__':
    n = [1, 3]
    t = 2
    print Solution().search(n, target=t)