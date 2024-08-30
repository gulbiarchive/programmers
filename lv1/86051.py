# 없는 숫자 더하기
def solution(numbers):
    result = 0

    for i in range(10):
        if i not in numbers:
            result += i

    return result
   
print(solution(numbers=[1, 2, 3, 4, 6, 7, 8, 0]))