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


def show_operators():
    print("\nAvailable operators:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("%  Modulus")
    print("q  Quit")


print("Welcome to My Calculator!")

while True:

    # Get first number
    try:
        num1 = float(input("\nEnter first number: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # Show available operators
    show_operators()

    # Get operator
    operator = input("\nChoose an operator: ").strip()

    # Quit
    if operator.lower() == "q":
        print("\nThank you for using My Calculator!")
        break

    # Validate operator
    if operator not in ["+", "-", "*", "/", "%"]:
        print("\nInvalid operator! Please choose +, -, *, /, or %.")
        continue

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

    # Display result
    print(f"\nResult: {result}")

    # Ask whether to continue
    again = input("\nDo you want to calculate again? (y/n): ").strip().lower()

    if again != "y":
        print("\nThank you for using My Calculator!")
        break
