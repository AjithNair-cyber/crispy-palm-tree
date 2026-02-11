# Python Code For Testing

print("Starting demo...")

# 1️⃣ Logical mistake
price = 100

tax_percent = 10
# Validate tax_percent to be non-negative
if tax_percent < 0:
    raise ValueError("tax_percent must be non-negative")
# Corrected calculation to include tax
 total = price + (price * tax_percent / 100)
print("Total price:", total)

# 2️⃣ ZeroDivisionError
a = 10
b = 0
try:
    print("Division result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

# 3️⃣ KeyError
user = {"name": "Ajith"}
print("Username:", user.get("username", "Not found"))

# 4️⃣ TypeError
points = 5
# Ensure points is an integer before adding
if not isinstance(points, int):
    raise TypeError("points must be an integer")
# Converted string '10' to integer 10
print("Updated points:", points + 10)

# 5️⃣ NameError
message = "Hello, World!"
print("Message:", message)

# 6️⃣ AttributeError
number = [10]  # Changed to a list to use append
number.append(5)

# 7️⃣ ValueError
try:
    int_value = int("abc")
except ValueError:
    print("Cannot convert to integer")

print("Demo completed.")