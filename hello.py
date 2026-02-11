# Python Code For Testing

print("Starting demo...")

# 1️⃣ Logical mistake
price = 100
tax_percent = 10
# Corrected tax calculation to add tax
Total = price + (price * tax_percent / 100)
print("Total price:", Total)

# 2️⃣ ZeroDivisionError
# Handling division by zero error
try:
    a = 10
    b = 0
    print("Division result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

# 3️⃣ KeyError
user = {"name": "Ajith"}
# Handling missing key
print("Username:", user.get("username", "No username found"))

# 4️⃣ TypeError
points = 5
# Converting '10' to integer for compatibility
print("Updated points:", points + int("10"))

# 5️⃣ NameError
message = "This is a message"
print("Message:", message)

# 6️⃣ AttributeError
# Changing number to a list to allow append
number = [10]
number.append(5)

# 7️⃣ ValueError
# Handling ValueError when converting
try:
    int_value = int("abc")
except ValueError:
    print("Invalid literal for int conversion")

print("Demo completed.")