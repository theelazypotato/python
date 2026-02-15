"""
Week 4 Homework: Chapters 1-4 Review (Exam 1 Prep)
==================================================

This homework reviews ALL concepts from Chapters 1-4.
Complete these exercises to prepare for Exam 1.
Stretch problems are optional extra credit.

Submit this file with your solutions.
"""


# ============================================================
# PART A: Variables and Strings (Chapter 2 Review)
# ============================================================

# A1. Create variables for a student profile:
#     - name (string)
#     - age (integer)
#     - gpa (float)
#     - is_fulltime (boolean)
#     Print each with a label


# A2. Using the name variable, print:
#     - The name in all uppercase
#     - The name in all lowercase
#     - The name with proper title case
#     - The number of characters in the name


# A3. Create a variable `course` with value "  CSCI 120: Intro to Programming  "
#     Print it with leading/trailing whitespace removed
#     Print just the course number (120) using string methods or slicing


# A4. Create variables for a price calculation:
#     - item_price = 29.99
#     - quantity = 3
#     - tax_rate = 0.07
#     Calculate and print the subtotal, tax, and total
#     Format all money values to 2 decimal places




# ============================================================
# PART B: Lists and List Operations (Chapter 3 Review)
# ============================================================

# B1. Create a list called `courses` with 5 course names you're taking
#     Print the first course and the last course


# B2. Make the following changes to your courses list:
#     - Add a new course to the end
#     - Insert a course at position 2
#     - Remove one course by name
#     - Print the updated list after each change


# B3. Create a list of 5 numbers (any numbers you choose)
#     - Sort the list and print it
#     - Reverse the sorted list and print it
#     - Print the original list (was it changed?)


# B4. Create two lists:
#     - breakfast_foods with 3 items
#     - lunch_foods with 3 items
#     Combine them into a new list called all_foods
#     Print all_foods and its length




# ============================================================
# PART C: Loops and Ranges (Chapter 4 Review)
# ============================================================

# C1. Use a for loop to print numbers 1 through 10


# C2. Use range() to create and print:
#     - Even numbers from 2 to 20
#     - Countdown from 10 to 1
#     - Multiples of 5 from 5 to 50


# C3. Given this list:
#     temperatures = [72, 68, 75, 71, 80, 78, 74]
#
#     Use a for loop to:
#     - Print each temperature
#     - Calculate and print the sum
#     - Calculate and print the average


# C4. Use a list comprehension to create:
#     - A list of squares from 1 to 10 (1, 4, 9, 16, ...)
#     - A list where each temperature is converted to Celsius
#       Formula: (temp - 32) * 5/9


# C5. Given this list of names:
#     students = ["alice", "bob", "charlie", "diana"]
#
#     Use enumerate() to print a numbered roster:
#     1. Alice
#     2. Bob
#     3. Charlie
#     4. Diana




# ============================================================
# PART D: Slices and Tuples (Chapter 4 Review)
# ============================================================

# D1. Given this list:
#     months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
#               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#
#     Use slicing to print:
#     - First quarter (Jan-Mar)
#     - Summer months (Jun-Aug)
#     - Last quarter (Oct-Dec)


# D2. Create a list of 8 numbers
#     - Print the first half and second half using slices
#     - Calculate the average of each half
#     - Print the average of each half


# D3. Demonstrate correct list copying:
#     - Create a list called original with 5 items
#     - Create a proper copy called backup using slicing
#     - Modify original (add an item)
#     - Print both lists to show backup wasn't changed


# D4. Create tuples for:
#     - Your birthday as (month, day, year)
#     - A location as (city, state, zip_code)
#     - Print formatted strings using each tuple


# D5. Create a list of 3 tuples, where each tuple contains:
#     (student_name, test1_score, test2_score, test3_score)
#
#     Loop through the list and print each student's:
#     - Name
#     - All three scores
#     - Average score




# ============================================================
# STRETCH: Comprehensive Review Problem
# ============================================================

# Create a "Course Grade Tracker" that demonstrates ALL concepts:
#
# 1. Create variables for course info (name, credits, semester)
#
# 2. Create a list of assignment scores (at least 8 scores)
#
# 3. Use loops to calculate:
#    - Total points
#    - Average score
#    - Highest and lowest scores
#
# 4. Use slicing to compare first half vs second half performance
#
# 5. Create a tuple with the final summary:
#    (course_name, num_assignments, average, total_points)
#
# 6. Print a nicely formatted grade report


