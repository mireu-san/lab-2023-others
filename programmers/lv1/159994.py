def solution(cards1, cards2, goal):
    i, j, k = 0, 0, 0  # i, j, k는 각각 cards1, cards2, goal 배열을 가리키는 인덱스.

    while k < len(goal):
        if i < len(cards1) and cards1[i] == goal[k]:
            i += 1
        elif j < len(cards2) and cards2[j] == goal[k]:
            j += 1
        else:
            return "No"  # 만약 goal[k]가 어느 카드 뭉치에도 없다면, "No"로 반환.
        k += 1

    return "Yes"  # 모든 goal 배열을 순회하면, "Yes"로 반환.
