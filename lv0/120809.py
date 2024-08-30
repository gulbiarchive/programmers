def solution(numbers):
    answer = []
    
    for i in numbers:
        answer.append(i*2)

    return answer

print(solution(numbers=[1, 2, 100, -99, 1, 2, 3]))

