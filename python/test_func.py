def 배수(n):
    def 적립(value):
        return (value * 0.1) * n

    return 적립


Feb = 배수(2)
Mar = 배수(3)

print(Feb(5000))
print(Mar(15000))
