# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-31
算法思想： 四数之和
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []

        result = []
        nums.sort()

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                start = j + 1
                end = len(nums)-1
                while start < end:
                    val = nums[i] + nums[j] + nums[start] + nums[end]
                    if val == target:
                        result.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        while start < end and start > j + 1 and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and end < len(nums) - 1 and nums[end] == nums[end + 1]:
                            end -= 1
                    elif val < target:
                        start += 1
                    else:
                        end -= 1

        return result

if __name__ == '__main__':
    nums = [-1, 0, -5, -2, -2, -4, 0, 1, -2]
    target = -9
    print Solution().fourSum(nums, target)