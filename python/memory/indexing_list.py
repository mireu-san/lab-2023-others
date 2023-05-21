def indexing_list(characters):
    target_list = ""
    for word in characters:
        if len(word) > len(target_list):
            target_list = word

    return target_list


if __name__ == "__main__":
    genshin = ["greetings", "traveller!", "welcometoteyvatandtravelwithpaimon"]
    target_list = indexing_list(genshin)
    print(target_list)
