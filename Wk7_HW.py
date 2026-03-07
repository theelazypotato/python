"""
Wk7_HW.py - Homework: Dictionaries and User Input
==================================================
CSCI 120 - Week 7
Chapters 6-7: Dictionaries, User Input, and While Loops

Due: Friday, March 7, 2026

Instructions:
- Complete all exercises below
- Test your code before submitting
- Submit this file to the LMS
"""

# ==============================================================
# PART 1: DICTIONARIES (Chapter 6)
# ==============================================================

# Exercise 1: Create a dictionary called 'student' with the following keys:
# - 'name' (your name)
# - 'major' (your major or "Undeclared")
# - 'year' (1, 2, 3, or 4)
# - 'gpa' (a float like 3.5)
# Then print each value using the keys.

# YOUR CODE HERE:
student = {"name": "Raina", "major": "Undeclared", "year": 2, "gpa": 2.8}

print(student["name"])
print(student["major"])
print(student["year"])
print(student["gpa"])

print()

# Exercise 2: Create a dictionary called 'favorite_foods' where:
# - Keys are names of 3 friends
# - Values are their favorite foods
# Use a for loop to print: "[Name]'s favorite food is [food]."

# YOUR CODE HERE:

favorite_foods = {"Vic": "burger", "Sam": "pasta", "Sprite": "pizza"}

for name, food in favorite_foods.items():
    print(f"{name.title()}'s favorite food is {food.title()}.")

print()

# Exercise 3: Create a dictionary called 'course_grades' with at least 4 courses
# and their letter grades (e.g., 'CSCI 120': 'A', 'MATH 101': 'B+')
# Use .items() to loop through and print each course and grade.

# YOUR CODE HERE:

course_grades = {"CSCI 120": "A+", "HIST 260": "A", "ENGL 210": "A+", "IDST 251": "A-"}

for course, grade in course_grades.items():
    print(f"{course}: {grade}")

print()

# ==============================================================
# PART 2: USER INPUT (Chapter 7)
# ==============================================================

# Exercise 4: Ask the user for their favorite color using input().
# Then print a message like "Great choice! [color] is a nice color."

# YOUR CODE HERE:

favorite_color = input("What's your favorite color: ")
print(f"\nGreat choice! {favorite_color} is a nice color.")

print()

# Exercise 5: Ask the user for their age using input().
# Convert it to an integer using int().
# Print whether they are a "teenager" (13-19), "adult" (20+), or "child" (<13).

# YOUR CODE HERE:

age = input("Please enter your age: ")
age = int(age)

if age >= 20:
    print("adult (20+)")
elif age <= 13:
    print("teenager (13-19)")
else:
    print("child (<13)")

print()

# ==============================================================
# PART 3: WHILE LOOPS (Chapter 7)
# ==============================================================

# Exercise 6: Write a while loop that counts from 1 to 5 and prints each number.
# Use a variable to track the count.

# YOUR CODE HERE:

number = 1
while number <=5:
    print(number)
    number += 1

print()

# Exercise 7: Write a while loop that asks the user to enter numbers.
# Keep asking until they enter 'quit'.
# After they quit, print the sum of all the numbers they entered.
# Hint: Convert input to int() only if it's not 'quit'.

# YOUR CODE HERE:

prompt = "\nEnter a number: "
prompt += "\nEnter 'quit' to end the program "

total_sum = 0
numbers = ""

while numbers != "quit":
    numbers = input(prompt)
    
    if numbers != "quit":
        total_sum += int(numbers)
        print(numbers)

print(f"The total sum is: {total_sum}")

# ==============================================================
# PART 4: COMBINING CONCEPTS
# ==============================================================

# Exercise 8: Create a simple contact book program:
# - Start with an empty dictionary called 'contacts'
# - Use a while loop to repeatedly ask:
#   "Enter a name (or 'done' to finish): "
# - If they enter a name, ask for that person's phone number
# - Add the name and phone to the contacts dictionary
# - When they enter 'done', exit the loop and print all contacts

# YOUR CODE HERE:

contacts = {}
active = True

while active:
    name = input("\nEnter a name (or 'done to finish): ")
    
    if name == "done":
        active = False
    else:
        contact = input("What is their phone#?: ")
        contacts[name] = contact

print("\nContact Book")
for name, contact in contacts.items():
    print(f"{name}: {contact}")

print("\n--- Homework Complete! ---")
