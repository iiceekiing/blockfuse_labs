# name = 'odobi'

# if name.startswith('o'):
#     print(f"{name} starts with 'o'")
# else:
#     print(f"{name} does not start with 'o'")


temp = input("Enter anything: ")

if isinstance(temp, str):
    print(f"{temp} is a string")
elif isinstance(temp, int):
    print(f"{temp} is an integer")
elif isinstance(temp, float):
    print(f"{temp} is a float")
elif isinstance(temp, list):
    print(f"{temp} is a list")
elif isinstance(temp, dict):    
    print(f"{temp} is a dictionary")
elif isinstance(temp, tuple):
    print(f"{temp} is a tuple")
elif isinstance(temp, set):
    print(f"{temp} is a set")
else:  
    print(f"{temp} is of unknown type")


