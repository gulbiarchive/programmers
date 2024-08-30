# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    # 배열의 어떤 요소도 divisor로 나누어 떨어지지 않을 떄 처리하기 위한 것
    # 즉, answer가 비어있는지 확인 비어있다면 -1 추가
    if not answer:
            answer.append(-1)
    answer.sort()
    return answer

print(solution(arr=[5, 9, 7, 10], divisor=5))