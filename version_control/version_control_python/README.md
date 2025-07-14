 # This directory is for creating basic calculator with different version for version control practice





Here's a clean, beginner-friendly `README.md` file for your three basic Python calculator scripts. It explains what each file does and is formatted nicely for GitHub:

---

````markdown

# 🧮 Basic Python Calculators

Welcome to this mini project where we explore how to build **very simple calculators in Python** — great for beginners just getting started with programming and input/output logic!

---

## 📁 Project Files

### `basic_cal1.py`

> 🟢 A simple calculator that adds two predefined numbers.

```python

num1 = 5

num2 = 6

summation = num1 + num2

print(summation)
````

📌 *This script demonstrates variable assignment and basic arithmetic addition.*

---

### `basic_cal2.py`


> 🟡 A calculator that asks the user for two numbers, then adds them **as strings**.

```python

num1 = input("Enter first number: ")

num2 = input("Enter second number: ")

summation = num1 + num2

print(summation)
```

⚠️ *This will **concatenate** the two inputs (e.g., "5" + "6" becomes "56").*

---

### `basic_cal3.py`

> 🔵 A proper calculator that takes user input and converts it to integers for accurate addition.

```python

num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

summation = num1 + num2

print("The sum is:", summation)
```


✅ *This correctly adds numbers after converting input strings to integers.*

---

## 📘 What You Learn

* How to store values in variables

* The difference between **string** and **integer** input

* How to get user input using `input()`

* How to use `int()` to convert user input

* Basic `print()` usage

* Arithmetic operations in Python

---


## 🚀 Getting Started



To run any of these scripts:

1. Make sure Python is installed on your machine (Python 3 recommended).

2. Open a terminal or command prompt.

3. Run the script using:


```bash

python basic_cal1.py

# or

python basic_cal2.py

# or

python basic_cal3.py
```


---


## �� Note for Beginners

* In `basic_cal2.py`, inputs are **not converted to numbers**, so Python treats them as strings.

* `basic_cal3.py` fixes that by wrapping the input with `int()`.


---

## ✨ Author

Made with by \[iiceekiing]

---
