students = {}
total_students = 3

for i in range (total_students):
    student_name = input("please enter student name: ")
    department =  input("enter department: ")
    print("Please remeber to separate each score with a space  ")
    score = input("enter three  scores for this student: ").split()
    #print(score)

    data = {
        "name": student_name,
        "department": department,
        "test_score": score
    }
    students.update(data)

for i in students:
    print(i)


