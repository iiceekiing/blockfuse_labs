word = input("type any word and i will print the unique characters for you!:  ").lower()

print(f"you've typed {word}, i will sort it and print the unique chars for you  ")

unique = set(word)

order = []

#print(unique)

for i in unique:
    print(i, end="")

print(" ")
