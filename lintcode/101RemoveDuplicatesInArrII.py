# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： 删除排序数组中的重复数字II
"""
class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        i = 0
        count = 1

        for j in range(1, len(nums)):
            if nums[j] == nums[i] and count < 2:
                count += 1
                i += 1
                nums[i] = nums[j]
            elif nums[j] != nums[i]:
                count = 1
                i += 1
                nums[i] = nums[j]

        del nums[i+1:]
        return len(nums)

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 2, 2, 3]
    print Solution().removeDuplicates(nums)