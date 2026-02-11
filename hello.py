# Python Code For Testing
print("Starting demo...")

# 1️⃣ Logical mistake
price = 100
tax_percent = 10
total = price + (price * tax_percent / 100)  # Correctly add tax
print("Total price:", total)

# 2️⃣ ZeroDivisionError
a = 10
b = 0  # Ensure 'b' is defined before division
# Adding check to prevent division by zero
if b != 0:
    print("Division result:", a / b)
else:
    print("Cannot divide by zero")

# 3️⃣ KeyError
user = {"name": "Ajith"}
print("Username:", user.get("username", "No username found"))

# 4️⃣ TypeError
points = 5
print("Updated points:", points + int("10"))  # Convert string to int

# 5️⃣ NameError
message = "Hello, World!"  # Define message before using it
print("Message:", message)

# 6️⃣ AttributeError
number = [10]  # Change to a list to use append
number.append(5)

# 7️⃣ ValueError
try:
    int_value = int("abc")
except ValueError:
    int_value = None
    print("Invalid integer conversion")

print("Demo completed.")