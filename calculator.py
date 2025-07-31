print("Welcome to Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose an operation: ")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

operation = input("Enter your choice (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print("Result is:", result)
elif operation == "-":
    result = num1 - num2
    print("Result is:", result)
elif operation == "*":
    result = num1 * num2
    print("Result is:", result)
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print("Result is:", result)
else:
    print("Invalid operation.")
