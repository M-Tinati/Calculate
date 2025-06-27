def calculator():
    try:
        number1 = float(input("Enter your first number: "))
        number2 = float(input("Enter your second number: "))
        operation = input("Select operation (+, -, *, /): ").strip()

        if operation == '+':
            result = number1 + number2
        elif operation == '-':
            result = number1 - number2
        elif operation == '*':
            result = number1 * number2
        elif operation == '/':
            if number2 == 0:
                print("Error: Cannot divide by zero!")
                return
            result = number1 / number2
        else:
            print("Invalid operation. Please use +, -, *, or /.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")
calculator()
