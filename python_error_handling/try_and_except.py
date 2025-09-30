
# student_grade = {"Alice": 85, "Bob": 92, "Charlie": 78}
# name = input("Enter the student's name: ")

# try:
#     grade = student_grade[name] 
#     print(f"{name}'s grade is {grade}")

# except KeyError:
#     print("Error: Student not found.")

# except Exception as ekuke:
#     print(f"An unexpected error occurred: {ekuke}")


# fruits = ["apple", "banana", "cherry", "date"]
# print(f"Available fruits: {fruits}")
# try:
#     position = int(input("Enter position number to fruit: "))
#     print(f"You got: {fruits[position]}")

# except IndexError:
#     print(f"Error: We don't have up to {position}.  fruit \n There no fruit in that position.")

# except ValueError:
#     print("Error: Please enter a valid number.")

# except Exception as ekuke:
#     print(f"An unexpected error occurred: {ekuke}")


# user_input = input("Enter a number separated by comma: ")
# total = 0   

# try:
#     numbers = user_input.split(",")
#     for num in numbers:
#         total += int(num)
#     print(f"Sum of all numbers: {total}")

# except ValueError:
#     print("Error: Please enter only numbers separated by commas.")

# except Exception as ekuke:
#     print(f"An unexpected error occurred: {ekuke}")

@class

def enums_(cls):
    cls._members_ = {k: v for v, k in enumerate(cls.__dict__) if not k.startswith('_')}
    return cls

@enums_
class AccountType:
    SAVINGS = "savings"
    CURRENT = "current"
    BUSINESS = "business"

print(AccountType._members_)