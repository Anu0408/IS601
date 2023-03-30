import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state
# python -m pytest BurgerMachine -rA

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine

# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order):
    first_order.handle_bun("lettuce wrap")
    first_order.handle_patty("turkey")
    first_order.handle_patty("turkey")
    first_order.handle_patty("next")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("done")
    #machine.handle_pay(10000,"10000")
    return first_order

# sample test case, can delete if not using
def test_production_line(second_order):
    for j in second_order.buns:
        print(second_order.inprogress_burger)
        if j.name.lower() == second_order.inprogress_burger[0].name.lower():
            assert True
            return

    assert False

# add required test cases below

def test_out_of_stock_exception(machine):
    with pytest.raises(OutOfStockException):
        for i in range(BurgerMachine.MAX_PATTIES + 1):
            machine.handle_patty("beef")

def test_exceeded_remaining_choices_exception(machine):
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_bun("no bun")
        machine.handle_patty("beef")
        machine.handle_patty("turkey")
        machine.handle_patty("veggie")
        machine.handle_toppings("lettuce")
        machine.handle_toppings("tomato")
        machine.handle_toppings("pickles")
        machine.handle_toppings("cheese")

def test_invalid_choice_exception(machine):
    with pytest.raises(InvalidChoiceException):
        machine.handle_bun("rye")

def test_invalid_stage_exception(machine):
    with pytest.raises(InvalidStageException):
        machine.handle_toppings("lettuce")

def test_build_burger(machine):
    # Test with a complete burger with a lettuce wrap, turkey patty, lettuce, tomato, and pickles
    machine.handle_bun("lettuce wrap")
    machine.handle_patty("turkey")
    machine.handle_toppings("lettuce")
    machine.handle_toppings("tomato")
    machine.handle_toppings("pickles")
    machine.handle_toppings("done")
    assert len(machine.inprogress_burger) == 5
    assert machine.inprogress_burger[0].name == "Lettuce Wrap"
    assert machine.inprogress_burger[1].name == "Turkey"
    assert machine.inprogress_burger[2].name == "Lettuce"
    assert machine.inprogress_burger[3].name == "Tomato"
    assert machine.inprogress_burger[4].name == "Pickles"
    assert machine.calculate_cost() == 2.25

    # Test with a burger with no toppings and no bun
    machine.handle_bun("no bun")
    machine.handle_patty("beef")
    machine.handle_toppings("done")
    assert len(machine.inprogress_burger) == 2
    assert machine.inprogress_burger[0].name == "No Bun"
    assert machine.inprogress_burger[1].name == "Beef"
    assert machine.calculate_cost() == 1

    # Test with a burger with multiple patties and multiple toppings
    machine.handle_bun("white burger bun")
    machine.handle_patty("veggie")
    machine.handle_patty("veggie")
    machine.handle_toppings("lettuce")
    machine.handle_toppings("tomato")
    machine.handle_toppings("cheese")
    machine.handle_toppings("cheese")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("done")
    assert len(machine.inprogress_burger) == 7
    assert machine.inprogress_burger[0].name == "White Burger Bun"
    assert machine.inprogress_burger[1].name == "Veggie"
    assert machine.inprogress_burger[2].name == "Veggie"
    assert machine.inprogress_burger[3].name == "Lettuce"
    assert machine.inprogress_burger[4].name == "Tomato"
    assert machine.inprogress_burger[5].name == "Cheese"
    assert machine.inprogress_burger[6].name == "Ketchup"
    assert machine.calculate_cost() == 2.5


def test_calculate_cost(machine):
    machine.handle_bun("white burger bun")
    machine.handle_patty("beef")
    machine.handle_patty("veggie")
    machine.handle_toppings("lettuce")
    machine.handle_toppings("tomato")
    machine.handle_toppings("ketchup")
    assert machine.calculate_cost() == 3.5
