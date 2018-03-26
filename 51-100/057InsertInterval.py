# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-26
算法思想：插入区间
"""
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        insertPos = 0

        for itl in intervals:
            if itl.end < newInterval.start:
                result.append(itl)
                insertPos += 1
            elif itl.start > newInterval.end:
                result.append(itl)
            else:
                newInterval.start = min(itl.start, newInterval.start)
                newInterval.end = max(itl.end, newInterval.end)

        result.insert(insertPos, newInterval)

        return result