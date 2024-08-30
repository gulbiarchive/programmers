# 음양 더하기
def solution(absolutes, signs):
    result = 0

    for i in range(len(absolutes)):
        if signs[i] == True:
            result += absolutes[i]
        else:
            result -= absolutes[i]
    return result

print(solution(absolutes=[4, 7, 12], signs=[True, False, True]))