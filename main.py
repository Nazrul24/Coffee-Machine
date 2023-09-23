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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
is_on = True


def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made and False when order can not be made"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received , price):
    """Returns true when payment is accepted, or False when money is insufficient"""
    if money_received >= price:
        change = round(money_received - price, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += price
        return True
    else:
        print("Sorry that's not enough money.")
        return False

def recalculate_resources(order_ingredients):
    """Recalculates resources after a succeful order"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            print(f"The cost of your drink is ${drink['cost']}")
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                recalculate_resources(drink["ingredients"])






# TODO 1. Print report of all coffee machine resources
# TODO 2. Check resources sufficient to make drink order
