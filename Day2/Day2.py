class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "woof"
    
class Cat(Animal):
    def speak(self):
        return "meow"
    
for animal in [Dog(), Cat()]:
    print(animal.speak())