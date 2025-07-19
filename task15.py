sentence = input("Enter a sentence: ")

words = sentence.split()

print(f"Word count: {len(words)}")

print("Every second word in uppercase:")
for i in range(1, len(words), 2):
    print(words[i].upper())

