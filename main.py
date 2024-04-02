from Menu import MENU
import Menu

p_resources = Menu.resources
turn_off = False


# TODO find the type of material
def type_menu(item, f_resources):
    for key in MENU[item]["ingredients"]:
        f_resources[key] -= MENU[item]["ingredients"][key]
    return f_resources


# TODO Calculator money input and change to Dollars
def dollars(money_quarters, money_dimes, money_nickles, money_pennies):
    return money_quarters*0.25 + money_dimes*0.1 + money_nickles*0.05 + money_pennies*0.01


# TODO report how many the machine have material(resources)
def report(item, money):
    """ print how many the machine have material(resources)"""
    print(f'Water = {item["water"]}mg')
    print(f'Milk = {item["milk"]}mg')
    print(f'Coffee = {item["coffee"]}g')
    print(f'money = ${money}')


# TODO check in return (True or False) and check out return value don't have enough
def check_in(item, f_resources):
    """ return (True or False) if value don't have enough"""
    for key in MENU[item]["ingredients"]:
        if MENU[item]["ingredients"][key] > f_resources[key]:
            return True
        else:
            return False


def check_out(item, f_resources):
    """return value don't have enough"""
    b = ""
    for key in MENU[item]["ingredients"]:

        if MENU[item]["ingredients"][key] > f_resources[key]:
            b += key
    return b


money_mach = 0
money_user = 0
# TODO loop if the machine turn on and break if the machine turn off
while not turn_off:
    material = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if material == "report":
        report(p_resources, money_mach)
    elif material == "espresso" or material == "latte" or material == "cappuccino":
        if check_in(material, p_resources):
            print(f"We don't have {check_out(material, p_resources)} enough")
        else:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?:    "))
            nickles = int(input("how many nickles?:  "))
            pennies = int(input("how many pennies?:  "))
            money_user += dollars(quarters, dimes, nickles, pennies)

            if money_user < MENU[material]["cost"]:
                print(f"Here is ${money_user:.2f} in change")
                print("Sorry that's not enough money. Money refunded.")
            else:
                type_menu(material, p_resources)
                money_user -= MENU[material]["cost"]
                print(f"Here is ${money_user:.2f} in change")
                print(f"Here is your {material} ☕️. Enjoy!")
                money_mach += MENU[material]["cost"]
    elif material == "full":
        p_resources = {
            "water": 300,    
            "milk": 200,  
            "coffee": 100  
        }
        report(p_resources, money_mach)
    elif material == "get money":
        money_mach = 0
        report(p_resources, money_mach)
    elif material == "turn off":
        turn_off = True
