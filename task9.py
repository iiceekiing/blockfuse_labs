first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()

username = first[:3].lower() + last[-3:].upper() + str(len(first + last))
print("Username:", username)

