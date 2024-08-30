def solution(array):
    answer = 0
    count = 0
    for _ in array:
        count += 1
    
    A = count // 2
    B = count % 2 
    
    array.sort()
    answer = array[A + B - 1]
    return answer