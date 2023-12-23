class Car:
    def __init__(self, brand, model) -> str:
        self.brand = brand
        self.model = model

        def move(self):
            print("Drive")

class Boat:
    def __init__(self, brand, model) -> str:
        self.brand = brand
        self.model = model

        def move(self):
            print ('sail')
            
class Plane:
    def __init__(self, brand, model) -> str:
        self.brand = brand
        self.model = model

        def move(self):
            print("fly")

car1 = Car("Toyota", "Fortuner")  
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

car1.move() 
boat1.move()
plane1.move()

#Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():