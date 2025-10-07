class Floor:
    def __init__(self,width:float,leng:float):
        self.width = width
        self.leng = leng

    def get_area(self):
        return self.width * self.leng

class Carpet:
    def __init__(self,cost:float):
        self.cost = cost if cost >= 0 else 0

    def get_cost(self):
        return self.cost

class Calculator:
    def __init__(self,floor:Floor,carpet:Carpet):
        self.floor = floor
        self.carpet = carpet

    def get_total(self) -> float:
        area =self.floor.get_area()
        cost_per_sqr_metr = self.carpet.get_cost()
        return  area * cost_per_sqr_metr

print("---------------------------------2")

class Wall:
    def __init__(self,width=0.0,height=0.0):
        self.width = width if width>= 0 else 0.0
        self.height = height if height >= 0 else 0.0

    def get_width(self) -> float:
        return self.width


    def get_height(self) -> float:
        return self.height

    def set_width(self,width: float):
        self.width = width if width >= 0 else 0.0

    def set_height(self,height: float):
        self.height = height if height >= 0 else 0.0


    def get_area(self) -> float:
        return self.width * self.height

wall1 =Wall(5,4)
print(wall1.get_area())
wall1.set_height(2)
print(wall1.get_area())
print(wall1.get_height())
print(wall1.get_width())
print("---------------------------------3")


def cus_join(separator: str,items:list) -> str:
    if not  items:
        return ""
    result = items[0]
    for item in items[1:]:
        result += separator + item

    return result
print(cus_join(" ",["hel","o"]))
print(cus_join("-",["10","4","24"]))

print("----------------------------4")

def cus_contains(items:list,target) -> bool:
    for item in items:
        if item == target:
            return  True
    return False
print(cus_contains([1,2,3,4,5],4))

print("--------------------5")

def cus_index(items:list,target) -> int:
    index= 0
    for item in items:
        if item == target:
            return index
        index += 1

    raise ValueError(f"{target} is not in the list")
try:
    print(cus_index([1,2,3,4,5],4))
except ValueError as e:
    print(e)

print("------------------------6")

def cus_count(items,target) -> int:
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count

print("------------------------7")

def cus_rev(items):
    rev_items = []
    for i in range(len(items)-1,-1,-1):
        rev_items.append(items[i])

    if isinstance(items,str):
        return ''.join(rev_items)
    elif isinstance(items,list):
        return rev_items
    else:
        raise TypeError("list or string input")

print("-----------------------------8")

def cus_find(text:str,sub_string:str) -> int:
    text_len = len(text)
    sub_string_len = len(sub_string)
    for i in range(text_len-sub_string_len + 1):
        if text[i:i+ sub_string_len] == sub_string:
            return i
    return -1















