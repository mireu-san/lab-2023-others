def solution(str1, str2):
    if str1 == str2:
        return 1

    l = len(str2)
    for i in range(len(str1) - 1):
        if str1[i : i + l].lower() == str2.lower():
            return 1
    return 2


# 다른이의 해답
def solution(str1, str2):
    return 1 if str2 in str1 else 2


# https://school.programmers.co.kr/learn/courses/30/lessons/120908
