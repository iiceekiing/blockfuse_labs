pwd = input("Enter your password: ")

first = pwd[0]

lenght  =  len(pwd)

visible = 2

num_stars = lenght - visible

last = pwd[-1]


stars = "*" * num_stars


#paswd = first+stars+last

print(f"your passwordis: {first}{stars}{last}")
