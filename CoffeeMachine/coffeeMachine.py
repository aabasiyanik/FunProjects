#requirements
COFFEES = {
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
# print(COFFEES['espresso']['ingredients']['water'])
def isItEnough(ingredients):
    for key, value in ingredients.items():
        if value is not None and resources[key] >= value:
            resources[key] -= value
        elif value is not None and resources[key] < value:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def coffeeMachine():
    penny = 0.01
    nickel = 0.05
    dime = 0.1
    quarter = 0.25

    isTrue = True
    while isTrue:
        isValid = True
        while isValid:
            global profit
            user_req = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if user_req not in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
                print("Invalid Output")
            else:
                isValid = False
        if user_req == 'off':
            exit()
        elif user_req == 'report':
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
        else:
            usr_water = COFFEES[user_req]['ingredients']['water']
            if 'milk' in COFFEES[user_req]['ingredients']:
                usr_milk = COFFEES[user_req]['ingredients']['milk']
            else:
                usr_milk = None
            usr_coffee = COFFEES[user_req]['ingredients']['coffee']
            
            isTrue = False
    ingredients = {'water': usr_water, 'milk': usr_milk, 'coffee': usr_coffee}
    isEnough = isItEnough(ingredients=ingredients)
    if isEnough:
        print("Please insert coints.")
        usr_quarter = int(input("How many quarters?: "))
        usr_dime = int(input("How many dimes?: "))
        usr_nickel = int(input("How many nickels?: "))
        usr_penny = int(input("How many pennies?: "))

        insreted_money = usr_penny * penny + usr_nickel * nickel + usr_dime * dime + usr_quarter * quarter

        if insreted_money < COFFEES[user_req]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            coffeeMachine()
        elif insreted_money >= COFFEES[user_req]['cost']:
            profit += COFFEES[user_req]['cost']
            if insreted_money > COFFEES[user_req]['cost']:
                usr_change = round(insreted_money - COFFEES[user_req]['cost'], 2)
                print(f"Here is ${usr_change}.")
            print(f"Here is your {user_req} ☕️. Enjoy!")
            coffeeMachine()
    elif not isEnough:
        coffeeMachine()

coffeeMachine()