sentence = input("Enter a sentence: ")

char_list = list(sentence)

vowels = "aeiouAEIOU"

i = 0
while i < len(char_list):
    if char_list[i] == " " or char_list[i] in vowels:
        char_list.pop(i)
    else:
        i += 1

print("Modified character list:", char_list)
print("Rejoined version:", "".join(char_list))

