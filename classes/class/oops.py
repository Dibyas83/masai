
# multiple inheritence (mro)

class Engine:
    def start11(self):
        print("eng started")

class Radio:
    def start22(self):
        print("radio on")

class Car(Engine,Radio):
    pass

c = Car()
print(c.start11())
print(c.start22())

#multilevel inheritance
class Engine1:
    def start1(self):
        print("eng started")

class Radio1(Engine1):
    def start2(self):
        print("radio on")

class Car1(Radio1):
    pass

c = Car1()
print(c.start1())
print(c.start2())

class Greeeet:
    def say_hello(self):
        print("hello")


g = Greeeet()
g.say_hello()


def new_hello():
    print("hi thre")

g.say_hello = new_hello
g.say_hello()






