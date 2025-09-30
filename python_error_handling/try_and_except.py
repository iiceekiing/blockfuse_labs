
# student_grade = {"Alice": 85, "Bob": 92, "Charlie": 78}
# name = input("Enter the student's name: ")
# grade = student_grade[name] 
# print(f"{name}'s grade is {grade}")

# try:
#     student_grade = {"Alice": 85, "Bob": 92, "Charlie": 78}
#     name = input("Enter the student's name: ")
#     grade = student_grade[name] 
#     print(f"{name}'s grade is {grade}")
# except KeyError:
#     print("Error: Student not found.")


# fruits = ["apple", "banana", "cherry", "date"]
# print(f"Available fruits: {fruits}")
# try:
#     position = int(input("Enter position number to fruit: "))
#     print(f"You got: {fruits[position]}")
# except:
#     print(f"Error: We don't have up to {position}.  fruit \n There no fruit in that position.")



user_input = input("Enter a number separated by comma: ")

try:
    numbers = user_input.split(",")
    for num in numbers:
        total += int(num)
    print(f"Sum of all numbers: {total}")

except:
    print("Error: Please enter only numbers separated by commas.")