max = 150
bio = input("Enter your bio: ")
print(f"Your input is:  {bio}")


print(len(bio))


print(f"Lenght of input: {bio[0:20]}")

last = bio[-1:-21:-1]
print(f"Last 20 char preview: {last}")
print(len(last))
