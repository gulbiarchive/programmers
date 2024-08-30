# 길이가 4, 6인 거 확인
def solution(s):
    if (len(s) in (4, 6)) and s.isdigit():
        return True
    else:
        return False