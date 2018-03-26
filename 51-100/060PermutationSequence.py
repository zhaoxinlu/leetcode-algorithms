# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-26
算法思想：按位操作
"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ''
        k -= 1
        size = 1
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(1, n):
            size *= i
        for i in reversed(range(n)):
            cur = nums[k/size]
            result += str(cur)
            nums.remove(cur)
            if i != 0:
                k %= size
                size /= i

        return result

if __name__ == '__main__':
    print Solution().getPermutation(3, 3)