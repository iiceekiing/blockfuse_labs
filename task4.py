

Mon = int(input("How many steps on Monday:  "))

Tues =  int(input("How many steps on Tuesday: "))

Wed = int(input("How many steps on Wednesday: "))

total = Mon + Tues + Wed

average = total / 3

print(f"You walked a total of {total:,} steps in 3 days. That is an average of {average:,.2f} steps per day")
