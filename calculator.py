def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def modulus(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a % b


print("Welcome to My Calculator")

while True:

    # Get first number
    try:
        num1 = float(input("\nEnter first number: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # Get operator
    operator = input("Enter operator (+, -, *, /, %): ")

    # Get second number
    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # Perform calculation
    if operator == "+":
        result = add(num1, num2)

    elif operator == "-":
        result = subtract(num1, num2)

    elif operator == "*":
        result = multiply(num1, num2)

    elif operator == "/":
        result = divide(num1, num2)

    elif operator == "%":
        result = modulus(num1, num2)

    else:
        result = "Invalid operator"

    print("Result:", result)

    # Ask whether to continue
    again = input("\nDo you want to calculate again? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using My Calculator!")
        break
