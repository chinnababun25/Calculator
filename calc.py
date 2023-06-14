def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 / num2

def calculator():
    print("Welcome to the Calculator App!")

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Thank you for using the Calculator App!")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
            print("Result: ", result)
        elif choice == '2':
            result = subtract(num1, num2)
            print("Result: ", result)
        elif choice == '3':
            result = multiply(num1, num2)
            print("Result: ", result)
        elif choice == '4':
            result = divide(num1, num2)
            print("Result: ", result)
        else:
            print("Invalid input! Please try again.")

calculator()
