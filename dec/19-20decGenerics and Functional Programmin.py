import json
data = '{"name":"john","age":45}' # data is a dict but saved in form of string
parsed = json.loads(data)
print(parsed["age"])
"""
json.dump is like saving or write,it will make dict and json.load is like loading or read,it will read or show as dict
json.dump will convert dict to json file
json.load will load a text file into json or one of data structure,only loads string no dict data
"""

print("---------------------1")

with open("sample.txt","w") as f:
    f.write("hello,world!\nwelcome to python.")
with open("sample.txt","r") as f:
    print(f.readline())


#  generic- a way to indicatethe type of data a structure or function can work with
# use pythons typing module to specify types like[int] or dict[str,float]
# generics helps fing type mismatch at compile time rather than run time
# provides better tool support -ex of tools are linter ih;o
#  if same type of data ,pointer moves 1 byte for char and 4 byte for int if same type
#  pointer will know next place easily
from  typing import List
numbers: List[int] = [1,2,3]   # will only use list of integers name of list is numbers
strig: List[str] = ["a","w","1"]   # will only use list of integers name of list is numbers

from  typing import Dict
dic:Dict[str,int]={"s":5,"g":7}
print(dic["s"])
import os
import sys
print(sys.getsizeof(strig))

# generic classes - create classes that can work with any classes
# use typevar to define a placeholder type,then apply it to attributes


from typing import TypeVar,Generic
T = TypeVar('T') # t can be int,str,float,bool ,one is, which is fixed
class Box(Generic[T]):
    def __init__(self,content:T): # content variable of type T
        self.content = content
from  typing import TypeVar,Generic
T = TypeVar('T')
class Box(Generic[T]):
    def __init__(self,content: T):
        self.content = content


b1= Box(10)
b2= Box([2,3,4])
print(b1.content)
print(b2.content)
print(type(b1))

# generic methods-declare a function that accepts or returns a generic type

from typing import TypeVar

T = TypeVar('T') # make it int but float can be added but paralle exection will slow
def get_first(items: list[T]) -> T: # the fuction takes a list of some data
    # type and return 1st item of list of same data type
    return items[0]

# funtional programing - treat functions like data - pass them around and return them

"""
ex in dict  1: x**2 ,2:x**4 
we can have one to many mapping, not many to one

"""
# filter - keep elements that match a condition
# parallel execution
nums =[1,2,3,4,5,6,7,8,11,13,24,35]
evens = list(filter(lambda x: x%2 == 0,nums))
doubled = list(map(lambda  x: x**2,evens))
print(evens)
print(doubled)

# higher order functions map,filter ,reduce

# reduce(function,iterable) reduces the iterable to a single value, it can hold multiple argument

from typing import List,TypeVar,Generic
T = TypeVar('T')
def rverse(items: List[T]) -> List[T]:
    return items[::-1]

num = [1,2,3,4,5]
rec_num = rverse(num)
print(rec_num)

fruits = ['apple','banana','cherry']
rev_fruits = rverse(fruits)
print(rev_fruits)


print("==========================")

from  typing import TypeVar,List
# def generic type variable
T = TypeVar('T')
# func to find the best course in alist


def best_course(courses:List[T]) -> T:  # t is string
    return courses[0] # assumes the first course is the best for simplicity


iitcourse = [ 1,"ai","data science","blockchain"]
mascourse = [True,"full-stack","bachhand"]

print(f"best iit course: {best_course(iitcourse)}")
print(f"best masai course:{best_course(mascourse)}")


from  typing import TypeVar,List
# def generic type variable
T = TypeVar('T')


class Course_manager:
    @staticmethod
    def top_courses(course:List[T]) -> List[T]:
        return course[:3]


# Usage
iitcourses1 = ["ai","block","iot","cubersecurity"]
mascourse1 = [True,"full-stack","backend"]

print(f"best iit course: {best_course(iitcourses1)}")
print(f"best masai course:{best_course(mascourse1)}")



from  typing import Generic,TypeVar,List
# def generic type variable
T = TypeVar('T')


class Course_repositery(Generic[T]):
    def __init__(self):
        self.courses: List[T] = []

    def add_course(self,course: T):
        self.courses.append(course)

    def get_couse(self,index:int) -> T:
        return self.courses[index]

    def listall_courses(self) -> List[T]:
        return self.courses

iit_repo = Course_repositery[str]()
iit_repo.add_course("ai")
iit_repo.add_course("blockchain")
print("iit_repo.",iit_repo.listall_courses())

mas_repo = Course_repositery[dict]()
mas_repo.add_course({"name": "full-stack","duration": 5})
mas_repo.add_course({"name":"data struc","duration": 8})
print("mascourse:", mas_repo.listall_courses())


students = [
    {"name":"alice", "institution":"iit","course":"ai","score":85},
    {"name":"bob", "institution":"mas","course":"full-stack","score":95}
]
from functools import reduce

def filter_stu_by_inst(students,institution):
    return list(filter(lambda s: s["institution"] == institution,students))

def transform_scores(students):
    return  list(map(lambda s: {**s,"score": s["score"] + 5},students))

def calculate_avscore(students):
    scores = list(map(lambda s: s["score"],students))
    return reduce(lambda x,y: x+y,scores) / len(scores)

# Functional pipeine
iit_students = filter_stu_by_inst(students,"iit")
iit_students_with_bonus = transform_scores(iit_students)
ave_score = calculate_avscore(iit_students_with_bonus)

print("filtered iit students:",iit_students)
print("transformed iitstu with bonus score:",iit_students_with_bonus)
print("ave score",ave_score)


from  functools import reduce
scores  = [20,30,44,55,66,77]

#  1 filter out
passing_score = filter(lambda x: x >= 50,scores)

# 2 add bonus to scores
new_score = map(lambda x:x+5,passing_score)

# 3 total score
tot_score = reduce(lambda x,y: x+y,new_score)
print(f"total score = {tot_score} ")
print("total score ",tot_score)


nums = [1,2,3]
evens = list(filter(lambda x: x%2 == 0,nums))
print(evens)





