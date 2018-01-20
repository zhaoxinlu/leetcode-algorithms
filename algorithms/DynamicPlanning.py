# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-20
Function: 几个动态规划dp算法经典案例的python实现
"""
import numpy as np

class DynamicPlanning(object):
    def climb_stairs(self, n):
        """
        求爬楼梯的方式的数量，每次可以爬一阶或两阶
        :param n: 楼梯高度
        :return: 返回爬楼梯的方式的数量
        """
        if n == 1 or n == 2:
            return n
        elif n == 0:
            return False
        else:
            dp = [0] * (n+1)
            # dp[i]表示到达i级台阶的方法数
            dp[1] = 1
            dp[2] = 2

            for i in range(3, n+1):
                dp[i] = dp[i-1] + dp[i-2] # dp-key

            return dp[n]

    def smallest_path_of_matrix(self, arr):
        """
        给定一个矩阵m，从左上角开始每次只能向右走或者向下走，最后达到右下角的位置，路径中所有数字累加起来就是路径和，返回所有路径的最小路径和.
        :param arr: 二维数组
        :return: 所有路径的最小路径和
        """
        array = np.array(arr)
        row = array.shape[0]
        col = array.shape[1]
        # 初始化dp数组，设为最大值2147483647
        dp = [([2147483647] * col) for i in range(row)]
        # dp[i][j]表示的是从原点到i,j位置的最短路径和
        i, j = 0, 0

        for i in range(0, row):
            for j in range(0, col):
                if dp[i][j] == 2147483647:
                    if i == 0 and j == 0:
                        dp[i][j] = array[i][j]
                    elif i == 0 and j != 0:
                        dp[i][j] = array[i][j] + dp[i][j-1]
                    elif i != 0 and j == 0:
                        dp[i][j] = array[i][j] + dp[i-1][j]
                    else:
                        dp[i][j] = array[i][j] + min(dp[i-1][j], dp[i][j-1]) # dp-key

        return dp[i][j] # dp

    def longest_increment_subsequence(self, arr):
        """
        给定数组arr，返回arr的最长递增子序列的长度，比如arr=[2,1,5,3,6,4,8,9,7]，最长递增子序列为[1,3,4,8,9]返回其长度为5.
        :param arr: 数组
        :return: 最长递增子序列的长度
        """
        dp = [0] * len(arr)
        # dp[i]表示以必须arr[i]这个数结束的情况下产生的最大递增子序列的长度
        dp[0] = 1

        for i in range(1, len(arr)):
            max_ = 0
            for j in range(0, i):
                if dp[j] > max_ and arr[i] > arr[j]:
                    max_ = dp[j]
            dp[i] = max_ + 1

        # 寻最长序列的长度
        maxdp = 0
        for i in range(0, len(dp)):
            if dp[i] > maxdp:
                maxdp = dp[i]

        return maxdp

    def longest_common_subsequence(self, str1, str2):
        """
        给定两个字符串str1和str2，返回两个字符串的最长公共子序列(#区别于 最长公共子串);
        例如：str1="1A2C3D4B56",str2="B1D23CA45B6A","123456"和"12C4B6"都是最长公共子序列，返回哪一个都行。
        :param str1: 字符串1
        :param str2: 字符串2
        :return: 最长公共子序列长度
        """
        size1 = len(str1)
        size2 = len(str2)
        if size1 == 0 or size2 == 0:
            return 0
        else:
            dp = [([0] * (size2 + 1)) for i in range(size1 + 1)]
            # dp[i][j]的含义是str1[0..i]与str2[0..j]的最长公共子序列的长度

            for i in range(0, size1):
                for j in range(0, size2):
                    if str1[i] == str2[j]:
                        dp[i + 1][j + 1] = dp[i][j] + 1
                    else:
                        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

            return dp[size1][size2]

    def backpack(self, cap, value, weight):
        """
        0-1背包问题，动态规划经典问题，一个背包有滴定的承重W，有N件物品，每件物品都有自己的价值，记录在数组V中，也都有自己的重量，记录在数组W中;
        每件物品只能选择要装入还是不装入背包，要求在不超过背包承重的前提下，选出的物品总价值最大。
        :param cap: weight of bag
        :param value: value list
        :param weight: weight list
        :return: 最大价值
        """
        if len(value) != len(weight):
            return False

        size = len(value)
        dp = [([0] * (cap+1)) for i in range(size+1)]
        # dp[i][j]表示前i件物品，不超过重量j的时候的最大价值

        for i in range(1, size+1):
            for j in range(1, cap+1):
                if j-weight[i-1] >= 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]]+value[i-1])
                    # dp key: weigh[i-1]&value[i-1] is the i-st goods
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[size][cap]

    def minimum_editing_cost(self, str1, str2, ic, dc, rc):
        """
        给定两个字符串str1，str2，在给定三个整数ic,dc,rc，分别代表插入，删除和替换一个字符的代价。返回将str1编辑成str2的最小代价.
        比如，str1="abc",str2="adc",ic=5,dc=3,rc=2,从str1到str2，将'b'换成'd'代价最小，所以返回2.
        :param str1: 字符串str1
        :param str2: 字符串str2
        :param ic: 插入一个字符的代价
        :param dc: 删除一个字符的代价
        :param rc: 替换一个字符的代价
        :return: 将str1编辑成str2的最小代价
        """
        size1 = len(str1)
        size2 = len(str2)
        dp = [([0] * (size2+1)) for i in range(size1+1)]
        # dp[i][j]是str1[0..i-1]变成str2[0...j-1]的最小代价

        for i in range(size2):
            dp[0][i] = ic * i
        for i in range(size1):
            dp[i][0] = dc * i
        for i in range(1, size1+1):
            for j in range(1, size2+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] + rc
                dp[i][j] = min(dp[i][j], dp[i-1][j]+ic)
                dp[i][j] = min(dp[i][j], dp[i][j-1]+dc)

        return dp[size1][size2]

if __name__ == '__main__':
    # 测试用例
    num = 10
    print DynamicPlanning().climb_stairs(num)

    arr1 = [[1, 3, 5, 9], [8, 1, 3, 4], [5, 0, 6, 1], [8, 8, 4, 0]]
    print DynamicPlanning().smallest_path_of_matrix(arr=arr1)

    arr2 = [2, 1, 5, 3, 6, 4, 8, 9, 7]
    print DynamicPlanning().longest_increment_subsequence(arr=arr2)

    str1 = '1A2C3D4B56'
    str2 = 'B1D23CA45B6A'
    print DynamicPlanning().longest_common_subsequence(str1=str1, str2=str2)

    cap = 10
    value = [42, 12, 40, 25]
    weight = [7, 3, 4, 5]
    print DynamicPlanning().backpack(cap=cap, value=value, weight=weight)

    str1s, str2s = 'abc', 'adc'
    ic, dc, rc = 5, 3, 20 # 先删除b，再插入d
    print DynamicPlanning().minimum_editing_cost(str1=str1s, str2=str2s, ic=ic, dc=dc, rc=rc)