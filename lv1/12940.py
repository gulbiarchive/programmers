# 최대공약수와 최소공배수
import math

def solution(n, m):
    result = []
    result.append(math.gcd(n,m))
    result.append(math.lcm(n, m))
    return result

n, m = map(int, input().split())
print(solution(n, m))