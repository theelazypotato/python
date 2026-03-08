"""
Week 8 Homework: Functions (Chapter 8)
======================================

This homework covers defining and using functions.
Complete both Part A and Part B.
Stretch problems are optional extra credit.

Submit this file with your solutions.
"""


# ============================================================
# PART A: Defining Functions (Chapter 8 Basics)
# ============================================================

# A1. Simple Function
# Create a function called 'greet' that:
#     - Takes a name as a parameter
#     - Prints "Hello, [name]!"
#
# Call it 3 times with different names


# A2. Function with Return Value
# Create a function called 'square' that:
#     - Takes a number as a parameter
#     - Returns the square of that number
#
# Test it: print the squares of 5, 10, and 7


# A3. Multiple Parameters
# Create a function called 'calculate_area' that:
#     - Takes length and width as parameters
#     - Returns the area (length * width)
#
# Test with several different dimensions


# A4. Default Parameter Values
# Create a function called 'make_sandwich' that:
#     - Takes bread (required)
#     - Takes filling (default: "cheese")
#     - Takes toasted (default: False)
#     - Prints a description of the sandwich
#
# Call it with: just bread, bread + filling, all three parameters


# A5. Multiple Return Values
# Create a function called 'get_stats' that:
#     - Takes a list of numbers
#     - Returns the minimum, maximum, and average
#
# Test with: [85, 90, 78, 92, 88]
# Print all three returned values




# ============================================================
# PART B: Working with Functions (Chapter 8 Advanced)
# ============================================================

# B1. Using Return Values
# Create a function called 'is_passing' that:
#     - Takes a score
#     - Returns True if score >= 60, False otherwise
#
# Use it in a loop to check these scores: [85, 55, 72, 48, 90]
# Print which scores are passing and which are failing


# B2. Functions Calling Functions
# Create these functions:
#     1. calculate_subtotal(prices) - returns sum of prices
#     2. calculate_tax(subtotal, rate=0.08) - returns tax amount
#     3. calculate_total(prices) - uses the above two functions
#                                  returns the total with tax
#
# Test with: prices = [19.99, 5.50, 12.00, 8.75]


# B3. Modifying Lists in Functions
# Create a function called 'double_all' that:
#     - Takes a list of numbers
#     - Modifies the list in place (doubles each number)
#     - Does NOT return anything
#
# Create another function called 'doubled_copy' that:
#     - Takes a list of numbers
#     - Returns a NEW list with doubled values
#     - Original list is unchanged
#
# Test both and show the difference


# B4. Arbitrary Number of Arguments (*args)
# Create a function called 'calculate_average' that:
#     - Takes any number of arguments
#     - Returns the average of all numbers passed
#
# Test with: (85, 90), (70, 80, 90, 100), (95,)


# B5. Functions with Lists
# Create a function called 'grade_students' that:
#     - Takes a list of dictionaries:
#       [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 72}, ...]
#     - Returns a new list with grade added:
#       [{"name": "Alice", "score": 85, "grade": "B"}, ...]
#
# Test with at least 4 students




# ============================================================
# PART C: Practical Applications
# ============================================================

# C1. Temperature Converter
# Create two functions:
#     - celsius_to_fahrenheit(c): returns (c * 9/5) + 32
#     - fahrenheit_to_celsius(f): returns (f - 32) * 5/9
#
# Use them to convert: 0°C, 100°C, 32°F, 212°F
# Print results formatted to 1 decimal place


# C2. Password Generator
# Create a function called 'generate_password' that:
#     - Takes length (default: 8)
#     - Takes include_numbers (default: True)
#     - Takes include_symbols (default: False)
#     - Returns a random password
#
# Hint: Use string module and random.choice()
# Test with different parameter combinations


# C3. Text Analyzer
# Create a function called 'analyze_text' that:
#     - Takes a string of text
#     - Returns a dictionary with:
#       - "words": word count
#       - "characters": character count (no spaces)
#       - "sentences": sentence count (count . ! ?)
#       - "average_word_length": average length of words
#
# Test with a paragraph of text


# C4. Shopping Cart Functions
# Create these functions to manage a shopping cart:
#
#     add_item(cart, item, price, quantity=1)
#         - Adds an item to the cart (cart is a list of dicts)
#
#     remove_item(cart, item)
#         - Removes an item from the cart by name
#         - Returns True if removed, False if not found
#
#     get_cart_total(cart)
#         - Returns the total price of all items
#
#     print_receipt(cart)
#         - Prints a formatted receipt with all items and total
#
# Test by adding items, removing one, and printing receipt


# C5. Validation Functions
# Create these validation functions:
#
#     is_valid_email(email)
#         - Returns True if email contains @ and .
#         - The @ must come before the .
#
#     is_valid_phone(phone)
#         - Returns True if phone has exactly 10 digits
#         - Should work with: "5551234567" or "555-123-4567"
#
#     is_valid_password(password)
#         - At least 8 characters
#         - Contains at least one uppercase
#         - Contains at least one digit
#
# Test each with valid and invalid inputs




# ============================================================
# STRETCH: Function Challenge
# ============================================================

# Create a "Grade Book" application using ONLY functions:
#
# Required functions:
#     1. create_gradebook() - returns an empty gradebook structure
#
#     2. add_student(gradebook, name) - adds a student
#
#     3. add_grade(gradebook, name, assignment, score)
#         - Adds a grade for a student
#
#     4. get_student_average(gradebook, name)
#         - Returns the student's average score
#
#     5. get_class_average(gradebook)
#         - Returns the average of all student averages
#
#     6. get_top_student(gradebook)
#         - Returns the name of the student with highest average
#
#     7. print_gradebook(gradebook)
#         - Prints a formatted report of all students and grades
#
# Test by:
#     - Creating a gradebook
#     - Adding 4 students
#     - Adding 3 grades per student
#     - Printing the report
#     - Finding the top student


