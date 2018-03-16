# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-01
算法思想： 带最小值操作的栈
"""
class MinStack:
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.helper = []

    def push(self, number):
        """
            @param: number: An integer
            @return: nothing
        """
        # write your code here
        self.stack.append(number)
        if len(self.helper) == 0:
            self.helper.append(number)
        else:
            self.helper.append(min(number, self.helper[-1]))

    def pop(self):
        """
            @return: An integer
        """
        # write your code here
        self.helper.pop()
        return self.stack.pop()

    def min(self):
        """
            @return: An integer
        """
        # write your code here
        return self.helper[-1]

if __name__ == '__main__':
    s = MinStack()
    s.push(1)
    print s.pop()
    s.push(2)
    s.push(3)
    print s.min()
    s.push(1)
    print s.min()