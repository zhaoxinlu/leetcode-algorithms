# -*- coding: utf-8 -*-
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDic = {}
        for i in range(len(nums)):
            if nums[i] in numDic:
                return [numDic[nums[i]], i]
            else:
                numDic[target-nums[i]] = i

if __name__ == '__main__':
    print Solution().twoSum([2, 7, 9, 11], 16)