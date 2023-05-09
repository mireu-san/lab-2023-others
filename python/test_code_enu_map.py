children = ["Rei", "Shinji", "Asuka", "Touji", "Kaoru"]
for i, child in enumerate(children):
    print("the number {} is {}".format(i + 1, child))

# Using map() function:
result = list(map(lambda x: (x[0] + 1, x[1]), enumerate(children)))
print(result)

# used lambda here, in order to use map() function, since it requires a function object as its first argument.

# x[0]+1 meant to be incremented by 1
# x[1] corresponding value from list, children

# once map applies lambda function to each element of children...
# it passes each element as the input 'x' to lambda function.
# then that lambda function returns a tuple of index, which incremented by 1,
# And then, the corresponding value from the list, children.

# tl;dr - x:, which is part of lambda function.It defines the input parameter.
# (x[0]+1, x[1]), which defines the output of the lambda function.
