def indexing_list(words):
    target_list = ""
    for word in words:
        if len(word) > len(target_list):
            target_list = word

    return target_list


if __name__ == "__main__":
    words = ["greetings", "traveller!", "welcometoteyvatandtravelwithpaimon"]
    target_list = indexing_list(words)
    print(target_list)
