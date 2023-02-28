class MyCalc:
    
    def __init__(self) -> None:
        self.ans = None
        
    def add(self, num1, num2):
        try:
            result = num1 + num2
            self.ans = result
            return result
        except TypeError:
            return "Invalid input. Please enter a number."
        
    def sub(self, num1, num2):
        try:
            result = num1 - num2
            self.ans = result
            return result
        except TypeError:
            return "Invalid input. Please enter a number."
        
def mult(self, num1, num2):
    try:
        if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
            raise TypeError
        result = num1 * num2
        self.ans = result
        return result
    except TypeError:
        return "Invalid input. Please enter a number."

        
    def div(self, num1, num2):
        try:
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
            self.ans = result
            return result
        except TypeError:
            return "Invalid input. Please enter a number."
        except ZeroDivisionError:
            return "Cannot divide by zero."
        
    def run(self):
        while True:
            response = input("Type an equation (or 'quit' to exit):\n")
            if response.lower() == "quit":
                break
            elif "ans" in response:
                response = str(self.ans) + response[3:]
            response = response.replace(" ","")
            if "*" in response or "x" in response or "X" in response:
                response = response.replace("x","*")
                response = response.replace("X","*")
                nums = response.split("*")
                if nums[0].isdigit() and nums[1].isdigit():
                    result = self.mult(float(nums[0]), float(nums[1]))
                    print(f"{nums[0]} * {nums[1]} = {result}")
            elif "/" in response:
                nums = response.split("/")
                if nums[0].isdigit() and nums[1].isdigit():
                    result = self.div(float(nums[0]), float(nums[1]))
                    print(f"{nums[0]} / {nums[1]} = {result}")
                else:
                    print("Invalid input. Please enter a valid math expression.")
            elif "+" in response:
                nums = response.split("+")
                if nums[0].isdigit() and nums[1].isdigit():
                    result = self.add(float(nums[0]), float(nums[1]))
                    print(f"{nums[0]} + {nums[1]} = {result}")
                else:
                    print("Invalid input. Please enter a valid math expression.")
            elif "-" in response:
                nums = response.split("-")
                if nums[0].isdigit() and nums[1].isdigit():
                    result = self.sub(float(nums[0]), float(nums[1]))
                    print(f"{nums[0]} - {nums[1]} = {result}")
                else:
                    print("Invalid input. Please enter a valid math expression.")
            else:
                print("Invalid input. Please enter a valid math expression.")
        

# Test cases
calc = MyCalc()
assert calc.add(2, 3) == 5
assert calc.add(2, "a") == "Invalid input. Please enter a number."
assert calc.sub(5, 3) == 2
assert calc.sub(5, "b") == "Invalid input. Please enter a number."
assert calc.mult(2, 3) == 6
assert calc.mult(2, "c") == "Invalid input. Please enter a number."
assert calc.div(6, 3) == 2
assert calc.div(6, 0) == "Cannot divide by zero."
assert calc.div(6, "d") == "Invalid input. Please enter a number."
