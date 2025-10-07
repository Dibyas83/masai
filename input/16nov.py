user_name = ["abc","def"]
#password = [123,456]
password = [123,"456"]
user = "def"
print(user_name.index(user))

if password[user_name.index(user)] == input("password",):
    print("logged")
else:print("incorrect")


def find_larges_value(inputlist):

    maxval = -100000
    for vale in inputlist:
        if maxval<vale:
            maxval=vale
    return maxval


input_list = [22,3,4,55,34,21,7,88,32]
print(find_larges_value(input_list))


def find2ndlargestvalue(inputlist,maxval):
    smaxval = -100000
    for vale in inputlist:
        if smaxval<vale and (vale != maxval):
            smaxval = vale
    return smaxval


# for each element in input do following
ip_list = [1, 12, 3,9, 2,8,9,4, 56]
print(find2ndlargestvalue(input_list,88))


def find_count(iplist):
    cout = 0
    for i in range(1, len(iplist)-1):
        if (iplist[i] >= iplist[i-1] ) and (iplist[i] >= iplist[i+1]):
            cout += 1
    return cout


print(find_count(ip_list),end="")
print("-------------------------------4444444444444444444")
inputlist = [1,2,4,2,5,4,1]

inputlist.sort()
outputlist = []
values = []
count = []
for val in inputlist:
    if val not in values:
        values.append(val)
        count.append(1)
        print(values,count)

    else:
        count[-1] += 1
        print("in else",val)
    print(values,count)
print()

print("----------------------------------==================121")
inplist = [1,2,8,4,2,5,4,1]
inplist.sort()
newval = []
count2 = []
for val in inplist:
    if val not in newval:
        newval.append(val)
        count2.append(1)
        print("in list",newval,count2)
    else:
        count2[-1] += 1
        print("not in list",val)
    print(newval,count2)
print()
print("------------------------------------------")
default_val = input("def val =")
def display(value = default_val):
    print("val=",value)

default_val = " changed default"

print(display())
print(display("New input"))
print("==================--------------------1122")

input_list11 = [1,2,8,4,5,2,5,4,1]
mydict = {}
for v in input_list11:
    if v not in mydict.keys():
        mydict[v] = 1
    else:
        mydict[v] += 1
print(mydict)


while(1):
    try:
        myint = int(input("enter num =  "))
        print(myint)
        break
    except (KeyError,ValueError): # keyerror wrong index in dictionary or lists
        print("wrong input")

name ,age = input("enter: name and age ").split()
print("name",name,"age",age)
nme ,age1 = input("enter name and age= ").split()
print(nme," ",age1)
# logarithmic O(log n) complexity skips parts of data
# memory inc speed inc
# memory dec speed dec

age = input("hoe old ")
print("ram your age is " + age + "years")
is_student = bool(input("1 or 0"))
age = int(input("enter age "))
height = float(input(" enter height "))
print("age: ",age,"height ",height,"student: ",is_student)
print(int("23"))

try:
    no = int(input("enter no = "))
    print("you entered")
#except (KeyError, ValueError):
except :
    print("not right no")

# calculator

num1 = float(input("enter num1 : "))
op =("+","/","-","=")
operator = input("enter(+,-,=,*,/): ")
num2 = float(input("enter num2: "))
if operator == "+":
    print("result: ",num1 + num2)
elif operator == "-":
    print("result: ",num1 - num2)
elif operator == "*":
    print("result: ",num1 * num2)
elif operator == "/":
    print("result: ",num1 / num2)
elif operator == "=":
    print("result: ",num1 == num2)
elif operator != op:
    print("of in bracket")
else:
    print("invalid operator")


def function_name(parameeters):
    #code block
    return values


def greet(name ="guest"):
    print(f"hello ,{name}!")# becase of f value of name(variable) is printed

greet(name="alicea")
greet()
#print(greet(name="alice"))
#print(greet())






















