def solution(arr):
    if len(arr) == 1:
        return [-1]

    min_value = min(arr)

    arr.remove(min_value)

    return arr


# somewhat fresh feeling. But obviously, this is easy one.
