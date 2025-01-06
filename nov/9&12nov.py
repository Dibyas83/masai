a=10
def foo():
    global a
    a += 1
    print(a)


print(foo())
print(1<2<3) # left to right
print(1<(2<3)) # 2<3 =1 or true
print((1<2)<3) # 1<2 =true or 0
fruit= ['app','rt','ty','edf','tyhg','dcv','fffef','ffef','fffs']
print(fruit[1:3])
print("================")
print(fruit[:3])
print(fruit[::-1])
print(fruit[::2]) # 3 is step
print(fruit[1::3]) # 3 is step
print(fruit[1:5:2]) # 3 is step
fruits =('ed','rt','gh') # tuplr do slicind,no changing
frits ={'ed','rt','gh'} # set  no slicing,no duplicate,does add not append
#check extend
t= (4,6,8)
print(t.index(4))
print(id(t))
t=t+(3,)
print(id(t)) # in tuple adres changes
print(id(frits))
fruit.insert(1,"hj")
print(fruit)
fruit.extend("6")
print(fruit)
even_sq = [x**2 for x in range(1,20) if x%2 == 0]  # comprehension is only for list not tuple
print(even_sq)
t1=[1,2,3,6,1,3]
t1.insert(1,3)
print(t1)
t1.pop(3)
print(t1)

l = sorted(t1)# is fundtion
#sort is method
print(l)
t1.sort()
print(t1)
h = "tyu,sad"
print(h.strip("tyu"))
print("------------------------------------q")
# list comprehension only for list[] not () or {}
squares =[x**2 for  x in range(1,11) if x%2 == 0]
print(squares)
# is equal to
a = []
for x in range(4):
    a.append(x**2)
print(a)

print("-------==========================-----------")

pl = [1,3,"jk",5,6,3,5,8,"df"]
pk = [1,3,"jk",5,6,3,5,8,"df"]
pj = [1,3,"jk",5,6,3,5,8,"df"]
po = [1,3,5,6,3,5,8]
pl = pl[::-1]
pj = pj[-1::-2]
e1=[1,3,4,2]
l2 = sorted(e1) # sorted is a function not method
pk = pk[-1::-1]
po = po[::-1]
po.sort()
print(pl)
print(pj)
print(pk)
print(po)
text ="hello World"
text5 ="helloWorld"
print(text.isalpha())
print(text5.isalpha())
num1 = "12345"
num2 = "12345.0"
num3 = " 12345.0"
print(num1.isdigit())
print(num2.isdigit())
print(num3.isdigit())
te = (text.find("h"),text.find("d"))
print(text.find("oll"))
print(text.find("ol"))
print(text.find("dl"))
print(text[0:5])
print(text[6:])
print(text[::-1])
print(text.find("o"))
print(text.split(" "))
print(text.split())
print(text[::-1])


x = 2
y = 3
t = x
x = y
y = t
print(x,y)
# x=x+y y=x-y x=x-y

print("algo--------------------------------")
# swap
x = 2
y = 3
t=x
x=y
y=t
print(x,y)






animals =["goat",34,"red",22]
v = 22
op = -1 # if ele not present
for ele in range(len(animals)):
    if animals[ele] == v:
        op = ele
        break
print(op)

qr = [22,45,56,64]
for i,v in enumerate(qr):
    print(i,v)


def linear_search(list_sorted,target):
    list_sorted = [1, 4, 6, 9, 10] # sorted
    target = 6
    for i,v in enumerate(list_sorted):
        if v == target:
            return  i
    return -1


h = [22,33,55,77,88]
print(linear_search(h,55))


def binary_search(lst,target2):
    target2 = 8
    lst = [2, 4,5, 6, 8, 11, 16, 22, 25, 31]
    low  , high = 0  , len(lst) - 1
    while low <= high:
        mid = (low + high)//2
        if lst[mid] == target2:
            return mid

        elif lst[mid] < target2:
            low = mid + 1
        else:
            high = mid - 1

    return - 1 # if not found after processes


nums_s = [1,2,3,4,5,6,8]
print(binary_search(nums_s ,5))

print("7=================================")
l =[12,2,45,4,67]
n = len(l)
for i in range(n):
    for j in range(0,n-i-1):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
    print(l)

for i in range(1000):
    istr = str(i)
    if len(istr) == 1:
        istr = "00" + istr
    elif len(istr) == 2:
        istr = "0" + istr
    print(istr)

# append(item) adds one,extend(iterable) adds anather list or iterable,insert(index,item)
# remove(item),pop(index),clear
# index(item,start,end),count(item),sort(reverse=true)for descending
# reverse()
# copy() newlist = list.copy() shallow copy(same address if modified copy changes) deep copy(anather address)
# strip(removes space or char)
# replace(old,new),split('," ",/tb),join(iterable like list)
# ex - ",".join(["aa","bb","hh"])
# find(substring)  - mystr.find("hello")
# count(substring)  - mystr.count("hello")

# startswith(prefix) and endswith(suffix) ex - mystr.startswith("hello")
# isalpha,isdigit,isstring



# linear_search()  - key-30 search in hlst if key is hlst[0]...if list not sorted
# time complexity o(1) time not dependent on input,o(n) time dependent on input
# binary_search() if data is big list is sorted first ,
# find mid if smaller search in right if bigger serch in left, dependent on o(logn)

# sorting algorithms- bubble sort ,selection sort,insertion sort,merge sort for all time complexity is o(n**2)





















