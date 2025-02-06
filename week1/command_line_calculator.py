import math

def calculate():
    # Prompt for the operator and the numbers
    operation = input('''\nSelect operation:
+ for Addition
- for Subtraction
* for Multiplication
/ for Division
s for Square Root
p for Power
Your choice: ''')

    # For operations that need two numbers
    if operation in ['+', '-', '*', '/', 'p','P']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            return

    # For square root, only one number is needed
    elif operation.lower() == 's':
        try:
            num1 = float(input("Enter the number: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            return
    else:
        print("Invalid operator selected.")
        return

    # Perform calculation based on operator
    if operation == '+':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
    elif operation.lower() == 's':
        if num1 < 0:
            print("Error: Cannot calculate square root of a negative number.")
        else:
            result = math.sqrt(num1)
            print(f"\nResult: Square root of {num1} = {result}")
    elif operation.lower() == 'p':
        result = num1 ** num2
        print(f"\nResult: {num1} raised to the power of {num2} = {result}")
    else:
        print("Invalid operation.")

def main():
    while True:
        calculate()
        # Ask if the user wants to perform another calculation
        choice = input("\nDo you want to calculate again? (Y/N): ")
        if choice.lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
