def solution(myString):
    capitalise = myString.upper()

    return capitalise


# better option


def solution(myString):
    answer = ""
    for i in myString:
        if i.islower:
            answer += i.upper()
        else:
            answer += i

    return answer
