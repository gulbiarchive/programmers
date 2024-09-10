def solution(s):
    count = 0 # 변환 횟수
    zeros_removed = 0 # 제거된 0 개수

    while s != '1':
        # 제거된 0 개수
        zeros = s.count('0')
        zeros_removed += zeros

        s = s.replace('0', '') # 0 제거
        length = len(s) # 남은 문자열 길이 구하기

        s = bin(length)[2:]

        count += 1
    
    return [count, zeros_removed]

print(solution(s = input()))