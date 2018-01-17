# -*- coding: utf-8 -*-
'''
Author: Zhao Xinlu
School: BUPT
Date: 2018-01-17
Function：单链表数据结构的实现--节点Node类与链表LinkedList类,
            并实现了链表的一些常用操作：

                __init__()，创建链表
                is_empty():判断该链表是否为空
                append(value):在链表末添加node/值
                insert(value, index):插入
                delete(index):删除
                update(value, index):更新
                get_value(index):查找
                get_length():获取链表长度
                clear():清空链表
                print_linkedlist():打印整个链表
'''

class Node:
    def __init__(self, data, _next=None):
        '''
        data: 节点保存的数据
        _next: 保存下一个节点对象
        '''
        self.data = data
        self._next = _next

    def __repr__(self):
        '''
        用来定义Node的字符输出，
        print为输出data
        :return:
        '''
        return str(self.data)

class LinkedList:
    def __init__(self):
        """
        链表初始化
        """
        self.head = None
        self.length = 0

    def is_empty(self):
        """
        判断链表是否为空链表
        :return: boolean
        """
        return self.length == 0

    def get_length(self):
        """
        获取链表长度
        :return: int
        """
        p = self.head

        if p:
            length = 1
            while p._next:
                p = p._next
                length += 1

            return length
        else:
            return 0

    def clear(self):
        """
        链表清空
        :return:
        """
        self.head = None
        self.length = 0

    def append(self, node):
        """
        链表末尾插入节点/值，链表长度加一
        :param node: 节点/值
        :return: None
        """
        if isinstance(node, Node):
            pass
        else:
            node = Node(data=node)

        if self.head == None:
            self.head = node
        else:
            q = self.head
            while q._next:
                q = q._next
            q._next = node

        self.length += 1

    def insert(self, value, index):
        """
        链表的元素插入操作，将元素插入到指定索引位置，链表长度加一
        :param value: 插入的元素的值
        :param index: 插入元素的索引位置
        :return: None
        """
        if index > self.get_length() or index < 0 or self.is_empty():
            print "Index value is out of range."
            return
        else:
            node = Node(value)
            current_node = self.head
            j = 0

            if index == 0:
                self.head = node
                node._next = current_node
                return

            while current_node._next != None and j < index-1:
                current_node = current_node._next
                j += 1

            if j == index-1:
                node._next = current_node._next
                current_node._next = node

            self.length += 1
            return

    def delete(self, index):
        """
        链表的删除元素操作， 删除指定索引位置的元素，链表长度减一
        :param index: 元素的索引位置
        :return: None
        """
        if self.is_empty() or index < 0 or index > self.get_length():
            print "Out of range."
            return

        if index == 0:
            self.head = self.head._next
        else:
            current_node = self.head
            j = 0

            while current_node._next != None and j < index-1:
                current_node = current_node._next
                j += 1

            if j == index-1:
                current_node._next = current_node._next._next

        self.length -= 1

    def update(self, value, index):
        """
        更新链表中某索引节点的值，链表长度不变
        :param value: 更新的值
        :param index: 索引位置
        :return: None
        """
        if self.is_empty() or index < 0 or index > self.length:
            print "Out of range! "
            return
        else:
            if index == 0:
                self.head.data = value
            else:
                current_node = self.head
                j = 0

                while current_node._next != None and j < index:
                    current_node = current_node._next
                    j += 1

                if j == index:
                    current_node.data = value

    def get_value(self, index):
        """
        获取链表中某索引位置节点的值，链表长度不变
        :param index: 索引位置
        :return: value
        """
        if self.is_empty() or index < 0 or index > self.length:
            print "OUT of RANGE! "
            return
        else:
            if index == 0:
                return self.head.data
            else:
                current_node = self.head
                j = 0
                while current_node._next != None and j < index:
                    current_node = current_node._next
                    j += 1

                if j == index:
                    return current_node.data

    def print_linkedlist(self):
        """
        整个链表的打印操作
        :return: None
        """
        if self.is_empty():
            print "Empty linked list!"
            return None
        else:
            node = self.head
            print "Head -->", node.data
            while node._next:
                node = node._next
                print "-->", node.data
            print "--> None. Linked node finished."

if __name__ == '__main__':
    node1 = Node(data=2)
    node2 = Node(data=6)
    node3 = Node(data=5)
    linkedlist = LinkedList()
    linkedlist.append(node1)
    linkedlist.append(node2)
    linkedlist.append(5)
    linkedlist.print_linkedlist()
    print linkedlist.length
    linkedlist.update(value=3, index=2)
    linkedlist.print_linkedlist()
    print linkedlist.length
    print linkedlist.get_value(index=0)
    print "#########"
    linkedlist.insert(value=4, index=2)
    linkedlist.print_linkedlist()
    print linkedlist.get_length()
    linkedlist.delete(index=3)
    linkedlist.print_linkedlist()
    print linkedlist.length
    linkedlist.clear()
    linkedlist.print_linkedlist()