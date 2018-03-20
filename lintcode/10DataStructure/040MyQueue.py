# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-20
算法思想： 两个栈实现队列
"""
class MyQueue:
    def __init__(self):
        # do intialization if necessary
        self.list1 = []
        self.list2 = []
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.list1.append(element)
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if len(self.list2) != 0:
            return self.list2.pop()
        else:
            while len(self.list1) != 0:
                self.list2.append(self.list1.pop())
            return self.list2.pop()
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if len(self.list2) == 0:
            while len(self.list1) != 0:
                self.list2.append(self.list1.pop())

        return self.list2[len(self.list2)-1]