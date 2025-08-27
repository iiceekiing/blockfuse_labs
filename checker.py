amount = int(input("Enter amount: "))

if amount > 50000:
    discount = (0/100)*(amount)
    price = amount - discount
    print(f"your purchase is greater 50k, you have got 20% of, now paying: ", price)

elif  amount >= 30000 and amount <= 50000:
    discount = (10/100)*(amount)
    price= amount-discount
    print("10% off now paying: ", price)

elif amount >= 10000 and  amount <=30000:
    discount = (5/100)*(amount)
    price = amount - discount
    print("5% off, now paying: ", price)

else:
    print("No discount for you")

    discount = (100/100)*(amount)
    price = amount - discount
    print(" ")

    print("0% off, no discount for you, you are paying : ", amount)

    print(" ")

    print("Final payment amount is: ", amount)
print(" ")
print("discount is: ", discount)
print(" ")
print("final ammount is: ", price)

