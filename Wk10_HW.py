"""
Week 10 Homework: Files and Exceptions (Chapter 10)
====================================================

This homework covers reading/writing files and handling errors.

Part A: File I/O (5 problems)
Part B: Exception Handling (3 problems)
Stretch: Optional extra practice

Plan for about 45-60 minutes of work.

Submit this file with your solutions.
"""


# ============================================================
# PART A: File I/O
# ============================================================

# A1. Write to a File
# Create a list of 5 of your favorite movies (or books, songs, etc.)
# Write them to a file called 'favorites.txt', one per line.
# After writing, print "Saved [count] favorites to favorites.txt"

favorites = ["The Matrix", "Inception", "Interstellar", "The Lord of the Rings", "The Dark Knight"]

with open("favorites.txt", "w") as f:
    for item in favorites:
        f.write(item + "\n")

print(f"Saved {len(favorites)} favorites to favorites.txt")
print()
# A2. Read a File
# Read 'favorites.txt' back in and print each line.
# Also print the total number of lines in the file.
#
# Hint: Use .strip() on each line to remove the newline character.

try:
    with open("favorites.txt", "r") as f:
        line = f.readline()
        count = 0
        while line:
            print(line.strip())
            count += 1
            line = f.readline()
    print(f"Total lines in favorites.txt: {count}")
except FileNotFoundError:
    print("favorites.txt not found.")

# A3. Append to a File
# Add 3 more items to 'favorites.txt' using append mode ('a').
# Then read the file again and print the updated contents.
# Print the new total count.

try:
    with open("favorites.txt", "a") as f:
        f.write("Pulp Fiction\n")
        f.write("The Shawshank Redemption\n")
        f.write("The Godfather\n")
    with open("favorites.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())
    print(f"Total lines in favorites.txt: {len(lines)}")
except FileNotFoundError:
    print("favorites.txt not found.")

# A4. Process a File
# The code below creates a file called 'scores.txt' with student scores.
# Run it first, then write code to:
#     - Read the file line by line
#     - Split each line into name and score
#     - Print each student's name and whether they passed (score >= 60)
#     - At the end, print the average score

# --- Run this setup code first ---
with open("scores.txt", "w") as f:
    f.write("Alice,85\n")
    f.write("Bob,42\n")
    f.write("Carol,91\n")
    f.write("David,58\n")
    f.write("Eve,73\n")
print("Created scores.txt")

# YOUR CODE HERE - read and process scores.txt



# A5. Write a Report
# Using the data from scores.txt, write a summary report to 'report.txt'.
# The report should include:
#     - A header line ("Score Report")
#     - A separator line ("=" * 30)
#     - Each student's name and score
#     - A blank line
#     - The average score
#     - The highest score (and who got it)
#     - The lowest score (and who got it)
#
# After writing, read report.txt and print its contents.




# ============================================================
# PART B: Exception Handling
# ============================================================

# B1. File Not Found
# Write code that:
#     - Tries to open and read a file called 'missing.txt'
#     - Catches FileNotFoundError and prints a friendly message
#     - Prints "Done!" whether the file was found or not (use finally)


# B2. Bad Input
# Write code that:
#     - Has a list of strings: ["42", "hello", "17", "", "93", "abc"]
#     - Loops through the list
#     - Tries to convert each to an integer
#     - If it works, print the number and its square
#     - If ValueError occurs, print "[value] is not a number - skipping"


# B3. Safe File Reader
# The code below creates a file with some good and bad data.
# Write code to:
#     - Try to open 'messy_data.txt'
#     - Read each line and try to convert it to a number
#     - Skip lines that can't be converted (catch ValueError)
#     - Keep a count of good lines and bad lines
#     - Print the sum and average of the valid numbers
#     - Print how many lines were skipped

# --- Run this setup code first ---
with open("messy_data.txt", "w") as f:
    f.write("25\n")
    f.write("not a number\n")
    f.write("30\n")
    f.write("\n")
    f.write("15\n")
    f.write("oops\n")
    f.write("40\n")
    f.write("10\n")
print("Created messy_data.txt")

# YOUR CODE HERE - safely read and process messy_data.txt




# ============================================================
# STRETCH (Optional)
# ============================================================

# Contact Book
# Create a simple contact book that saves to a file:
#
# 1. Write a function save_contact(name, phone) that:
#     - Appends "name,phone" to 'contacts.txt'
#     - Uses try/except in case of file errors
#
# 2. Write a function load_contacts() that:
#     - Reads 'contacts.txt' and returns a list of (name, phone) tuples
#     - Handles FileNotFoundError (returns empty list if file missing)
#     - Skips badly formatted lines
#
# 3. Write a function find_contact(name) that:
#     - Loads contacts and searches for a name
#     - Returns the phone number if found, None if not
#
# Test by saving 3 contacts, loading them, and finding one.
