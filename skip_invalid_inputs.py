"""
Using continue to skip invalid inputs
🧩 Goal:
Ask the user to enter numbers between 1 and 10.

If the number is out of range, print "Invalid input" and skip the rest of the loop.

If it's valid, print "Accepted!".

Accept exactly 5 valid numbers (not 5 total attempts).



valid_entries = 0

while valid_entries < 5:
    number = int(input("Enter a number between 1 and 10: "))
    
    if number < 1 or number > 10:
        print("Invalid input")
        continue  # Skip to the next loop iteration
    
    print("Accepted!")
    valid_entries += 1  # Only increase for valid entries

print("You entered 5 valid numbers.")
"""

username = input("Create your username: ")
pwd = input("Create a 4 digit pin: ")
if len(pwd) != 4:
    print("invalid pin format, must be exactly 4 digit!")
    print("please try again!!!")

attempts = 0

print("your used  attempts is: ", attempts)
print("\nRemember your max attempts is 4 trial")

while attempts < 4:
    pin = int(input("Enter your pin for validation!: "))
    if pin != pwd:
        print("You've entered a wrong pin, please try again!")
    print("You've successfuly loged in to ekuke fountion academy")
    print("Welcome to ekuke foundation!: ", username)

