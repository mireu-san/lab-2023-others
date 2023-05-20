quote = "There is a man who aims to change the world."

# split the string on whitespace here.
words = quote.split()

# get first letter of each word here.
first_letters = [word[0] for word in words]

# join the first letters together.
joined_first_letters = "".join(first_letters)

# print the joined first letters.
print(joined_first_letters)
