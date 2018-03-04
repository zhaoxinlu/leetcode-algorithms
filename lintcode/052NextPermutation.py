# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-04
算法思想： 下一个排列
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[i-1]:
                break

        if i > 0:
            for j in range(len(nums)-1, i-1, -1):
                if nums[j] > nums[i-1]:
                    nums[i-1], nums[j] = nums[j], nums[i-1]
                    break

        tmp = nums[i:]
        tmp.sort()

        return nums[0:i]+tmp

if __name__ == '__main__':
    nums = [1, 3, 2, 3]
    print Solution().nextPermutation(nums)