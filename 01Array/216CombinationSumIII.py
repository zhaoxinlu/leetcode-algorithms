# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-03
算法思想：组合之和III--递归回溯
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.combinationSum3DFS(k, n, 1, [], result)
        return result

    def combinationSum3DFS(self, k, n, m, tmp, result):
        if n < 0:
            return
        if k == 0 and n == 0:
            result.append(tmp[:])
        for i in range(m, 10):
            tmp.append(i)
            self.combinationSum3DFS(k-1, n-i, i+1, tmp, result)
            tmp.pop()

if __name__ == '__main__':
    print Solution().combinationSum3(3, 9)