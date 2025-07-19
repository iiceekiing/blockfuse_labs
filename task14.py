words = input("Enter some words separated by space: ").split()

if len(words) >= 2:
    words.pop()      # Remove last
    words.pop(0)     # Remove first

    words.reverse()

    print("Reversed list (without first and last):", words)
else:
    print("Please enter at least 3 words!")

