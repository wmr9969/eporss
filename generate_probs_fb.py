import numpy as np
import os
import sys
import time


def load_graph():
    EDGE_PATH = 'datasets/fb_graph/edges_200.txt'
    PROB_PATH = 'datasets/fb_graph/probs_200.txt'

    edges = np.loadtxt(EDGE_PATH, dtype=int)
    probs = np.loadtxt(PROB_PATH)
    return edges, probs


def generate_subgraph(F_num, prob_change):
    path = 'datasets/fb_graph'

    edges, probs = load_graph()
    edges_num = len(edges)

    for i in range(F_num):
        new_probs_coef = np.random.random(edges_num) * prob_change + 1.0 - prob_change / 2
        new_probs = new_probs_coef * probs
        np.savetxt(os.path.join(path, 'probs200_c'+ str(prob_change) + '_' + str(i) + '.txt'), new_probs)


if __name__ == '__main__':
    generate_subgraph(6, 0.2)