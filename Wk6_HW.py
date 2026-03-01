"""
Week 6 Homework: Conditionals Practice (Chapter 5 Continued)
=============================================================

This homework provides more practice with conditionals and
combines them with loops for real-world scenarios.
Complete both Part A and Part B.
Stretch problems are optional extra credit.

Submit this file with your solutions.
"""


# ============================================================
# PART A: Advanced Conditionals (Chapter 5 Review)
# ============================================================

# A1. Multiple Conditions
# Create variables for a job applicant:
age = 25
years_experience = 3
has_degree = True
has_certification = False
#
# Check if they qualify for a position that requires:
#     - At least 21 years old
#     - Either a degree OR 5+ years experience
#     - If no degree, must have certification
#
# Print whether they qualify and explain why/why not
if age >= 21 and (has_degree or years_experience >= 5) and (has_degree or has_certification):
    print("The applicant qualifies for the position.")
else:
    print("The applicant does not qualify.")
    if age > 21:
        print("- Must be at least 21 years old.")
    if not has_degree and years_experience < 5:
        print("- Must have a degree or 5+ years of experience.")
    if not has_degree and not has_certification:
        print("- Must have a certification if no degree is present.")
print()

# A2. Nested Conditionals
# Create a shipping cost calculator:
weight = 5  
destination = "domestic"  # or "international"
is_express = False
cost = 0
#
# Base rates:
#     - Domestic: $5 for first lb, $1 each additional
#     - International: $15 for first lb, $3 each additional
#
# Express shipping doubles the cost
# Free domestic shipping for orders over 10 lbs
#
# Print the shipping cost
if destination == "domestic":
    if weight > 10:
        cost = 0 # free shipping
    else:
        # $5 for first lb + $1 for additional
        cost = 5 + (weight - 1) * 1
else:  # international
    # $15 for first lb + $3 for additional
    cost = 15 + (weight - 1) * 3
# express multiplier
if is_express:
    cost *= 2

print(f"Total shipping cost: ${cost}")
print()


# A3. Complex Boolean Logic
# Create a password validator that checks:
password = "MyP@ss123"
#
# Requirements (check ALL):
#     - At least 8 characters long
#     - Contains at least one number
#     - Contains at least one uppercase letter
#
# Print each requirement status and final verdict
# Hint: Use any() and loops, or check character by character

# length check
length_ok = len(password) >= 8
# number check
has_number = any(char.isdigit() for char in password)
# uppercase check
has_upper = any(char.isupper() for char in password)

print(f"Length (8+): {length_ok}")
print(f"Has Number: {has_number}")
print(f"Has Uppercase: {has_upper}")

if length_ok and has_number and has_upper:
    print("Strong Password")
else:
    print("Weak Password")
print()
# A4. Status Checker
# Create a system status checker:
cpu_usage = 75
memory_usage = 82
disk_usage = 45
error_count = 2
#
# Status levels:
#     - CRITICAL: cpu OR memory > 90, OR error_count > 5
#     - WARNING: cpu OR memory > 75, OR disk > 80, OR error_count > 0
#     - OK: everything else
#
# Print the status with reason
if (cpu_usage or memory_usage > 90) or (error_count > 5):
    print("Status: CRITICAL")
elif (cpu_usage or memory_usage > 75) or (disk_usage > 80) or (error_count > 0):
    print("Status: WARNING")
else:
    print("Status: OK")
print()
# A5. Date Validator
# Create variables:
month = 3
day = 17
year = 2026

is_valid = True

#
# Check if the date is valid:
#     - Month must be 1-12
#     - Day must be valid for that month
#     - February has 28 days (29 in leap years)
#     - Leap year: divisible by 4, except centuries unless divisible by 400
#
# Print whether the date is valid

if not (1 <= month <= 12):
    is_valid = False

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_valid:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    elif month == 2:
        max_days = 29 if is_leap else 28
        
    if not (1 <= day <= max_days):
        is_valid = False

print(f"Is the date: {month}/{day}/{year} valid? {is_valid}")
print()
# ============================================================
# PART B: Conditionals with Loops (Chapter 5 + 4)
# ============================================================

# B1. Grade Distribution
Given: scores = [85, 92, 78, 65, 95, 88, 72, 58, 90, 83, 67, 91]
#
# Loop through and count how many scores fall into each grade:
#     A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)
#
# Print the count for each grade and the class average


# B2. Filter and Transform
# Given: numbers = [-5, 12, -3, 8, -1, 15, 7, -9, 20, 3]
#
# Create three new lists:
#     - positive_numbers: only positive numbers
#     - negative_numbers: only negative numbers (as positive values)
#     - big_numbers: numbers where absolute value > 10
#
# Print all three lists


# B3. Find Extremes
# Given: temperatures = [72, 68, 75, 80, 65, 82, 71, 78, 69, 85]
#
# WITHOUT using min() or max(), find:
#     - The highest temperature
#     - The lowest temperature
#     - The day (index) of each
#
# Print: "Highest: 85 on day 10" (using 1-based day numbers)


# B4. Duplicate Finder
# Given: names = ["Alice", "Bob", "Charlie", "Alice", "Diana", "Bob", "Eve"]
#
# Find and print all names that appear more than once
# Also print how many times each duplicate appears


# B5. Range Checker
# Given: values = [15, 42, 8, 67, 23, 91, 5, 38, 72, 19]
#
# Categorize each value:
#     - "low" if < 20
#     - "medium" if 20-50
#     - "high" if 51-80
#     - "very high" if > 80
#
# Create a summary showing count in each category




# ============================================================
# PART C: Putting It All Together
# ============================================================

# C1. Shopping Cart Discount
# Given:
#     cart_total = 125.00
#     is_member = True
#     coupon_code = "SAVE20"
#     valid_coupons = ["SAVE10", "SAVE20", "HOLIDAY"]
#
# Apply discounts:
#     - Members get 5% off
#     - SAVE10 = $10 off, SAVE20 = $20 off, HOLIDAY = 15% off
#     - Can combine member discount with ONE coupon
#     - Orders over $100 get free shipping (otherwise $8.99)
#
# Print itemized receipt with all discounts and final total


# C2. Divisibility Analyzer
# Given: numbers = [12, 15, 20, 25, 30, 35, 42, 50, 60, 77]
#
# For each number, check:
#     - Is it divisible by both 3 AND 5? Print "FizzBuzz"
#     - Is it divisible by 3 only? Print "Fizz"
#     - Is it divisible by 5 only? Print "Buzz"
#     - Otherwise print the number
#
# Also count how many FizzBuzz, Fizz, and Buzz you found


# C3. Number Classifier
# Given: values = [2, 4, 7, 10, 13, 15, 21, 25, 29, 30]
#
# For each number, determine if it's prime or composite.
# Use a boolean flag and loop (the pattern from class!).
# Collect primes in one list and composites in another.
#
# Print:
#     - The list of primes
#     - The list of composites
#     - How many of each




# ============================================================
# STRETCH: Comprehensive Challenge
# ============================================================

# Goldbach's Conjecture Tester
# Goldbach's conjecture says every even number greater than 2
# can be written as the sum of two prime numbers.
#
# Given: even_numbers = [4, 6, 8, 10, 20, 50, 100]
#
# For each even number, find TWO primes that add up to it.
# (There may be multiple pairs — just find the first one.)
#
# Strategy:
#     - For each even number n, check pairs: (2, n-2), (3, n-3), ...
#     - For each pair, check if BOTH numbers are prime
#     - Use your prime-checking skills from class!
#
# Print:
#     - Each even number and the prime pair you found
#     - Example: "4 = 2 + 2"
#     - Example: "10 = 3 + 7"
#     - Example: "100 = 3 + 97"


