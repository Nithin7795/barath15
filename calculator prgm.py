# Function Definitions

def add(x, y):
    """Returns the sum of x and y."""
    return x + y

def subtract(x, y):
    """Returns the difference between x and y."""
    return x - y

def multiply(x, y):
    """Returns the product of x and y."""
    return x * y

def divide(x, y):
    """Returns the quotient of x divided by y. Handles division by zero."""
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

# Main Calculator Function

def calculator():
    """Runs the calculator program."""
    # Display the menu of operations
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    # Get user choice
    choice = input("Enter choice (1/2/3/4): ")
    
    # Validate the choice
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please select a valid operation.")
        return
    
    # Get numbers from user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Perform the selected operation
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    
    # Display the result
    print(f"The result is: {result}")

# Run the calculator
calculator()
