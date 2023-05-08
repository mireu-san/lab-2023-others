math_score = {"Alice": 80, "Rabbit": 90, "Queen": 100}
top_math_score = max(math_score, key=math_score.get)
print("highest grade earner:", top_math_score)
