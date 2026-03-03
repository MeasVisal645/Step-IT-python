
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
]

by_grade = {}

for student in students:
    grade = student["grade"]
    
if grade not in by_grade:
    by_grade[grade] = []
    by_grade[grade].append(student["name"])

print(by_grade)