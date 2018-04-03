# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-03
算法思想：主元素II--摩尔投票法
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        时间O(n)，空间O(1)
            任意一个数组出现次数大于n/3的众数最多有两个(摩尔投票法)
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        mE1, mE2 = 0, 0
        count1, count2 = 0, 0

        for i in range(len(nums)):
            if nums[i] == mE1:
                count1 += 1
            elif nums[i] == mE2:
                count2 += 1
            elif count1 == 0:
                mE1 = nums[i]
                count1 += 1
            elif count2 == 0:
                mE2 = nums[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == mE1:
                count1 += 1
            elif nums[i] == mE2:
                count2 += 1

        if count1 * 3 > len(nums):
            result.append(mE1)
        if count2 * 3 > len(nums):
            result.append(mE2)

        return result

if __name__ == '__main__':
    nums = [1, 3, 2, 2, 3]
    print Solution().majorityElement(nums)