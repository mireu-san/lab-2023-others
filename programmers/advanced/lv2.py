import re


def solution(s):
    string1 = s[1 : len(s) - 1]
    flag = 0
    num_list = []
    for i in range(1, len(string1)):
        if string1[i] == "}":
            num = re.findall("\d+", string1[flag:i])
            # map will return anything as object in default. so convert it to int.
            num_list.append(list(map(int, num)))
            flag = i

        num_list.sort(key=lambda x: len(x))

        answer = []
        for a in range(0, len(num_list)):
            for b in range(0, len(num_list[a])):
                if not num_list[a][b] in answer:
                    answer.append(num_list[a][b])
        return answer
