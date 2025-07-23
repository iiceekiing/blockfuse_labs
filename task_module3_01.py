# Task: Check student eligibility based on age and scores

age = int(input("Enter your age: "))
math_score = int(input("Enter your Math score (0-100): "))
science_score = int(input("Enter your Science score (0-100): "))

# Conditions:
# - age must be >= 16
# - either math or science must be above 75
# - both scores must not be below 40

eligible = (
    age >= 16 and 
    (math_score > 75 or science_score > 75) and 
    not (math_score < 40 or science_score < 40)
)

print("Eligibility Status:", "Eligible" if eligible else "Not Eligible")

