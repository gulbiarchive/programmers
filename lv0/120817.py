def solution(numbers):
    answer = 0
    
    result = 0
    count = 0
    
    for i in numbers:
        result += i
        count += 1
    
    answer = result / count
    
    
    return answer
