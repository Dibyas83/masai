# in list
import math


def cus_contains(items:list,target) -> bool:
    for item in items:
        if item == target:
            return  True
    return False
print(cus_contains([4,6,8,9],6))
print(cus_contains(["ab","cd","ef","gh"],"gh"))


# index function
def cus_index(items:list,target1):
    index = 0
    for item in items:
        if item == target1:
            return index
        index += 1 # index of next no inc by 1
    raise ValueError(f"{target} is not in the list ")

print(cus_index([2,4,7,9,66],4))


def custom_count(items2,target3) -> int:
    count = 0
    for item in items2:
        if item == target3:
            count += 1

    return  count

print(custom_count([4,5,67,8,9],67))

def cus_rev(items):
    rev_item = []
    for i in range(len(items) -1,-1,-1):
        rev_item.append(items[i])

    if isinstance(items,str):
        return " ".join(rev_item)
    elif isinstance(items,list):
        return rev_item
    else:
        raise TypeError(" Input must be string")

print(cus_rev([5,6,7,8,9]))
print(cus_rev("string"))


def cus_find(text:str,target1:str):
    text_len =len(text)
    target1_len =len(target1)
    for i in range(text_len - target1_len +1):
        if text[i:i +target1_len] == target1:
            return i

    return -1

print(cus_find("helo","o"))


class Point:
    def __init__(self,x=0,y =0):
        self.x = x
        self.y = y

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def set_x(self,x:int):
        self.x = x

    def set_y(self,y:int):
        self.y = y

# to origin
    def distance(self ,x: int, y: int) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

# to another x,y
    def distance1(self, x: int, y: int) -> float:
        return math.sqrt((x-self.x) ** 2 + (y- self.y) ** 2)

# to another point object
    def distance2(self,other_point:"Point") -> float:
        return math.sqrt((other_point.get_x()-self.x) ** 2 + (other_point.get_y() - self.y) ** 2)


first = Point(6,5)
second = Point(3,1)
# distance to origin
print("distance(0,0) = ", first.distance(0, 0))
# distance to anather Point object
print("distance(second) = ",first.distance2(second))
print("distance(second) = ",first.distance2(second))
# distance to coordinates(2,2)
print("distance(2,2) = ",first.distance1(2,2))
# testing with origin point
point = Point()
print("distance() = ",point.distance(3,3))


# slicing
def cus_slice(lst,start,end):
    # empty list initialize
    result = []
    if end >= len(lst):
        end = len(lst) - 1
    for i in range(start,end):
        result.append(lst[i])

    return result


print(cus_slice([3,4,5,6,7],2,4))
print(cus_slice([3,4,5,6,7,8,9],2,9))


# to find the last occurrence of a item
# start from the last element of list
def cus_rindex(lst, target):
    for i in range(len(lst)-1,-1,-1):
        if lst[i] == target:
            return  i
    return  -1

print(cus_rindex([3,4,5,6,7,4,6],4))

# slicing
def cus_slice(stsstrin,start,end):
    # empty list initialize
    result = ""
    if end >= len(stsstrin):
        end = len(stsstrin) - 1
    for i in range(start,end):
        result += stsstrin[i]

    return result


print(cus_slice("hello , world",2,4))
print(cus_slice("andpeoplesrun",2,9))






