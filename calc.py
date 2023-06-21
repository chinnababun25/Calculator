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
        # Display menu options
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Prompt for user's choice
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            # Exit the program if choice is 5
            print("Thank you for using the Calculator App!")
            break

        # Prompt for input numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            # Call add() function and print the result
            result = add(num1, num2)
            print("Result: ", result)
        elif choice == '2':
            # Call subtract() function and print the result
            result = subtract(num1, num2)
            print("Result: ", result)
        elif choice == '3':
            # Call multiply() function and print the result
            result = multiply(num1, num2)
            print("Result: ", result)
        elif choice == '4':
            # Call divide() function and print the result
            result = divide(num1, num2)
            print("Result: ", result)
        else:
            # Handle invalid input
            print("Invalid input! Please try again.")

# Call the calculator function to start the program
calculator()
