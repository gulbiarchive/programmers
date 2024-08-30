def solution(s):
    # s = sorted(s, reverse=True)
    # return ''.join(s)

    # 한 줄 표현
    '''
    sorted()만 사용하면 오름차순이지만
    reverse = True 이기 때문에 내림차순
    sorted()는 리스트 반환하므로
    join()으로 다시 문자열 변환

    sort()는 리스트에만 사용할 수 있으므로 복잡하고
    sorted()는 문자열과 같은 모든 iterable 자료형 처리 가능
    '''
    return ''.join(sorted(s, reverse=True))

print(solution(s=input()))

'''
파이썬에서 문자열 정렬할 때 기본적으로 아스키 코드 값 사용
대문자가 소문자보다 작음
예) 대문자 A : 65, 소문자 a : 97

따라서 sorted() 함수를 사용할 때 기본적으로 대소문자를 구분하여
대문자를 소문자보다 작은 것으로 간주
'''