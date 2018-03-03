# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-03
算法思想： 俩数之和
"""
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        numDict = {}
        for i in range(len(numbers)):
            if numbers[i] in numDict:
                return [numDict[numbers[i]], i]
            else:
                numDict[target - numbers[i]] = i

if __name__ == '__main__':
    print Solution().twoSum([2, 7, 11, 15], 18)