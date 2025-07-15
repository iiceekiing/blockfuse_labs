#try:
    # Code that might cause a problem
#except:
    # What to do if a problem happens



# Example 1

''' What’s happening?

try: means: “Try this risky code”.

If it works, you get the result.

If it fails (e.g., dividing by 0), Python jumps into the except: and runs what’s inside it

'''


try:
    num = int(input("Enter a number to divide 10 by: "))
    result = 10 / num
    print("Result is:", result)

except:
    print("Oops! You can't divide by zero.")


# Example 2

'''  Catching Input Errors
What if someone types letters instead of a number?
'''


try:
    age = int(input("How old are you? "))
    print("Next year, you’ll be", age + 1)
except:
    print("Please enter a number, not text 🙃")


# Example 3
 
# Catching Specific Errors
# ZeroDivisionError: If someone enters 0

# ValueError: If someone enters abc

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("You can't divide by zero, champ.")
except ValueError:
    print("That's not a number!")


# Example 4 

 # With else and finally

try:
    number = int(input("Enter a number: "))
    print("Half of it is", number / 2)
except:
    print("Something went wrong!")
else:
    print("Yay! Everything worked.")
finally:
    print("This always runs, no matter what.")

