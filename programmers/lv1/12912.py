def solution(a, b):
    # range 로 합을 구하기 위한 사전정의 작업.
    if a > b:
        a, b = b, a

    # range 사용해서 a 와 b 사이의 모든 정수의 합(sum) 구하기
    return sum(range(a, b + 1))
