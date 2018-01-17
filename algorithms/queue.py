# -*- coding: utf-8 -*-
"""
Author: Zhao Xinlu
School: BUPT
Date: 2018-01-17
Function: 利用列表的append()和pop()方法可以实现队列的入队enqueue和出队dequeue的操作
"""
class Queue:
    def __init__(self, size):
        """
        初始化类
        :param size:
        """
        self.size = size
        self.queue = []
        self.front = -1
        self.rear = -1

    def is_empty(self):
        """
        判断队列是否为空
        :return:
        """
        return self.front == self.rear

    def is_full(self):
        """
        判断队列是否已满
        :return:
        """
        return self.rear - self.front + 1 == self.size

    def print_queue(self):
        """
        打印队列所有元素
        :return:
        """
        print self.queue

    def enqueue(self, value):
        """
        模拟元素入队列
        :param value:
        :return:
        """
        if self.is_full():
            print "QUEUE IS FULL!"
            return
        else:
            self.queue.append(value)
            self.rear = self.rear + 1

    def dequeue(self):
        """
        模拟元素出队列
        :return:
        """
        if self.is_empty():
            print "QUEUE IS EMPTY!"
            return
        else:
            self.queue.pop(0)
            self.front = self.front + 1

if __name__ == '__main__':
    queue = Queue(10)
    for i in range(6):
        queue.enqueue(i)
    queue.print_queue()

    queue.dequeue()
    queue.print_queue()

    print queue.is_empty()
    print queue.is_full()