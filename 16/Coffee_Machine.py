from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    order = input("\nWhat would you like to order? (E,L,C or off): ").upper()
    match order:
        case "OFF":
            is_on = False
        case "REPORT":
            coffee_maker.report()
            money_machine.report()
        case "E" | "L" | "C":
            coffee_shortcuts = {"E": "espresso" , "L": "latte", "C": "cappuccino" }
            order =  coffee_shortcuts[order]
            drink = menu.find_drink(order)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        case _:
            print("Please repeat your order.")

