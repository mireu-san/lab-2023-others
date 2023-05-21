def letters(strings):
    if not strings:
        return ""

    indexing_str = min(strings, key=len)

    for i in range(len(indexing_str)):
        if not all(s.startswith(indexing_str[: i + 1]) for s in strings):
            return indexing_str[:i]

    return indexing_str


print(letters(["Mondstadt", "Mond", "MondMond", "Mondori", "Mondtown"]))
