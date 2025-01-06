class Floor:
    def __init__(self,width:float,length:float):
        # self.width = float(input(width))
        self.width = width if width > 0 else 0
        self.length = length if length > 0 else 0

    def get_area(self) -> float:
        return self.width * self.length


class Carpet:

    def __init__(self,cost:float):
        self.cost = cost if cost >=0 else 0

    def get_cost(self) -> float:
        return self.cost

class Calculator:
    def __init__(self,floor:Floor,carpet:Carpet):
        self.floor = floor
        self.carpet = carpet

    def get_total_cost(self) -> float:
        area = self.floor.get_area()
        cost_per_square_meter = self.carpet.get_cost()
        return  area * cost_per_square_meter


carpet = Carpet(5)
floor = Floor(5.4,4.5)
calculator = Calculator(floor,carpet)
print("Total:", calculator.get_total_cost())

carpet = Carpet(1.5)
floor = Floor(7.5,4.5)
calculator = Calculator(floor,carpet)
print("Total:", calculator.get_total_cost())

























