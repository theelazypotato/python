"""
Week 9 Homework: Functions (Ch 8) & Classes (Ch 9)
===================================================

This homework covers two chapters:
  - Part A: Functions (Chapter 8) - 5 problems
  - Part B: Classes (Chapter 9) - 5 problems
  - Stretch: Optional extra practice (1 from each chapter)

Plan for about 60-75 minutes of work.

Submit this file with your solutions.
"""


# ============================================================
# PART A: Functions (Chapter 8)
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
#         Example: "Wheat bread with turkey (toasted)" or
#                  "White bread with cheese (not toasted)"
#
# Call it with: just bread, bread + filling, all three parameters


# A5. Using Return Values
# Create a function called 'is_passing' that:
#     - Takes a score
#     - Returns True if score >= 60, False otherwise
#
# Use it in a loop to check these scores: [85, 55, 72, 48, 90]
# Print which scores are passing and which are failing




# ============================================================
# PART B: Classes (Chapter 9)
# ============================================================

# B1. Dog Class
# Create a class called 'Dog' with:
#     - __init__ that takes name and breed
#     - Attributes: self.name, self.breed
#     - Method sit(): prints "[name] is now sitting."
#     - Method roll_over(): prints "[name] rolled over!"
#
# After your class, create one Dog instance and call both methods.


# B2. Student Class
# Create a class called 'Student' with:
#     - __init__ that takes name and major
#     - Attributes: self.name, self.major
#     - Method introduce(): prints "Hi, I'm [name] and my major is [major]."
#
# After your class, create one Student instance and call introduce().


# B3. Rectangle Class
# Create a class called 'Rectangle' with:
#     - __init__ that takes width and height
#     - Attributes: self.width, self.height
#     - Method area(): returns width * height
#
# After your class, create one Rectangle and print its area.


# B4. Multiple Dogs
# Using your Dog class from B1:
#     - Create 3 different Dog instances
#     - Print each dog's name and breed using dot notation
#     - Call sit() on one dog and roll_over() on another


# B5. Multiple Rectangles
# Using your Rectangle class from B3:
#     - Create 3 rectangles with different dimensions
#     - Print the area of each one
#     - Print which rectangle has the largest area




# ============================================================
# STRETCH (Optional)
# ============================================================

# STRETCH A: Temperature Converter
# Create two functions:
#     - celsius_to_fahrenheit(c): returns (c * 9/5) + 32
#     - fahrenheit_to_celsius(f): returns (f - 32) * 5/9
#
# Use them to convert: 0°C, 100°C, 32°F, 212°F
# Print results formatted to 1 decimal place


# STRETCH B: Pet Class
# Create a class called 'Pet' with:
#     - __init__ that takes name, species, and age
#     - Attributes: self.name, self.species, self.age
#     - Method describe(): prints "[name] is a [species] who is [age] years old."
#     - Method birthday(): adds 1 to age and prints
#           "Happy birthday [name]! You are now [age] years old."
#
# Create 3 Pet instances (different species), describe each one,
# then call birthday() on one of them and describe it again.
