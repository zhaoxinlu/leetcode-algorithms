# -*- coding: utf-8 -*-
"""
Editor: 九章算法
School: BUPT
Date: 2018-03-14
算法思想： 数字组合--回溯法/深度优先搜索
"""
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = list(set(candidates))
        candidates.sort()
        self.results = []
        self.DFS(candidates, target, 0, [])
        return self.results

    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            self.results.append(valuelist)
            return
        else:
            for i in range(start, length):
                if target < candidates[i]:
                    return
                self.DFS(candidates, target-candidates[i], i, valuelist+[candidates[i]])

if __name__ == '__main__':
    c = [2, 3, 6, 7]
    target = 7
    print Solution().combinationSum(c, target)