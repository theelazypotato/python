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

name = "Raina"
age = 19
gpa = 2.7
is_fulltime = True

print(f"Student Name: {name}")
print(f"Age: {age}")
print(f"GPA: {gpa}")
print(f"Fulltime: {is_fulltime}")
print()

# A2. Using the name variable, print:
#     - The name in all uppercase
#     - The name in all lowercase
#     - The name with proper title case
#     - The number of characters in the name

print(name.upper())
print(name.lower())
print(name.title())
print(len(name))
print()

# A3. Create a variable `course` with value "  CSCI 120: Intro to Programming  "
#     Print it with leading/trailing whitespace removed
#     Print just the course number (120) using string methods or slicing

course = "  CSCI 120: Intro to Programming  "
print(course.strip())
print(course[7:10])
print()

# A4. Create variables for a price calculation:
#     - item_price = 29.99
#     - quantity = 3
#     - tax_rate = 0.07
#     Calculate and print the subtotal, tax, and total
#     Format all money values to 2 decimal places

item_price = 29.99
quantity = 3
tax_rate = 0.07

subtotal = item_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Subtotal: {subtotal: .2f}")
print(f"Tax: {tax: .2f}")
print(f"Total: {total: .2f}")
print()


# ============================================================
# PART B: Lists and List Operations (Chapter 3 Review)
# ============================================================

# B1. Create a list called `courses` with 5 course names you're taking
#     Print the first course and the last course

courses = ["Python", "Urban Studies", "Essentials in Film", "Superheroes and American Society"]
print(courses[0])
print(courses[3])

# B2. Make the following changes to your courses list:
#     - Add a new course to the end
#     - Insert a course at position 2
#     - Remove one course by name
#     - Print the updated list after each change

courses.append("Intro to Music")
print(courses)
courses.insert(2, "Digital Art")
print(courses)
del courses[3]
print(courses)
print()

# B3. Create a list of 5 numbers (any numbers you choose)
#     - Sort the list and print it
#     - Reverse the sorted list and print it
#     - Print the original list (was it changed?)

num_list = [7, 22, 81, 99, 45]
num_list.sort()
print(f"Sorted: {num_list}") # sorted
num_list.reverse()
print(f"Reversed: {num_list}") # reversed
print(f"Original List: {num_list}") # changed
print()

# B4. Create two lists:
#     - breakfast_foods with 3 items
#     - lunch_foods with 3 items
#     Combine them into a new list called all_foods
#     Print all_foods and its length

breakfast_foods = ["french toast", "scrambled eggs", "orange juice"]
lunch_foods = ["cheeseburger", "fries", "rootbeer"]

all_foods = breakfast_foods + lunch_foods
print(f"All Foods: {all_foods}")
print(f"Amount:", len(all_foods))
print()

# ============================================================
# PART C: Loops and Ranges (Chapter 4 Review)
# ============================================================

# C1. Use a for loop to print numbers 1 through 10

# start at 1, stop before 11
for value in range(1, 11):
    print(value)
print()

# C2. Use range() to create and print:
#     - Even numbers from 2 to 20
#     - Countdown from 10 to 1
#     - Multiples of 5 from 5 to 50

# start at 2, stop before 21, count by 2
even_numbers = list(range(2, 21, 2))
print(even_numbers)

# start at 10, stop before 0, countdown by 1
countdown = list(range(10, 0, -1))
print(countdown)

# start at 5, stop before 51, count by 5
multiples = list(range(5, 51, 5))
print(multiples)

print()

# C3. Given this list:
#     temperatures = [72, 68, 75, 71, 80, 78, 74]
#
#     Use a for loop to:
#     - Print each temperature
#     - Calculate and print the sum
#     - Calculate and print the average

temperatures = [72, 68, 75, 71, 80, 78, 74]
total_sum = 0

for temp in temperatures:
    print(temp)
    total_sum += temp

average = total_sum / len(temperatures)
print(f"Sum: {total_sum}")
print(f"Avg: {average}")
print()
# C4. Use a list comprehension to create:
#     - A list of squares from 1 to 10 (1, 4, 9, 16, ...)
#     - A list where each temperature is converted to Celsius
#       Formula: (temp - 32) * 5/9

# list comprehension for squares (1 to 10)
squares = [value**2 for value in range(1, 11)]
print(f"Squares: {squares}")

# list comprehension for F - C conversion
celsius_temps = [(temp-32) * 5/9 for temp in temperatures]
print(f"Celsius: {[round(c, 1) for c in celsius_temps]}")
print()
# C5. Given this list of names:
#     students = ["alice", "bob", "charlie", "diana"]
#
#     Use enumerate() to print a numbered roster:
#     1. Alice
#     2. Bob
#     3. Charlie
#     4. Diana

students = ["alice", "bob", "charlie", "diana"]

for i, student in enumerate(students, start=1):
    print(f"{i}. {student.title()}")
print()


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

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

print(f"First Quarter: {months[0:3]}")
print(f"Summer Months: {months[5:8]}")
print(f"Last Quarter: {months[9:12]}")
print()

# D2. Create a list of 8 numbers
#     - Print the first half and second half using slices
#     - Calculate the average of each half
#     - Print the average of each half

num = [14, 33, 88, 58, 42, 68, 91, 29]

print(f"First half: {num[0:4]}")
print(f"Second half: {num[4:8]}")

average = sum(num) / len(num)

print(f"Average: {average: .2f}")
print()
# D3. Demonstrate correct list copying:
#     - Create a list called original with 5 items
#     - Create a proper copy called backup using slicing
#     - Modify original (add an item)
#     - Print both lists to show backup wasn't changed

original = ["Comic Book", "Phone", "Mouse", "Pen", "Rubber Duck"]
copy = original[:]

original.append("Energy Drink")

print(f"Original: {original}")
print(f"Copy: {copy}")
print()

# D4. Create tuples for:
#     - Your birthday as (month, day, year)
#     - A location as (city, state, zip_code)
#     - Print formatted strings using each tuple

birthday = ("March", 17, 2006)
location = ("North Adams", "MA", "01247")

print(f"My birthday is {birthday[0]} {birthday[1]}th, {birthday[2]}.")
print(f"I am located in {location[0]}, {location[1]} {location[2]}")

# D5. Create a list of 3 tuples, where each tuple contains:
#     (student_name, test1_score, test2_score, test3_score)
#
#     Loop through the list and print each student's:
#     - Name
#     - All three scores
#     - Average score

students = [
    ("Sarah", 85, 92, 78),
    ("Quinn", 90, 88, 94),
    ("John", 76, 80, 82)
]

for student in students:
    name, s1, s2, s3 = student
    average = (s1 + s2 + s3) / 3
    print(f"{name} has an average score of {average:.2f}")


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
