import pytest

from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

def reset_machine(machine):
    machine.reset()
    for bun in machine.buns:
        bun.quantity = 10
    for patty in machine.patties:
        patty.quantity = 10
    for topping in machine.toppings:
        topping.quantity = 10

@pytest.fixture
def Test_Case1_first_order(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("mayo")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), "2.25")
    return machine
#UCID: ac298  Date: 03/27/23

@pytest.fixture
def Test_Case1_second_order(Test_Case1_first_order):
    Test_Case1_first_order.handle_bun("white burger bun")
    Test_Case1_first_order.handle_patty("turkey")
    Test_Case1_first_order.handle_patty("veggie")
    Test_Case1_first_order.handle_patty("next")
    Test_Case1_first_order.handle_toppings("cheese")
    Test_Case1_first_order.handle_toppings("mayo")
    Test_Case1_first_order.handle_toppings("done")
    return Test_Case1_first_order
#UCID: ac298  Date: 03/27/23


def test_1(Test_Case1_second_order):
    print(f"Order 2 (Inprogress Burger): {Test_Case1_second_order.inprogress_burger}")
    for j in Test_Case1_second_order.buns:
        if j.name.lower() == Test_Case1_second_order.inprogress_burger[0].name.lower():
            assert True
            return
    assert False
#UCID: ac298  Date: 03/27/23


@pytest.fixture
def Test_Case2_first_order(machine):
    reset_machine(machine)
    i = 0
    while i < 5:
        machine.handle_bun("no bun")
        machine.handle_patty("turkey")
        machine.handle_patty("turkey")
        machine.handle_patty("next")
        machine.handle_toppings("done")
        machine.handle_pay(machine.calculate_cost(), "2")
        i += 1
    return machine
#UCID: ac298  Date: 03/27/23


def test_2(Test_Case2_first_order):
    try:
        Test_Case2_first_order.handle_bun("no bun")
        Test_Case2_first_order.handle_patty("turkey")
        assert False, "Error not raised on adding 11th veggie"
    except OutOfStockException:
        assert True  
#UCID: ac298  Date: 03/27/23


@pytest.fixture
def Test_Case3_first_order(machine):
    reset_machine(machine)
    i = 0
    while i < 5:
        machine.handle_bun("no bun")
        machine.handle_patty("veggie")
        machine.handle_patty("next")
        machine.handle_toppings("cheese")
        machine.handle_toppings("cheese")
        machine.handle_toppings("done")
        machine.handle_pay(machine.calculate_cost(), "1.5")
        i += 1
    return machine
#UCID: ac298  Date: 03/27/23


def test_3(Test_Case3_first_order):
    try:
        Test_Case3_first_order.handle_bun("no bun")
        Test_Case3_first_order.handle_patty("veggie")
        Test_Case3_first_order.handle_patty("next")
        Test_Case3_first_order.handle_toppings("cheese")
        assert False, "Error not raised on adding 11th bbq"
    except OutOfStockException:
        assert True  
#UCID: ac298  Date: 03/27/23


@pytest.fixture
def Test_Case4_first_order(machine):
    reset_machine(machine)
    global Test_Case4_result_1
    Test_Case4_result_1 = False
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("turkey")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    plist = []
    for patty in machine.patties:
        if patty in machine.inprogress_burger:
            plist.append(str(patty).lower())
    if ("veggie" in plist) and ("turkey" in plist) and ("turkey" in plist):
        Test_Case4_result_1 = True
    machine.handle_pay(machine.calculate_cost(), "3")
    return machine
#UCID: ac298  Date: 03/27/23


@pytest.fixture
def Test_Case4_second_order(Test_Case4_first_order):
    global Test_Case4_result_2
    Test_Case4_result_2 = False
    Test_Case4_first_order.handle_bun("no bun")
    Test_Case4_first_order.handle_patty("veggie")
    Test_Case4_first_order.handle_patty("turkey")
    Test_Case4_first_order.handle_patty("turkey")
    Test_Case4_first_order.handle_patty("next")
    Test_Case4_first_order.handle_toppings("done")
    plist = []
    for patty in Test_Case4_first_order.patties:
        if patty in Test_Case4_first_order.inprogress_burger:
            plist.append(str(patty).lower())
    if ("veggie" in plist) and ("turkey" in plist) and ("turkey" in plist):
        Test_Case4_result_2 = True
    Test_Case4_first_order.handle_pay(Test_Case4_first_order.calculate_cost(), "3")
    return Test_Case4_first_order
#UCID: ac298  Date: 03/27/23


def test_4(Test_Case4_second_order):
    if Test_Case4_result_1 and Test_Case4_result_2:
        assert True
        return
    assert False
#UCID: ac298  Date: 03/27/23


@pytest.fixture
def Test_Case5_first_order(machine):
    reset_machine(machine)
    global Test_Case5_result_1
    Test_Case5_result_1 = False
    machine.handle_bun("wheat burger bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    machine.handle_toppings("bbq")
    machine.handle_toppings("mayo")
    machine.handle_toppings("done")
    tlist = []
    for topping in machine.toppings:
        if topping in machine.inprogress_burger:
            tlist.append(str(topping).lower())
    if ("cheese" in tlist) and ("bbq" in tlist) and ("mayo" in tlist):
        Test_Case5_result_1 = True
    machine.handle_pay(machine.calculate_cost(), "3.0")
    return machine
#UCID: ac298  Date: 03/27/23


@pytest.fixture
def Test_Case5_second_order(Test_Case5_first_order):
    global Test_Case5_result_2
    Test_Case5_result_2 = False
    Test_Case5_first_order.handle_bun("lettuce wrap")
    Test_Case5_first_order.handle_patty("turkey")
    Test_Case5_first_order.handle_patty("next")
    Test_Case5_first_order.handle_toppings("mayo")
    Test_Case5_first_order.handle_toppings("mustard")
    Test_Case5_first_order.handle_toppings("cheese")
    Test_Case5_first_order.handle_toppings("done")
    print(f"Toppings Used (Order 2): {Test_Case5_first_order.inprogress_burger[2:]}")
    tlist = []
    for topping in Test_Case5_first_order.toppings:
        if topping in Test_Case5_first_order.inprogress_burger:
            tlist.append(str(topping).lower())
    if ("cheese" in tlist) and ("mayo" in tlist) and ("mustard" in tlist):
        Test_Case5_result_2 = True
    Test_Case5_first_order.handle_pay(Test_Case5_first_order.calculate_cost(), "3.25")
    return Test_Case5_first_order
#UCID: ac298  Date: 03/27/23


def test_5(Test_Case5_second_order):
    if Test_Case5_result_1 and Test_Case5_result_2:
        assert True
        return
    assert False

@pytest.fixture
def Test_Case6_first_order(machine):
    reset_machine(machine)
    global Test_Case6_result_1
    Test_Case6_result_1 = False
    try:
        machine.handle_bun("wheat burger bun")
        machine.handle_patty("veggie")
        machine.handle_patty("next")
        machine.handle_toppings("cheese")
        machine.handle_toppings("done")
        machine.handle_pay(machine.calculate_cost(), "2.5")
        if len(machine.inprogress_burger) == 0:
            Test_Case6_result_1 = True
        return machine
    except:
        print("Invalid Payment Exception")
#UCID: ac298  Date: 03/27/23

@pytest.fixture
def Test_Case6_second_order(Test_Case6_first_order):
    global Test_Case6_result_2
    Test_Case6_result_2 = False
    try:
        Test_Case6_first_order.handle_bun("lettuce wrap")
        Test_Case6_first_order.handle_patty("veggie")
        Test_Case6_first_order.handle_patty("turkey")
        Test_Case6_first_order.handle_patty("beef")
        Test_Case6_first_order.handle_patty("next")
        Test_Case6_first_order.handle_toppings("cheese")
        Test_Case6_first_order.handle_toppings("bbq")
        Test_Case6_first_order.handle_toppings("mustard")
        Test_Case6_first_order.handle_toppings("done")
        Test_Case6_first_order.handle_pay(Test_Case6_first_order.calculate_cost(),"5.25")
        if len(Test_Case6_first_order.inprogress_burger) == 0:
            Test_Case6_result_2 = True
        return Test_Case6_first_order
    except:
        print("Invalid Payment Exception")
#UCID: ac298  Date: 03/27/23


@pytest.fixture
def Test_Case6_third_order(Test_Case6_second_order):
    global Test_Case6_result_3
    Test_Case6_result_3 = False
    try:
        Test_Case6_second_order.handle_bun("white burger bun")
        Test_Case6_second_order.handle_patty("veggie")
        Test_Case6_second_order.handle_patty("next")
        Test_Case6_second_order.handle_toppings("cheese")
        Test_Case6_second_order.handle_toppings("cheese")
        Test_Case6_second_order.handle_toppings("done")
        Test_Case6_second_order.handle_pay(Test_Case6_third_order.calculate_cost(), "2.75")
        if len(Test_Case6_second_order.inprogress_burger) == 0:
            Test_Case6_result_3 = True
        return Test_Case6_second_order
    except:
        print("Invalid Payment Exception")
#UCID: ac298  Date: 03/27/23


def test_6(Test_Case6_third_order):
    print("\nAmount paid for Order 1, Order 2, and Order 3 is exactly same where as amount paid for Order 4 is not exact")
    if Test_Case6_result_1==True and Test_Case6_result_2==True and Test_Case6_result_3==False:
        assert True
    else:
        assert False
#UCID: ac298  Date: 03/27/23


@pytest.fixture
def Test_Case7_first_order(machine):
    reset_machine(machine)
    machine.handle_bun("no bun")
    machine.handle_patty("Turkey")
    machine.handle_patty("Turkey")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), "2")
    return machine
#UCID: ac298  Date: 03/27/23


@pytest.fixture
def Test_Case7_second_order(Test_Case7_first_order):
    Test_Case7_first_order.handle_bun("wheat burger bun")
    Test_Case7_first_order.handle_patty("veggie")
    Test_Case7_first_order.handle_patty("turkey")
    Test_Case7_first_order.handle_patty("beef")
    Test_Case7_first_order.handle_patty("next")
    Test_Case7_first_order.handle_toppings("cheese")
    Test_Case7_first_order.handle_toppings("mayo")
    Test_Case7_first_order.handle_toppings("bbq")
    Test_Case7_first_order.handle_toppings("done")
    Test_Case7_first_order.handle_pay(Test_Case7_first_order.calculate_cost(), "5.0")
    return Test_Case7_first_order
#UCID: ac298  Date: 03/27/23


@pytest.fixture
def Test_Case7_third_order(Test_Case7_second_order):
    Test_Case7_second_order.handle_bun("lettuce wrap")
    Test_Case7_second_order.handle_patty("veggie")
    Test_Case7_second_order.handle_patty("turkey")
    Test_Case7_second_order.handle_patty("next")
    Test_Case7_second_order.handle_toppings("cheese")
    Test_Case7_second_order.handle_toppings("mustard")
    Test_Case7_second_order.handle_toppings("bbq")
    Test_Case7_second_order.handle_toppings("done")
    Test_Case7_second_order.handle_pay(Test_Case7_second_order.calculate_cost(), "4.25")
    return Test_Case7_second_order
#UCID: ac298  Date: 03/27/23


def test_7(Test_Case7_third_order):
    print(f"Total Sales: ${Test_Case7_third_order.total_sales}")
    if float(Test_Case7_third_order.total_sales) == float("11.25"):
        assert True
    else:
        assert False
#UCID: ac298  Date: 03/27/23


@pytest.fixture
def Test_Case8_first_order(machine):
    reset_machine(machine)
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), "1.5")
    return machine
#UCID: ac298  Date: 03/27/23


@pytest.fixture
def Test_Case8_second_order(Test_Case8_first_order):
    Test_Case8_first_order.handle_bun("lettuce wrap")
    Test_Case8_first_order.handle_patty("veggie")
    Test_Case8_first_order.handle_patty("turkey")
    Test_Case8_first_order.handle_patty("next")
    Test_Case8_first_order.handle_toppings("ketchup")
    Test_Case8_first_order.handle_toppings("cheese")
    Test_Case8_first_order.handle_toppings("bbq")
    Test_Case8_first_order.handle_toppings("done")
    Test_Case8_first_order.handle_pay(Test_Case8_first_order.calculate_cost(), "4.25")
    return Test_Case8_first_order
#UCID: ac298  Date: 03/27/23


def test_8(Test_Case8_second_order):
    print(f"Total Burgers Sold: {Test_Case8_second_order.total_burgers}")
    if Test_Case8_second_order.total_burgers == 2:
        assert True
    else:
        assert False
#UCID: ac298  Date: 03/27/23