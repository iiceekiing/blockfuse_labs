student = {
    "name": "Tom",
    "department": "Computer Science",
    "grades" : [{"csc 111": 90, "math": 50, "physics": 70}, [1, 2, 3, 4], {"bio": {"name": "joy", "age": 18}}],
    'address': {"city": "Jos", "town": "Rayfield", "Street": "Atiku Street"},
    "hobbies": ["Trading", "Reading", "Coding", "Praying"]
}
#print(student)
print('')
print('')

#student.pop("hobbies")
#print(student.i.tems())
#student["grades"].pop()
#student.pop()
#student["hobbies"].remove("Trading")
#student["grades"].pop("csc 111")


print(f"output should be  : {student["grades"][2]["bio"]["name"]}")


