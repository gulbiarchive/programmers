# 서울에서 김서방 찾기
def solution(seoul):

    for i in seoul:
        if i == "Kim":
            Kim_index = seoul.index(i)
    return f'김서방은 {Kim_index}에 있다'

print(solution(seoul=["Jane", "Kim"]))