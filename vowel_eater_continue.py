# Prompt the user to enter a word
user_word = input("Enter a word: ")

# Convert the word to uppercase
user_word = user_word.upper()

# Loop through each letter in the word
for letter in user_word:
    # If the letter is a vowel, skip it
    if letter in "AEIOU":
        continue
    # Otherwise, print the letter
    print(letter)

