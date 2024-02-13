class Fruits:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    # method
    def onyesha(self):
        print(f"My favourite fruit is {self.name} and its cost is Ksh. {self.price} and it is {self.color} in color.")


# object
myobj = Fruits("Orange", 50, "orange")
myobj2 = Fruits("Apple", 40, "red")
# function
myobj.onyesha()
myobj2.onyesha()
