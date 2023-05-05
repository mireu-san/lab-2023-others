members = [
    {"name": "Alice", "age": 16},
    {"name": "Rabbit", "age": 50},
    {"name": "Card", "age": 25},
    {"name": "Queen", "age": 60},
]

for idx, members in enumerate(members):
    print(f"Members {idx + 1}: {members['name']}, Age: ({members['age']})")
