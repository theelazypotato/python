"""
Week 4 Homework: Decision Making & Data Organization
=====================================================

Complete both Part A and Part B.
Both parts use a restaurant theme but are independent.
Stretch problems are optional extra credit.

Submit this file with your solutions.
"""


# ============================================================
# PART A: Restaurant Order System (Chapter 5 - If Statements)
# ============================================================

# A1. Create variables for a customer order:
#     - meal_type: "breakfast", "lunch", or "dinner"
#     - is_member: True or False
#     - order_total: a number
#
# Write if statements to determine the discount:
#     - Breakfast: 10% off
#     - Lunch: 15% off
#     - Dinner: no discount
#     - Members get an extra 5% off
# Print the original total, discount, and final price

meal_type = "lunch"
is_member = True
order_total = 12

discount_percent = 0

if meal_type == "breakfast":
    discount_percent = 0.10
elif meal_type == "lunch":
    discount_percent = 0.15
else:
    discount_percent = 0
    
if is_member:
    discount_percent += 0.05
    
discount_amount = order_total * discount_percent
final_price = order_total - discount_amount

print(f"Original Total: ${order_total: .2f}")
print(f"Discount: ${discount_amount: .2f}")
print(f"Final Price: ${final_price: .2f}")
print()

# A2. Create a kid's meal age checker:
#     - Kids under 12 can order from the kid's menu
#     - Seniors 65+ get the senior menu
#     - Everyone else gets the regular menu
# Print which menu the customer can order from
age = 30

if age < 12:
    print("you can order from the kid's menu")
elif age >= 65:
    print("you can order from the senior menu")
else:
    print("you get the regular menu")

# A3. Happy Hour Checker:
#     Create variables for current_hour (24-hour format) and day_of_week
#     Happy Hour is:
#     - Monday-Friday, 4pm-6pm (16-18)
#     - All day Sunday
#
# Print whether it's currently Happy Hour and what the special is:
#     - Happy Hour drinks are 50% off
#     - Not Happy Hour: regular prices

current_hour = 17 # 5:00 PM
day_of_week = "Monday"

# Happy Hour is M-F (4-6pm) OR all-day Sunday
if day_of_week == "Sunday" or (day_of_week != "Saturday" and 16 <= current_hour <= 18):
    print("It's Happy Hour, drinks are 50% off")
else:
    print("No Happy Hour: regular prices")

# A4. Order Validator:
#     Given these variables:
#     items_ordered = ["burger", "fries", "shake"]
#     available_items = ["burger", "pizza", "salad", "fries", "soda"]
#
# Check each ordered item:
#     - If available: print "Adding [item] to order"
#     - If not available: print "Sorry, [item] is not available"

items_ordered = ["burger", "fries", "shake"]
available_items = ["burger", "pizza", "salad", "fries", "soda"]



# A-STRETCH: Complex Order System
# Create a full order processing system that checks:
# 1. If the restaurant is open (hours: 8am-10pm)
# 2. If the ordered item is on the menu
# 3. If there are any dietary restrictions (create a list)
# 4. Apply appropriate discounts (time-based, membership, order size)
# Print a detailed order summary with all checks and final price




# ============================================================
# PART B: Restaurant Menu System (Chapter 6 - Dictionaries)
# ============================================================

# B1. Create a menu dictionary where:
#     - Keys are item names
#     - Values are prices
# Include at least 6 items across appetizers, mains, and drinks
# Print the full menu nicely formatted




# B2. Create an order by:
# 1. Starting with an empty dictionary for the customer's order
# 2. Adding 3 items with their quantities
#    Example: {"burger": 2, "fries": 1, "soda": 2}
# 3. Calculate and print the total cost using your menu prices




# B3. Menu Categories:
# Create a dictionary where:
#     - Keys are categories ("appetizers", "mains", "desserts")
#     - Values are lists of items in that category
#
# Loop through and print a categorized menu:
# APPETIZERS:
#   - wings
#   - nachos
# MAINS:
#   - burger
#   - pizza
# etc.




# B4. Daily Specials:
# Create a dictionary mapping days to their specials:
#     {"Monday": "Taco Tuesday (on Monday)", "Tuesday": "Wing Night", ...}
#
# Given a current_day variable, print today's special
# If the day doesn't have a special, print "No special today"




# B5. Customer Profiles:
# Create a dictionary for a restaurant loyalty program:
#     - Keys: customer names
#     - Values: dictionaries with "visits" and "total_spent"
#
# 1. Create profiles for 3 customers
# 2. A customer makes a new purchase - update their stats
# 3. Print all customers who have spent over $100
# 4. Find and print the customer with the most visits




# B-STRETCH: Full Restaurant Management System
# Create a comprehensive system with:
# 1. Menu dictionary with items, prices, and categories
# 2. Inventory dictionary tracking available quantities
# 3. Customer dictionary with name, order, and preferences
#
# Simulate an order:
# - Check if items are available in inventory
# - Update inventory when ordered
# - Calculate total with category-based discounts
#   (10% off appetizers, 5% off drinks)
# - Store the order in the customer's history
# - Print a detailed receipt


