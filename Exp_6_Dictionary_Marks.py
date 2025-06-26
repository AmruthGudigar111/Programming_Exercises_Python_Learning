
students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 60
}

for name, marks in students.items():
    if marks > 75:
        print(name, ":", marks)
