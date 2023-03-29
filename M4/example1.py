ans = 0  # Internal variable for running total/value

# Addition function
def add(num):
    global ans
    try:
        ans = num + num
        return ans
    except TypeError:
        return "Invalid input. Please enter a number."

# Subtraction function
def sub(num):
    global ans
    try:
        ans = num - num
        return ans
    except TypeError:
        return "Invalid input. Please enter a number."

# Multiplication function
def mult(num):
    global ans
    try:
        ans = num * num
        return ans
    except TypeError:
        return "Invalid input. Please enter a number."

# Division function
def div(num):
    global ans
    try:
        ans = num / num
        if ans == float('inf') or ans == float('-inf'):
            raise ZeroDivisionError
        return ans
    except TypeError:
        return "Invalid input. Please enter a number."
    except ZeroDivisionError:
        return "Cannot divide by zero."


# Main logic
while True:
    user_input = input("Enter a math expression (or 'quit' to exit): ")
    if user_input.lower() == "quit":
        break
    elif user_input.lower() == "ans":
        user_input = str(ans) + input()[3:]
    try:
        operator_index = next(i for i in range(len(user_input)) if user_input[i] in ["+", "-", "*", "/"])
        num1 = float(user_input[:operator_index])
        num2 = float(user_input[operator_index+1:])
        operator = user_input[operator_index]
        if operator == "+":
            print(add(num2))
        elif operator == "-":
            print(sub(num2))
        elif operator == "*":
            print(mult(num2))
        elif operator == "/":
            print(div(num2))
    except (ValueError, TypeError):
        print("Invalid input. Please enter a valid math expression.")


# Test cases
assert add(2) == 2
assert add(3) == 5
assert add("a") == "Invalid input. Please enter a number."
assert sub(1) == 4
assert sub(2) == 2
assert sub("b") == "Invalid input. Please enter a number."
assert mult(3) == 6
assert mult(2) == 12
assert mult("c") == "Invalid input. Please enter a number."
assert div(2) == 6
assert div(3) == 2
assert div(0) == "Cannot divide by zero."
assert div("d") == "Invalid input. Please enter a number."
assert add(4) == 6
assert mult(5) == 30
assert sub(2) == 28
assert div(8) == 3.5
assert add("e") == "Invalid input. Please enter a number."
assert mult("f") == "Invalid input. Please enter a number."
assert sub("g") == "Invalid input. Please enter a number."
assert div("h") == "Invalid input. Please enter a number."
