# ============================================
# CS1350 COMPUTER SCIENCE II
# WEEK 2 PRACTICE EXERCISES
# DICTIONARIES III + SETS
# ============================================


# ============================================
# LECTURE 1 - DICTIONARY III
# ============================================


# ============================================
# UNIT 3.1 - ITERATING THROUGH DICTIONARIES
# ============================================


# UNIT 3.1 - BEGINNER EXERCISE 1
# Print each product name using default iteration.

inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25
}

for product in inventory:
    print(product)


# UNIT 3.1 - BEGINNER EXERCISE 2
# Calculate total items using values().

inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25
}

total = sum(inventory.values())
print("Total items:", total)


# UNIT 3.1 - BEGINNER EXERCISE 3
# Print each product with quantity using items().

inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25
}

for product, quantity in inventory.items():
    print(f"{product}: {quantity}")


# ============================================
# UNIT 3.1 - INTERMEDIATE EXERCISES
# ============================================


# UNIT 3.1 - INTERMEDIATE EXERCISE 1
# Print products sorted alphabetically.

prices = {
    "laptop": 999,
    "phone": 699,
    "tablet": 449,
    "watch": 299
}

for product in sorted(prices):
    print(product)


# UNIT 3.1 - INTERMEDIATE EXERCISE 2
# Print products sorted by price, cheapest first.

prices = {
    "laptop": 999,
    "phone": 699,
    "tablet": 449,
    "watch": 299
}

for product in sorted(prices, key=prices.get):
    print(f"{product}: ${prices[product]}")


# UNIT 3.1 - INTERMEDIATE EXERCISE 3
# Find and print the most expensive item.

prices = {
    "laptop": 999,
    "phone": 699,
    "tablet": 449,
    "watch": 299
}

most_expensive = None
highest_price = 0

for product, price in prices.items():
    if price > highest_price:
        highest_price = price
        most_expensive = product

print(f"Most expensive: {most_expensive} (${highest_price})")


# ============================================
# UNIT 3.1 - ADVANCED EXERCISES
# ============================================


# UNIT 3.1 - ADVANCED EXERCISE 1
# Calculate average temperature using values().

temps = {
    "Mon": 72,
    "Tue": 68,
    "Wed": 75,
    "Thu": 80,
    "Fri": 65
}

average = sum(temps.values()) / len(temps)

print(f"Average temperature: {average:.1f}")


# UNIT 3.1 - ADVANCED EXERCISE 2
# Find the hottest and coldest days in a single loop.

temps = {
    "Mon": 72,
    "Tue": 68,
    "Wed": 75,
    "Thu": 80,
    "Fri": 65
}

hottest_day = None
hottest_temp = float("-inf")

coldest_day = None
coldest_temp = float("inf")

for day, temp in temps.items():

    if temp > hottest_temp:
        hottest_temp = temp
        hottest_day = day

    if temp < coldest_temp:
        coldest_temp = temp
        coldest_day = day

print(f"Hottest: {hottest_day} ({hottest_temp})")
print(f"Coldest: {coldest_day} ({coldest_temp})")


# UNIT 3.1 - ADVANCED EXERCISE 3
# Count how many days were above the average.

temps = {
    "Mon": 72,
    "Tue": 68,
    "Wed": 75,
    "Thu": 80,
    "Fri": 65
}

average = sum(temps.values()) / len(temps)

above_average = 0

for temp in temps.values():
    if temp > average:
        above_average += 1

print("Days above average:", above_average)


# ============================================
# UNIT 3.2 - ADVANCED ITERATION & NESTED DICTIONARIES
# ============================================


# UNIT 3.2 - BEGINNER EXERCISE 1
# Print the laptop's price.

products = {
    "laptop": {
        "price": 999,
        "stock": 15
    },
    "phone": {
        "price": 699,
        "stock": 50
    }
}

print(products["laptop"]["price"])


# UNIT 3.2 - BEGINNER EXERCISE 2
# Print each product with its stock level.

products = {
    "laptop": {
        "price": 999,
        "stock": 15
    },
    "phone": {
        "price": 699,
        "stock": 50
    }
}

for product, info in products.items():
    print(f"{product}: {info['stock']} in stock")


# UNIT 3.2 - INTERMEDIATE EXERCISE 1
# Given two lists, create a dictionary using zip().

countries = [
    "USA",
    "Canada",
    "Mexico"
]

capitals = [
    "Washington",
    "Ottawa",
    "Mexico City"
]

country_capitals = dict(zip(countries, capitals))

print(country_capitals)


# UNIT 3.2 - INTERMEDIATE EXERCISE 2
# Add a new product "tablet".

products = {
    "laptop": {
        "price": 999,
        "stock": 15
    },
    "phone": {
        "price": 699,
        "stock": 50
    }
}

products["tablet"] = {
    "price": 449,
    "stock": 30
}

print(products)


# UNIT 3.2 - INTERMEDIATE EXERCISE 3
# Safely remove all products with stock < 20.

products = {
    "laptop": {
        "price": 999,
        "stock": 15
    },
    "phone": {
        "price": 699,
        "stock": 50
    },
    "tablet": {
        "price": 449,
        "stock": 30
    }
}

for product, info in list(products.items()):
    if info["stock"] < 20:
        del products[product]

print(products)


# UNIT 3.2 - ADVANCED EXERCISE 1
# Print all employees with their salaries.

company = {
    "Engineering": {
        "Alice": 95000,
        "Bob": 85000
    },
    "Marketing": {
        "Carol": 75000,
        "Dave": 70000
    }
}

for department, employees in company.items():

    print(f"\n{department}:")

    for employee, salary in employees.items():
        print(f"{employee}: ${salary}")


# UNIT 3.2 - ADVANCED EXERCISE 2
# Calculate the average salary per department.

company = {
    "Engineering": {
        "Alice": 95000,
        "Bob": 85000
    },
    "Marketing": {
        "Carol": 75000,
        "Dave": 70000
    }
}

for department, employees in company.items():

    average = sum(employees.values()) / len(employees)

    print(f"{department} average: ${average:.2f}")


# UNIT 3.2 - ADVANCED EXERCISE 3
# Find the highest-paid employee across all departments.

company = {
    "Engineering": {
        "Alice": 95000,
        "Bob": 85000
    },
    "Marketing": {
        "Carol": 75000,
        "Dave": 70000
    }
}

highest_employee = None
highest_salary = 0

for department, employees in company.items():

    for employee, salary in employees.items():

        if salary > highest_salary:
            highest_salary = salary
            highest_employee = employee

print(f"Highest-paid employee: {highest_employee}")
print(f"Salary: ${highest_salary}")


# ============================================
# UNIT 3.3 - DICTIONARY PATTERNS & TRANSFORMATIONS
# ============================================


# UNIT 3.3 - BEGINNER EXERCISE 1
# Create a comprehension mapping numbers 1-5 to their cubes.

cubes = {
    x: x ** 3
    for x in range(1, 6)
}

print(cubes)


# UNIT 3.3 - BEGINNER EXERCISE 2
# Create a new dictionary with Celsius values.

temps = {
    "Mon": 72,
    "Tue": 68,
    "Wed": 75
}

celsius = {
    day: (temp - 32) * 5 / 9
    for day, temp in temps.items()
}

print(celsius)


# UNIT 3.3 - INTERMEDIATE EXERCISE 1
# Create passing dictionary with only scores >= 70.

scores = {
    "Alice": 88,
    "Bob": 65,
    "Carol": 92,
    "Dave": 71,
    "Eve": 58
}

passing = {
    name: score
    for name, score in scores.items()
    if score >= 70
}

print("Passing:", passing)


# UNIT 3.3 - INTERMEDIATE EXERCISE 2
# Create letter_grades converting scores to letters.

scores = {
    "Alice": 88,
    "Bob": 65,
    "Carol": 92,
    "Dave": 71,
    "Eve": 58
}

def to_letter(score):

    if score >= 90:
        return "A"

    if score >= 80:
        return "B"

    if score >= 70:
        return "C"

    return "F"


letter_grades = {
    name: to_letter(score)
    for name, score in scores.items()
}

print("Letter grades:", letter_grades)


# UNIT 3.3 - INTERMEDIATE EXERCISE 3
# Invert student_ids to look up by ID.

student_ids = {
    "Alice": 101,
    "Bob": 102
}

inverted = {
    student_id: name
    for name, student_id in student_ids.items()
}

print("Inverted:", inverted)


# UNIT 3.3 - ADVANCED EXERCISE 1
# Calculate total sales by region.

sales = [
    ("North", "Alice", 5000),
    ("South", "Bob", 4500),
    ("North", "Carol", 6000),
    ("South", "Alice", 3500)
]

region_totals = {}

for region, person, amount in sales:

    region_totals[region] = (
        region_totals.get(region, 0) + amount
    )

print("Sales by region:", region_totals)


# UNIT 3.3 - ADVANCED EXERCISE 2
# Calculate total sales by salesperson.

sales = [
    ("North", "Alice", 5000),
    ("South", "Bob", 4500),
    ("North", "Carol", 6000),
    ("South", "Alice", 3500)
]

person_totals = {}

for region, person, amount in sales:

    person_totals[person] = (
        person_totals.get(person, 0) + amount
    )

print("Sales by salesperson:", person_totals)


# UNIT 3.3 - ADVANCED EXERCISE 3
# Create nested dictionary: {region: {person: total}}.

sales = [
    ("North", "Alice", 5000),
    ("South", "Bob", 4500),
    ("North", "Carol", 6000),
    ("South", "Alice", 3500)
]

nested_sales = {}

for region, person, amount in sales:

    if region not in nested_sales:
        nested_sales[region] = {}

    nested_sales[region][person] = (
        nested_sales[region].get(person, 0) + amount
    )

print("Nested sales:", nested_sales)


# ============================================
# LECTURE 2 - SETS
# ============================================


# ============================================
# UNIT 1 - SET THEORY AND PYTHON SETS
# ============================================


# UNIT 1 - BEGINNER EXERCISE 1
# Create a set called vowels containing all vowels.

vowels = {
    "a",
    "e",
    "i",
    "o",
    "u"
}

print(vowels)


# UNIT 1 - BEGINNER EXERCISE 2
# Create a set from the list and find how many elements it has.

numbers = [
    1, 2, 2, 3, 3, 3, 4, 4, 4, 4
]

unique_numbers = set(numbers)

print(unique_numbers)
print("Number of elements:", len(unique_numbers))


# UNIT 1 - BEGINNER EXERCISE 3
# What's wrong with: empty = {}?

empty = {}

print(type(empty))

# {} creates an empty dictionary, NOT a set.

empty_set = set()

print(type(empty_set))


# UNIT 1 - INTERMEDIATE EXERCISE 1
# Given text = "mississippi", create a set of unique characters.

text = "mississippi"

unique_letters = set(text)

print(unique_letters)
print("Unique letters:", len(unique_letters))


# UNIT 1 - INTERMEDIATE EXERCISE 2
# Remove duplicates from the email list and convert back to a list.

emails = [
    "a@b.com",
    "c@d.com",
    "a@b.com",
    "e@f.com",
    "c@d.com"
]

unique_emails = list(set(emails))

print(unique_emails)


# UNIT 1 - INTERMEDIATE EXERCISE 3
# Why does this fail?
# s = {[1, 2], [3, 4]}

# It fails because lists are not hashable.
# Set elements must be hashable.


# UNIT 1 - ADVANCED EXERCISE 1
# Compare checking membership in a set vs. a list.

numbers_set = set(range(1000000))
numbers_list = list(range(1000000))

print(999999 in numbers_set)
print(999999 in numbers_list)

# Set membership is O(1) on average.
# List membership is O(n).


# UNIT 1 - ADVANCED EXERCISE 2
# Create a frozenset and use it as a dictionary key.

my_set = frozenset([
    "Python",
    "SQL"
])

dictionary = {
    my_set: "Programming Skills"
}

print(dictionary)


# UNIT 1 - ADVANCED EXERCISE 3
# Create a set of unique nodes from graph edges.

edges = [
    (1, 2),
    (2, 3),
    (1, 3),
    (3, 4)
]

nodes = set()

for a, b in edges:
    nodes.add(a)
    nodes.add(b)

print(nodes)


# ============================================
# UNIT 2 - SET OPERATIONS
# ============================================


# UNIT 2 - BEGINNER EXERCISE 1
# Find all unique numbers (union).

a = {
    1, 2, 3, 4
}

b = {
    3, 4, 5, 6
}

print("Union:", a | b)


# UNIT 2 - BEGINNER EXERCISE 2
# Find numbers in both sets (intersection).

a = {
    1, 2, 3, 4
}

b = {
    3, 4, 5, 6
}

print("Intersection:", a & b)


# UNIT 2 - BEGINNER EXERCISE 3
# Find numbers only in set a (difference).

a = {
    1, 2, 3, 4
}

b = {
    3, 4, 5, 6
}

print("Difference:", a - b)


# UNIT 2 - INTERMEDIATE EXERCISE 1
# Find employees who work ALL shifts.

morning_shift = {
    "Alice",
    "Bob",
    "Carol"
}

evening_shift = {
    "Carol",
    "Dave",
    "Eve"
}

weekend_shift = {
    "Alice",
    "Eve",
    "Frank"
}

all_shifts = (
    morning_shift
    & evening_shift
    & weekend_shift
)

print("All shifts:", all_shifts)


# UNIT 2 - INTERMEDIATE EXERCISE 2
# Find employees who work at least one shift.

morning_shift = {
    "Alice",
    "Bob",
    "Carol"
}

evening_shift = {
    "Carol",
    "Dave",
    "Eve"
}

weekend_shift = {
    "Alice",
    "Eve",
    "Frank"
}

any_shift = (
    morning_shift
    | evening_shift
    | weekend_shift
)

print("At least one shift:", any_shift)


# UNIT 2 - INTERMEDIATE EXERCISE 3
# Find employees who ONLY work morning.

morning_shift = {
    "Alice",
    "Bob",
    "Carol"
}

evening_shift = {
    "Carol",
    "Dave",
    "Eve"
}

weekend_shift = {
    "Alice",
    "Eve",
    "Frank"
}

morning_only = (
    morning_shift
    - evening_shift
    - weekend_shift
)

print("Morning only:", morning_only)


# UNIT 2 - INTERMEDIATE EXERCISE 4
# Find employees who work exactly one shift.

morning_shift = {
    "Alice",
    "Bob",
    "Carol"
}

evening_shift = {
    "Carol",
    "Dave",
    "Eve"
}

weekend_shift = {
    "Alice",
    "Eve",
    "Frank"
}

all_employees = (
    morning_shift
    | evening_shift
    | weekend_shift
)

exactly_one = set()

for employee in all_employees:

    count = 0

    if employee in morning_shift:
        count += 1

    if employee in evening_shift:
        count += 1

    if employee in weekend_shift:
        count += 1

    if count == 1:
        exactly_one.add(employee)

print("Exactly one shift:", exactly_one)


# UNIT 2 - ADVANCED EXERCISE 1
# Find students eligible to enroll.
# Must meet ALL three criteria.

prereqs_met = {
    "Alice",
    "Bob",
    "Carol",
    "Dave"
}

has_space = {
    "Bob",
    "Carol",
    "Eve",
    "Frank"
}

paid_tuition = {
    "Alice",
    "Carol",
    "Eve"
}

eligible = (
    prereqs_met
    & has_space
    & paid_tuition
)

print("Eligible:", eligible)


# UNIT 2 - ADVANCED EXERCISE 2
# Find students who met prerequisites but haven't paid tuition.

prereqs_met = {
    "Alice",
    "Bob",
    "Carol",
    "Dave"
}

paid_tuition = {
    "Alice",
    "Carol",
    "Eve"
}

not_paid = prereqs_met - paid_tuition

print("Need to pay tuition:", not_paid)


# UNIT 2 - ADVANCED EXERCISE 3
# Find students who are missing at least one requirement.

prereqs_met = {
    "Alice",
    "Bob",
    "Carol",
    "Dave"
}

has_space = {
    "Bob",
    "Carol",
    "Eve",
    "Frank"
}

paid_tuition = {
    "Alice",
    "Carol",
    "Eve"
}

all_students = (
    prereqs_met
    | has_space
    | paid_tuition
)

needs_something = set()

for student in all_students:

    if (
        student not in prereqs_met
        or student not in has_space
        or student not in paid_tuition
    ):
        needs_something.add(student)

print("Missing at least one requirement:", needs_something)


# ============================================
# UNIT 3 - SET METHODS, COMPREHENSIONS & PATTERNS
# ============================================


# UNIT 3 - BEGINNER EXERCISE 1
# Create {1, 2, 3}, add 4, and remove 1.

numbers = {
    1,
    2,
    3
}

numbers.add(4)
numbers.remove(1)

print(numbers)


# UNIT 3 - BEGINNER EXERCISE 2
# Create a set comprehension of even numbers from 0-20.

evens = {
    x
    for x in range(21)
    if x % 2 == 0
}

print(evens)


# UNIT 3 - BEGINNER EXERCISE 3
# Use discard() vs remove() to safely try removing
# an element that doesn't exist.

numbers = {
    1,
    2,
    3
}

numbers.discard(5)

print(numbers)

# discard() does not cause an error if the element
# does not exist.


# ============================================
# UNIT 3 - INTERMEDIATE EXERCISES
# ============================================


# UNIT 3 - INTERMEDIATE EXERCISE 1
# Remove duplicates while preserving order.

numbers = [
    4, 5, 2, 4, 8, 5, 2, 1, 9, 4
]

seen = set()
result = []

for number in numbers:

    if number not in seen:
        seen.add(number)
        result.append(number)

print(result)


# UNIT 3 - INTERMEDIATE EXERCISE 2
# Extract all unique words from the sentence.
# Convert to lowercase first.

sentence = "To be or not to be that is the question"

words = {
    word.lower()
    for word in sentence.split()
}

print(words)


# UNIT 3 - INTERMEDIATE EXERCISE 3
# Find the missing numbers.

expected = set(range(1, 11))

actual = {
    1, 2, 4, 5, 7, 8, 10
}

missing = expected - actual

print("Missing:", missing)


# ============================================
# UNIT 3 - ADVANCED EXERCISES
# ============================================


# UNIT 3 - ADVANCED EXERCISE 1
# Write a function that returns all elements
# that appear more than once.

def find_duplicates(lst):

    seen = set()
    duplicates = set()

    for item in lst:

        if item in seen:
            duplicates.add(item)

        else:
            seen.add(item)

    return duplicates


print(
    find_duplicates(
        [1, 2, 2, 3, 3, 3, 4]
    )
)


# UNIT 3 - ADVANCED EXERCISE 2
# Given three sets of employee skills, find:
# 1. Skills all three have
# 2. Skills only Alice has
# 3. All unique skills across the team

alice = {
    "Python",
    "SQL",
    "Excel",
    "Tableau"
}

bob = {
    "Python",
    "Java",
    "SQL",
    "AWS"
}

carol = {
    "Python",
    "R",
    "SQL",
    "Tableau"
}

all_three = alice & bob & carol

only_alice = alice - bob - carol

all_skills = alice | bob | carol

print("Skills everyone has:", all_three)
print("Skills only Alice has:", only_alice)
print("All unique skills:", all_skills)


# UNIT 3 - ADVANCED EXERCISE 3
# Create a function that takes two strings
# and returns the common characters.

def common_chars(string1, string2):

    return set(string1) & set(string2)


print(common_chars("hello", "world"))


# ============================================
# END OF WEEK 2 PRACTICE EXERCISES
# ============================================