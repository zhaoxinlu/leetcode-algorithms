# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-02
算法思想： 主元素--"它在数组中的出现次数严格大于数组元素个数的二分之一"
        由于是 二分之一， 可排序找中位数，可统计消除
"""
class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        elem = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if count == 0:
                count = 1
                elem = nums[i]
            elif nums[i] == elem:
                count += 1
            else:
                count -= 1

        return elem

if __name__ == '__main__':
    nums = [2, 1, 2, 1, 1, 1, 2]
    print Solution().majorityNumber(nums)