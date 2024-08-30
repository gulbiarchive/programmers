# 내적
def solution(a, b):
    result = 0
    
    '''
    zip(a, b): 두 리스트 a, b를 같은 인덱스의 요소들끼리 묶어주는 역할
    a의 첫 번째 요소와 b의 첫 번째 요소, a의 두 번째 요소와 b의 두 번째 요소
    '''
    for x, y in zip(a, b):
        result += x * y
    
    return result