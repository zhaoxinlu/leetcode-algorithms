# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-24
算法思想：递归实现，如果左括号还有剩余，则可以放置左括号，如果右括号的剩余数大于左括号，则可以放置右括号。--回溯
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate(n, n, '', result)
        return result

    def generate(self, left, right, s, result):
        if left == 0 and right == 0:
            result.append(s)

        if left > 0:
            self.generate(left-1, right, s+'(', result)
        if right > left:
            self.generate(left, right-1, s+')', result)

if __name__ == '__main__':
    print Solution().generateParenthesis(3)