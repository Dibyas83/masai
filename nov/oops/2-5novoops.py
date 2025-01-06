matrix = [[1,2,3],[4,5,6],[7,9,8]]
print(matrix[1][0],matrix[2][1])























def add_value(a,b=5):
    return a+b
print(add_value(3),add_value(3,7))


u = add_value(4,8)
print(u)


def multi(y,x=2):
    return x*y


print(multi(6))



andy=lambda d,f:(d+f)*f
print(andy(5,6))
# objects are instances of classes
# constructors are default initial function that is executed while creating objects;

# in object
# attribute -variable or data
# method - functions or behaviour in object and clases

print("=================================================================2")
class Car:
    vehicle = "car"  # class attribute  it is shared attribute among  instances
    def __init__(self,make,model,year=2020): #  init is constructor or default function of this class
        self.make = make           # when we call car init will be executed
        self.model = model         # class is storing what the  user gives data here
        self.year = year
        self.my_list =[]
        # this constructor initializes the attributes of an object
        # self refers to the current instance of the object

    @classmethod
    def update_veh(cls,new_veh):
        cls.vehicle = new_veh



    @classmethod
    def from_string(cls,car_str):
        make,model = car_str.split("-")
        return cls(make,model)

    @staticmethod # are regular function but belong to a class without using self,cls
    def add(a,b=10):
        return a+b

    @staticmethod  # are regular function but belong to a class without using self,cls
    def multi(a, b=2):
        return a * b

    def display_info(self): # no init is called ,this is a class method not instance method
        print(f"Car: {self.make} {self.model} {self.year}")
        # the init data was called into this method by self

    def my_split(self):
        local_str = ""
        for letter in self.model:
            if letter == " ":
                self.my_list.append(local_str)
                local_str = ""
            else:
                local_str += letter
        self.my_list.append((local_str))


s1 = Car("ui","hello worldly people")
s1.my_split()
print(s1.my_list)

my_car5 = Car.from_string("toyotal-kanta") # called forthis instance
my_car = Car("toyota","corolla",year=1920) # object creation ,data is going to init function when car is called.
my_car1 = Car("toy","rata",year=5610)
my_car2 = Car("tata","olla")
my_car3 = Car("yota","cor",2010)
Car.update_veh("ghj")
print(Car.add(5,Car.multi(2)))
my_car2.display_info()

print(my_car2.model)
print(my_car1.make)
my_car2.model = "hyun"
my_car2.size = 10
my_car1.size = 15
my_car1.vehicle = "bus"
print(my_car2)
print(my_car2.model)
print(my_car2.vehicle)
print(my_car1.vehicle)
print(my_car5.model)
print(my_car5.vehicle)

print("=============================")
print(my_car3.vehicle)
k = -31.235478
print(abs(k))
print(round(k,2))
print(pow(k,3))
print("hello world".split())
print(" ".join("hello world".split()))
d = "hello-world-peoplg"
parts = d.split("-",1)
print(d.replace("hello","done"))
result ="-".join(parts[::-1])
print(result)


class person:
    place ="earth"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod  # class methods are used to change class variables
    def update_place(cls,new_place):
        cls.place = new_place


    def my_func(self):
        print("hello my name is " + self.name + " age is " + str(self.age))

    def __str__(self):
        return f"a person named{self.name} is {self.age} years old."


p1 = person("ajay",34)
p2 = person("aram",56)
p1.my_func()
print(p2)

# static variables are types of global variables

print(p1.place)
person.place = "moon"
print(p2.place)
print("===================78")
person.update_place("olla")
# p2.update_place("po")   p1 and p2 linked through person/  update place is updated
print(p1.place)
print(p2.place)
p1.place = "io"
# p1.update_place = "io"
print(p1.place)
print(p2.place)





