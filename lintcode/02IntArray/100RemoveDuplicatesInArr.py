# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： 删除排序数组中的重复数字
"""
class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]

        del nums[k+1:]
        return len(nums)

if __name__ == '__main__':
    nums = [1, 1, 2, 2, 2, 3]
    print Solution().removeDuplicates(nums)