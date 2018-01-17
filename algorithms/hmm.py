# -*- coding: utf-8 -*-
"""
隐马尔可夫模型有3个基本问题：
    1.概率计算问题（前向forward算法与后向backword算法）
        给定模型lamada=(A,B,Pi)和观测序列O(o1,o2,...,on)，计算模型lamada下观测序列O出现的概率P(O|lamada).
    2.学习问题（Baum-Welch算法）
    3.预测问题（维特比算法）
"""
import numpy as np

class HMM:
    """
    1 Hidden Markov Model.

    A : numpy.ndarray
        State transition probability matrix
    B: numpy.ndarray
        Output emission probability matrix with shape(N, number of output types)
    Pi: numpy.ndarray
        Initial state probablity vector
    """
    def __init__(self, A, B, Pi):
        self.A = A
        self.B = B
        self.Pi = Pi

    def simulate(self, T):
        '''
        观测序列的生成过程.
        :param T: 长度
        :return: 观测序列、状态向量
        '''
        def draw_from(probs):
            return np.where(np.random.multinomial(1, probs) == 1)[0][0]

        observations = np.zeros(T, dtype=int)
        states = np.zeros(T, dtype=int)
        states[0] = draw_from(self.Pi)
        observations[0] = draw_from(self.B[states[0], :])
        for t in range(1, T):
            states[t] = draw_from(self.A[states[t-1], :])
            observations[t] = draw_from(self.B[states[t], :])
        return observations, states