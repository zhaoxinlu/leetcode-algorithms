# -*- coding: utf-8 -*-
"""
Editor: 九章算法
School: BUPT
Date: 2018-03-14
算法思想： 组合--回溯法/深度优先搜索
"""
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        self.results = []
        #tmplist = []
        self.DFS(n, k, 1, 0, [])
        return self.results

    def DFS(self, n, k, m, length, tmplist):
        if k == length:
            self.results.append(tmplist[:])
            return
        else:
            for i in range(m, n+1):
                tmplist.append(i)
                self.DFS(n, k, i+1, length+1, tmplist)
                tmplist.pop()

if __name__ == '__main__':
    print Solution().combine(4, 2)