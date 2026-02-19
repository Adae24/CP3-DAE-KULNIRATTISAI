class Customer:                 #ชื่อ class มักขึ้นด้วยตัวพิมพ์ใหญ่
    name = ""                   #ประกาศ attribute
    lastName = ""
    age = 0                     #ตั้งเป็นค่า default

    def addCart(self):
        print("Add to cart", self.name, self.lastName, "'s cart")

customer1 = Customer()      #class Customer เหมือน blueprint ที่เราจะนำมาใช้กับ customer คนแรกและไปเรื่อยๆ
customer1.name = "Dae"
customer1.lastName = "Kul"
customer1.addCart()
customer2 = Customer()
customer2.name = "Fai"
customer2.lastName = "Tap"
customer2.addCart()
customer3 = Customer()
customer3.name = "X"
customer3.lastName = "Y"
customer3.addCart()