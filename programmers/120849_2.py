def solution(my_string):
    string = "aeiou"
    for i in string:
        my_string = my_string.replace(i, "")
    return my_string


# import re

# def solution(my_string):
#     return re.sub(r"[aeiou]", "", my_string)
