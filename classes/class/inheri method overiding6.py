
from abc import ABC ,abstractmethod

class IDrivable(ABC): # methods called first without execution or late binding
    @abstractmethod
    def drive(self,distance):
        pass


class IFlyable(ABC):
    @abstractmethod
    def fly(self, distance):
        pass


class FlyingCar(IDrivable,IFlyable):
    def drive(self,distance):
        speed = 100.0 # constant value
        return distance/speed
    def fly(self,distance):
        speed = 300.0
        return distance/speed

car = FlyingCar()
N = int(input())
for _ in range(N):
    data = input().split(" ")
    cmd = data[0]
    dist = float(data[1])

    if cmd == "drive":
        print(f"{car.drive(dist):.2f}")
    elif cmd == "fly":
        print(f"{car.fly(dist):.2f}")
    else:
        print("not possible")








































