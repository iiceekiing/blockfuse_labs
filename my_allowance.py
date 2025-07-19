# Step 0: Initial allowance
balance = 120000

# 1. Paid ₦7,500 for hostel
balance -= 7500  # balance = balance - 7500

# 2. Bought textbooks worth ₦3,200
balance -= 3200

# 3. Spent ₦1,850 on printing
balance -= 1850

# 4. Added ₦500 found in old wallet
balance += 500  # balance = balance + 500

# 5. Paid 12.5% of current balance for internet
balance -= balance * 12.5 / 100

# 6. Gave 1/6 of what was left to sister
balance -= balance / 6

# 7. Bought groceries worth ₦9,750
balance -= 9750

# 8. Bank deducted 7.3% as service charge
balance -= balance * 7.3 / 100

# 9. Saved 1/4 of current balance
balance -= balance / 4

# 10. Spent ₦2,100 on transport
balance -= 2100

# 11. Contributed 5.8% for friend's birthday
balance -= balance * 5.8 / 100

# 12. Gave 1/3 of balance to church
balance -= balance / 3

# 13. Shopping spree ₦4,500
balance -= 4500

# 14. Uncle gave ₦1,200
balance += 1200

# 15. Paid 15% for online course
balance -= balance * 15 / 100

# 16. Gave 1/8 to younger brother
balance -= balance / 8

# 17. Spent ₦3,600 on medicals
balance -= 3600

# 18. Saved 10% for emergency fund
balance -= balance * 10 / 100

# 19. Divide remaining into 5 equal parts (for 5 days)
balance //= 5  # Keep only one part for today

# 20. Set aside ₦200 for snacks (keep the rest)
balance %= 200  # Keep the remainder after removing 200

# Final output
print("Final balance remaining: ₦", round(balance, 2))

