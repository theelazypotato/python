"""
Week 5 Homework: If Statements (Chapter 5)
==========================================

This homework covers conditional logic introduced in Chapter 5.
Complete both Part A and Part B.
Stretch problems are optional extra credit.

Submit this file with your solutions.
"""


# ============================================================
# PART A: Conditional Tests (Chapter 5 - Basics)
# ============================================================

# A1. Simple Comparisons
# Create variables and write conditional tests for each:
#     age = 18
#     temperature = 72
#     name = "Alice"

age = 18
temperature = 72
name = "Alice"

#
# Write and print the result of these tests:
#     - Is age exactly 18?
#     - Is age at least 21?
#     - Is temperature less than 80?
#     - Is name equal to "alice" (case-insensitive)?

print(age == 18)
print(age >= 21)
print(temperature <= 80)
print(name.lower() == "alice")
print()

# A2. Voting Eligibility
# Create a variable `age` with any value
# Write an if-else statement that prints:
#     - "You can vote!" if 18 or older
#     - "You cannot vote yet." if under 18
age = 20

if (age == 20):
    print("You can vote!")
else:
    print("You cannot vote yet.")
print()


# A3. Grade Checker
# Create a variable `score` with a value 0-100
# Write an if-elif-else chain that prints the letter grade:
#     - 90-100: A
#     - 80-89: B
#     - 70-79: C
#     - 60-69: D
#     - Below 60: F
score = 93

if (score >= 90):
    print("A")
elif (score <= 89):
    print("B")
elif (score <= 79):
    print("C")
elif (score <= 69):
    print("D")
else:
    print("F")
print()


# A4. Even or Odd
# Create a variable `number` with any integer
# Use the modulo operator (%) to determine if it's even or odd
# Print "[number] is even" or "[number] is odd"

number = 50

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
print()

# A5. Ticket Pricing
# Create a variable `age` for a movie theater visitor
# Write if-elif-else to determine ticket price:
#     - Under 4: Free
#     - 4-12: $8
#     - 13-64: $12
#     - 65+: $10 (senior discount)
# Print the ticket price

age = 23

if (age <= 4):
    print("Free")
elif (age <= 12):
    print("$8")
elif (age <= 64):
    print("$12")
else:
    print("$10 (Senior Discount)")
print()



# ============================================================
# PART B: Combining Conditions (Chapter 5 - Advanced)
# ============================================================

# B1. Login Validator
# Create variables:
#     username = "admin"
#     password = "secret123"
#     input_user = "admin"
#     input_pass = "secret123"
#
# Use `and` to check if BOTH username AND password match
# Print "Login successful!" or "Invalid credentials"

username = "admin"
password = "secret123"
input_user = "admin"
input_pass = "secret123"

if input_user == username and input_pass == password:
    print("Login successful!")
else:
    print("Invalid credentials")
print()

# B2. Weekend or Weekday
# Create a variable `day` with a day name (e.g., "Monday")
# Use `or` to check if it's a weekend (Saturday or Sunday)
# Print "It's the weekend!" or "It's a weekday."

day = "Friday"

if (day == "Saturday" or day == "Sunday"):
    print("It's the weekend!")
else:
    print("It's a weekday")
print()

# B3. Amusement Park Ride
# Create variables:
#     height = 48  (inches)
#     age = 10
#

height = 62
age = 19

# A ride requires: height >= 48 AND age >= 8
# Check both conditions and print whether they can ride

if (height >= 48 and age >= 8):
    print("They are elligible to ride")
print()
# A ride requires: height >= 48 AND age >= 8
# Check both conditions and print whether they can ride


# B4. Menu Availability
# Create a list of available toppings:
#     available = ["pepperoni", "mushrooms", "onions", "cheese", "olives"]

availiable = ["peppers", "mushrooms", "tomatoes", "lettuce", "bacon"]

# Create a variable for the requested topping
topping = "mushrooms"
# Use `in` to check if it's available
# Print "Adding [topping]!" or "Sorry, [topping] is not available"

if (topping in availiable):
    print(f"Adding {topping}")
else:
    print(f"{topping} are not availiable")
print()

# B5. VIP Access
# Create variables:
is_member = True
years_member = 7
vip_pass = True
#
# Create a variable for the requested topping
# Use `in` to check if it's available
# Print "Adding [topping]!" or "Sorry, [topping] is not available"


# B5. VIP Access
# Create variables:
#     is_member = True
#     years_member = 3
#
# VIP access requires: is_member AND at least 5 years
# Also grant access if they have a vip_pass = True
#
# Use `and` / `or` to check access
# Print whether they have VIP access

if (is_member and years_member >= 5) or vip_pass:
    print("VIP Access Granted")
else:
    print("Standard Access")
print()



# ============================================================
# PART C: Conditionals with Lists (Chapter 5 + 4)
# ============================================================

# C1. Filtering a List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use a for loop with an if statement to print only even numbers

for number in numbers:
    if (number % 2 == 0):
        print(number)
print()

# C2. Counting Matches
temperatures = [68, 72, 75, 80, 82, 78, 71, 69, 85, 77]
count = 0
# Count how many temperatures are 75 or above
# Print the count

for temp in temperatures:
    if temp >= 75:
        count += 1

print (f"Number of temperatures 75 or above: {count}")
print()

# C3. Finding in a List
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
index = students.index("Charlie")

# Given: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use a for loop with an if statement to print only even numbers


# C2. Counting Matches
# Given: temperatures = [68, 72, 75, 80, 82, 78, 71, 69, 85, 77]
# Count how many temperatures are 75 or above
# Print the count


# C3. Finding in a List
# Given: students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
# Search for "Charlie" in the list
# Print "Found!" or "Not found"
# Also print the position if found

if "Charlie" in students:
    print("Found!")
    print(index)
print()

# C4. Categorizing Items
scores = [88, 92, 67, 75, 84, 91, 59, 78, 95, 82]
passes = 0
fails = 0

# C4. Categorizing Items
# Given: scores = [88, 92, 67, 75, 84, 91, 59, 78, 95, 82]
# Loop through and categorize each score:
#     - Print "Pass" if 60 or above
#     - Print "Fail" if below 60
# Also count total passes and fails
for score in scores:
    if (score >= 60):
        print("Pass")
        passes += 1
    else:
        print("Fail")
        fails += 1
print()
print(f"Total Passes: {passes}")
print(f"Total Fails: {fails}")
print()

# C5. Processing Special Cases
usernames = ["admin", "alice", "bob", "guest", "root", "charlie"]


# C5. Processing Special Cases
# Given: usernames = ["admin", "alice", "bob", "guest", "root", "charlie"]
# Loop through the list:
#     - If "admin" or "root": print "[name] - ADMINISTRATOR"
#     - If "guest": print "[name] - LIMITED ACCESS"
#     - Otherwise: print "[name] - standard user"

if (name == "admin" or name == "root"):
    print(f"{name} - ADMINISTRATION")
elif (name == "guest"):
    print(f"{name} - LIMITED ACCESS")
else:
    print(f"{name} - STANDARD USER")



# ============================================================
# STRETCH: Comprehensive Problem
# ============================================================

# Create a "Movie Ticket Kiosk" that:
#
# 1. Create variables for a customer:
#    - name
#    - age
#    - is_student (True/False)
#    - is_military (True/False)
#    - movie_time (like 14 for 2pm, 20 for 8pm)
#
# 2. Calculate ticket price with these rules:
#    - Base prices by age:
#      * Under 4: Free
#      * 4-12: $8
#      * 13-64: $12
#      * 65+: $10
#
#    - Discounts (apply the best one, not all):
#      * Students: 15% off
#      * Military: 20% off
#      * Matinee (before 5pm/17:00): $3 off
#
# 3. Print a ticket receipt showing:
#    - Customer name
#    - Base price
#    - Any discount applied
#    - Final price
#
# Test with different customer profiles!


