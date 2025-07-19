import time


dob = input("hello!, please input your date of birth :\n")

#current_year = 2025

age = 2025 - int(dob)

print(f"you are {age} year old")

#init_bal = 10000

cur_bal = float(input("please enter your current balance: "))

spend = float(input("how much do you want to spend: "))

print("calculating your balance....")

time.sleep(1) 

while true do;

if cur_bal < spend:
	print("you can't spend more than your current balance")
	print("please enter amount less than your balance!")
else:
	cur_bal = userbal - spend

	print(f"your remaining  balance is:{cur_bal:,.2f}")
break

'''
msg = "rPyoagrhmotn is cool"
new = msg.split(" ")

 
py = new[0][1:3] 
t = new[0][-2]
h = new[0][7]
o = new[0][-3]
n = new[0][-1]

py = msg[1:3]
t = msg[10:11]
h = msg[7:8]
o = msg[3:4]
n = msg[11:12]
 

print(py+t+h+o+n)
'''
