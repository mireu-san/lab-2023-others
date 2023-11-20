def solution(numbers):
    answer = sum(numbers) / len(numbers)
    return answer


# 다른 사람의 풀이
import numpy as np


def solution(numbers):
    return np.mean(numbers)
