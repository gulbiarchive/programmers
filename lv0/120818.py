def solution(price):
    answer = 0
# 1 - 0.05 = 0.95
# else 신경 쓰기
    if price >= 500000:
        return int(price * (1 - 0.2))
    elif price >= 300000:
        return int(price * (1 - 0.1))
    elif price >= 100000:
        return int(price * 0.95)
    else:
       answer = int(price)
    
    return answer