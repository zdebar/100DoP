MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print("\n", resources, "profit:", profit)


def check_resources():
    for i in MENU[order]["ingredients"]:
        if resources[i] < MENU[order]["ingredients"][i]:
            print(f"Not enough {i}!")
            return False
    return True


def process_coins():
    print(f"\nYour price is ${MENU[order]["cost"]}.")
    paid = 0
    while True:
        quarters = int(input("\nInsert quartes ($0.25): "))
        dimes =    int(input("Insert dimes   ($0.10): "))
        nickles =  int(input("Insert nickles ($0.05): "))
        pennies =  int(input("Insert pennies ($0.01): "))
        paid = paid + quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
        if paid < MENU[order]["cost"]:
            print(f"\n${paid}. Please insert coins.")
        else:
            print(f"\nThank you. Returning ${round(paid-MENU[order]["cost"],2)}")
            global profit
            profit += MENU[order]["cost"] 
            return
   

def make_coffee():
    for i in MENU[order]["ingredients"]:
        resources[i] -= MENU[order]["ingredients"][i]
    print("Thank you for your order. Enjoy your coffee")
    print("☕")


while True:
    for i in MENU:
        print("\nitem:  ", i, "\nprice: $", MENU[i]["cost"])
    order = input("\nWhat would you like to order? (E,L,C or off): ").upper()
    match order:
        case "OFF":
            break
        case "REPORT":
            report()
        case "E" | "L" | "C":
            coffee_shortcuts = {"E": "espresso" , "L": "latte", "C": "cappuccino" }
            order =  coffee_shortcuts[order]
            if check_resources() == False:
                continue
            process_coins()
            make_coffee()
        case _:
            print("Please repeat your order.")