# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
        
#     def moves(self):
#         print(f"{self.make} {self.model} moves")
#         print(f"movies along the road")
        
#     def stops(self):
#         print(f"{self.make} {self.model} stops")
#         print(f"stops along the road")
        
        


# my_vehicle = Vehicle('Toyota', 'Corolla')
# favorite_vehicle = Vehicle('Civic', 'Honda')
# print(my_vehicle.make)
# print(my_vehicle.model)
# my_vehicle.moves()
# my_vehicle.stops()
# favorite_vehicle.stops()
# favorite_vehicle.moves()



class Dog:
    species = "Canis familiaris"
  
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"


dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
print(dog1.name)  
print(dog2.age)   
print(dog1.bark())  
print(dog2.species)  