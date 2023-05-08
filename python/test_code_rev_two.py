d = {"first": 14, "second": 24, "third": 29}
max_key = max(d, key=d.get)
print("the key in max value: ", max_key)
print("max value: ", d[max_key])
