raw_list = ["Alice", "Rabbit", "Card", "Queen", "us", "kr"]
filtered = list(filter(lambda x: len(x) >= 3, raw_list))
print(filtered)

filtered_removal = [x for x in raw_list if x != "Card"]
print(filtered_removal)

multiple_removal = [x for x in raw_list if x not in ["us", "kr"]]
print(multiple_removal)
