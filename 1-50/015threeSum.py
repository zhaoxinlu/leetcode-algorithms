# -*- coding:utf-8 -*-
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
# Time Limit Exceeded
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2:
            return []

        result = []
        nums.sort()

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val == 0 and [nums[i], nums[left], nums[right]] not in result:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif val < 0:
                    left += 1
                else:
                    right -= 1

        return result

if __name__ == '__main__':
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])