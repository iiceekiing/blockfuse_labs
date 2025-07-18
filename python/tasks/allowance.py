allowance = 2000

allowance -= 400
#print(allowance)

allowance += 100 
#print(allowance)

allowance -= 250
#print(allowance)

percent = 25 / 100

percent *= allowance

#print(percent)

allowance  -= percent

#print(allowance)

one_third = (1/3) * (allowance)

#print(one_third)

allowance -= one_third 
#print(allowance)

allowance //= 2

print(allowance)

allowance %= 100

print(f"balance: {allowance:.4f}")


