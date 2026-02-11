print("hello world")

b = 100
c = 20

define_d = 50  # Define 'd' before use
# 1️⃣ Logical bug (comment says subtract, but actually adding)
print(c - b)  # Corrected to subtraction as per comment

# 2️⃣ NameError (undefined variable)
print(define_d)  # Changed 'd' to 'define_d'

# 3️⃣ TypeError (int + str)
x = 50  # Changed from string to int
print(b + x)

# 4️⃣ ZeroDivisionError
z = 0
if z != 0:
    print(b / z)
else:
    print("Cannot divide by zero")  # Added error handling for division by zero

# 5️⃣ SyntaxError (missing colon)
if b > c:
    print("b is greater")  # Added colon

# 6️⃣ IndentationError
for i in range(3):
    print(i)  # Indented the print statement

# 7️⃣ AttributeError
num = [10]  # Changed to a list to allow append
num.append(5)

# 8️⃣ Unreachable code
raise Exception("Forced crash")
# print("You will never see this")  # Removed unreachable code

def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

data = [10, 20, "30", None, 50]

print("Average:", calculate_average(data))