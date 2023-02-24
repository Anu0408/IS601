class MyCalc:
    
    def __init__(self) -> None:
        self.ans = None
        
        
        
        def run(self):
            while True:
                if self.ans != None and "ans" in response:
                response = input("Type an equation\n")
                
                
                    response = response.replace(" ","")
                #    ops = ["*", "x"]
                    if "*" in response or "X" in response:
                        response = response.replace("X","*")  
                        nums = response.split("*")
                        
                        if nums[0].isdigit() and nums[1].isdigit():
                            
                        self.ans = float(nums[0]) * float(nums[1])
                        printf(f"{nums[0]}*{nums[1]}= {self.ans}")
                        #mult
                        pass
                    elif "/" in response:
                            #div
                            pass
                    elif "+" in response:
                        pass
                    elif "-" in response:
                        pass
            