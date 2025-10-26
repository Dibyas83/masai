# object or function or methods are instances of class


# init(constructor) initializes attributes of object.automatically called when an object is created
# self refers to current instance of the classes.used to access attributes and methods within the class.
#
class car:
    vehicle ="car" # class attribute
    no_wheels = 4
    total_car = 0

    def __init__(self,make ,model):
        self.make = make
        self.model = model
        car.total_car += 1

    @classmethod
    def set_wheels(cls,count):
        cls.no_wheels =count


    @classmethod
    def update_wheels(cls,neew_count):
        cls.no_wheels = neew_count

    @classmethod
    def from_string(clscls,car_str):
        make,model = car_str.split("_")
        return cls(make,model)

    def display_info(self):  # instance method s are defined within a class,that
        # operate on instances of class,can access and modify instanxe atributes
        print(f"car: {self.make} {self.model}")
        print(f"car: {self.make} {self.model}")


    def get_details(self):
        return f" {self.model} is a good product of {self.make}"

    @staticmethod  # are like regular functions but belong to a class.
    def add(a,b):
        return a+b


car.update_wheels(6)
car.set_wheels(5)
car3 = car("m","d")
car1 =car("Nissan","ultima")
car2 =car("Nissan","ultima")
print(f"car wheels: {car3.no_wheels}")
car1.display_info()
print(car1.no_wheels)
print(car1.vehicle)
print(car2.vehicle)
print(car.add(5,8))

# list.append  = list is class  append is method


#x12 = "12"
x12 = 22
if isinstance(x12,int) or type(x12) == int:
    print("int")
else:
    print("int no")



accounts =[]


def cre_acc(acc_no,acc_holder,balance):
    acc1 = {"acc_no":3424324,"acc_holder":"ghgfh","balance":balance}
    accounts.append(acc1)


def deposit(acc_no,amount):
    for acc1 in accounts:
        if acc1["acc_no"] == acc_no:
            acc1["balance"] += amount
            return f"deposited {amount}.new balance:{acc1["balance"]}"


def withdraw(acc_no,amount):
    for acc1 in accounts:
        if acc1["acc_no"] == acc_no:

            if acc1["balance"] >= amount:
                acc1["balance"] -= amount
                return f"deposited {amount}.new balance:{acc1["balance"]}"
            else:
                return "insufficient"
    return "not found"











