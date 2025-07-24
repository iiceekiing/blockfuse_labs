"""
for i in range(11):
    # do_something()
    print(i, '\n')
    pass




for i in range(11):
    print("The value of i is currently\n", i)




for i in range(2, 8):
    print("The value of i is currently", i)




for i in range(1, 10, 2):
    print(i)


print("Example of break instruction:")
for i in range(1, 6):  # i goes from 1 to 5
    if i == 3:
        break          # Stop the loop when i == 3
    print("Inside the loop.", i)
print("Outside the loop.")


print("\nExample of  continue instruction:")
for i in range(1, 6):  # i goes from 1 to 5
    if i == 3:
        continue       # Skip rest of this loop when i == 3
    print("Inside the loop.", i)
print("Outside the loop.")
"""



#complete version 
largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))

    if number == -1:
        break

    if number < 0:
        print("Negative numbers are skipped.")
        continue

    counter += 1
    if number > largest_number:
        largest_number = number

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

