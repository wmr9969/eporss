import numpy as np
import os
import sys
import time


NODES_NUM = 4039


def select_nodes(num):
    EDGE_PATH = 'datasets/facebook/facebook_combined.txt'

    with open(EDGE_PATH, 'r') as f:
        lines = f.readlines()

    outdegree = [0] * NODES_NUM
    edges = []
    for i in range(len(lines)):
        edge = [int(s) for s in lines[i].split()]
        outdegree[edge[0]] += 1
        edges.append(edge)

    selected_nodes = list(np.argsort(outdegree)[-num:])
    selected_nodes.reverse()
    indegree = [0] * num
    selected_edges = []
    for edge in edges:
        if edge[0] in selected_nodes and edge[1] in selected_nodes:
            e0 = selected_nodes.index(edge[0])
            e1 = selected_nodes.index(edge[1])
            selected_edges.append([e0, e1])
            indegree[e1] += 1

    probs = []
    for edge in selected_edges:
        probs.append(1/indegree[edge[1]])

    if not os.path.exists('datasets/fb_graph'):
        os.mkdir('datasets/fb_graph')
    np.savetxt('datasets/fb_graph/nodes_' + str(num) + '.txt', np.array(selected_nodes), fmt='%d')
    np.savetxt('datasets/fb_graph/edges_' + str(num) + '.txt', np.array(selected_edges), fmt='%d')
    np.savetxt('datasets/fb_graph/probs_' + str(num) + '.txt', np.array(probs), fmt='%.4f')


if __name__ == '__main__':
    select_nodes(200)
