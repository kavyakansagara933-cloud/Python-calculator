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
    print("h  History")
    print("q  Quit")


def show_history(history):
    print("\n========== HISTORY ==========")

    if not history:
        print("No calculations yet.")
    else:
        for calculation in history:
            print(calculation)

    print("=============================")


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def calculate(num1, operator, num2):
    if operator == "+":
        return add(num1, num2)

    elif operator == "-":
        return subtract(num1, num2)

    elif operator == "*":
        return multiply(num1, num2)

    elif operator == "/":
        return divide(num1, num2)

    elif operator == "%":
        return modulus(num1, num2)


def main():
    print("Welcome to My Calculator!")

    history = []

    while True:

        show_operators()

        operator = input("\nChoose an operator: ").strip()

        # History
        if operator.lower() == "h":
            show_history(history)
            continue

        # Quit
        if operator.lower() == "q":
            print("\nThank you for using My Calculator!")
            break

        # Validate operator
        if operator not in ["+", "-", "*", "/", "%"]:
            print("\nInvalid operator! Please choose +, -, *, /, %, h, or q.")
            continue

        # Get numbers
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        # Calculate
        result = calculate(num1, operator, num2)

        # Display result
        print(f"\nResult: {result}")

        # Save calculation
        calculation = f"{num1} {operator} {num2} = {result}"
        history.append(calculation)

        # Continue?
        again = input("\nDo you want to calculate again? (y/n): ").strip().lower()

        if again != "y":
            print("\nThank you for using My Calculator!")
            break


if __name__ == "__main__":
    main()