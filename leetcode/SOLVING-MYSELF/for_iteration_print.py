# check up problem - revision of for iteration

# Q1.
a, b = input().strip().split(' ')
b = int(b)

result = a * b
print(result)

# Q2. 대소문자 바꿔서 출력 - list comprehension
print(''.join(x.upper() if x.lower() else x.lower() for x in input()))
