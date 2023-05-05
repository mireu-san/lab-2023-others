raw_list = ["Alice", "Rabbit", "Card", "Queen", "us", "kr"]
filtered = list(filter(lambda x: len(x) >= 3, raw_list))
print(filtered)
