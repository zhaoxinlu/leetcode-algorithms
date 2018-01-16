# -*- coding: utf-8 -*-
'''
Test 1-HMM
'''
import numpy as np
import hmm

def generate_index_map(labels):
    """
    :param labels:
    :return:
    """
    index_label = {}
    label_index = {}
    i = 0
    for l in labels:
        index_label[i] = l
        label_index[l] = i
        i += 1
    return label_index, index_label

def convert_observations_to_index(observations, label_index):
    lists = []
    for o in observations:
        lists.append(label_index[o])
    return lists

def convert_map_to_vector(map, label_index):
    v = np.empty(len(map), dtype=float)
    for e in map:
        v[label_index[e]] = map[e]
    return v

def convert_map_to_matrix(map, label_index1, label_index2):
    # {'Healthy': 0, 'Fever': 1}
    m = np.empty((len(label_index1), len(label_index2)), dtype=float)
    for line in map:
        for col in map[line]:
            m[label_index1[line]][label_index2[col]] = map[line][col]
    return m

if __name__ == '__main__':
    # 隐状态
    states = ('Healthy', 'Fever')
    # 观测序列（显状态）
    observations = ('normal', 'cold', 'dizzy')
    # 初始概率（隐状态）
    start_probability = {"Healthy": 0.6, "Fever": 0.4}
    # 转移概率（隐状态）A
    transition_probability = {
        'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
        'Fever': {'Healthy': 0.4, 'Fever': 0.6},
    }
    # 发射概率（隐状态表现为显状态的概率）B
    emission_probability = {
        'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
        'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
    }

    states_label_index, states_index_label = generate_index_map(states)
    # {'Healthy': 0, 'Fever': 1}
    observations_label_index, observations_index_label = generate_index_map(observations)
    # {'cold': 1, 'dizzy': 2, 'normal': 0}

    A = convert_map_to_matrix(transition_probability, states_label_index, states_label_index)
    print A
    B = convert_map_to_matrix(emission_probability, states_label_index, observations_label_index)
    print B
    observations_index = convert_observations_to_index(observations, observations_label_index)
    Pi = convert_map_to_vector(start_probability, states_label_index)
    print Pi

    h = hmm.HMM(A, B, Pi)
    observations_data, states_data = h.simulate(10)
    print observations_data, states_data