# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-25
算法思想：寻找消失的最小正数--桶排序
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1

        i = 0
        while i < len(nums):
            if nums[i] == i+1 or nums[i] <= 0 or nums[i] > len(nums):
                i += 1
            elif nums[i] != nums[nums[i]-1]:
                self.swap(nums, i, nums[i]-1)
            else:
                i += 1

        for j in range(len(nums)):
            if nums[j] != j+1:
                return j+1

        return len(nums)+1


    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

if __name__ == '__main__':
    print Solution().firstMissingPositive([1, 2])