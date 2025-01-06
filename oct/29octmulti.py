test = [22,33,44,55,34]
test2 = [66,55,88,33,22]
list3 = list((list((test)),list((test2)),list('papaya')))
list4 =list((list((22,33,44,55,34)),list((66,55,88,33,22))))
list3[1][0] = "new"
list3.insert(1,"t")
#list3.insert([0][1],"t")
list3.append("apple")
#list3.remove(22)
print(list3)
print(list4)
print(list4[0])
print(list4[0:2][1])
print(list3[2][1])
print(list4[0][-1])
print(len(list3))
print(len(list4))
print(len(test2))


def my_function(food):
    for y in food:
        print(y)
fruits = ['ui','gh','kkl','hj']
my_function(fruits)


def my_function2():
    pass


my_function2()



x = lambda a,b : a*10 + b
print(x(4,6))





















