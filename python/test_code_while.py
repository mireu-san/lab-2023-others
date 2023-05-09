import random

result = random.randint(1, 100)


while True:
    user_input = int(input())
    if user_input > result:
        print("down")
    elif user_input < result:
        print("up")
    else:
        print("Correct!")
        print("Program terminated.")
        break
