# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-06
算法思想： 木材加工--二分查找思想
"""
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if len(L) == 0:
            return 0

        maxL = max(L)

        left = 1
        right = maxL

        while left + 1 < right:
            mid = left + (right - left) / 2
            if self.helper(L, mid) >= k:
                left = mid
            else:
                right = mid

        if self.helper(L, right) >= k:
            return right
        if self.helper(L, left) >= k:
            return left

        return 0

    def helper(self, L, length):
        count = 0
        for i in range(len(L)):
            count += (L[i] / length)
        return count

if __name__ == '__main__':
    L = [2147483644, 2147483645, 2147483646, 2147483647]
    k = 4
    print Solution().woodCut(L, k)