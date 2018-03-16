# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-16
算法思想： 乘积最大子序列--动态规划
"""
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        if nums == None:
            return None

        maxProduct = [nums[0]]
        minProduct = [nums[0]]

        for i in range(1, len(nums)):
            maxProduct.append(max(maxProduct[i - 1] * nums[i], minProduct[i - 1] * nums[i], nums[i]))
            minProduct.append(min(maxProduct[i - 1] * nums[i], minProduct[i - 1] * nums[i], nums[i]))

        return max(maxProduct)

if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    print Solution().maxProduct(nums)