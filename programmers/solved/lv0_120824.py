def solution(num_list):
    even_result = 0
    odd_result = 0

    for num in num_list:
        if num % 2 == 0:
            even_result += 1
        else:
            odd_result += 1
            
    return [even_result, odd_result]

# https://school.programmers.co.kr/learn/courses/30/lessons/120824