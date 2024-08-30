def solution(s):

    s = s.lower()

    p = s.count('p')
    y = s.count('y')

# p, y 개수가 0이어도 둘의 개수가 0으로 같으므로 True 반환
    if p == y:
        return True
    else:
        return False

s = input()
print(solution(s))