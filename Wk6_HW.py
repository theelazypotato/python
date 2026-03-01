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
scores = [85, 92, 78, 65, 95, 88, 72, 58, 90, 83, 67, 91]

count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_f = 0
#
# Loop through and count how many scores fall into each grade:
#     A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)
#
# Print the count for each grade and the class average

for score in scores:
    if score >= 90:
        count_a += 1
    elif score >= 80:
        count_b += 1
    elif score >= 70:
        count_c += 1
    elif score >= 60:
        count_d += 1
    else:
        count_f += 1

average = sum(scores) / len(scores)

print(f"A: {count_a}")
print(f"B: {count_b}")
print(f"C: {count_c}")
print(f"D: {count_d}")
print(f"F: {count_f}")
print(f"Class Average: {average:.1f}")
print()
# B2. Filter and Transform
numbers = [-5, 12, -3, 8, -1, 15, 7, -9, 20, 3]
positive_numbers = [n for n in numbers if n > 0]
negative_numbers = [abs(n) for n in numbers if n < 0]
big_numbers = [n for n in numbers if abs(n) > 10]
#
# Create three new lists:
#     - positive_numbers: only positive numbers
#     - negative_numbers: only negative numbers (as positive values)
#     - big_numbers: numbers where absolute value > 10
#
# Print all three lists

print(f"Positives: {positive_numbers}")
print(f"Negatives as Pos: {negative_numbers}")
print(f"Absolute > 10: {big_numbers}")
print()
# B3. Find Extremes
temperatures = [72, 68, 75, 80, 65, 82, 71, 78, 69, 85]

highest = temperatures[0]
highest_index = 0
# WITHOUT using min() or max(), find:
#     - The highest temperature
#     - The lowest temperature
#     - The day (index) of each
#
# Print: "Highest: 85 on day 10" (using 1-based day numbers)

for i in range(len(temperatures)):
    if temperatures[i] > highest:
        highest = temperatures[i]
        highest_index = i

print(f"Highest: {highest} on day {highest_index + 1}")
print()

# B4. Duplicate Finder
names = ["Alice", "Bob", "Charlie", "Alice", "Diana", "Bob", "Eve"]
seen = []
duplicates = []
#
# Find and print all names that appear more than once
# Also print how many times each duplicate appears

for name in names:
    if name in seen:
        if name not in duplicates:
            duplicates.append(name)
    else:
        seen.append(name)

for dup in duplicates:
    count = names.count(dup)
    print(f"{dup} appeared {count} times")
print()
# B5. Range Checker
values = [15, 42, 8, 67, 23, 91, 5, 38, 72, 19]

low_count = 0  # < 20
medium_count = 0  # 20-50
high_count = 0  # 51-80
very_high_count = 0 # > 80
#
# Categorize each value:
#     - "low" if < 20
#     - "medium" if 20-50
#     - "high" if 51-80
#     - "very high" if > 80
#
# Create a summary showing count in each category

for val in values:
    if val < 20:
        low_count += 1
    elif val <= 50:
        medium_count += 1
    elif val <= 80:
        high_count += 1
    else:
        very_high_count += 1

print("Range Summary: ")
print(f"Low: {low_count}")
print(f"Medium: {medium_count}")
print(f"High: {high_count}")
print(f"Very High: {very_high_count}")
print()

# ============================================================
# PART C: Putting It All Together
# ============================================================

# C1. Shopping Cart Discount
# Given:
cart_total = 125.00
is_member = True
coupon_code = "SAVE20"
valid_coupons = ["SAVE10", "SAVE20", "HOLIDAY"]
shipping_fee = 8.99
#
# Apply discounts:
#     - Members get 5% off
#     - SAVE10 = $10 off, SAVE20 = $20 off, HOLIDAY = 15% off
#     - Can combine member discount with ONE coupon
#     - Orders over $100 get free shipping (otherwise $8.99)
#
# Print itemized receipt with all discounts and final total

# Member Discount (5% off)
if is_member:
    member_discount = cart_total * 0.05
    cart_total -= member_discount
    print(f"Member Discount Applied: -${member_discount:.2f}")

# Coupon Discount
if coupon_code in valid_coupons:
    if coupon_code == "SAVE10":
        cart_total -= 10
    elif coupon_code == "SAVE20":
        cart_total -= 20
    elif coupon_code == "HOLIDAY":
        cart_total *= 0.85  # 15% off
    print(f"Coupon {coupon_code} Applied!")

# Shipping Fee
if cart_total > 100:
    shipping_fee = 0
    print("Free Shipping Applied!")
else:
    cart_total += shipping_fee

print(f"Final Total: ${cart_total:.2f}")
print()
# C2. Divisibility Analyzer
numbers = [12, 15, 20, 25, 30, 35, 42, 50, 60, 77]

fizzbuzz_count = 0
fizz_count = 0
buzz_count = 0
#
# For each number, check:
#     - Is it divisible by both 3 AND 5? Print "FizzBuzz"
#     - Is it divisible by 3 only? Print "Fizz"
#     - Is it divisible by 5 only? Print "Buzz"
#     - Otherwise print the number
#
# Also count how many FizzBuzz, Fizz, and Buzz you found

for num in numbers:
    # check both first
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        fizzbuzz_count += 1
    # check individual divisibility
    elif num % 3 == 0:
        print("Fizz")
        fizz_count += 1
    elif num % 5 == 0:
        print("Buzz")
        buzz_count += 1
    # otherwise print the number
    else:
        print(num)

print(f"\nSummary: ")
print(f"FizzBuzz found: {fizzbuzz_count}")
print(f"Fizz found: {fizz_count}")
print(f"Buzz found: {buzz_count}")
print()
# C3. Number Classifier
values = [2, 4, 7, 10, 13, 15, 21, 25, 29, 30]
primes = []
composites = []
#
# For each number, determine if it's prime or composite.
# Use a boolean flag and loop (the pattern from class!).
# Collect primes in one list and composites in another.
#
# Print:
#     - The list of primes
#     - The list of composites
#     - How many of each

for num in values:
    if num < 2:
        composites.append(num)
        continue
    
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        primes.append(num)
    else:
        composites.append(num)

print(f"Primes: {primes} (Total: {len(primes)})")
print(f"Composites: {composites} (Total: {len(composites)})")


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


