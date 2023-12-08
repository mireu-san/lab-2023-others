# note: 이 문제에는 for range 로 하면 안되는게, 변환을 해야 하는 경우임.
# 목적은 문자열을 int 로 변환해야 하는데, 입력값이니 그냥 int 로 변환하는 구성으로도 OK.
# 예: return int(s)


def solution(s):
    result = 0
    # 문자열 s 를 뒤집어서, 각 숫자인 idx 를 이용해 숫자를 역순으로 처리
    for idx, number in enumerate(s[::-1]):
        if number == "-":
            # 문자가 "-" 이면, 전체 결과의 부호 변경. 요컨데, +로 만들어 줌.
            result *= -1
        else:
            # 각 숫자에 해당하는 자릿수의 가치(10의 idx 제곱)를 곱하여 결과에 더함
            result += int(number) * (10**idx)
    return result


# https://school.programmers.co.kr/learn/courses/30/lessons/12925
