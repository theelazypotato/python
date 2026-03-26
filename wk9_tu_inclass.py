"""
Chapter 8: Functions - In-Class Exercises
==========================================

Practice defining and calling functions.

Instructions:
- Work through exercises 1-7
- Try the stretch challenge if you finish early
- Ask for help if you get stuck!
"""


# %% EXERCISE 1: FILL IN THE BLANK
# Complete the function definition and call
# Replace ___ with the correct syntax

def say_hello():
    print("Hello, World!")

# Call the function
say_hello()




# %% EXERCISE 2: FILL IN THE BLANK
# Complete the function to return the sum of two numbers
# Replace ___ with the correct keyword

def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")




# %% EXERCISE 3: FILL IN THE BLANK
# Add a default value so the greeting defaults to "Hello"
# Replace ___ with the correct syntax

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")           # Should print: Hello, Alice!
greet("Bob", "Hi")       # Should print: Hi, Bob!




# %% EXERCISE 4: GUIDED
# Create a function called 'calculate_tip' that:
# 1. Takes two parameters: bill_amount and tip_percent
# 2. Calculates the tip amount
# 3. Returns the tip amount
#
# Then call it with a $50 bill and 20% tip
# Print the result

# Your code here

def calculate_tip(bill_amount, tip_percent):
    tip_amount = (tip_percent / 100) * bill_amount
    return tip_amount

result = calculate_tip(50,20)
print(result)

# %% EXERCISE 5: GUIDED
# Create a function called 'format_name' that:
# 1. Takes first_name and last_name as parameters
# 2. Returns the full name in "Last, First" format
# 3. The result should be in title case
#
# Test with: format_name("john", "doe") should return "Doe, John"

# Your code here

def format_name(first_name, last_name):
    # return a formatted full name
    return f"{last_name} {first_name}".title()
    
name = format_name("raina", "duffy")
print(f"Full Name: {name}")


# %% EXERCISE 6: TRY YOURSELF
# Create a temperature converter with TWO functions:
#
# 1. celsius_to_fahrenheit(celsius)
#    Formula: F = C * 9/5 + 32
#
# 2. fahrenheit_to_celsius(fahrenheit)
#    Formula: C = (F - 32) * 5/9
#
# Test both functions with several values
# Print results formatted to 1 decimal place

# Your code here

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

c_val = 100
f_result = celsius_to_fahrenheit(c_val)
print(f"{c_val}°C = {f_result:.1f}°F")

f_val = 10
c_result = fahrenheit_to_celsius(f_val)
print(f"{f_val}°F = {c_result:.1f}°C")

c_val = 4
f_result = celsius_to_fahrenheit(c_val)
print(f"{c_val}°C = {f_result:.1f}°F")

f_val = 68
c_result = fahrenheit_to_celsius(f_val)
print(f"{f_val}°F = {c_result:.1f}°C")

# %% EXERCISE 7: TRY YOURSELF
# Create a simple grade calculator with these functions:
#
# 1. calculate_average(scores)
#    Takes a list of scores, returns the average
#
# 2. get_letter_grade(average)
#    Takes an average, returns "A", "B", "C", "D", or "F"
#
# 3. print_report(name, scores)
#    Uses the above functions to print:
#    "Name: [name]"
#    "Scores: [scores]"
#    "Average: [average]"
#    "Grade: [letter]"
#
# Test with: print_report("Alice", [85, 92, 78, 90, 88])

# Your code here

def calculate_average(scores):
    average = sum(scores) / len(scores)
    return average

def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def print_report(name, scores):
    average = calculate_average(scores)
    letter_grade = get_letter_grade(average)
    print(f"Name: {name}")
    print(f"Scores: {scores}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {letter_grade}")

print_report("Raina", [75, 70, 78, 97, 82])
# %% STRETCH CHALLENGE
# Create a simple text-based RPG combat calculator!
#
# Create these functions:
#
# 1. calculate_damage(base_attack, weapon_bonus, critical=False)
#    - Returns base_attack + weapon_bonus
#    - If critical is True, double the damage
#
# 2. apply_armor(damage, armor_value)
#    - Returns damage reduced by armor_value (minimum 1)
#
# 3. attack(attacker_stats, defender_stats)
#    - attacker_stats is a dict: {"attack": 10, "weapon": 5}
#    - defender_stats is a dict: {"hp": 100, "armor": 3}
#    - Calculate damage, apply armor, return damage dealt
#
# 4. battle_round(player, enemy)
#    - Both attack each other
#    - Print what happens
#    - Return updated hp values
#
# Simulate a battle between a player and an enemy!


