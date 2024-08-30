# 3진법 뒤집기
def solution(n):
    answer = ''
    
    while n > 0:
        n, r = divmod(n, 3)
        answer += str(r)
    
    return int(answer, 3)
