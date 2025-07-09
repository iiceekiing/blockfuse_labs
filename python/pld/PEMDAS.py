
"""
Operator Precedence: PEMDAS

P → Parentheses

E → Exponents

M D → Multiplication/Division (Left to Right)

A S → Addition/Subtraction (Left to Right)
"""


# -----------------------EXAMPLES:---------------------------

print(2 + 3 * 4)  # 2 + 12 = 14

print((2 + 3) * 4)  # 5 * 4 = 20

result = 2 + 3 * 4 ** 2

print(result)

result = (2 + 3) * 4 ** 2

print(result)
