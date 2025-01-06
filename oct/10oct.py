
# 0,1,10,11,100,101,111,1000,1001,1010,1011,1100,1101,1110,1111

print(1^0)
print(1^1)
# 123=3*1 + 2*10 + 1*100
# 1111111 = 2**7 - 1
# ist no  2*0 = 1
# 11 + 1 = 100 in bin
# add = 11 sub = 01 in memory
# var are memory loc names where value is stored

import sys
print(sys.getsizeof(0)) # overhead or function 24byte + 4 bytes
print(sys.getsizeof(1))
print(sys.getsizeof(9999999))
print(sys.getsizeof(1000))
print(sys.getsizeof("a"))
print(sys.getsizeof("and")) # 41 +3
print(sys.getsizeof('f'))
print("===================")
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print(sys.getsizeof(10.2))
print(sys.getsizeof(1234567890))
a = "i want cake"
a = a.replace("cake","aw")
print("--------------")
print(a)
print(a + " 4")












# variables are proxy to address in memory
u=bool(10)
r=bool(1)
w=bool("")
t= True
y=False
print(t,w,y,r,u)
print("--------------------------")
print(True << 1)# left sift
print(5 << 1)
print(5 >> 1)
print(False << 1)
print(True >> 1)
print(3 & 5)
print(3 | 5)
print(bin(3))
print(bin(5))
#1&1=1,1&0=0
print(4/2)

sav = 100
for years in range(1,6):
    itt = 5
    sav = sav + sav * 5/100
print(sav)

age = 25
print("your age is " + str(age) + " years old")
print("your age is " + "25" + " years old")
print(len(" er rty_"))

