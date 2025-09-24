  def show():
    nom = user_name()
    print(f"hello {nom}")

def user_name():
    name = input("Enter your name:  ")
    return name

show()

array = []

def collector():
    num = input("Enter multiple numbers separated with space: ").split()
    for item in num:
        return num

def updater():
    data = collector()
    print(array.append(data))

updater()


array = []

array = []

def collector():
    num = input("Enter multiple numbers separated with space: ").split()
    numbers = [int(item) for item in num]
    return numbers

def updater():
    data = collector()      
    array.extend(data)        
    print(array)           
updater()


def num1():
    number1 = int(input("Enter any number (first number): "))
    return number1

def num2():
    number2 = int(input("Enter any number(second number): "))
    return number2

def adder():
    first_number = num1()
    second_number = num2()
    added = first_number + second_number
    print(f"the sum of {first_number} + {second_number} is = {added}")

adder()

