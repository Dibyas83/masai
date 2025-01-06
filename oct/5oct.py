"""
decimal n0 = 0-9 digits base 10 ,(10,100,1000)
binary = 0,1 (2bits)10,11,100,101,110,111 - binary no base 2(2,4,8,16)
1 + 1 = 10 (binary sum)
XOR - 0  1 = 1
    1  0  = 1
    1  1 = 0
    0  0 = 0

comp stores value 5 in mem addresses like 0101 in 4 bit memory
memory address could have program in 0 & 1 and data in address(mysum=1+1)
(1+1)=10
1 1 - (2 to pow 2) - 1
 +

  =100(2 to pow 2 )

mysum1(stores adress location 0f 11,can be thought of as itself adress) of 7+4
mysum2 =4+9
sum (calls both address) = mysum1 + mysum2

getsizeof(0)=24bytes(integer object o/h)
getsizeof(1)=28bytes(24byte stores is object overhead to work on int- object is collection of function and method
getsizeof(1)=28bytes
a=1234 getsizeof(a)=28bytes ,a is int
a="and" getsizeof(a)=52bytes ,a is str
getsizeof(1233435)=28bytes max 1073741823
getsizeof(1073741824)=32 bytes(long int)
getsizeof("")=49 bytes(char)
getsizeof("c")=50 bytes(char)
getsizeof("cd")=51 bytes(char)

primitive int,float,bool,str

str(12.231) gives "12.231"
int("23.1") gives 23.1

"""

a = " i want icecream "
a = a.replace("want","am") # replace is method, depends on object
# a = a.replace("am",2) # replace() argument 2 must be str, not int
print(a)
print(len(a)) # len is function , it is not dependent on object

# control structures if else while,for
print(bool(-3))
print(bool())
print(bool(""))
print(int(float("23.1")))

# True = 1
print(True << 1) # from 01 to 10
print(True << 3) # from 01 to 1000 shift by 3 places

print(3 & 5)
print(3 & 4)
print(3 & 0)
print(3 & -1) # 11 & 1_

print(3 & -2) # 11 & 10
print(4 & -1) # 100 & 1
print(5 & -1) # 101 & 1
print(9 & -3) # 1001 & 11
print(9 & -2) # 1001 & 10
print(9 & 2) # 1001 & 0010
print(3 & -2)  # 11 & 10 = 2
print(1 & -1)
print(bin(4))
print(bin(-1))
print(bin(1))
print(10/3) # float
print(10//3) # floor div
print(10%3) # modulus
saving = 500
depo = -20
int = 5
print((saving+depo) + (saving+depo)*.05)

















