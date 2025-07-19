text = input("Enter a sentence with an email address: ")

# Find position of '@'
at_index = text.find('@')

# Find the space before the email starts
start = text.rfind(' ', 0, at_index) + 1

# Find the space after the email ends
end = text.find(' ', at_index)

# If no space after, assume it's at the end
if end == -1:
    end = len(text)

email = text[start:end]
print(f"Extracted Email: {email}")

