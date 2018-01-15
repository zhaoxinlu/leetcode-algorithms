# -*- coding: utf-8 -*-
"""
散列表：所有的元素之间没有任何关系。元素的存储位置，是利用元素的关键字通过某个函数直接计算出来的。这个一一对应的关系函数称为散列函数或Hash函数。
采用散列技术将记录存储在一块连续的存储空间中，称为散列表或哈希表（Hash Table）。关键字对应的存储位置，称为散列地址。

好的散列函数：计算简单、散列地址分布均匀
"""

class HashTable:
    # 忽略了对数据类型，元素溢出等问题的判断。
    def __init__(self, size):
        # 使用list数据结构作为哈希表元素保存方法
        self.elem = [None for i in range(size)]
        # 最大表长
        self.count = size

    def hash(self, key):
        # 散列函数采用除留余数法
        return key % self.count

    def hash_insert(self, key):
        """
        插入关键字到哈希表内
        """
        address = self.hash(key)
        while self.elem[address]:
            address = (address+1) % self.count
        self.elem[address] = key

    def hash_search(self, key):
        """
        查找关键字，返回布尔值
        """
        start = address = self.hash(key)
        while self.elem[address] != key:
            address = (address+1) % self.count
            if not self.elem[address] or address == start:
                # 说明没找到或者循环到了开始的位置
                print "Can't find", key
                return False
        print "Its address in HashTable is", address
        return True

if __name__ == '__main__':
        TestList = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
        hash_table = HashTable(len(TestList))
        for i in TestList:
            hash_table.hash_insert(i)

        for i in hash_table.elem:
            if i:
                print i, hash_table.elem.index(i)
        print "\n"

        print hash_table.hash_search(22)