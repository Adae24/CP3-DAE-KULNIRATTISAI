usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput == "Dae" and passwordInput == "0007":
    print("Welcome")
    print("Apple: 10 THB")
    print("Banana: 5 THB")
    toBuy = input("Buy: ")
    if toBuy == "Apple":
        Apple = 10
        AmountApple = int(input("Amount Apple(e.a ) :"))
        result1 = (Apple * AmountApple)
        print(result1)
    elif toBuy == "Banana":
        Banana = 5
        AmountBanana = int(input("Amount Banana(e.a ) :"))
        result2 = (Banana * AmountBanana)
        print(result2)
else:
    print("Please enter a valid input")