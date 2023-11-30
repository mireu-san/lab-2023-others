def solution(money):
    price_cup_ea = 5500
    price_max = money // price_cup_ea
    rest_amount = money % price_cup_ea
    return [price_max, rest_amount]


# 다른 사람이 푼 것
def solution(money):
    answer = [money // 5500, money % 5500]
    return answer


def solution(money):
    return divmod(money, 5500)


def solution(money):
    cup = money // 5500
    change = money % 5500
    return [cup, change]


# https://school.programmers.co.kr/learn/courses/30/lessons/120819#qna
