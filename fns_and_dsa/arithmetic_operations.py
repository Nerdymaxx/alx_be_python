def perform_operation(num1, num2, operation=["add", "subtract","multiply","divide"]):
    if operation == "add":
        result =num1 + num2
        print(result)
    elif operation == "subtract":
        result = num2 - num1
        print(result)
    elif operation == "multiply":
        result = num1 * num2
        print(result)
    elif operation == "divide":
        result = num2 / num1
        print(result)
    else:
        print("not an operation...")
perform_operation(8, 5, "subtract")