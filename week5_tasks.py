# Question 1
my_age = 23
pi = 3.14159

magic_number = (my_age * 3 + pi) % 7
print(magic_number)
print(type(magic_number))


# Question 2
secret_word = "PythonIsAmazing"

# First 6 characters
first_word = secret_word[0:6]
print(first_word)

# Last 7 characters
print(secret_word[-7:])

# Middle word "Is"
middle_word = secret_word[6:8]
print(middle_word)

# Reversed string
reverse = secret_word[::-1]
print(reverse)

# Every second character
second_characters = secret_word[::2]
print(second_characters)


# Question 3
first_word_uppercase = first_word.upper()
print(first_word_uppercase)

last_word_lowercase = secret_word[6:].lower()
print(last_word_lowercase)

new_string = first_word_uppercase + last_word_lowercase
print(new_string)

