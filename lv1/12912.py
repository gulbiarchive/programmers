# 두 정수 사이의 합
def solution(a, b):
    sum = 0
    if a > b:
        for i in range(b, a + 1):
            sum += i
        return sum
    elif b > a:
        for i in range(a, b + 1):
            sum += i
        return sum
    else:
        return a

a, b = map(int, input().split())
print(solution(a, b))