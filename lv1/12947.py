def solution(x):
    result = sum([int(i) for i in str(x)])

    # 비교 연산의 반환은 True or False
    return x % result == 0

    
    
print(solution(10))