import numpy as np
import math
import os
from scipy import optimize

N_YATSUHASHIS = 11
N_WORKERS = 9
LAMBDA = 0.1

path_src = os.path.abspath(os.path.dirname(__file__))
path_data = path_src + '/../data'

arr_a1 = np.genfromtxt('{0}/a1.tsv'.format(path_data), delimiter='\t')
arr_a2 = np.genfromtxt('{0}/a2.tsv'.format(path_data), delimiter='\t')
arr_a3 = np.genfromtxt('{0}/a3.tsv'.format(path_data), delimiter='\t')
arr_a4 = np.genfromtxt('{0}/a4.tsv'.format(path_data), delimiter='\t')
arr_a5 = np.genfromtxt('{0}/a5.tsv'.format(path_data), delimiter='\t')
arr_a6 = np.genfromtxt('{0}/a6.tsv'.format(path_data), delimiter='\t')
arr_a7 = np.genfromtxt('{0}/a7.tsv'.format(path_data), delimiter='\t')
arr_a8 = np.genfromtxt('{0}/a8.tsv'.format(path_data), delimiter='\t')
arr_a9 = np.genfromtxt('{0}/a9.tsv'.format(path_data), delimiter='\t')

arr_all = arr_a1 + arr_a2 + arr_a3 + arr_a4 + arr_a5 + arr_a6 + arr_a7 + arr_a8 + arr_a9

dict_member_data = {
    "a1": arr_a1,
    "a2": arr_a2,
    "a3": arr_a3,
    "a4": arr_a4,
    "a5": arr_a5,
    "a6": arr_a6,
    "a7": arr_a7,
    "a8": arr_a8,
    "a9": arr_a9
}


def L(eta, score):
    result = 0
    for member, data in dict_member_data.items():
        for i in range(N_YATSUHASHIS):
            for j in range(N_YATSUHASHIS):
                if(data[i][j] == 1):
                    denominator = math.exp(score[i]) + math.exp(score[j])
                    result += math.log(eta[member] * math.exp(score[i]) / denominator + (1 - eta[member]) * math.exp(score[j]) / denominator)
    return result


def R(s0, score):
    result = 0
    for i in score:
        denominator = math.exp(s0) + math.exp(i)
        result += math.log(math.exp(s0) / denominator) + math.log(math.exp(i) / denominator)
    return result


def obj_func(x0):
    eta = {'a{0}'.format(i + 1): x0[i] for i in range(N_YATSUHASHIS)}
    score = x0[N_WORKERS:N_WORKERS + N_YATSUHASHIS]
    s0 = x0[N_WORKERS + N_YATSUHASHIS]
    return - (L(eta, score) + LAMBDA * R(s0, score))


def obj_func_BT(x0):
    eta = {'a{0}'.format(i + 1): x0[i] for i in range(N_YATSUHASHIS)}
    score = x0[N_WORKERS:N_WORKERS + N_YATSUHASHIS]
    return - L(eta, score)


def outputPrimaryEigenvectorResults():
    rankingVector = np.ones([N_YATSUHASHIS, 1])  # r_0 = (1, 1, ..., 1)^T とする
    normRankingVector = np.linalg.norm(rankingVector)
    normPrefernceMatrix = np.linalg.norm(arr_all)

    rankingVector /= normRankingVector  # r_0 / |r_0| を計算

    for i in range(100):
        rankingVector = np.dot(arr_all, rankingVector) / normPrefernceMatrix

    result_score = (rankingVector / np.linalg.norm(rankingVector)).flatten()

    for i in range(N_YATSUHASHIS):
        print('Score of Yatsuhashi y{0} = {1:.3f}'.format(i + 1, result_score[i]))


def outputBradleyTerryResults():
    x0 = [1 for i in range(N_WORKERS)] + [0.5 for i in range(N_YATSUHASHIS)] + [0.5, ]

    bnds_BT = [(1, 1) for i in range(N_WORKERS)] + [(None, None) for i in range(N_YATSUHASHIS)] + [(None, None), ]
    cons_BT = {'type': 'eq', 'fun': lambda x: x[9] + x[10] + x[11] + x[12] + x[13] + x[14] + x[15] + x[16] + x[17] + x[18] + x[19]}

    result = optimize.minimize(obj_func_BT, x0=x0, bounds=bnds_BT, constraints=cons_BT, method='SLSQP')

    result_score = result.x[N_WORKERS:N_WORKERS + N_YATSUHASHIS]

    for i in range(N_YATSUHASHIS):
        print('Score of Yatsuhashi y{0} = {1:.3f}'.format(i + 1, result_score[i]))


def outputCrowdBTResults():
    x0 = [1 for i in range(N_WORKERS)] + [0.5 for i in range(N_YATSUHASHIS)] + [0.5, ]
    bnds_CrowdBT = [(0, 1) for i in range(N_WORKERS)] + [(None, None) for i in range(N_YATSUHASHIS)] + [(None, None), ]

    result = optimize.minimize(obj_func, x0=x0, bounds=bnds_CrowdBT, method='SLSQP')

    result_eta = result.x[:N_WORKERS]
    result_score = result.x[N_WORKERS:N_WORKERS + N_YATSUHASHIS]

    for i in range(N_YATSUHASHIS):
        print('Score of Yatsuhashi y{0} = {1:.3f}'.format(i + 1, result_score[i]))

    for i in range(N_WORKERS):
        print('Eta of Worker a{0} = {1:.3f}'.format(i + 1, result_eta[i]))


if __name__ == '__main__':
    print('Results of primary eigenvector:')
    outputPrimaryEigenvectorResults()
    print('')

    print('Results of Bradley-Terry model:')
    outputBradleyTerryResults()
    print('')

    print('Results of Crowd-BT model:')
    outputCrowdBTResults()
