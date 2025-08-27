customer = {
    'name': "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False
}

amount = customer["order_amount"]
discount = (10/100)*(amount)
price = amount - discount
#print(price)


while True:

    if customer['loyalty_card'] == True:
        #print(f"you have a royal card, enjoy 10% discount, you are now paying: ",  amount - discount)
        print(f"you have a royal card, enjoy 10% discount, you are now paying: ",  price)

    if customer['order_amount'] > 20000:
        discount = (5/100)*(price)
        price -= discount
        print(price)

        if customer['loyalty_card'] == True:
            print(f"your order is above 20,000 NGN, 10% off, you are now paying: ", price)

        if customer['order_amount'] > 20000:
            print(f"\nyou order is above 20,000 NGN, but you don't have a loyalty card so enjoy a free soft drink")
 
    if customer['is_student'] == True:
        discount = (5/100)*(price)
        price -= discount
        print(price)
        print(f"\nyou pass all three checks, you have gotten 3x discount, now paying: ", price)

    break
print(f"\nfinal discount is: {discount}")

order_summary = {}

order_summary.update(customer)
#print(order_summary)
order_summary['initial_amount'] = customer['order_amount']
order_summary['final_amount'] = price
order_summary['final_discount'] = discount
print('\norder summary for cashier: ', order_summary)
