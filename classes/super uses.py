

# used in child class to call methods from parent class(superclass).
# allows you to extend the functionality of the inherited methods
class Shape:  # super class
    def __init__(self, col, is_filled):
        self.col = col
        self.is_filled = is_filled

    def describe(self):
        print(f'it is {self.col} and {'filled' if self.is_filled else 'not filled'}')

class Circle(Shape):
    def __init__(self, col, is_filled, radius):
        super().__init__(col, is_filled)
        self.radius = radius
        # self.col = col
        # self.is_filled = is_filled

class Square(Shape):
    def __init__(self, col, is_filled, width):
        super().__init__(col, is_filled)
        self.width = width
        # self.col = col
        # self.is_filled = is_filled

    def describe(self):
        print(f'Area of circle is {self.width * self.width}')
        super().describe() # also calling parent method

class Triangle(Shape):
    def __init__(self,col, is_filled, width, height):
        super().__init__(col, is_filled)
        self.width = width
        self.height = height
        # self.col = col
        # self.is_filled = is_filled

cir = Circle(col="red",is_filled= True, radius= 4)
square1 = Square(col="red",is_filled= True, width = 4)
print(cir.col)
cir.describe()
square1.describe()



