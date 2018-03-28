# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-27
算法思想：Combinations
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return 0

    def combine_dfs(self, n, k):
        """
        超时 Time Limit Exceeded
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.DFS(n, k, 1, [], result)
        return result

    def DFS(self, n, k, m, tmp, result):
        if k == len(tmp):
            result.append(tmp[:])
        else:
            for i in range(m, n+1):
                tmp.append(i)
                self.DFS(n, k, i+1, tmp, result)
                tmp.pop()

if __name__ == '__main__':
    print Solution().combine_dfs(4, 2)