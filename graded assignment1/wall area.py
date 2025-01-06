class Wall:
    def __init__(self,height=0.0,width=0.0):
        self.width = width if width >= 0 else 0.0
        self.height = height if height >= 0 else 0.0

    def get_width(self) -> float:
        return self.width

    def get_height(self) -> float:
        return self.height

    def set_width(self,width:float):
        self.width = width if width >= 0 else 0.0

    def set_height(self, height: float):
        self.height = height if height >= 0 else 0.0


    def get_area(self) -> float:
        return self.width * self.height


wall1 = Wall(5,6)
print("Area =",wall1.get_area())

wall1.set_height(-1)
print("width =", wall1.get_width())
print("height =", wall1.get_height())
print("area =", wall1.get_area())



