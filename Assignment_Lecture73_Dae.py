systemMenu = {"rice":30, "soup":40, "beef":60}
menuList = []

def showBill():
    print("--------My Food--------")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        totalPrice += menuList[number][1]
        print("Total Price:", totalPrice)

while True:
    menuName = input("Enter your Menu :")
    if (menuName.lower()== "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
print(menuList)


showBill()