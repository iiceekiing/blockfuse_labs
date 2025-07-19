sentence = input("Enter a sentence: ")

words = sentence.split()

print(f"Total number of words: {len(words)}")

last_three = words[-3:]

print("Last three words (uppercase):")
for word in last_three:
    print(word.upper())

