
class Car:
    # class variables in python  ,which is shared among all instances or objects of a class
    # it is defined outside of the constructor
    wheels = 4
    noof_cars = 0

    def __init__(self,model,year,color,for_sale):
        self.model= model # when we receive the name of the model we assign it to object self.model
        self.year = year
        self.color = color
        self.for_sale = for_sale #boolean
        Car.noof_cars += 1



    # methods are actions that an object can perform.a method of drive is formed
    def drive(self):
        print(f"car {self.model} is running")

    def stop(self):
        print(f"{self.model} has stopped")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")














