# 약수의 개수와 덧셈
def solution(left, right):
    answer = 0 # 모든 숫자 누적해서 더하거나 뺀 값 return해야 되므로 밖에 초기화
    for i in range(left, right + 1):
        result = 0 # for 바깥쪽에 있으면 숫자 바뀔 때마다 초기화 안 됨
        for j in range(1, i + 1):
            if i % j == 0:
                result += 1
        
        if result % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer

left, right = map(int, input().split())
print(solution(left, right))