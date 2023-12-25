def solution(numbers):
    init = 0

    for i in range(10):
        if i not in numbers:
            init += i
    return init


# https://school.programmers.co.kr/learn/courses/30/lessons/86051
