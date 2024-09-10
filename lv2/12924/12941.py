# 그냥 푸니까 효율성 0이어서 코드 줄여서 작성함
def solution(A,B):
    return sum(map(lambda a,b : a*b, sorted(A), sorted(B, reverse = True)))