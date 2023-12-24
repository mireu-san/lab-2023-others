def solution(name, yearning, photo):
    # init
    result = []
    # name and yearnung are in info.
    info = dict(zip(name, yearning))

    # people in photo
    for people in photo:
        # init
        score = 0

        # number of person among in 'people'
        for person in people:
            # accumulate person only from 0.
            score += info.get(person, 0)

        # append the final 'score' to result.
        result.append(score)

    # updated result presented.
    return result


# https://school.programmers.co.kr/learn/courses/30/lessons/176963
