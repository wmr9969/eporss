import numpy as np
import os
import sys
import time


def file2graph(lines):
    graph = []
    for line in lines[4:]:
        graph.append([int(s) for s in line.split()])
    return np.array(graph)


def load_as_graph(F_num):
    DIRPATH = 'datasets/as-733'
    file_list = os.listdir(DIRPATH)

    graph_list = []
    for i in range(F_num):
        file_path = os.path.join(DIRPATH, file_list[i])
        with open(file_path, 'r') as f:
            lines = f.readlines()
        graph_list.append(file2graph(lines))

    return graph_list


def get_total_nodes(graph_list):
    total_nodes = set()
    for graph in graph_list:
        nodes = set(graph.flatten())
        total_nodes = total_nodes | nodes
    return list(total_nodes)


def select_nodes(num):
    F_num = 6
    graph_list = load_as_graph(F_num)
    nodes = get_total_nodes(graph_list)

    outdegree = [0] * len(nodes)
    for graph in graph_list:
        for edge in graph:
            outdegree[nodes.index(edge[0])] += 1

    selected_nodes = list(np.argsort(outdegree)[-num:])
    selected_nodes.reverse()
    if not os.path.exists('datasets/as_graph'):
        os.mkdir('datasets/as_graph')
    np.savetxt('datasets/as_graph/nodes_' + str(num) + '.txt', np.array(selected_nodes), fmt='%d')

    for i in range(F_num):
        selected_edges = []
        for edge in graph_list[i]:
            if nodes.index(edge[0]) in selected_nodes and nodes.index(edge[1]) in selected_nodes:
                e0 = selected_nodes.index(nodes.index(edge[0]))
                e1 = selected_nodes.index(nodes.index(edge[1]))
                selected_edges.append([e0, e1])
        # print(len(selected_edges))
        np.savetxt('datasets/as_graph/edges_' + str(num) + '_g' + str(i) + '.txt', np.array(selected_edges), fmt='%d')


if __name__ == '__main__':
    select_nodes(200)
