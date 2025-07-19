pwd = input("Enter your password: ")

# If password is shorter than 3 characters, we don't need to mask it
if len(pwd) <= 2:
    print(pwd)
else:
    masked = f"{pwd[0]}{'*' * (len(pwd) - 2)}{pwd[-1]}"
    print(masked)







pwd = input("Enter your password: ")

# Use slicing to keep first and last, then fill middle with '*'
masked = pwd if len(pwd) <= 2 else pwd[0] + "*" * (len(pwd) - 2) + pwd[-1]

print(masked)



