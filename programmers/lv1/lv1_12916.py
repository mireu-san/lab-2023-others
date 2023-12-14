def solution(s):
    answer = True
    pCount = yCount = 0

    for i in range(len(s)):
        if s[i].lower() == "p":
            pCount += 1
        elif s[i].lower() == "y":
            yCount += 1

    if pCount != yCount:
        answer = False

    return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/12916
# https://ykss.netlify.app/algorithm/programmers_7/
