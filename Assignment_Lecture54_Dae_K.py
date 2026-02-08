def login():
    usernameInput = input("Username: ")
    passwordInput = input("Password: ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("----------iShop-----------")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelect = int(input("-->"))
    return userSelect

def vatCalculate(totalPrice):
    Vat = 7
    result = totalPrice + (totalPrice * Vat / 100)
    return result

def priceCalculator():
    price1 = int(input("Price1 (THB) :"))
    price2 = int(input("Price2 (THB) :"))
    return vatCalculate(price1 + price2)

if login() == True:
    showMenu()
    if menuSelect() == 1:
        price= int(input("Price (THB) :"))
        print("Total Price: ", vatCalculate(price))
    elif menuSelect() == 2:
        print("Total Price: ", priceCalculator())
else:
    print("Invalid input")
