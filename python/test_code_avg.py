student_score = {
    "홍의": 97,
    "원희": 60,
    "동해": 77,
    "변수": 79,
    "창현": 89,
}

print(student_score)

avg = 0
for i in student_score.values():
    avg += i

avg = avg / len(student_score)

print(str(avg))
