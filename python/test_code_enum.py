children = ["Rei", "Shinji", "Asuka", "Touji", "Kaoru"]
for i, child in enumerate(children):
    print("the number {} is {}".format(i + 1, child))

# Using list comprehension:
result = [(i, child) for i, child in enumerate(children)]
print(result)
