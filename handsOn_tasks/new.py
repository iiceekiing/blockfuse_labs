pwd = input("Enter your password let me hash for your: ")

first = pwd[0]
last = pwd[-1]

visible = 2

len_pwd = len(pwd)

hidden = len_pwd - visible

starts = "*" * hidden

print(f"hashed password is: {first}{starts}{last}")

