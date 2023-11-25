import argparse
import numpy as np
import os
import sys
import time

from algorithms import Algorithms


NODES_NUM = 200
eval_num = 100


def load_graph(num, prob_change):
    EDGE_PATH = 'datasets/fb_graph/edges_200.txt'
    PROB_PATH = 'datasets/fb_graph/probs200_c' + str(prob_change) + '_' + str(num) + '.txt'

    edges = np.loadtxt(EDGE_PATH, dtype=int)
    probs = np.loadtxt(PROB_PATH)

    graph = [[] for _ in range(NODES_NUM)]
    probs_list = [[] for _ in range(NODES_NUM)]
    for i in range(len(edges)):
        edge = edges[i]
        graph[edge[0]].append(edge[1])
        probs_list[edge[0]].append(probs[i])

    return graph, probs_list


def IC(S, graph, probs):
    influence = 0
    for i in range(eval_num):
        activated_nodes = [0] * NODES_NUM
        selected_nodes = S
        next_nodes = []
        for element in S:
            activated_nodes[element] = 1

        flag = 1
        while flag:
            for node in selected_nodes:
                edges = graph[node]
                n_probs = probs[node]
                for i in range(len(edges)):
                    if np.random.random() < n_probs[i] and activated_nodes[edges[i]] == 0:
                        next_nodes.append(edges[i])
                        activated_nodes[edges[i]] = 1
            selected_nodes = next_nodes
            next_nodes = []
            if len(selected_nodes) == 0:
                flag = 0
        influence += np.sum(activated_nodes)
    return influence / eval_num


graph_0, probs_0 = load_graph(0, 0.2)
graph_1, probs_1 = load_graph(1, 0.2)
graph_2, probs_2 = load_graph(2, 0.2)
graph_3, probs_3 = load_graph(3, 0.2)
graph_4, probs_4 = load_graph(4, 0.2)
graph_5, probs_5 = load_graph(5, 0.2)


def f0(S):
    return IC(S, graph_0, probs_0)


def f1(S):
    return IC(S, graph_1, probs_1)


def f2(S):
    return IC(S, graph_2, probs_2)


def f3(S):
    return IC(S, graph_3, probs_3)


def f4(S):
    return IC(S, graph_4, probs_4)


def f5(S):
    return IC(S, graph_5, probs_5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test in dataset facebook')
    parser.add_argument('--k', type=int, default=5, help='Budget k')
    parser.add_argument('--m', type=int, default=3, choices=range(2, 7), help='Objectives m')
    parser.add_argument('--t', type=int, default=1, help='Index of this run of the k,m setting')
    args = parser.parse_args()

    V = list(range(NODES_NUM))
    functions = [f0, f1, f2, f3, f4, f5]
    k = args.k
    m = args.m
    times = args.t
    algorithms = Algorithms(V, functions[:m], k)

    greedy_subset = algorithms.Greedy(times, 'output_fb')
    modified_greedy_subset = algorithms.ModifiedGreedy(times, 'output_fb')
    alpha = 1.0
    SATURATE_subset = algorithms.SATURATE(alpha, times, 'output_fb')
    EPORSS_subset = algorithms.EPORSS(times, 'output_fb')

