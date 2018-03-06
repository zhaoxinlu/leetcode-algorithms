# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-03
算法思想： 三数之和最接近某值(超时Time)
"""
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        if len(numbers) < 3:
            return None

        if len(numbers) == 3:
            return sum(numbers)

        numbers.sort()
        result = 2147483647

        for i in range(len(numbers)-2):
            left = i + 1
            right = len(numbers) - 1
            while left < right:
                val = numbers[i] + numbers[left] + numbers[right]
                if abs(val - target) < abs(result - target):
                    result = val
                elif val <= target:
                    left += 1
                else:
                    right -= 1

        return result

if __name__ == '__main__':
    nums = [1, 0, -1, -1, -1, -1, 0, 1, 1, 1, 2]
    print Solution().threeSumClosest(nums, 7)