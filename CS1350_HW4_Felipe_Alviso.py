# ==============================================================================
# WEEK 2 LECTURE 1: DICTIONARY III
# ==============================================================================

# ------------------------------------------------------------------------------
# Unit 3.1 Practice Exercises
# ------------------------------------------------------------------------------

# --- Beginner ---
inventory = {"apples": 50, "bananas": 30, "oranges": 25}

# 1. Print each product name using default iteration.
for product in inventory:
    print(product)

# 2. Calculate total items using values().
total_items = sum(inventory.values())
print(f"Total items: {total_items}")

# 3. Print each product with quantity using items().
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")


# --- Intermediate ---
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

# 1. Print products sorted alphabetically.
for item in sorted(prices):
    print(f"{item}: {prices[item]}")

# 2. Print products sorted by price (cheapest first).
for item, price in sorted(prices.items(), key=lambda x: x[1]):
    print(f"{item}: ${price}")

# 3. Find and print the most expensive item using items().
most_expensive = max(prices.items(), key=lambda x: x[1])
print(f"Most expensive: {most_expensive[0]} (${most_expensive[1]})")


# --- Advanced ---
temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}

# 1. Calculate average temperature using values().
avg_temp = sum(temps.values()) / len(temps)
print(f"Average temperature: {avg_temp:.2f}")

# 2. Find the hottest and coldest days in a single loop.
hottest_day = coldest_day = None
for day, temp in temps.items():
    if hottest_day is None or temp > temps[hottest_day]:
        hottest_day = day
    if coldest_day is None or temp < temps[coldest_day]:
        coldest_day = day

print(f"Hottest day: {hottest_day} ({temps[hottest_day]}°)")
print(f"Coldest day: {coldest_day} ({temps[coldest_day]}°)")

# 3. Count how many days were above the average.
above_avg_count = sum(1 for temp in temps.values() if temp > avg_temp)
print(f"Days above average: {above_avg_count}")


# ------------------------------------------------------------------------------
# Unit 3.2 Practice Exercises
# ------------------------------------------------------------------------------

# --- Beginner ---
products = {
    "laptop": {"price": 999, "stock": 15},
    "phone": {"price": 699, "stock": 50}
}

# 1. Print the laptop's price.
print(f"Laptop price: ${products['laptop']['price']}")

# 2. Print each product with its stock level.
for item, info in products.items():
    print(f"{item}: stock={info['stock']}")


# --- Intermediate ---
# 1. Given two lists, create a dictionary using zip():
countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]
country_capitals = dict(zip(countries, capitals))
print(f"Country capitals: {country_capitals}")

# 2. Add a new product "tablet": {"price": 449, "stock": 30} to products.
products["tablet"] = {"price": 449, "stock": 30}

# 3. Safely remove all products with stock < 20 from a dictionary.
for item, info in list(products.items()):
    if info["stock"] < 20:
        del products[item]
print(f"Products after low-stock cleanup: {products}")


# --- Advanced ---
company = {
    "Engineering": {"Alice": 95000, "Bob": 85000},
    "Marketing": {"Carol": 75000, "Dave": 70000}
}

# 1. Print all employees with their salaries (nested iteration).
for dept, employees in company.items():
    for name, salary in employees.items():
        print(f"{dept} - {name}: ${salary}")

# 2. Calculate the average salary per department.
for dept, employees in company.items():
    avg_salary = sum(employees.values()) / len(employees)
    print(f"{dept} average salary: ${avg_salary:.2f}")

# 3. Find the highest-paid employee across all departments.
highest_paid = max(
    ((name, salary) for dept in company.values() for name, salary in dept.items()),
    key=lambda x: x[1]
)
print(f"Highest-paid employee: {highest_paid[0]} (${highest_paid[1]})")


# ------------------------------------------------------------------------------
# Unit 3.3 Practice Exercises
# ------------------------------------------------------------------------------

# --- Beginner ---
# 1. Create a comprehension mapping numbers 1-5 to their cubes.
cubes = {x: x**3 for x in range(1, 6)}
print(f"Cubes: {cubes}")

# 2. Given temps, create a new dict with Celsius values.
temps_f = {"Mon": 72, "Tue": 68, "Wed": 75}
temps_c = {day: (temp - 32) * 5 / 9 for day, temp in temps_f.items()}
print(f"Celsius temps: {temps_c}")


# --- Intermediate ---
scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}

# 1. Create passing dict with only scores >= 70.
passing_scores = {name: score for name, score in scores.items() if score >= 70}
print(f"Passing scores: {passing_scores}")

# 2. Create letter_grades dict converting scores to letters.
def to_letter(s):
    if s >= 90: return "A"
    if s >= 80: return "B"
    if s >= 70: return "C"
    return "F"

letter_grades = {name: to_letter(score) for name, score in scores.items()}
print(f"Letter grades: {letter_grades}")

# 3. Invert student_ids to look up by ID.
student_ids = {"Alice": 101, "Bob": 102}
id_lookup = {v: k for k, v in student_ids.items()}
print(f"Inverted student IDs: {id_lookup}")


# --- Advanced ---
sales = [
    ("North", "Alice", 5000),
    ("South", "Bob", 4500),
    ("North", "Carol", 6000),
    ("South", "Alice", 3500)
]

# 1. Calculate total sales by region.
sales_by_region = {}
for region, _, amount in sales:
    sales_by_region[region] = sales_by_region.get(region, 0) + amount
print(f"Sales by region: {sales_by_region}")

# 2. Calculate total sales by salesperson.
sales_by_person = {}
for _, person, amount in sales:
    sales_by_person[person] = sales_by_person.get(person, 0) + amount
print(f"Sales by person: {sales_by_person}")

# 3. Create a nested dict: {region: {person: total}}.
nested_sales = {}
for region, person, amount in sales:
    if region not in nested_sales:
        nested_sales[region] = {}
    nested_sales[region][person] = nested_sales[region].get(person, 0) + amount
print(f"Nested sales: {nested_sales}")


# ==============================================================================
# WEEK 2 LECTURE 2: SETS
# ==============================================================================

# ------------------------------------------------------------------------------
# Unit 1 Practice Exercises
# ------------------------------------------------------------------------------

# --- Beginner ---
# 1. Create a set from a list with duplicates to get unique values.
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print(f"Unique numbers: {unique_numbers}")

# 2. Add 'orange' and remove 'banana' from a set.
fruit_set = {"apple", "banana"}
fruit_set.add("orange")
fruit_set.discard("banana")
print(f"Updated fruits: {fruit_set}")

# 3. Check membership of 'apple' in the set.
is_apple_present = "apple" in fruit_set
print(f"Is 'apple' in set? {is_apple_present}")


# --- Intermediate ---
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# 1. Find union, intersection, and difference between set_a and set_b.
print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference (a - b): {set_a - set_b}")

# 2. Remove duplicates from a list while preserving original order.
dup_list = [4, 1, 2, 1, 3, 2, 4]
seen = set()
ordered_unique = [x for x in dup_list if not (x in seen or seen.add(x))]
print(f"Ordered unique list: {ordered_unique}")

# 3. Find symmetric difference between set_a and set_b.
print(f"Symmetric difference: {set_a ^ set_b}")


# --- Advanced ---
# 1. Find elements present in all three sets.
s_a = {1, 2, 3, 4}
s_b = {2, 3, 4, 5}
s_c = {3, 4, 5, 6}
common_three = s_a & s_b & s_c
print(f"Common across all three sets: {common_three}")

# 2. Perform subset and superset checks.
sub_set = {2, 3}
print(f"Is sub_set a subset of s_a? {sub_set.issubset(s_a)}")
print(f"Is s_a a superset of sub_set? {s_a.issuperset(sub_set)}")

# 3. Check if two sets are disjoint.
s_d = {7, 8}
print(f"Are s_a and s_d disjoint? {s_a.isdisjoint(s_d)}")


# ------------------------------------------------------------------------------
# Unit 2 Practice Exercises
# ------------------------------------------------------------------------------

# --- Beginner ---
# 1. Clear all elements from a set.
clear_demo = {10, 20, 30}
clear_demo.clear()
print(f"Cleared set: {clear_demo}")

# 2. Create a frozenset.
frozen_data = frozenset([1, 2, 3])
print(f"Frozenset: {frozen_data}")

# 3. Demonstrate difference between remove() and discard().
demo_set = {1, 2}
demo_set.discard(99)  # Does nothing, no error raised
# demo_set.remove(99) # Uncommenting this line would raise a KeyError


# --- Intermediate ---
# 1. Demonstrate in-place set updates (update and intersection_update).
update_target = {1, 2, 3}
update_target.update({3, 4, 5})
print(f"After update: {update_target}")

inter_target = {1, 2, 3}
inter_target.intersection_update({2, 3, 4})
print(f"After intersection_update: {inter_target}")

# 2. Use a frozenset as a dictionary key.
group_data = {frozenset(["Alice", "Bob"]): "Group A"}
print(f"Dict with frozenset key: {group_data}")

# 3. Pop elements from a set.
pop_set = {"a", "b", "c"}
popped_item = pop_set.pop()
print(f"Popped item: {popped_item}, Remaining: {pop_set}")


# --- Advanced ---
# 1. Safely remove even numbers from a set while iterating.
modifiable_set = {1, 2, 3, 4, 5, 6}
for val in list(modifiable_set):
    if val % 2 == 0:
        modifiable_set.remove(val)
print(f"Set after removing evens safely: {modifiable_set}")

# 2. Find elements unique to each set in a list of sets.
list_of_sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
all_elements = set().union(*list_of_sets)
unique_to_each = [s - (all_elements - s) for s in list_of_sets]
print(f"Unique elements per set: {unique_to_each}")

# 3. Perform set operations using frozensets.
fz1 = frozenset([1, 2, 3])
fz2 = frozenset([3, 4, 5])
print(f"Frozenset intersection: {fz1 & fz2}")


# ------------------------------------------------------------------------------
# Unit 3 Practice Exercises
# ------------------------------------------------------------------------------

# --- Beginner ---
# 1. Set comprehension for squares of 1 to 5.
set_squares = {x**2 for x in range(1, 6)}
print(f"Set of squares: {set_squares}")

# 2. Extract unique first letters from a list of words.
words = ["apple", "banana", "apricot", "cherry"]
first_letters = {w[0] for w in words}
print(f"Unique first letters: {first_letters}")

# 3. Filter odd numbers into a set.
odd_set = {x for x in range(10) if x % 2 != 0}
print(f"Odd numbers set: {odd_set}")


# --- Intermediate ---
# 1. Unique word count ignoring case.
text = "Apple banana APPLE cherry Banana"
unique_words_case_insensitive = {word.lower() for word in text.split()}
print(f"Unique words count: {len(unique_words_case_insensitive)}")

# 2. Find common elements across multiple lists using set operations.
l1, l2, l3 = [1, 2, 3], [2, 3, 4], [3, 4, 5]
common_list_elements = set(l1) & set(l2) & set(l3)
print(f"Common elements across lists: {common_list_elements}")

# 3. Find missing numbers in a range from 1 to N.
given_nums = {1, 2, 4, 5, 7, 8, 10}
full_set = set(range(1, 11))
missing_nums = full_set - given_nums
print(f"Missing numbers: {missing_nums}")


# --- Advanced ---
# 1. Fast lookup comparison vs list lookup.
large_set = set(range(100000))
print(f"Is 99999 in large_set? {99999 in large_set}")  # O(1) hash table lookup

# 2. Find all unique pairs whose sum equals a target.
num_pool = [1, 2, 3, 4, 5, 6]
target_sum = 7
seen_vals = set()
target_pairs = set()

for num in num_pool:
    complement = target_sum - num
    if complement in seen_vals:
        target_pairs.add((min(num, complement), max(num, complement)))
    seen_vals.add(num)

print(f"Pairs summing to {target_sum}: {target_pairs}")

# 3. Group words by length using set comprehensions & dicts.
sample_words = ["cat", "dog", "elephant", "bear", "lion"]
lengths = {len(w) for w in sample_words}
words_by_length = {length: {w for w in sample_words if len(w) == length} for length in lengths}
print(f"Words grouped by length: {words_by_length}")