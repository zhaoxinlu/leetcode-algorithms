# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-25
算法思想：变位词--字符串排序+字典
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        tmpStrs = []
        strDict = {}

        for s in strs:
            tmp = list(s)
            tmp.sort()
            tmpStrs.append(''.join(tmp))

        for i in range(len(tmpStrs)):
            if tmpStrs[i] not in strDict:
                strDict[tmpStrs[i]] = [strs[i]]
            else:
                strDict[tmpStrs[i]].append(strs[i])

        for key in strDict.keys():
            result.append(strDict[key])

        return result

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print Solution().groupAnagrams(strs)