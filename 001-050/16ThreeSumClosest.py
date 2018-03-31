# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-31
算法思想： 三数之和最接近某值
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == None or len(nums) < 3:
            return 0
        if len(nums) == 3:
            return sum(nums)

        nums.sort()
        result = 2147483647

        for i in range(len(nums)-2):
            start = i+1
            end = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while start < end:
                val = nums[i] + nums[start] + nums[end]
                if abs(val-target) < abs(result-target):
                    result = val
                if val <= target:
                    start += 1
                else:
                    end -= 1

        return result

if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    print Solution().threeSumClosest(nums, target)