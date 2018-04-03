# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-03
算法思想：组合之和等于target--递归回溯
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.combinationSumDFS(candidates, target, 0, [], result)
        return result

    def combinationSumDFS(self, candidates, target, m, tmp, result):
        if target < 0:
            return
        if target == 0:
            result.append(tmp[:])
        for i in range(m, len(candidates)):
            tmp.append(candidates[i])
            self.combinationSumDFS(candidates, target-candidates[i], i, tmp, result)
            tmp.pop()

if __name__ == '__main__':
    c = [2, 3, 6, 7]
    t = 7
    print Solution().combinationSum(c, t)