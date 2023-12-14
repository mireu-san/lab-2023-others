def solution(n):
    answer = 0

    for i in range(1, n + 1):
        if n % i == 0:
            answer += i

    return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/12928


# list comprehension 방식
def solution(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)
