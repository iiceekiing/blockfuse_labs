

while True:
    choice = input("Enter any number: ").split()
    operator = input("Enter any operator of your choice, '+', '-', '*'...: ")
    total = 0
    for item in choice:
        nums = int(item)

        total += nums
    print(total)

    # if operator == "+":
    #     add = sum(choice)

    # elif operator == "-":
    #     sub = sub(choice)

    # elif operator == "*":
    #     mul = mul(choice)

    # else:
    #     print("invalid")
    #     break