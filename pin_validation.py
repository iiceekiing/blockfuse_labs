username = input("Create your username: ")

pwd = input("Create a 4-digit pin: ")

# Check if pin is exactly 4 digits and all digits
if len(pwd) != 4 or not pwd.isdigit():
    print("Invalid pin format, must be exactly 4 digits!")
    print("Please try again!!!")
    exit()  # Stop the program if pin is invalid

print("\nYour pin has been set successfully!", username)

# Now we track login attempts
attempts = 0

print("Your used attempts is:", attempts)
print("Remember your max attempts is 4 trials\n")

while attempts < 4:
    pin = input("Enter your pin for validation: ")
    
    if pin != pwd:
        print("You've entered a wrong pin, please try again!")
        attempts += 1
        print("Attempts left:", 4 - attempts)
    else:
        print("You've successfully logged in to Ekuke Foundation Academy")
        print("Welcome to Ekuke Foundation,", username)
        break  # End the loop after successful login

# Optional: block access after 4 failed attempts
if attempts == 4:
    print("\nToo many failed attempts. Access denied.")

