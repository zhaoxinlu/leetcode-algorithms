# -*- coding: utf-8 -*-
"""
Author: Zhao Xinlu
School: BUPT
Date: 2018-01-17
Function: 利用列表的append()和pop()方法可以实现栈的出栈pop和入栈push的操作
"""
class Stack:
    def __init__(self, size):
        """
        初始化栈类
        :param size:
        """
        self.size = size
        self.stack = []
        self.top = -1

    def is_empty(self):
        """
        判断栈是否为空
        :return:
        """
        return self.top == -1

    def is_full(self):
        """
        判断是否栈满
        :return:
        """
        return self.top+1 == self.size

    def push(self, value):
        """
        元素入栈
        :param value:
        :return:
        """
        if self.is_full():
            print "Stack is full!"
            return
        else:
            self.stack.append(value)
            self.top += 1

    def pop(self):
        """
        最后一元素出栈
        :return:
        """
        if self.is_empty():
            print "Stack is empty!"
            return
        else:
            self.top = self.top-1
            self.stack.pop()

    def print_stack(self):
        """
        打印栈所有元素
        :return:
        """
        print self.stack

if __name__ == '__main__':
    stack = Stack(10)
    for i in range(0, 6):
        stack.push(i)
    stack.print_stack()

    stack.pop()
    stack.print_stack()