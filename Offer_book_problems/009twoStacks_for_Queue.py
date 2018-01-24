# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-23
Function: 两个栈实现队列
"""
class Queue_with_2Stack(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, elem):
        """
        插入队列
        :param elem:
        :return:
        """
        return self.stack1.append(elem)

    def pop(self):
        """
        队列头部删除节点
        :return:
        """
        if self.stack2:
            return self.stack2.pop()
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()