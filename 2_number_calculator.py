# This is an calculator but it can only calculate 2 numbers.

number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))

operation = input("Choose an operation: (+, -, *, /, )")

if operation == "+":
    print("Result:", number1 + number2)
elif operation == "-":
    print("Result:", number1 - number2)
elif operation == "*":
    print("Result:", number1 * number2)
elif operation == "/":
    print("Result:", number1 / number2)
else:
    print("Invalid Operation.")