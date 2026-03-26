student = {"name": "Alex", "age": 20, "major": "computer science"}

print(student)
student["email"] = "email@example.com"
for key, value in student.items():
    print(f"{key}: {value}")
    
x = 15
if x > 20:
    print("A")
elif x > 10:
    print("B")
elif x > 5:
    print("C")
else:
    print("D")
    
words = []

while True:
    user_input = input("Enter a word: ")
    if user_input == "quit":
        break
    else:
        words.append(user_input)

print(F"Total words: {len(words)}")
print(words)

inventory = {'apples': 5, 'bananas': 2, 'oranges': 8, 'grapes': 1}
total = 0
low_stock = []
for item, count in inventory.items():
    total += count
    if count < 3:
        low_stock.append(item)
print(total)
print(low_stock)

count = 1
while count <= 4:
    if count == 2:
        count += 1
        continue
    print(count, end=" ")
    count += 1

data = {'a': 1, 'b': 2, 'c': 3}
data['b'] = 5
data['d'] = 4
print(data['b'], data.get('e', 0))

nums = [10, 25, 5, 30, 15]
count = 0
for num in nums:
    if num > 20:
        count += 1
    elif num > 10:
        count += 2

print(count)

numbers = [4, 7, 2, 9, 1, 8]
result = []
for num in numbers:
    if num > 5:
        result.append(num)
    elif num < 3:
        result.append(num * 10)
print(result)

scores = [85, 72, 90, 58, 76, 95, 61]
passing = []

for s in scores:
    if s >= 70:
        passing.append(s)
print(len(passing))