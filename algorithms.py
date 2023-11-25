import numpy as np
import os
import time


class Algorithms():
    def __init__(self, V, functions, k):
        '''
        :param V: ground set
        :param functions: objective functions
        :param k: size constraint
        '''

        self.N = len(V)
        assert k < self.N
        self.V = V
        self.functions = functions
        self.m = len(self.functions)
        self.k = k
        self.eval_num = 0
        return

    def F(self, x):
        return np.min([function(x) for function in self.functions])

    def Greedy(self, times, directory):
        '''
        :param times: the times-th run
        :param directory: directory of output file
        :return: best subset
        '''

        print('\nGreedy Algorithm Start, k={}, m={}'.format(self.k, self.m))
        if not os.path.exists('output'):
            os.mkdir('output')
        if not os.path.exists(os.path.join('output', directory)):
            os.mkdir(os.path.join('output', directory))
        output_file = open('output/' + directory + '/Greedy_k' + str(self.k)
                           + '_m' + str(self.m) + '_t' + str(times) + '.txt', 'w+')

        self.eval_num = 0
        X_j = []
        X_j_complement = list(set(self.V) - set(X_j))
        start = time.perf_counter()
        while len(X_j) < self.k:
            last = time.perf_counter()

            F_max = - np.infty
            v_star = X_j_complement[0]
            for v in X_j_complement:
                temp = X_j.copy()
                temp.append(v)
                value = self.F(temp)
                self.eval_num += 1
                if value > F_max:
                    v_star = v
                    F_max = value

            X_j.append(v_star)
            X_j_complement = list(set(self.V) - set(X_j))

            now = time.perf_counter()
            score = self.F(X_j)
            print('Time used to select {} elements: {:.2f}s'.format(len(X_j), now - start))
            print('Time used to select this element: {:.2f}s'.format(now - last))
            print('Number of evaluations: {}'.format(self.eval_num))
            print('The subset is: {}'.format(X_j))
            print('Score of the subset: {}'.format(score))

            print('Time used to select {} elements: {:.2f}s'.format(len(X_j), now - start),
                  file=output_file, flush=True)
            print('Time used to select this element: {:.2f}s'.format(now - last), file=output_file, flush=True)
            print('Number of evaluations: {}'.format(self.eval_num), file=output_file, flush=True)
            print('The subset is: {}'.format(X_j), file=output_file, flush=True)
            print('Score of the subset: {}'.format(score), file=output_file, flush=True)

        output_file.close()

        return X_j

    def ModifiedGreedy(self, times, directory):
        '''
        :param times: the times-th run
        :param directory: directory of output file
        :return: best subset
        '''

        print('\nModified Greedy Algorithm Start, k={}, m={}'.format(self.k, self.m))
        if not os.path.exists('output'):
            os.mkdir('output')
        if not os.path.exists(os.path.join('output', directory)):
            os.mkdir(os.path.join('output', directory))
        output_file = open('output/' + directory + '/ModifiedGreedy_k' + str(self.k)
                           + '_m' + str(self.m) + '_t' + str(times) + '.txt', 'w+')

        self.eval_num = 0
        X_j = []
        X_j_complement = list(set(self.V) - set(X_j))
        start = time.perf_counter()
        value_last = [0] * self.m
        while len(X_j) < self.k:
            last = time.perf_counter()

            fi_max = [0] * self.m
            for v in X_j_complement:
                temp = X_j.copy()
                temp.append(v)
                values = [self.functions[i](temp) - value_last[i] for i in range(self.m)]
                self.eval_num += 1
                for i in range(self.m):
                    if values[i] > fi_max[i]:
                        fi_max[i] = values[i]

            F_max = 0
            v_star = X_j_complement[0]
            for v in X_j_complement:
                temp = X_j.copy()
                temp.append(v)
                value = np.min([(self.functions[i](temp) - value_last[i]) / fi_max[i] for i in range(self.m)])
                self.eval_num += 1
                if value > F_max:
                    v_star = v
                    F_max = value

            X_j.append(v_star)
            value_last = [f(X_j) for f in self.functions]
            X_j_complement = list(set(self.V) - set(X_j))

            now = time.perf_counter()
            score = self.F(X_j)
            print('Time used to select {} elements: {:.2f}s'.format(len(X_j), now - start))
            print('Time used to select this element: {:.2f}s'.format(now - last))
            print('Number of evaluations: {}'.format(self.eval_num))
            print('The subset is: {}'.format(X_j))
            print('Score of the subset: {}'.format(score))

            print('Time used to select {} elements: {:.2f}s'.format(len(X_j), now - start),
                  file=output_file, flush=True)
            print('Time used to select this element: {:.2f}s'.format(now - last), file=output_file, flush=True)
            print('Number of evaluations: {}'.format(self.eval_num), file=output_file, flush=True)
            print('The subset is: {}'.format(X_j), file=output_file, flush=True)
            print('Score of the subset: {}'.format(score), file=output_file, flush=True)

        output_file.close()

        return X_j

    def Fbar_c(self, A, c):
        self.eval_num += 1
        return np.mean([min(function(A), c) for function in self.functions])

    def GPC(self, c, alpha):
        A = []
        Fbar_c_A = self.Fbar_c(A, c)
        while Fbar_c_A < c:
            A_complement = list(set(self.V) - set(A))
            deltas = [self.Fbar_c(A + [s], c) - Fbar_c_A for s in A_complement]
            best_index = np.argmax(deltas)
            s_best = A_complement[best_index]
            A.append(s_best)
            Fbar_c_A += deltas[best_index]
            if len(A) > alpha * self.k:
                return False
        return A

    def SATURATE(self, alpha, times, directory):
        '''
        :param times: the times-th run
        :param directory: directory of output file
        :return: best subset
        '''

        print('\nSATURATE Algorithm Start, k={}, m={}'.format(self.k, self.m))
        if not os.path.exists('output'):
            os.mkdir('output')
        if not os.path.exists(os.path.join('output', directory)):
            os.mkdir(os.path.join('output', directory))
        output_file = open('output/' + directory + '/SATURATE_k' + str(self.k)
                           + '_m' + str(self.m) + '_t' + str(times) + '.txt', 'w+')

        self.eval_num = 0
        c_min = 0
        c_max = self.F(self.V)
        A_best = []
        iters = 0
        start = time.perf_counter()
        while c_max - c_min >= 1/self.m:
            iters += 1
            last = time.perf_counter()

            c = (c_min + c_max) / 2
            A_hat = self.GPC(c, alpha)
            if not A_hat:
                c_max = c
            else:
                c_min = c
                A_best = A_hat

            now = time.perf_counter()
            score = self.F(A_best)
            print('Time used for {} iterations: {:.2f}s'.format(iters, now - start))
            print('Time used for one iteration: {:.2f}s'.format(now - last))
            print('Number of evaluations: {}'.format(self.eval_num))
            print('The subset is: {}'.format(A_best))
            print('Score of the subset: {}'.format(score))

            print('Time used for {} iterations: {:.2f}s'.format(iters, now - start),
                  file=output_file, flush=True)
            print('Time used for one iteration: {:.2f}s'.format(now - last), file=output_file, flush=True)
            print('Number of evaluations: {}'.format(self.eval_num), file=output_file, flush=True)
            print('The subset is: {}'.format(A_best), file=output_file, flush=True)
            print('Score of the subset: {}'.format(score), file=output_file, flush=True)

        output_file.close()

        return A_best

    def vector2subset(self, x):
        return [self.V[i] for i in range(self.N) if x[i]]

    def objective_function(self, x):
        x = self.vector2subset(x)
        self.eval_num += 1
        if len(x) >= 2 * self.k:
            return [-np.inf, -len(x)]
        else:
            return [self.F(x), -len(x)]

    def mutation(self, x):
        rand_rate = 1.0 / (self.N)
        change = np.random.binomial(1, rand_rate, self.N)
        return np.abs(x - change)

    def dominates(self, x_values, y_values, weakly=0):
        f_any = 1
        f_exist = 0
        for o0, o1 in zip(x_values, y_values):
            if o0 < o1:
                f_any = 0
            if o0 > o1:
                f_exist = 1
        if weakly:
            return f_any
        else:
            return (f_any and f_exist)

    def get_best_subset(self, objective_value):
        objective_value = np.array(objective_value)
        P_legal = [i for i in range(len(objective_value)) if -objective_value[i][1] <= self.k]
        assert len(P_legal) > 0, 'No legal solution'
        Fvalues = objective_value[P_legal][:, 0]
        best = np.argmax(Fvalues)
        return P_legal[best]

    def EPORSS(self, times, directory):
        '''
            :param times: the times-th run
            :param directory: directory of output file
            :return: best subset
            '''

        print("\nEPORSS Algorithm Start, k={}, m={}".format(self.k, self.m))
        if not os.path.exists('output'):
            os.mkdir('output')
        if not os.path.exists(os.path.join('output', directory)):
            os.mkdir(os.path.join('output', directory))
        output_file = open('output/' + directory + '/EPORSS_k' + str(self.k)
                           + '_m' + str(self.m) + '_t' + str(times) + '.txt', 'w+')

        self.eval_num = 0
        P = [np.zeros(self.N, dtype=int)]
        objective_value = [self.objective_function(P[0])]
        T = int(2 * np.e * self.k * self.k * self.N)
        start = time.perf_counter()
        last = start
        for t in range(T):
            if t % self.N == 0:
                last = time.perf_counter()

            x = P[np.random.randint(len(P))]
            offspring = self.mutation(x)
            offspring_value = self.objective_function(offspring)

            dominated_set = []
            for i in range(len(P)):
                if self.dominates(objective_value[i], offspring_value, weakly=0):
                    break
                if self.dominates(offspring_value, objective_value[i], weakly=1):
                    dominated_set.append(i)
            else:
                P_1 = []
                objective_value_1 = []
                for i in range(len(P)):
                    if i not in dominated_set:
                        P_1.append(P[i])
                        objective_value_1.append(objective_value[i])
                P = P_1
                objective_value = objective_value_1
                P.append(offspring)
                objective_value.append(offspring_value)

            if (t + 1) % self.N == 0:
                now = time.perf_counter()
                best_subset = self.get_best_subset(objective_value)
                score = objective_value[best_subset][0]
                print('Time used for {}N iterations: {:.2f}s'.format((t + 1) // self.N, now - start))
                print('Time used for N iterations: {:.2f}s'.format(now - last))
                print('Number of evaluations: {}'.format(self.eval_num))
                print('The subset is: {}'.format(self.vector2subset(P[best_subset])))
                print('Score of the subset: {}'.format(score))

                print('Time used for {}N iterations: {:.2f}s'.format((t + 1) // self.N, now - start),
                      file=output_file, flush=True)
                print('Time used for N iterations: {:.2f}s'.format(now - last), file=output_file, flush=True)
                print('Number of evaluations: {}'.format(self.eval_num), file=output_file, flush=True)
                print('The subset is: {}'.format(self.vector2subset(P[best_subset])), file=output_file, flush=True)
                print('Score of the subset: {}'.format(score), file=output_file, flush=True)

        output_file.close()

        best_subset = self.get_best_subset(objective_value)
        return self.vector2subset(P[best_subset])
