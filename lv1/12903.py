# def solution(s):
#     if len(s) % 2 != 0:
#         find_index = len(s) // 2
#         result = s[find_index:find_index+1]
#     else:
#         find_index1 = (len(s) // 2 -1)
#         find_index2 = (len(s) // 2)
#         result = s[find_index1:find_index2 + 1]
#     return result

def solution(s):
    if len(s) % 2 != 0:
        result = s[len(s) // 2]
    else:
        result = s[(len(s) // 2 -1):(len(s) // 2) + 1]
    return result


print(solution(s='abcd'))