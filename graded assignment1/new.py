
n=5
for x in range(n):
    even_or_odd = "even" if x%2 == 0 else "odd"
    print(even_or_odd)

list1 = ["a","b","c","d"]
for var in list1:
    print("list1",list1)
    print(list1)

def min(a,b,c):
    min = a if (a < b & a < c) else (b if b < c else c)




n = 20
for i in range(n):
    l = chr(97 + i)
    print(f"{l} == {i+1}")