# UCID: 00525752
# Date: 03/01/2023

class MyCalc:
    def __init__(self):
        self.ans = 0.0

    def add(self, num):
        self.ans += num
        return self.ans

    def subtract(self, num):
        self.ans -= num
        return self.ans

    def multiply(self, num):
        self.ans *= num
        return self.ans

    def divide(self, num):
        if num == 0:
            print("Cannot divide by zero")
            return self.ans
        else:
            self.ans /= num
            return self.ans

calc = MyCalc()

while True:
    user_input = input("Enter a valid number, operator and number (ex: 2 + 3) or (ans * 2) : ")
    input_list = user_input.split()

    if len(input_list) == 3:
        num1, operator, num2 = input_list

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid input")
            continue

        if operator == "+":
            result = calc.add(num1 + num2)
        elif operator == "-":
            result = calc.subtract(num1 + num2)
        elif operator == "*":
            result = calc.multiply(num1 * num2)
        elif operator == "/":
            result = calc.divide(num1 / num2)
        else:
            print("Invalid operator")
            continue

    elif len(input_list) == 3 and input_list[0] == "ans":
        num1 = calc.ans
        num2 = input_list[2]

        try:
            num2 = float(num2)
        except ValueError:
            print("Invalid input")
            continue

        operator = input_list[1]

        if operator == "+":
            result = calc.add(num1 + num2)
        elif operator == "-":
            result = calc.subtract(num1 + num2)
        elif operator == "*":
            result = calc.multiply(num1 * num2)
        elif operator == "/":
            result = calc.divide(num1 / num2)
        else:
            print("Invalid operator")
            continue

    else:
        print("Invalid input")
        continue

    print(result)
