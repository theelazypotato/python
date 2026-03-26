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

def greet(name):
    print(f"Hello, {name}!")
  
greet("Raina")
greet("Sam")
greet("Oscar")

print()
# A2. Function with Return Value
# Create a function called 'square' that:
#     - Takes a number as a parameter
#     - Returns the square of that number
#
# Test it: print the squares of 5, 10, and 7

def square(num):
    return num ** 2

print(square(5))
print(square(10))
print(square(7))

print()
# A3. Multiple Parameters
# Create a function called 'calculate_area' that:
#     - Takes length and width as parameters
#     - Returns the area (length * width)
#
# Test with several different dimensions

def calculate_area(length,width):
    return length * width
  
print(calculate_area(5, 3))
print(calculate_area(10, 2))
print(calculate_area(7, 4))

print()
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
def make_sandwich(bread, filling="cheese", toasted=False):
    toast_status = "toasted" if toasted else "not toasted"
    print(f"{bread} bread with {filling} ({toast_status})")

make_sandwich("Rye")
make_sandwich("Sourdough", "ham")
make_sandwich("Whole Wheat", "turkey", True)

print()
# A5. Using Return Values
# Create a function called 'is_passing' that:
#     - Takes a score
#     - Returns True if score >= 60, False otherwise
#
# Use it in a loop to check these scores: [85, 55, 72, 48, 90]
# Print which scores are passing and which are failing

def is_passing(score):
  return score >= 60

scores = [85, 55, 72, 48, 90]
for score in scores:
  if is_passing(score):
    print(f"{score} is passing.")
  else:
    print(f"{score} is failing.")

print()
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

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def sit(self):
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        print(f"{self.name} rolled over!")
    
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.sit()
my_dog.roll_over()

print()
# B2. Student Class
# Create a class called 'Student' with:
#     - __init__ that takes name and major
#     - Attributes: self.name, self.major
#     - Method introduce(): prints "Hi, I'm [name] and my major is [major]."
#
# After your class, create one Student instance and call introduce().

class Student:
    def __init__ (self, name, major):
        self.name = name
        self.major = major
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and my major is {self.major}.")
    
my_student = Student("Raina", "Computer Undeclared")
my_student.introduce()

print()

# B3. Rectangle Class
# Create a class called 'Rectangle' with:
#     - __init__ that takes width and height
#     - Attributes: self.width, self.height
#     - Method area(): returns width * height
#
# After your class, create one Rectangle and print its area.

class Rectangle:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
my_rectangle = Rectangle(12, 3)
print(f"The area of the rectangle is: {my_rectangle.area()}")

print()

# B4. Multiple Dogs
# Using your Dog class from B1:
#     - Create 3 different Dog instances
#     - Print each dog's name and breed using dot notation
#     - Call sit() on one dog and roll_over() on another

dog1 = Dog("Max", "Labrador")
dog2 = Dog("Bella", "Poodle")
dog3 = Dog("Charlie", "Beagle")

print(f"Dog 1: {dog1.name}, {dog1.breed}")
print(f"Dog 2: {dog2.name}, {dog2.breed}")
print(f"Dog 3: {dog3.name}, {dog3.breed}")

dog1.sit()
dog2.roll_over()

print()

# B5. Multiple Rectangles
# Using your Rectangle class from B3:
#     - Create 3 rectangles with different dimensions
#     - Print the area of each one
#     - Print which rectangle has the largest area

rectangle1 = Rectangle(5, 4)
rectangle2 = Rectangle(10, 2)
rectangle3 = Rectangle(7, 3)

print(f"Area of Rectangle 1: {rectangle1.area()}")
print(f"Area of Rectangle 2: {rectangle2.area()}")
print(f"Area of Rectangle 3: {rectangle3.area()}")

areas = [rectangle1.area(), rectangle2.area(), rectangle3.area()]
largest_area = max(areas)
if largest_area == rectangle1.area():
    print("Rectangle 1 has the largest area.")  
elif largest_area == rectangle2.area():
    print("Rectangle 2 has the largest area.")  
else:
    print("Rectangle 3 has the largest area.")  
    
print()

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
