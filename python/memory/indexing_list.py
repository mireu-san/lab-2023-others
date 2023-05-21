def indexing_list(characters):
    target_list = ""
    for character in characters:
        if len(character) > len(target_list):
            target_list = character

    return target_list


if __name__ == "__main__":
    paimon = ["greetings", "traveller!", "welcometoteyvatandtravelwithpaimon"]
    target_list = indexing_list(paimon)
    print(target_list)
