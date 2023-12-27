# 문제 해석에 시간이 걸린 문제
def solution(arr, divisor):
    answer = []

    for num in arr:
        if num % divisor == 0:
            answer.append(num)

    if len(answer) == 0:
        answer = [-1]

    return list(sorted(answer))


# 다른 풀이 예시
def solution(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]
