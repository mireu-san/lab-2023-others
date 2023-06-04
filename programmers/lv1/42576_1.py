# one level of sort/loop


def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant) - 1]


print(
    solution(
        ["marina", "josipa", "nikola", "vinko", "filipa"],
        [["josipa", "filipa", "marina", "nikola"]],
    )
)
