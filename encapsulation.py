class Customer:
    
    def __init__(self):
        self.__maxprice =2000

    def price(self):
        print("Price:",self.__maxprice)

    def modify(self, price):
        self.__maxprice = price

obj = Customer()
obj.__maxprice = 1000
obj.price()
obj.modify(1000)
obj.price()