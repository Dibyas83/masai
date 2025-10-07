bal = 4900
x = True
while(x):
    if bal <=5000:
        bal = bal + 500
    else:
        print("you have 5400")
        x=False
print(x)
print(bal)


a = 10
for i in range(1,6):
    if(a%2 == 0):
        a=a+2
    else:
        a=a+1
print(a)# a + 2 5 times 1-5

name1="dgdf_dgd"
name ="erter_rter "
full_name=f"{name} {name1}"
print(full_name)
print(name.title())


for i in range(4):
    for j in range(5):

        print(f"i:{i} , j:{j}")
        print(f"hello,{i,j}")

zen= '''iit mandi'''
for char in zen:
    print(char)
    if char not in 'aeiou':
        print(char)


for no in range(10,0,-3):
    print(no,end='')




