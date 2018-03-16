# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-02
算法思想： 主元素II--"它在数组中的出现次数严格大于数组元素个数的三分之一"
        数组中只有唯一的主元素
"""
class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        numDict = {}

        for i in range(len(nums)):
            if nums[i] in numDict:
                numDict[nums[i]] += 1
            else:
                numDict[nums[i]] = 1
            if numDict[nums[i]] > len(nums) / 3:
                return nums[i]

        return None

if __name__ == '__main__':
    nums = [1, 2, 3, 2]
    print Solution().majorityNumber(nums)