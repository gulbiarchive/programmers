# 삼총사
from itertools import combinations

def solution(number):
    answer = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            answer += 1
    return answer

'''
combinations('ABCD', 2)
AB AC AD BC BD CD 
'''