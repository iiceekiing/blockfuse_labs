"""
students = {}
total_students = 3

for i in range(total_students):
    student_name = input("Please enter student name: ")
    department = input("Enter department: ")
    print("Please remember to separate each score with a space")
    score = input("Enter three scores for this student: ").split()
    score = list(map(int, score))  # Convert all to integers

    data = {
        "name": student_name,
        "department": department,
        "test_score": score,
        "total": sum(score)
    }

    students[student_name] = data  # Use name as key to store each student

# To print each student's total score
for name, record in students.items():
    print(f"{name}'s total score is: {record['total']}")
""""


students = {
    "iceking": {"dp": "csc", "score": [60, 40, 20]}
}
students.update({"total": sum(score)})
for name, value in students.items():
    print(f"total score is: {name["total"]}")

