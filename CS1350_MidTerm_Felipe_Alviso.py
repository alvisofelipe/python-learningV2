# ============================================================
# PROBLEM 1: Library Catalog (Dictionaries)
# ============================================================

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, copies):
        if isbn in self.books:
            self.books[isbn]["copies"] += copies
        else:
            self.books[isbn] = {
                "title": title,
                "author": author,
                "copies": copies
            }

    def checkout(self, isbn):
        if isbn not in self.books:
            return False

        if self.books[isbn]["copies"] == 0:
            return False

        self.books[isbn]["copies"] -= 1
        return True

    def by_author(self, author):
        titles = []

        for isbn in self.books:
            if self.books[isbn]["author"].lower() == author.lower():
                titles.append(self.books[isbn]["title"])

        return sorted(titles)

    def inventory_value(self, prices):
        total = 0

        for isbn in self.books:
            if isbn in prices:
                total += self.books[isbn]["copies"] * prices[isbn]

        return total

    def low_stock(self, threshold):
        result = {}

        for isbn in self.books:
            if self.books[isbn]["copies"] < threshold:
                result[isbn] = self.books[isbn]["copies"]

        return result


# TEST CASES: PROBLEM 1

print("\n========== PROBLEM 1 TESTS ==========")

lib = Library()

lib.add_book("111", "Python Basics", "Jane Doe", 2)
lib.add_book("222", "Data Science", "John Roe", 1)
lib.add_book("333", "Advanced Python", "Jane Doe", 3)

# Add another copy to an existing ISBN
lib.add_book("111", "Python Basics", "Jane Doe", 1)

print(lib.checkout("222"))  # True
print(lib.checkout("222"))  # False: no copies left
print(lib.checkout("999"))  # False: unknown ISBN

print(lib.by_author("jane doe"))
# ['Advanced Python', 'Python Basics']

print(lib.inventory_value({
    "111": 20.0,
    "333": 30.0,
    "999": 5.0
}))
# 150.0

print(lib.low_stock(3))
# {'222': 0}


# ============================================================
# PROBLEM 2: Conference Sessions (Sets)
# ============================================================

class Session:
    def __init__(self, name):
        self.name = name
        self.attendees = set()

    def register(self, person):
        self.attendees.add(person)

    def unregister(self, person):
        self.attendees.discard(person)

    def attendee_count(self):
        return len(self.attendees)


def attended_all(sessions):
    if not sessions:
        return set()

    result = sessions[0].attendees.copy()

    for session in sessions[1:]:
        result = result & session.attendees

    return result


def attended_exactly_one(sessions):
    counts = {}

    for session in sessions:
        for person in session.attendees:
            if person not in counts:
                counts[person] = 0

            counts[person] += 1

    result = set()

    for person in counts:
        if counts[person] == 1:
            result.add(person)

    return result


def no_shows(expected, sessions):
    registered = set()

    for session in sessions:
        registered = registered | session.attendees

    return sorted(set(expected) - registered)


def summary(sessions):
    distinct = set()

    for session in sessions:
        print(f"{session.name}: {session.attendee_count()} attendees")
        distinct = distinct | session.attendees

    print(f"Distinct attendees: {len(distinct)}")


# TEST CASES: PROBLEM 2

print("\n========== PROBLEM 2 TESTS ==========")

keynote = Session("Keynote")
for p in ["Ana", "Ben", "Cruz", "Dee"]:
    keynote.register(p)

workshop = Session("Workshop")
for p in ["Ana", "Cruz", "Eli"]:
    workshop.register(p)

panel = Session("Panel")
for p in ["Ana", "Dee", "Eli", "Fay"]:
    panel.register(p)

workshop.unregister("Eli")
workshop.unregister("Zed")  # No error if person is absent

print(workshop.attendee_count())
# 2

sessions = [keynote, workshop, panel]

print(attended_all(sessions))
# {'Ana'}

print(attended_exactly_one(sessions))
# {'Ben', 'Fay'}

print(no_shows(["Ana", "Ben", "Fay", "Gus"], sessions))
# ['Gus']

summary(sessions)
# Keynote: 4 attendees
# Workshop: 2 attendees
# Panel: 4 attendees
# Distinct attendees: 6


# ============================================================
# PROBLEM 3: Order Log Processor (File Processing)
# ============================================================

import json


def process_orders(in_file, json_file, big_file, threshold):
    customers = {}
    big_count = 0

    with open(in_file, "r") as f:
        with open(big_file, "w") as big:
            for line in f:
                if line.strip() == "":
                    continue

                parts = line.strip().split(",")

                order_id = parts[0].strip()
                customer = parts[1].strip()
                amount_text = parts[2].strip()
                amount = float(amount_text)

                if customer not in customers:
                    customers[customer] = {
                        "orders": 0,
                        "total": 0.0,
                        "largest": 0.0
                    }

                customers[customer]["orders"] += 1
                customers[customer]["total"] += amount

                if amount > customers[customer]["largest"]:
                    customers[customer]["largest"] = amount

                if amount >= threshold:
                    big.write(
                        f"{order_id} {customer} {amount_text}\n"
                    )
                    big_count += 1

    with open(json_file, "w") as f:
        json.dump(customers, f, indent=2)

    return big_count


# TEST CASES: PROBLEM 3

print("\n========== PROBLEM 3 TESTS ==========")

with open("orders.txt", "w") as f:
    f.write("1001, ana, 25.50\n")
    f.write("1002, ben, 12.00\n")
    f.write("\n")
    f.write("1003, ana, 40.00\n")
    f.write("1004, cruz, 30.00\n")
    f.write("1005, ana, 4.50\n")

big = process_orders(
    "orders.txt",
    "customers.json",
    "big_orders.txt",
    30.0
)

print(big)
# 2

with open("customers.json", "r") as f:
    customer_summary = json.load(f)

print(customer_summary["ana"])
# {'orders': 3, 'total': 70.0, 'largest': 40.0}

print(customer_summary["ben"])
# {'orders': 1, 'total': 12.0, 'largest': 12.0}

with open("big_orders.txt", "r") as f:
    print(f.read(), end="")
# 1003 ana 40.00
# 1004 cruz 30.00


# ============================================================
# PROBLEM 4: Hotel Rooms (Inheritance & Polymorphism)
# ============================================================

from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, number, nights):
        Room.validate_nights(nights)
        self.number = number
        self.nights = nights

    @abstractmethod
    def cost(self):
        pass

    def receipt(self):
        return (
            f"Room {self.number} ({self.nights} nights): "
            f"${self.cost():.2f}"
        )

    @staticmethod
    def validate_nights(nights):
        if nights <= 0:
            raise ValueError("Nights must be positive")


class StandardRoom(Room):
    def __init__(self, number, nights, rate=100.00):
        super().__init__(number, nights)
        self.rate = rate

    def cost(self):
        return self.nights * self.rate


class DeluxeRoom(StandardRoom):
    def __init__(
        self, number, nights, rate=100.00, breakfast=15.00
    ):
        super().__init__(number, nights, rate)
        self.breakfast = breakfast

    def cost(self):
        return super().cost() + self.nights * self.breakfast


class Suite(Room):
    def __init__(
        self, number, nights, rate=250.00, discount_pct=0.10
    ):
        super().__init__(number, nights)
        self.rate = rate
        self.discount_pct = discount_pct

    def cost(self):
        total = self.nights * self.rate

        if self.nights >= 3:
            total *= (1 - self.discount_pct)

        return total


def invoice(rooms):
    total = 0

    for room in rooms:
        print(room.receipt())
        total += room.cost()

    print(f"Total: ${total:.2f}")
    return total


# TEST CASES: PROBLEM 4

print("\n========== PROBLEM 4 TESTS ==========")

rooms = [
    StandardRoom(101, 2),
    DeluxeRoom(205, 2, rate=120.00),
    Suite(901, 3)
]

total = invoice(rooms)
# Room 101 (2 nights): $200.00
# Room 205 (2 nights): $270.00
# Room 901 (3 nights): $675.00
# Total: $1145.00

print("Returned total:", total)
# Returned total: 1145.0

try:
    Room.validate_nights(0)
except ValueError as e:
    print("Caught:", e)
# Caught: Nights must be positive

# Test that a room cannot have zero nights
try:
    StandardRoom(102, 0)
except ValueError as e:
    print("Caught:", e)
# Caught: Nights must be positive
