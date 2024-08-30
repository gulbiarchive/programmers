# JadenCase 문자열 만들기
def solution(s):
    s = s.split(' ')
    result = []

    for i in s:
        result.append(i.capitalize())
    # 변환된 리스트의 단어를 하나의 문자열로 합침
    return ' '.join(result)

'''
대소문자 확인 함수
islower()
isupper()
capitalize() : 맨 첫글자만 대문자로 변환
title() : 알파벳 외의 문자(숫자, 특수기호, 띄어쓰기 등)로 나누어져 있는 영단어들의 첫 글자 모두 대문자로 변환
'''

'''
s1 = 'hello  world'
s2 = '  hello world  '

# split()
print(s1.split())  # ['hello', 'world']
print(s2.split())  # ['hello', 'world']

# split(' ')
print(s1.split(' '))  # ['hello', '', 'world']
print(s2.split(' '))  # ['', '', 'hello', 'world', '', '']


# 결과
['hello', 'world']
['hello', 'world']
['hello', '', 'world']
['', '', 'hello', 'world', '', '']

split() vs split(' ')
split()
연속된 공백은 하나의 공백으로 취급된다.
이는 split() 함수가 인자 없이 호출될 때
모든 공백 문자(스페이스, 탭, 개행 등)를 구분자로 취급하고,
연속되 공백을 하나의 구분자로 간주하기 때문이다.

반면 split(' ')을 사용하면,
연속된 스페이스는 각각 별도의 구분자로 취급되어,
'hello', 'world'사이에 빈 문자열을 추가로 반환한다.

또한, 문자열의 시작과 끝에 있는 공백도 각각 별도의 구분자로 취급되어
시작과 끝에도 빈 문자열을 반환
'''