# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-05
算法思想： 落单的数III
    （后续有位操作思想算法更新）
"""
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        # write your code here
        numDict = {}
        for i in range(len(A)):
            if A[i] in numDict:
                numDict[A[i]] += 1
            else:
                numDict[A[i]] = 1

        results = []
        for num in numDict:
            if numDict[num] == 1:
                results.append(num)

        return results

if __name__ == '__main__':
    A = [1, 1, 2, 3, 3, 4]
    print Solution().singleNumberII(A)