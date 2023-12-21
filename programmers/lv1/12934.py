def solution(n):
    # 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단
    answer = 0
    num = n**0.5

    if num == int(num):
        # n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴
        answer = (num + 1) ** 2
    else:
        # 제곱이 아니라면 -1을 리턴하는 함수
        answer = -1

    return answer


# 가장 깔끔한 풀이. 문제를 기반으로 풀이.


# 아래는 math 써서 풀이하는 예시.
# import math

# def solution(n):
#     sqrt = math.sqrt(n)

#     if sqrt.integer():
#         return int((sqrt + 1) ** 2)
#     else:
#         return - 1
