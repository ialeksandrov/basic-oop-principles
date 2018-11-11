class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

comp = Computer()
comp.sell()

# change the Price
comp.__maxprice = 1000
comp.sell()

# using setter function
comp.setMaxPrice(1000)
comp.sell()
