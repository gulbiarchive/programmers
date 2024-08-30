def solution(price, money, count):
    
    result = 0
    for i in range(1, count+1):
        result += price * i

    # if result - money > 0:
    #     return result - money
    # else:
    #     return 0

    '''
    파이썬의 삼항 조건 연산자 
    if - else 조건문 한 줄 표현

    true_answer if condition else false_answer

    condition이 참일 땐 true_anwer 반환
    condition이 거짓일 땐 flase_answer 반환
    '''

    # 금액 부족하지 않으면 0 반환 기억
    # reuslt가 작다는 건 money가 더 커서 부족하지 않으므로 0 반환
    return result - money if result > money else 0

print(solution(price=3, money=20, count=4))