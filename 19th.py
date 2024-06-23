# using lambda functions
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
try:
    print("Division:", divide(num1, num2))
except ZeroDivisionError:
    print("Cannot divide by zero.")
