"""
Week 3 Homework: Working with Lists
===================================

Complete both Part A and Part B.
Part B builds on Part A (sequential).
Stretch problems are optional extra credit.

Submit this file with your solutions.
"""


# ============================================================
# PART A: Grade Calculator (Chapter 4a - Loops)
# ============================================================

# A1. Create a list called `test_scores` with at least 6 test scores
#     (use realistic scores between 0-100)

test_scores = [ 60,  75,  82,  100, 98, 93]


# A2. Use a for loop to print each score with its test number:
#     Test 1: 85
#     Test 2: 92
#     ... etc.

for index, score in enumerate(test_scores, start=1):
    print(f"Test {index}: {score}")

# A3. Calculate and print the following statistics:
#     - Total number of tests
#     - Highest score
#     - Lowest score
#     - Sum of all scores
#     - Average score (formatted to 1 decimal place)

num_tests = len(test_scores)
highest_score = max(test_scores)
lowest_score = min(test_scores)
total_sum = sum(test_scores)
average = total_sum / num_tests
print()
# %%
print(f"Total Tests Taken: {num_tests}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Sum of Scores: {total_sum}")
print(f"Average Score: {average:.1f}\n")

# A4. Use a for loop to count how many scores are:
#     - 90 or above (A)
#     - 80-89 (B)
#     - 70-79 (C)
#     - 60-69 (D)
#     - Below 60 (F)
#     Print the count for each category

grade_a = 0
grade_b = 0
grade_c = 0
grade_d = 0
grade_f = 0

for i in range(len(test_scores)):
    current_score = test_scores[i]
    
    grade_a += (current_score >= 90)
    grade_b += (80 <= current_score <= 89)
    grade_c += (70 <= current_score <= 79)
    grade_d += (60 <= current_score <= 69)
    grade_f += (current_score < 60)
# %%        
print(f"A: {grade_a}")
print(f"B: {grade_b}")
print(f"C: {grade_c}")
print(f"D: {grade_d}")
print(f"F: {grade_f}\n")

# A5. Create a new list called `curved_scores` using a for loop
#     that adds 5 points to each original score (max 100)
#     Print both lists

curved_scores = []

for i in range(len(test_scores)):
    new_score = test_scores[i] + 5
    
    final_curve = min(new_score, 100)
    
    curved_scores.append(final_curve)
# %%
print(f"Original Scores: {test_scores}")
print(f"Curved Scores: {curved_scores}\n")

# A-STRETCH: Use a list comprehension to create a list of letter grades
# for each score. Then print each score with its letter grade.
# Example: "Score: 85 -> Grade: B"

letter_grades = ["A" if s >= 90 else "B" if s >= 80 else "C" if s >= 70 else "D" if s >= 60 else "F" for s in test_scores]

for i in range(len(test_scores)):
    print(f"Score: {test_scores[i]} -> Grade: {letter_grades[i]}")
print()

# ============================================================
# PART B: Grade Analysis (Chapter 4b - Slices and Tuples)
# ============================================================

# Use the same test_scores list from Part A

# B1. Using slicing, print:
#     - The first 3 test scores (early tests)
#     - The last 3 test scores (recent tests)
#     - Compare their averages - did you improve?
# %%
print(f"Early Tests: {test_scores[0:3]}")
print(f"Recent Tests: {test_scores[3:6]}\n")

e_sum = sum(test_scores[0:3])
r_sum = sum(test_scores[3:6])

early_sum = e_sum / 3
recent_sum = r_sum /3

improvement = recent_sum - early_sum
# %%
print(f"Average for recent tests: {recent_sum: .1f}")
print(f"Average for early tests: {early_sum: .1f}")
print(f"Improvement: {improvement: .1f}")

# B2. Create a copy of test_scores called `what_if_scores`
#     In the copy, replace the lowest score with 100
#     Calculate the new average
#     Print how much the average changed
#     (Make sure original test_scores is unchanged!)

what_if_scores = test_scores[:]
what_if_scores[0] = 100
what_if_sum = sum(what_if_scores)
num_score = len(what_if_scores)
what_if_average = what_if_sum / num_score
what_if_improvement = what_if_average - average

print("what if's: ")
print(what_if_scores)
print(f"Average: {what_if_average: .1f}")
print(f"Improvement: {what_if_improvement: .1f}")
print()


# B3. Create tuples for grade boundaries:
#     a_range = (90, 100)
#     b_range = (80, 89)
#     c_range = (70, 79)
#     d_range = (60, 69)
#
#     Use these tuples to print grade cutoffs:
#     "A: 90-100", "B: 80-89", etc.

a_range = (90, 100)
b_range = (80, 89)
c_range = (70, 79)
d_range = (60, 69)

print(f"A: {a_range}")
print(f"B: {b_range}")
print(f"C: {c_range}")
print(f"D: {d_range}")
print()


# B4. Create a tuple called `course_info` containing:
#     (course_name, instructor, num_tests, average_score)
#     Print a formatted course summary using this tuple

course_info = ("Math", "Anderson", 8, 90.7)
name, teacher, tests, grade = course_info
print(f"Course: {name} | Instructor: {teacher} | Tests: {tests} | Avg: {grade}")
print()


# B5. Create a list of 3 course tuples (like course_info above)
#     for different classes. Loop through and print a summary
#     of each course.

courses = [("History", "Miller", 5, 88.5),
           ("Science", "Davis", 10, 92.3),
           ("Art", "Butterfield", 4, 95.0)]

for course in courses:
    name, teacher, tests, grade = course
    print(f"Course: {name} | Instructor: {teacher} | Tests: {tests} | Avg: {grade}")



# B-STRETCH: Grade Trend Analyzer
# Using slices, compare the first half of test_scores to the second half.
# Calculate the average for each half.
# Determine if you're improving, declining, or staying consistent.
# Print a detailed analysis:
#   - First half scores and average
#   - Second half scores and average
#   - The difference
#   - A message: "Improving!", "Need more practice", or "Consistent performance"

# %%
