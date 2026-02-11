# Simple Demo File – Line-Based Errors

print("Starting demo...")

# 1️⃣ Logical mistake
price = 100
 tax_percent = 10
total = price + (price * tax_percent / 100)  # Corrected to add tax
print("Total price:", total)

# 2️⃣ ZeroDivisionError
try:
    a = 10
    b = 0
    print("Division result:", a / b)
except ZeroDivisionError:
    print("Error: Division by zero")

# 3️⃣ KeyError
user = {"name": "Ajith"}
print("Username:", user.get("username", "Not found"))  # Using get to avoid KeyError

# 4️⃣ TypeError
points = 5
print("Updated points:", points + 10)  # Converted '10' to an integer

# 5️⃣ NameError
message = "Hello, World!"  # Defined message variable
print("Message:", message)

# 6️⃣ AttributeError
number = [10]  # Changed to a list to use append
number.append(5)

# 7️⃣ ValueError
try:
    int_value = int("abc")
except ValueError:
    int_value = None
    print("Error: Could not convert to int")

print("Demo completed.")