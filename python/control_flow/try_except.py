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

