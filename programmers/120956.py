import re


def solution(babbling):
    regex = re.compile("^(aya|ye|woo|ma)+$")
    cnt = 0
    for e in babbling:
        if regex.match(e):
            cnt += 1
    return cnt
