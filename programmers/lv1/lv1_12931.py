def solution(n):
    num = str(n)
    add = 0

    for i in range(len(num)):
        add += int(num[i])
    return add


# 다른 풀이
def solution(n):
    if n < 10:
        return n

    return n % 10 + solution(n // 10)


print(solution(123))


# 또 다른 풀이
def solution(n):
    num_to_string = str(n)

    sum_of_digits = sum(int(digit) for digit in num_to_string)

    return sum_of_digits
