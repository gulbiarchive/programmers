# 직사각형 별찍기
n, m = map(int, input().split())
for _ in range(m):
    for _ in range(1, n + 1):
        print('*', end = '')
    print()