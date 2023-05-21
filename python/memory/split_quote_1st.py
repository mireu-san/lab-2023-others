quote = "There is a man who aims to change the world."

# split the string on whitespace here.
words = quote.split()

# get beginning word of each word here.
extractor = [word[0] for word in words]

# join the beginning words together.
joined_extractor = "".join(extractor)

# print the joined beginning words.
print(joined_extractor)
