def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i


# https://school.programmers.co.kr/learn/courses/30/lessons/87389


# 다른 사람의 풀이 예시(참고용)
def solution(n):
    return min([i for i in range(2, n) if n % i == 1])


def solution(n):
    return [x for x in range(1, n + 1) if n % x == 1][0]
