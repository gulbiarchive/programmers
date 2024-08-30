# 핸드폰 번호 가리기
def solution(phone_number):
    # 슬라이싱 기법
    return '*' * len(phone_number[:-4]) + phone_number[-4:]

print(solution(phone_number='027778888'))