# task6.py
from datetime import datetime

birth_year = int(input("Enter your birth year (e.g. 2002): "))

current_year = datetime.now().year

age = current_year - birth_year

print(f"You are {age} years old.")

