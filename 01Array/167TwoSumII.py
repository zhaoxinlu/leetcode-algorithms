# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-02
算法思想：两数之和II
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}
        for i in range(len(numbers)):
            if numbers[i] in numDict:
                return [numDict[numbers[i]], i+1]
            else:
                numDict[target-numbers[i]] = i+1

if __name__ == '__main__':
    n = [2, 7, 9, 11]
    t = 9
    print Solution().twoSum(n, t)