class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        self.programming_language = programming_language
        super().__init__(name, salary)  # This calls the parent class __init__

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


y = Developer("ty",56,"pyyhon")
y.display_info()



class Shape:
    def Area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def Area(self):
        return self.height * self.width


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        pi =3.14
        return pi * self.radius**2


N = int(input())
shapes = []
for _ in range(N):
    Inp = input().split()
    shape_type = Inp[0]
    if shape_type == "Rectangle":
        width = float(Inp[1])
        height = float(Inp[2])
        shapes.append(Rectangle(width, height)) # storing data
    elif shape_type == "Circle":
        radius = float(Inp[1])
        shapes.append(Circle(radius))
print(shapes)


for shape in shapes:
    print([shapes])
    print(shape)

    area = shape.Area()
    print(f"{Shape.__class__.__name__}: {area:.2f}")




































