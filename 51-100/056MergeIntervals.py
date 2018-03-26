# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-26
算法思想：合并区间
"""
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        result = []

        for i in range(len(intervals)):
            if result == []:
                result.append(intervals[i])
            else:
                if intervals[i].start <= result[len(result)-1].end:
                    result[len(result)-1].end = max(result[len(result)-1].end, intervals[i].end)
                else:
                    result.append(intervals[i])

        return result