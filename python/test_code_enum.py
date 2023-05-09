children = ["Rei", "Shinji", "Asuka", "Touji", "Kaoru"]
for i, child in enumerate(children):
    print("the number {} is {}".format(i + 1, child))

# # Using list comprehension:
# result = [(i, child) for i, child in enumerate(children)]
# print(result)

# list comprehension (renewed)
result = list(enumerate(children, 1))
print(result)

# wrong example to use map here.
# Why? Because enumerate is bulit-in python function.
# result = list(map(enumerate(children, 1)))
