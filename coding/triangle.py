

"""a = 5
b = 6
c = 3

if a ** 2 == (b ** 2) + (c ** 2):
    print("yes")
elif b ** 2 == c ** 2 + a ** 2:
    print("yes")

elif c ** 2 == a ** 2 + b ** 2:
    print("yes")
else:
    print("no")

find max then use pythagoras
"""




def tri(list1):

    max1 = 0
    if list1[0] > list1[1]:
        max1 = list1[0]
    elif list1[1]>list1[0]:
        max1 = list1[1]
    if  list1[2] > max1:
        max1 = list1[2]

    print(max1)
    list1.remove(max1)
    if max1 ** 2 == (list1[0] ** 2) + (list1[1] ** 2):
        print("yes")
    else:
        print("no")

list1 = list(map(int,input().split(" ")))
print(tri(list1))



















