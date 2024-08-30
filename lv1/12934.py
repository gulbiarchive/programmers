def solution(n):
    # 주어진 수의 제곱근을 구함
    x = int(n ** 0.5)
    # 만약 주어진 수가 양의 정수 x의 제곱이라면 (x+1)의 제곱을 반환
    if x * x == n:
        return (x + 1) ** 2
    else:
        return -1
    
print(solution(121))