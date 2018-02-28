# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-02-28
算法思想： Fize Buzz问题
"""
class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        result = []

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("fizz buzz")
            elif i % 3 == 0:
                result.append("fizz")
            elif i % 5 == 0:
                result.append("buzz")
            else:
                i = str(i)
                result.append(i)

        return result

if __name__ == '__main__':
    print Solution().fizzBuzz(15)