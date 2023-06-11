def solution(clothes):
    hash_map = {}
    for cloth, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1

    answer = 1
    for type in hash_map:
        answer *= hash_map[type] + 1

    return answer - 1


print(
    solution(
        [["crowmark", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
    )
)
