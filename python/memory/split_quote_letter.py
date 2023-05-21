quote = "There is a man who aims to change the world."

# split the string on whitespace here.
words = quote.split()

# get beginning letter of each word here.
extractor = [word[0] for word in words]

# join the beginning letters together.
joined_extractor = "".join(extractor)

# print the joined beginning letters.
print(joined_extractor)
