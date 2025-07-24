best_plant = input("Please enter name of best plant: ")

plant_name = "Spathiphyllum"

if best_plant == plant_name.upper():
    print("Yes - 'Spathiphyllum' is the best plant ever!")

elif best_plant == plant_name.lower():
    print("No!!! 🙅 🙅 I want big Spathiphyllum (in upper case!)")

elif best_plant == plant_name.title():
    print(" nope!  🤦 🤦  I want everything in upper case not only the first alphabet! ")

else:
    print("invalid input! expected best plant name. hint==> : Sp******um")
