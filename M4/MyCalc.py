#UCID: ac298  #date: 02/26/23
class MyCalc:
    def __init__(self):
        self.ans = 0
    
    
    def add(self, x):
        self.ans += x
    #UCID: ac298  #date: 02/26/23
    
    def subtract(self, x):
        self.ans -= x
    #UCID: ac298  #date: 02/26/23
  
    def multiply(self, x):
        self.ans *= x
    #UCID: ac298  #date: 02/26/23
  
    def divide(self, x):
        if x == 0:
            print("Error: Cannot divide by zero.")
        else:
            self.ans /= x
    #UCID: ac298  #date: 02/26/23
    
    
if __name__ == '__main__':
    calculator = MyCalc()
    while True:
        user_input = input("Enter a math expression or 'exit' to quit: ")
        if user_input.lower() == "exit":
            break
        
        try:
            if "ans" in user_input:
                user_input = user_input.replace("ans", str(calculator.ans))
            result = eval(user_input)
            print("Result: ", result)
            calculator.ans = result
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except:
            print("Error: Invalid input.")
            #UCID: ac298  #date: 02/26/23
            
def test_add():
    calculator = MyCalc()
    calculator.add(2)
    calculator.add(3)
    assert calculator.ans == 5
#UCID: ac298  #date: 02/26/23

def test_ans_add():
    calculator = MyCalc()
    calculator.add(2)
    calculator.add(3)
    calculator.add(4)
    user_input = "ans + 5"
    result = eval(user_input.replace("ans", str(calculator.ans)))
    assert result == 9
    assert calculator.ans == 9
#UCID: ac298  #date: 02/26/23

def test_subtract():
    calculator = MyCalc()
    calculator.subtract(2)
    calculator.subtract(3)
    assert calculator.ans == -5
#UCID: ac298  #date: 02/26/23

def test_ans_subtract():
    calculator = MyCalc()
    calculator.add(2)
    calculator.subtract(3)
    calculator.subtract(4)
    user_input = "ans - 5"
    result = eval(user_input.replace("ans", str(calculator.ans)))
    assert result == -10
    assert calculator.ans == -10
#UCID: ac298  #date: 02/26/23

def test_multiply():
    calculator = MyCalc()
    calculator.add(2)
    calculator.multiply(3)
    assert calculator.ans == 6
#UCID: ac298  #date: 02/26/23

def test_ans_multiply():
    calculator = MyCalc()
    calculator.add(2)
    calculator.multiply(3)
    user_input = "ans * 4"
    result = eval(user_input.replace("ans", str(calculator.ans)))
    assert result == 24
    assert calculator.ans == 24
#UCID: ac298  #date: 02/26/23

def test_divide():
    calculator = MyCalc()
    calculator.add(8)
    calculator.divide(4)
    assert calculator.ans == 2
#UCID: ac298  #date: 02/26/23

def test_ans_divide():
    calculator = MyCalc()
    calculator.add(8)
#UCID: ac298  #date: 02/26/23    


