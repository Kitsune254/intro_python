class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


myobject1 = Person("John", 23)
myobject2 = Person("Jane", 22)
myobject3 = Person("Paul", 21)
myobject4 = Person("Mary", 24)
myobject5 = Person("Ken", 22)
myobject1.show()
myobject2.show()
myobject3.show()
myobject4.show()
myobject5.show()
