# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： 子数组之和为0
"""
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        if len(nums) < 1:
            return []
        results = []

        for i in range(len(nums)):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                if curSum == 0:
                    results.append([i, j])

        return results

    def subarraySumII_On(self, nums):
        """
        利用一个 map 记录从第一个元素开始到当前元素之和 与 当前元素的下标 的对应关系，
        若有一段子数组和为0，那么势必出现同一和对应2个下标，此时就找到了和为零的连续序列，时间复杂度是O(n)
        :param nums:
        :return:
        """
        tDict = {0: -1}
        results = []
        tmp = 0

        for i in range(len(nums)):
            tmp += nums[i]
            if tmp in tDict:
                results.append([tDict[tmp]+1, i])
            else:
                tDict[tmp] = i

        return results

if __name__ == '__main__':
    nums = [-3, 1, 2, -3, 4]
    print Solution().subarraySum(nums)
    print Solution().subarraySumII_On(nums)