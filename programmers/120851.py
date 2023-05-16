def solution(my_string):
    s = 0
    for i in my_string:
        if i.isdigit():
            s += int(i)
    return s
