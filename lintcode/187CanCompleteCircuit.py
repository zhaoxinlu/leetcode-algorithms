# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-07
算法思想： 加油站
"""
class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        """
        gas_sum（gas累加）大于cost_sum（cost累加）时必有解。

        当cur<0，意味着，前面在cur对应i之前的gas之和小于cost，若要有解，必须i之后gas的累加>cost的累加，则可以直接从i+1开始累加判断，不需要返回开始节点（即不是从i+1处开始）。
        后面gas_sum>cost_sum可以使得不需要从头判断
        :param gas:
        :param cost:
        :return:
        """
        gasSum = 0
        costSum = 0
        curDiff = 0
        result = 0

        for i in range(0, len(gas)):
            gasSum += gas[i]
            costSum += cost[i]
            curDiff += (gas[i]-cost[i])
            if curDiff < 0:
                result = i + 1
                curDiff = 0

        if gasSum >= costSum:
            return result

        return -1

    def canCompleteCircuit_On2(self, gas, cost):
        # write your code here
        """
        Time Limit Exceeded.
        油箱置空，从每个加油站出发，加油，减去消耗，出现小于零说明不能从该加油站出发。没有出现说明可以从这个加油站出发。
        注意“环路”，用取余的方法循环。
        :param gas:
        :param cost:
        :return:
        """
        for i in range(0, len(gas)):
            diff = 0
            for j in range(0, len(gas)):
                diff += gas[(i+j)%len(gas)]
                diff -= cost[(i+j)%len(gas)]
                if diff < 0:
                    break

            if diff >= 0:
                return i

        return -1

if __name__ == '__main__':
    gas = [1, 1, 3, 1]
    cost = [2, 2, 1, 1]
    print Solution().canCompleteCircuit(gas, cost)
    print Solution().canCompleteCircuit_On2(gas, cost)