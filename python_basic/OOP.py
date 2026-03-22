print("let's go")
import csv
"""
class is a blueprint 
"""
class softWareEngineer:
    #class attribute 
    definition  = "software engineer class attribute" 
    print(definition)
    #instance attribute
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
    
    #instsnace method
    def code(self):
        print(f"{self.name} is a student")


#instance of the clas
se1 = softWareEngineer("abdu", 18, "unilorin")
print(se1.name)
print(softWareEngineer.definition)
se1.code()

"""
static method decorator 
"""

#freecode camp course 
item1 = "phone"
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

class Item:
    #class attribute 
    pay_rate = 0.8 #the pay rate after 20% discount 
    all =[]

    #instance attribute
    def __init__(self, name, price: float, quantity ):
        # run validaion to the recieved arguments
        assert price >= 0, f" price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero"
        
        #assigned to self object
        self.name = name 
        self.price = price
        self.quantity = quantity

        #actions to excute 
        Item.all.append(self)

    def calc_total_price(self):
        return (self.price * self.quantity)
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}, {self.price}, {self.quantity}')"
    
    @classmethod
    def instantiate_from_csv(cls):
        with open("python_basic\item.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            print(item)

Item.instantiate_from_csv()

# print(Item.all)


# print(Item.__dict__) #sjow all attribute assigned to Item class
# print(item1.__dict__) #sjow all attribute assigned to item1 


# defining a class
#methods identify the actions the object can perform with it data 
#class is a blueprint 
#instances are objects built from class 

class Dog:
    specie = "chiwawa"
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        
    
    def __str__(self): #dunder method that shows a description of our instance 
        return f"{self.name} is {self.age} years old "
    
    def speak(self, sound ):
        return f"{self.name} barks: {sound}"

class local(Dog):
    def speak(self, sound = "Arf woof"):
        return super().speak(sound)
    
class foreign(Dog):
    def speak(self,sound):
        return  f'{self.name} says: {super().speak(sound)}'
class Mixed(Dog):
    pass

# dog1 = Dog("raf", 2)
# dog2 = Dog("keb", 4)
# dog3 = Dog("lac", 3)

#dogs of specific breed
wendy = local("wendy", 7)
kennedy = foreign("kennedy", 9)
lutos = Mixed("lotus", 12)

print(wendy.speak())

# print(wendy.specie)
# print(kennedy.name)
# print(kennedy.speak( "arf woof"))
# print(dog1.name)
# print(dog1)


# print(dog1.description())
# print(dog1.speak("woof woof"))
# print(dog1.breed) #class attribute 
# print(dog2.name)

#inheriting from another class in python
#inheriting is when a class takes the attribute and method of another class 
#newly formed classes are called child class while the classes you derive child class
#are called parent class 

#EXERCISE (CLASS, INHERITANCE, SUPER(), INSTANCES, METHODS)

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    

# Create a GoldenRetriever class that inherits from the Dog class. 
# Give the sound argument of GoldenRetriever.speak() a default value of "Bark"

class Goldenretriever(Dog):
    def speak( self, sound= "Bark"):
        return super().speak(sound)

Goldenretriever = Goldenretriever("goldenretriever", 18)
print(Goldenretriever.speak())