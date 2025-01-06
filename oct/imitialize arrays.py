# initializes a 4 by 3 array matrix all with 0's
c =  [[0] * 4] * 3
print("Intitialising 2D empty list of zeros: ", c)

# empty list which is not null, it's just empty.
d = []
print("Intitialising empty list of zeros: ", d)

# initialize the spaces with 0’s with
# the help of list comprehensions
a = [0 for x in range(10)]
print(a)

b = [[0] * 4 for i in range(3)]
print(b)
b = []
for x in range(5):
    b.append([[]])

print(b)

c = []
for x in range(5):
    c.append(0)

print(c)

def initialize_twodlist(foo):
    twod_list = []
    new = []
    for i in range (0, 10):
        for j in range (0, 10):
            new.append(foo)
        twod_list.append(new)
        new = []













