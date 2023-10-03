
def add(*args):
    result = 0
    for num in args:
        result += num
    return result


def subtract(*args):
    if len(args) < 2:
        return "Subtraction requires at least two numbers"
    result = args[0]
    for i in range(1, len(args)):
        result -= args[i]
    return result


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


def divide(*args):
    if len(args) < 2:
        return "Division requires at least two numbers"
    result = args[0]
    for i in range(1, len(args)):
        if args[i] == 0:
            return "Division by zero is not allowed"
        result /= args[i]
    return result


while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")
    
    user_input = input(": ")
    
    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        numbers = input("Enter numbers separated by spaces: ").split()
        numbers = [float(num) for num in numbers]
        
        if user_input == "add":
            print("Result:", add(*numbers))
        elif user_input == "subtract":
            print("Result:", subtract(*numbers))
        elif user_input == "multiply":
            print("Result:", multiply(*numbers))
        elif user_input == "divide":
            print("Result:", divide(*numbers))
    else:
        print("Invalid input. Please enter a valid option.")
