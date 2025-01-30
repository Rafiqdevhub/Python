
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

cat = Cat("Whiskers")
dog = Dog("Buddy")

print(cat.speak())  
print(dog.speak()) 
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Chirp!"

def animal_sound(animal):
    print(animal.speak())


cat = Cat("Whiskers")
dog = Dog("Buddy")
bird = Bird("Tweety")

animal_sound(cat)  
animal_sound(dog) 
animal_sound(bird)  