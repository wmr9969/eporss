import argparse
import numpy as np
import matplotlib.pyplot as plt
import os


def draw_errorbar_k(dataset, k_list, m, times):
    DIR_PATH = 'output/output_' + dataset + '/'

    stds = []
    scores = []
    for k in k_list:
        g_score = []
        P_score = []
        S_score = []
        M_score = []
        for t in range(times):
            g_file = 'greedy_output_k' + str(k) + '_m' + str(m) + '_t' + str(t+1) + '.txt'
            S_file = 'SATURATE_output_k' + str(k) + '_m' + str(m) + '_t' + str(t+1) + '.txt'
            P_file = 'PORSM_output_k' + str(k) + '_m' + str(m) + '_t' + str(t+1) + '.txt'
            M_file = 'ModifiedGreedy_output_k' + str(k) + '_m' + str(m) + '_t' + str(t+1) + '.txt'

            with open(DIR_PATH + g_file, 'r') as f:
                lines = f.readlines()
            g_score.append(eval(lines[-1].split()[-1]))

            with open(DIR_PATH + S_file, 'r') as f:
                lines = f.readlines()
            S_score.append(eval(lines[-1].split()[-1]))

            with open(DIR_PATH + P_file, 'r') as f:
                lines = f.readlines()
            P_score.append(eval(lines[-1].split()[-1]))

            with open(DIR_PATH + M_file, 'r') as f:
                lines = f.readlines()
            M_score.append(eval(lines[-1].split()[-1]))

        stds.append([np.std(g_score), np.std(S_score), np.std(P_score), np.std(M_score)])
        scores.append([np.mean(g_score), np.mean(S_score), np.mean(P_score), np.mean(M_score)])

    plt.rcParams["errorbar.capsize"] = '4'
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Times New Roman'
    plt.rcParams['font.size'] = '18'
    plt.rcParams['lines.linestyle'] = '--'
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.markerfacecolor'] = 'none'
    plt.rcParams['lines.markeredgewidth'] = 1.5
    plt.rcParams['lines.markersize'] = 11
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['mathtext.rm'] = 'sans'
    plt.rcParams['mathtext.it'] = 'sans:italic'
    plt.rcParams['mathtext.default'] = 'it'

    std_list = np.array(stds)
    score_list = np.array(scores)
    # print(std_list)
    plt.errorbar(k_list, score_list[:, 2], yerr=std_list[:, 2], c='r', marker='s', label='EPORSS')
    plt.errorbar(k_list, score_list[:, 0], yerr=std_list[:, 0], c='b', marker='x', label='Greedy')
    plt.errorbar(k_list, score_list[:, 3], yerr=std_list[:, 3], c='g', marker='^', label='Modified greedy')
    plt.errorbar(k_list, score_list[:, 1], yerr=std_list[:, 1], c='c', marker='o', label='SATURATE')
    plt.xlabel('Budget $\it{k}$', fontsize='20')
    plt.ylabel('Objective $\it{F}$', fontsize='20')
    # plt.yticks(np.arange(104, 115, 2))
    # plt.legend(fontsize='16')
    plt.gcf().subplots_adjust(left=0.15, bottom=0.15)
    if not os.path.exists('pictures'):
        os.mkdir('pictures')
    plt.savefig('pictures/results_' + dataset + '_k5-10_m3.png', bbox_inches='tight')
    plt.savefig('pictures/results_' + dataset + '_k5-10_m3.pdf', bbox_inches='tight')
    plt.show()


def draw_errorbar_m(dataset, k, m_list, times):
    DIR_PATH = 'output/output_' + dataset + '/'

    stds = []
    scores = []
    for m in m_list:
        g_score = []
        P_score = []
        S_score = []
        M_score = []
        for t in range(times):
            g_file = 'greedy_output_k' + str(k) + '_m' + str(m) + '_t' + str(t + 1) + '.txt'
            S_file = 'SATURATE_output_k' + str(k) + '_m' + str(m) + '_t' + str(t + 1) + '.txt'
            P_file = 'PORSM_output_k' + str(k) + '_m' + str(m) + '_t' + str(t + 1) + '.txt'
            M_file = 'ModifiedGreedy_output_k' + str(k) + '_m' + str(m) + '_t' + str(t + 1) + '.txt'

            with open(DIR_PATH + g_file, 'r') as f:
                lines = f.readlines()
            g_score.append(eval(lines[-1].split()[-1]))

            with open(DIR_PATH + S_file, 'r') as f:
                lines = f.readlines()
            S_score.append(eval(lines[-1].split()[-1]))

            with open(DIR_PATH + P_file, 'r') as f:
                lines = f.readlines()
            P_score.append(eval(lines[-1].split()[-1]))

            with open(DIR_PATH + M_file, 'r') as f:
                lines = f.readlines()
            M_score.append(eval(lines[-1].split()[-1]))

        stds.append([np.std(g_score), np.std(S_score), np.std(P_score), np.std(M_score)])
        scores.append([np.mean(g_score), np.mean(S_score), np.mean(P_score), np.mean(M_score)])

    plt.rcParams["errorbar.capsize"] = '4'
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Times New Roman'
    plt.rcParams['font.size'] = '18'
    plt.rcParams['lines.linestyle'] = '--'
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.markerfacecolor'] = 'none'
    plt.rcParams['lines.markeredgewidth'] = 1.5
    plt.rcParams['lines.markersize'] = 11
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['mathtext.rm'] = 'sans'
    plt.rcParams['mathtext.it'] = 'sans:italic'
    plt.rcParams['mathtext.default'] = 'it'

    std_list = np.array(stds)
    score_list = np.array(scores)
    # print(std_list)
    plt.errorbar(m_list, score_list[:, 2], yerr=std_list[:, 2], c='r', marker='s', label='EPORSS')
    plt.errorbar(m_list, score_list[:, 0], yerr=std_list[:, 0], c='b', marker='x', label='Greedy')
    plt.errorbar(m_list, score_list[:, 3], yerr=std_list[:, 3], c='g', marker='^', label='Modified greedy')
    plt.errorbar(m_list, score_list[:, 1], yerr=std_list[:, 1], c='c', marker='o', label='SATURATE')
    plt.xlabel('Budget $\it{k}$', fontsize='20')
    plt.ylabel('Objective $\it{F}$', fontsize='20')
    # plt.yticks(np.arange(104, 115, 2))
    # plt.legend(fontsize='16')
    plt.gcf().subplots_adjust(left=0.15, bottom=0.15)
    if not os.path.exists('pictures'):
        os.mkdir('pictures')
    plt.savefig('pictures/results_' + dataset + '_k' + str(k) + '_m2-6.png', bbox_inches='tight')
    plt.savefig('pictures/results_' + dataset + '_k' + str(k) + '_m2-6.pdf', bbox_inches='tight')
    plt.show()


def draw_change(dataset, k, m, times):
    DIR_PATH = 'output/output_' + dataset + '/'

    g_score = 0
    M_score = 0
    S_score = 0
    P_scores = []
    for t in range(times):
        g_file = 'greedy_output_k' + str(k) + '_m' + str(m) + '_t' + str(t + 1) + '.txt'
        S_file = 'SATURATE_output_k' + str(k) + '_m' + str(m) + '_t' + str(t + 1) + '.txt'
        P_file = 'PORSM_output_k' + str(k) + '_m' + str(m) + '_t' + str(t + 1) + '.txt'
        M_file = 'ModifiedGreedy_output_k' + str(k) + '_m' + str(m) + '_t' + str(t + 1) + '.txt'

        with open(DIR_PATH + g_file, 'r') as f:
            lines = f.readlines()
        g_score += eval(lines[-1].split()[-1])

        with open(DIR_PATH + S_file, 'r') as f:
            lines = f.readlines()
        S_score += eval(lines[-1].split()[-1])

        with open(DIR_PATH + P_file, 'r') as f:
            lines = f.readlines()
        scores = []
        for i in range(4, len(lines), 5 * 5):
            scores.append(eval(lines[i].split()[-1]))
        P_scores.append(scores)

        with open(DIR_PATH + M_file, 'r') as f:
            lines = f.readlines()
        M_score += eval(lines[-1].split()[-1])

    P_scores = np.mean(P_scores, axis=0)

    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Times New Roman'
    plt.rcParams['font.size'] = '18'
    plt.rcParams['lines.linestyle'] = '--'
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.markerfacecolor'] = 'none'
    plt.rcParams['lines.markeredgewidth'] = 1.5
    plt.rcParams['lines.markersize'] = 11
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['mathtext.rm'] = 'sans'
    plt.rcParams['mathtext.it'] = 'sans:italic'
    plt.rcParams['mathtext.default'] = 'it'

    plt.plot(P_scores, color='r', label='EPORSS')
    plt.axhline(y=g_score / times, color='b', label='Greedy')
    plt.axhline(y=M_score / times, color='g', label='Modified greedy')
    plt.axhline(y=S_score / times, color='c', label='SATURATE')
    # plt.axvline(x=0.6, ymax=(M_score/times-104.5)/3, linestyle=':', color='k')
    # plt.annotate('0.6$\it{kn}$', xy=(0.4, 104.5), xytext=(4, 104.7), arrowprops=dict(arrowstyle='-|>', color='k'),)
    plt.xlabel('Running time in $\it{kn}$', fontsize='20')
    plt.ylabel('Objective $\it{F}$', fontsize='20')
    plt.xlim(0, 27)
    # plt.yticks(np.arange(104.5, 108.0, 0.5))

    plt.legend(fontsize='16')
    plt.gcf().subplots_adjust(left=0.18, bottom=0.15)

    if not os.path.exists('pictures'):
        os.mkdir('pictures')
    plt.savefig('pictures/changes_' + dataset + '_k' + str(k) + '_m' + str(m) + '.png', bbox_inches='tight')
    plt.savefig('pictures/changes_' + dataset + '_k' + str(k) + '_m' + str(m) + '.pdf', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draw pictures')
    parser.add_argument('dataset', type=str, choices=['as', 'fb'], help='choose which dataset to draw pictures')
    parser.add_argument('--k', type=int, default=5, help='Budget k')
    parser.add_argument('--m', type=int, default=3, help='Objectives m')
    parser.add_argument('times', type=int, help='Number of results to use')

    k_list = list(range(5, 11))
    m_list = list(range(2, 7))
    draw_errorbar_k(parser.dataset, k_list, parser.m, parser.times)
    draw_errorbar_m(parser.dataset, parser.k, m_list, parser.times)
    draw_change(parser.dataset, parser.k, parser.m, parser.times)