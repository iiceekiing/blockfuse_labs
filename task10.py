snacks = input("Enter 5 favorite snacks, separated by commas: ")

# Convert string to list
snack_list = snacks.split(",")

# Remove last item
snack_list.pop()

# Add 'water' to the list
snack_list.append("water")

# Show updated list
print("Updated Snack List:")
for snack in snack_list:
    print("-", snack.strip())

