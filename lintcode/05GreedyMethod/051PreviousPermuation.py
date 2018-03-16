# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-03
算法思想： 上一个排列, 要对找到的递减序列前一个数，和该递减序列的第一个大于它的数的前一个数进行交换
"""
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        # write your code here
        flag = len(nums) - 1
        while flag > 0 and nums[flag] >= nums[flag-1]:
            flag -= 1
        peakEnd = flag - 1
        if peakEnd >= 0:
            while flag < len(nums) and nums[flag] < nums[peakEnd]:
                flag += 1
            flag -= 1
            nums[peakEnd], nums[flag] = nums[flag], nums[peakEnd]

        sortStart = peakEnd + 1
        sortEnd = len(nums) - 1
        while sortStart < sortEnd:
            nums[sortStart], nums[sortEnd] = nums[sortEnd], nums[sortStart]
            sortStart += 1
            sortEnd -= 1

        return nums

if __name__ == '__main__':
    #nums = [4, 0, 7, 1, 2, 3, 8, 9]
    nums = [1, 1, 2]
    print Solution().previousPermuation(nums)