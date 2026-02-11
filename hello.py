print("hello world")

b = 100
c = 20

# 1️⃣ Logical bug (comment says subtract, but actually adding)
print(c + b)

# 2️⃣ NameError (undefined variable)
print(d)

# 3️⃣ TypeError (int + str)
x = "50"
print(b + x)

# 4️⃣ ZeroDivisionError
z = 0
print(b / z)

# 5️⃣ SyntaxError (missing colon)
if b > c
    print("b is greater")

# 6️⃣ IndentationError
for i in range(3):
print(i)

# 7️⃣ AttributeError
num = 10
num.append(5)

# 8️⃣ Unreachable code
raise Exception("Forced crash")
print("You will never see this")
