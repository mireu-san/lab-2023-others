def writefile(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        output = {"a": args[0], "b": args[1], "a+b": result}
        with open("result.txt", "w") as file:
            file.write(str(output))
        return result

    return wrapper


@writefile
def add(a, b):
    return a + b
