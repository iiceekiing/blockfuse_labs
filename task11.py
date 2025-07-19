name = input("Enter your full name (first middle last): ")

# Split into words
parts = name.strip().split()

# Get initials
initials = ".".join([p[0].upper() for p in parts])

# Count total characters excluding spaces
total_letters = len("".join(parts))

print("Initials:", initials)
print("Total letters:", total_letters)

