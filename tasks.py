students = {
    "iceking": {"dp": "csc", "score": [60, 40, 20]}
}

for name, value in students.items():
    total = sum(students[name]['score'])
    print("total score is: " total)
