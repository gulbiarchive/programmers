def solution(money):
    answer = []
    count = money // 5500

    for i in range(count):
        money -= 5500

  

    answer.append(count)
    answer.append(money)
    
    return answer 

