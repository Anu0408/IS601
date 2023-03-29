import sys

class STAGE:
    Bun, Patty, Toppings, Pay = range(4)

class InvalidStageException(Exception):
    pass

class OutOfStockException(Exception):
    pass

class NeedsCleaningException(Exception):
    pass

class InvalidChoiceException(Exception):
    pass

class ExceededRemainingChoicesException(Exception):
    pass

class InvalidPaymentException(Exception):
    pass

class BurgerComponent:
    def __init__(self, name, cost, remaining):
        self.name = name
        self.cost = cost
        self.remaining = remaining

    def in_stock(self):
        return self.remaining > 0

    def __str__(self):
        return self.name

class BurgerMachine:
    def __init__(self):
        # Define the burger components
        self.buns = [
            BurgerComponent("Plain Bun", 0.5, 10),
            BurgerComponent("Seeded Bun", 0.75, 5)
        ]
        self.patties = [
            BurgerComponent("Beef Patty", 1.5, 10),
            BurgerComponent("Veggie Patty", 1.75, 3),
            BurgerComponent("Chicken Patty", 2, 7)
        ]
        self.toppings = [
            BurgerComponent("Lettuce", 0.25, 10),
            BurgerComponent("Tomato", 0.4, 7),
            BurgerComponent("Cheese", 0.75, 5),
            BurgerComponent("Bacon", 1, 3)
        ]
        self.sauces = [
            BurgerComponent("Mayo", 0.25, 10),
            BurgerComponent("Ketchup", 0.25, 10),
            BurgerComponent("BBQ Sauce", 0.5, 5),
            BurgerComponent("Hot Sauce", 0.4, 3)
        ]

        # Define the default burger components
        self.default_burger = [
            self.buns[0],
            self.patties[0],
            self.toppings[0],
            self.toppings[1],
            self.toppings[2],
            self.sauces[0]
        ]

        # Define the variables to keep track of the state of the burger machine
        self.currently_selecting = STAGE.Bun
        self.inprogress_burger = []
        self.total_burgers = 0
        self.total_sales = 0

    def handle_bun(self, bun_name):
        bun = next((b for b in self.buns if b.name.lower() == bun_name.lower()), None)
        if bun is None:
            raise InvalidChoiceException("Invalid bun choice")
        if not bun.in_stock():
            raise OutOfStockException("Buns are out of stock")
        self.inprogress_burger.append(bun)
        self.currently_selecting = STAGE.Patty

    def handle_patty(self, patty_name):
        if patty_name.lower() == "next":
            if not self.inprogress_burger:
                raise ExceededRemainingChoicesException("Cannot proceed without a bun")
            self.currently_selecting = STAGE.Toppings
            return
        patty = next((p for p in self.patties if p.name.lower() == patty_name.lower()), None)
        if patty is None:
            raise InvalidChoiceException("Invalid patty choice")
        if not patty.in_stock():
            raise OutOfStockException("Patties are out of stock")
        self.inprogress_burger.append(patty)

        def handle_toppings(self, topping_name):
            if topping_name.lower() == "done":
             if not self.inprogress_burger:
                raise ExceededRemainingChoicesException("Cannot proceed without a bun")
            self.currently_selecting = STAGE.Pay
            return
            topping = next((t for t in self.toppings if t.name.lower() == topping_name.lower()), None)
            if topping is None:
                 raise InvalidChoiceException("Invalid topping choice")
            if not topping.in_stock():
                raise OutOfStockException("Topping is out of stock")
            self.inprogress_burger.append(topping)

    def handle_payment(self, payment_amount):
        if not payment_amount.isdigit():
            raise InvalidPaymentException("Invalid payment amount")
        payment_amount = int(payment_amount)
        if payment_amount < self.total_price():
            raise InvalidPaymentException("Payment amount is less than total price")
        self.total_sales += self.total_price()
        self.total_burgers += 1
        self.reset_burger()

    def total_price(self):
        return sum(c.cost for c in self.inprogress_burger)

    def reset_burger(self):
        self.currently_selecting = STAGE.Bun
        self.inprogress_burger = []

    def order_burger(self, bun_name):
        try:
            if self.currently_selecting != STAGE.Bun:
                raise InvalidStageException("Cannot order a burger at this stage")
            self.handle_bun(bun_name)
        except Exception as e:
            print(e)

    def add_patty(self, patty_name):
        try:
            if self.currently_selecting != STAGE.Patty:
                raise InvalidStageException("Cannot add patty at this stage")
            self.handle_patty(patty_name)
        except Exception as e:
            print(e)

    def add_topping(self, topping_name):
        try:
            if self.currently_selecting != STAGE.Toppings:
                raise InvalidStageException("Cannot add topping at this stage")
            self.handle_toppings(topping_name)
        except Exception as e:
            print(e)

    def make_payment(self, payment_amount):
        try:
            if self.currently_selecting != STAGE.Pay:
                raise InvalidStageException("Cannot make payment at this stage")
            self.handle_payment(payment_amount)
        except Exception as e:
            print(e)

