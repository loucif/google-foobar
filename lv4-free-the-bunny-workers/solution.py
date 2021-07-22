import math
import itertools


# def solution(num_buns, num_required):
#    # Your code here
#    l = [[] for _ in range(num_buns)]
#    l_ = list(itertools.combinations(
#        range(num_buns), num_buns - num_required + 1))
#    for i in range(int((math.comb(num_buns, num_required)*num_required)/(num_buns - num_required + 1))):
#        for j in l_[i]:
#            l[j].append(i)
#
#    return l

def solution(num_buns, num_required):
    # Your code here
    l = [[] for _ in range(num_buns)]
    l_len = len(list(itertools.combinations(
        range(num_buns), num_required)))*num_required
    l_ = list(itertools.combinations(
        range(num_buns), num_buns - num_required + 1))
    for i in range(int(l_len/(num_buns - num_required + 1))):
        for j in l_[i]:
            l[j].append(i)

    return l


print(solution(5, 3))
print(solution(2, 1))
print(solution(4, 4))
