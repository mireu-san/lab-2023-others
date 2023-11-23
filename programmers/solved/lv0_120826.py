def solution(my_string, letter):
    answer = ""

    for char in my_string:
        if char != letter:
            answer += char
    return answer


def solution(my_string, letter):
    return my_string.replace(letter, "")


# https://school.programmers.co.kr/learn/courses/30/lessons/120826#qna
