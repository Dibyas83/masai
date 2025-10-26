#  using type annotations to create constants
from typing import Final
from  datetime import  datetime

def show_date() -> None:  # returns none
    print('this is the curr date: ')
    print(datetime.now())

show_date()  # by just changing func def the print will change
show_date()
def greet(name: str ) -> None:
    print(f"Hello,{name}")

greet('bob')

def add(a: float,b:float) -> float:
    return a + b

VERSION_No: Final[str] = '1.0.12' # making version as constant
PI: Final[float] = 3.14

number: int=66
names: list = ["h","gh","fghgf","fgfjh"]
data: dict = {"jk": 55,"name":"gh"}
active: bool = False
unique: set = {4,5,7,8}










