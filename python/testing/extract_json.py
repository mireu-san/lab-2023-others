# https://www.pythontutorial.net/python-basics/python-write-text-file/
# https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file

import json


def writefile(func):
    def wrapper(a, b):
        result = func(a, b)
        data = {"a": a, "b": b, "a+b": result}
        with open("result.txt", "w") as f:
            f.write(json.dumps(data, indent=4))
        return result

    return wrapper


@writefile
def add(a, b):
    return a + b


add(10, 20)
