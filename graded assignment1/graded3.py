def add_to_list(lst=[]):
    lst.append("X")
    return lst

l1 = add_to_list()
l2 = add_to_list()
print(l1, l2)


class MyClass:
    def __init__(self, val):
        self.val = val

obj1 = MyClass(5)
obj2 = MyClass(5)
print(obj1 == obj2, obj1.val == obj2.val)













