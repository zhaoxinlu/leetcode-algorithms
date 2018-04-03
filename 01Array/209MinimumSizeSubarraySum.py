# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-03
算法思想：求子数组之和大于等于给定值的最小长度
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        时间复杂度O(n):
            定义两个指针left和right，分别记录子数组的左右的边界位置，
            然后我们让right向右移，直到子数组和大于等于给定值或者right达到数组末尾，此时我们更新最短距离，
            并且将left像右移一位，然后再sum中减去移去的值，
            然后重复上面的步骤，直到right到达末尾，且left到达临界位置，即要么到达边界，要么再往右移动，和就会小于给定值。
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        left, right, tmp = 0, 0, 0
        minLength = len(nums)+1

        while right < len(nums):
            while tmp < s and right < len(nums):
                tmp += nums[right]
                right += 1
            while tmp >= s:
                minLength = min(minLength, right - left)
                tmp -= nums[left]
                left += 1

        if minLength == len(nums)+1:
            return 0
        return minLength

if __name__ == '__main__':
    nums = [1, 1]
    s = 2
    print Solution().minSubArrayLen(s, nums)