"""
CS1350 - Week 1 Dictionary Exercises - Worked Solutions
Lecture 1: Dictionary Fundamentals
Lecture 2: Dictionary Keys & Methods

"""

# ======================================================================
# LECTURE 1 - UNIT 1.1: What Are Dictionaries?
# ======================================================================

# --- Unit 1.1 | Beginner ---
# Create a dictionary called my_info with name, age, and major.
my_info = {
    "name": "Felipe",     
    "age": 19,           
    "major": "Cybersecurity"  
}
print(my_info)


# --- Unit 1.1 | Intermediate ---

# 1. Dictionary with at least 4 food items and their prices
menu = {
    "burger": 8.99,
    "fries": 3.49,
    "soda": 1.99,
    "salad": 6.50
}
print(menu)

# 2. Dictionary mapping course names to credit hours
course_credits = {
    "CS1350": 3,
    "MATH201": 4,
    "ENG101": 3,
    "HIST110": 3
}
print(course_credits)


# --- Unit 1.1 | Advanced ---
# Use dict() instead of curly braces to map days of the week to temps
weekly_temps = dict(
    Monday=70,
    Tuesday=72,
    Wednesday=68,
    Thursday=75,
    Friday=77,
    Saturday=80,
    Sunday=78
)
print(weekly_temps)


# ======================================================================
# LECTURE 1 - UNIT 1.2: Accessing Dictionary Elements
# ======================================================================

# --- Unit 1.2 | Beginner ---
pet = {"name": "Buddy", "type": "dog", "age": 3}

# Square-bracket access is fine here because we KNOW these keys exist
print(pet["name"])   # Buddy
print(pet["age"])    # 3


# --- Unit 1.2 | Intermediate ---

# 1. Safely access "color" (doesn't exist) with a default of "unknown"
color = pet.get("color", "unknown")
print(color)  # unknown

# 2. Check if a student passed a course using get()
grades = {"CS1350": "A", "MATH201": "B"}
# get() lets us provide a fallback instead of crashing with KeyError
course = "PHYS101"
grade = grades.get(course, "Not enrolled")
if grade == "Not enrolled":
    print(f"{course}: not enrolled")
else:
    print(f"{course}: passed with grade {grade}")


# --- Unit 1.2 | Advanced ---
products = {"laptop": 999.99, "mouse": 29.99, "keyboard": 79.99}

def get_price(product_dict, name):
    """Print the price if found, otherwise print 'Product not available'."""
    price = product_dict.get(name)   # returns None if missing
    if price is None:
        print("Product not available")
    else:
        print(f"{name}: ${price}")

get_price(products, "mouse")     # exists -> prints price
get_price(products, "monitor")   # doesn't exist -> prints not available


# ======================================================================
# LECTURE 1 - UNIT 1.3: Modifying Dictionaries
# ======================================================================

# --- Unit 1.3 | Beginner ---
inventory = {}
# Assigning to a new key adds it to the dictionary
inventory["apples"] = 10
inventory["bananas"] = 5
inventory["oranges"] = 8
print(inventory)


# --- Unit 1.3 | Intermediate ---
scores = {"Team A": 45, "Team B": 38}

# 1. Update Team B's score and add Team C
scores["Team B"] = 52          # same syntax as adding -> updates existing key
scores["Team C"] = 41          # new key -> adds it
print(scores)

# 2. Remove Team A using pop() and print what score they had
removed_score = scores.pop("Team A")  # pop() removes AND returns the value
print(f"Team A had a score of {removed_score}")
print(scores)


# --- Unit 1.3 | Advanced ---
# Simple shopping cart system
cart = {}

# 1. Add 3 items with prices
cart["shirt"] = 19.99
cart["shoes"] = 49.99
cart["hat"] = 12.99
print("Cart after adding items:", cart)

# 2. Update the price of one item
cart["shoes"] = 44.99   # shoes went on sale
print("Cart after price update:", cart)

# 3. Remove one item and print what was removed
removed_item_price = cart.pop("hat")
print(f"Removed hat, which cost ${removed_item_price}")
print("Cart after removal:", cart)

# 4. Print the final cart
print("Final cart:", cart)

# Bonus: total price of remaining items
total_price = sum(cart.values())
print(f"Total price of remaining items: ${total_price:.2f}")


# ======================================================================
# LECTURE 2 - UNIT 2.1: How Dictionaries Work
# ======================================================================

# --- Unit 2.1 | Beginner ---
# Which of these are valid dictionary keys?
#
# a) "student_name"   -> VALID   (strings are immutable & hashable)
# b) [1, 2, 3]         -> INVALID (lists are mutable -> unhashable)
# c) 100               -> VALID   (numbers are immutable & hashable)
# d) ("x", "y")        -> VALID   (tuples are immutable, as long as their
#                                  contents are also immutable)
# e) {"a": 1}           -> INVALID (dictionaries are mutable -> unhashable)
# f) frozenset({1,2})  -> VALID   (frozensets are the immutable version of
#                                  sets, so they ARE hashable)


# --- Unit 2.1 | Intermediate ---

# 1. Fix the error: lists can't be used as dict keys, convert to tuples
# Broken version (would raise TypeError):
# locations = {[40.7, -74.0]: "New York", [34.0, -118.2]: "Los Angeles"}
locations = {
    (40.7, -74.0): "New York",
    (34.0, -118.2): "Los Angeles"
}
print(locations)

# 2. Predict the output, then verify
data = {"a": 1, "b": 2, "a": 3, "b": 4}
print(data)      # {'a': 3, 'b': 4}  -> duplicate keys: last value wins
print(len(data))  # 2                -> only 2 unique keys ("a" and "b")

# 3. Investigate hash values
my_name = "Jordan"
print(f"hash('{my_name}') = {hash(my_name)}")
print(f"hash(100) = {hash(100)}")   # integers hash to themselves: 100


# --- Unit 2.1 | Advanced ---

# 1. Track game high scores using (player_name, game_name) tuples as keys
high_scores = {
    ("Alice", "Tetris"): 15000,
    ("Bob", "Pac-Man"): 9800,
    ("Carol", "Tetris"): 21000
}
print(high_scores)
# Retrieve one score
print(high_scores[("Alice", "Tetris")])  # 15000

# 2. Compare list search speed vs dictionary search speed
import time

big_list = list(range(100000))
big_dict = {i: True for i in range(100000)}

start = time.time()
99999 in big_list          # O(n) - has to scan through the list
list_time = time.time() - start

start = time.time()
99999 in big_dict          # O(1) - jumps straight to the hash location
dict_time = time.time() - start

print(f"List search time: {list_time:.6f} seconds")
print(f"Dict search time: {dict_time:.6f} seconds")
if dict_time > 0:
    print(f"Dict is roughly {list_time / dict_time:.0f}x faster")


# ======================================================================
# LECTURE 2 - UNIT 2.2: The keys() and values() Methods
# ======================================================================

# --- Unit 2.2 | Beginner ---
temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}

# 1. Print all day names
print(list(temps.keys()))     # ['Monday', 'Tuesday', 'Wednesday']

# 2. Print all temperatures
print(list(temps.values()))   # [72, 75, 68]

# 3. Print how many days are in the dictionary
print(len(temps))             # 3


# --- Unit 2.2 | Intermediate ---

# 1. Highest and lowest temperatures
print(f"Highest: {max(temps.values())}")   # 75
print(f"Lowest: {min(temps.values())}")    # 68

# 2. Check if "Friday" is in the dictionary
if "Friday" in temps:            # checking keys directly is O(1) and clean
    print("Friday is in the schedule")
else:
    print("Friday is NOT in the schedule")

# 3. Use setdefault() to add "Thursday" only if it doesn't already exist
temps.setdefault("Thursday", 70)
print(temps)

# 4. Demonstrate that views are dynamic
keys_view = temps.keys()
print("Before adding Friday:", keys_view)
temps["Friday"] = 77
print("After adding Friday:", keys_view)  # view auto-updates, no copy needed


# --- Unit 2.2 | Advanced ---
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

# 1. Total value and average price
total_value = sum(prices.values())
average_price = total_value / len(prices)
print(f"Total value: ${total_value}")
print(f"Average price: ${average_price:.2f}")

# 2. Most and least expensive items (name AND price)
most_expensive_name = max(prices, key=prices.get)   # prices.get used as the sort key
least_expensive_name = min(prices, key=prices.get)
print(f"Most expensive: {most_expensive_name} (${prices[most_expensive_name]})")
print(f"Least expensive: {least_expensive_name} (${prices[least_expensive_name]})")

# 3. Compare memory usage between the view and a list
import sys
view_size = sys.getsizeof(prices.keys())
list_size = sys.getsizeof(list(prices.keys()))
print(f"keys() view size: {view_size} bytes")
print(f"list(keys()) size: {list_size} bytes")

# 4. Add 3 new products with update(), then show all products
prices.update({"monitor": 199, "keyboard": 59, "mouse": 25})
print(prices)


# ======================================================================
# LECTURE 2 - UNIT 2.3: The items() Method
# ======================================================================

# --- Unit 2.3 | Beginner ---
colors = {"apple": "red", "banana": "yellow", "grape": "purple"}

# 1. Loop through fruit + color pairs
for fruit, color in colors.items():
    print(f"The {fruit} is {color}")

# 2. Predict list(colors.items())
# Answer: [('apple', 'red'), ('banana', 'yellow'), ('grape', 'purple')]
print(list(colors.items()))


# --- Unit 2.3 | Intermediate ---
prices2 = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}

# 1. Print each item with 10% tax added
for item, price in prices2.items():
    price_with_tax = price * 1.10
    print(f"{item}: ${price:.2f} + tax = ${price_with_tax:.2f}")

# 2. Count items that cost more than $4.00
count_over_4 = 0
for item, price in prices2.items():
    if price > 4.00:
        count_over_4 += 1
print(f"Items over $4.00: {count_over_4}")

# 3. Swap two variables using tuple unpacking (one line)
x, y = 10, 20
x, y = y, x
print(f"x={x}, y={y}")   # x=20, y=10

# 4. Extended unpacking: first, last, and middle elements
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"first={first}, middle={middle}, last={last}")
# first=1, middle=[2, 3, 4], last=5


# --- Unit 2.3 | Advanced ---
scores2 = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}

# 1. Find the student with the highest score using items() + max() + lambda
best_name, best_score = max(scores2.items(), key=lambda pair: pair[1])
print(f"Top student: {best_name} with {best_score}")

# 2. Split into passed (>=70) and failed (<70) dictionaries
passed = {}
failed = {}
for name, score in scores2.items():
    if score >= 70:
        passed[name] = score
    else:
        failed[name] = score
print("Passed:", passed)
print("Failed:", failed)

# 3. Class average + each student's deviation from the average
class_average = sum(scores2.values()) / len(scores2)
deviations = {}
for name, score in scores2.items():
    deviations[name] = round(score - class_average, 2)
print(f"Class average: {class_average:.2f}")
print("Deviations from average:", deviations)

# 4. Performance test: items() iteration vs keys() + lookup (50,000 entries)
big_scores = {i: i * 2 for i in range(50000)}

start = time.time()
for k, v in big_scores.items():      # direct iteration over stored pairs
    _ = k + v
items_time = time.time() - start

start = time.time()
for k in big_scores.keys():          # extra hash lookup every iteration
    v = big_scores[k]
    _ = k + v
keys_lookup_time = time.time() - start

print(f"items() time: {items_time:.4f}s")
print(f"keys()+lookup time: {keys_lookup_time:.4f}s")
if items_time > 0:
    print(f"items() is roughly {keys_lookup_time / items_time:.1f}x faster")