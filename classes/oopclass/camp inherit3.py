
class Parent:
    def __init__(self):
        self.__num = 100

    def show(self):
        print('parent',self.__num)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var = 10

    def show(self):
        print('Child',self.__var)

d = Parent()
d.show()
s = Child()
s.show()









