
class Vehicle:
    def __init__(self,model,year):
        self.model = model
        self.year = year

    def move(self,distance):
        pass


class Car(Vehicle):
    def __init__(self,model,year,speed):
        super().__init__(model, year)
        self.speed = speed


    def move(self,distance):

        return distance/self.speed


class Bicycle(Vehicle):

    def __init__(self,model,year,speed):
        super().__init__(model, year)
        self.speed = speed

    def move(self, distance):
        return distance / self.speed


N = int(input())
vehicles = {}
for _ in range(N):
    data = input().split(" ")
    vehicle_typ = data[0]
    model = data[1]
    year = int(data[2])
    speed = float(data[3])

    if vehicle_typ == "Car":
        vehicles[model] = Car(model,year,speed)
    elif vehicle_typ == "Bicycle":
        vehicles[model] = Bicycle(model,year,speed)

M = int(input())
for _ in range(M):
    data = input().split(" ")
    model = data[0]
    distance = float(data[1])
    vehicle = vehicles.get(model)
    if vehicle:
        time = vehicle.move(distance)
        print(f"{model} {time:.2f}")
    else:
        print(f"{model} not_found")






































