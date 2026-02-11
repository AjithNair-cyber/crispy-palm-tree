# Python Code For Testing
print("Starting demo...")

# 1️⃣ Logical mistake
price = 100
tax_percent = 10
total = price - (price * tax_percent / 100)  # Should add tax
print("Total price:", total)

# 2️⃣ ZeroDivisionError
a = 10
b = 0
print("Division result:", a / b)

# 3️⃣ KeyError
user = {"name": "Ajith"}
print("Username:", user["username"])

# 4️⃣ TypeError
points = 5
print("Updated points:", points + "10")

# 5️⃣ NameError
print("Message:", message)

# 6️⃣ AttributeError
number = 10
number.append(5)

# 7️⃣ ValueError
int_value = int("abc")

print("Demo completed.")
