import re

ans = 0

while True:
    input_str = input("Enter a valid number, operator and number (ex: 2 + 3) or (ans * 2): ")
    if input_str.lower() == "ans":
        input_str = str(ans)
    input_list = re.split('(\W)', input_str.strip())
    if len(input_list) == 3:
        try:
            num1 = float(input_list[0])
            operator = input_list[1]
            num2 = float(input_list[2])
            if operator == "+":
                result = num1 + num2
                print(result)
                ans = result
            elif operator == "-":
                result = num1 - num2
                print(result)
                ans = result
            elif operator == "*":
                result = num1 * num2
                print(result)
                ans = result
            elif operator == "/":
                if num2 == 0:
                    print("Invalid input")
                else:
                    result = num1 / num2
                    print(result)
                    ans = result
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")
    else:
        print("Invalid input")
