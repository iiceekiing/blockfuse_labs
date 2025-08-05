food = {"gotteh", "furah da nunu", "masa", "awara", "gotteh"}

print(type(food))

check = input("Please type any local food to check if it's in the menu: ")

if check in food:
    print(f"Yes there's {check} in the list of food")

else:
    print("not found")
