def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operation choice.")
        return

    print(f"Result: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()
