def solve(N):

    symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
    for i, symbol in enumerate(symbols):
        print(f"{symbol} -{N +i*2}")


N= int(input())
solve(N)

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):

    def speak(self):
        print("Woof!")
class Cat(Animal):
    def speak(self):
        print("Meow!")
# Example Usage


animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()


from  abc import ABC,abstractmethod

class Pet(ABC):
    @abstractmethod
    def obey(self):
        pass

class Dog(Pet):
    def obey(self):
        print("attack")

class Cat(Pet):
    def obey(self):
        print("cudle")

prts = [Dog(),Cat()]
for i in prts:
    i.obey()

print("-------------------66")

from  abc import ABC,abstractmethod

class Pet(ABC):
    @abstractmethod
    def obey(self):
        pass

class Dog(Pet):
    def obey(self):
        print("attack")

class Cat(Pet):
    def obey(self):
        print("cudle")


prts = [Dog(),Cat()]
prts[1].obey()
prts[0].obey()












