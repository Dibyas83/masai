noOfCases = 2 # input
case1size = 5  # input
Case1str = "1,2,3,4,5"  # input
case1list = Case1str.split(",")
for i in range(int(case1size)):
    case1list[i] = int(case1list[i])+ 1
print(case1list)
for v in case1list:
    print(v,end=" ")

print('--------------------------12')

n = 6
lit = [2,3,4,7,9,5,4]
print(lit)
for i in range(n):
    completeflag = True
    #print(lit[6])
    for ele in lit[i+1:]:  # list are sorted
        if ele > lit[i]:  # lit[i] is cuurent element
            print(ele)
            print(lit[i])
            print("-------------------")
            completeflag = False
            break
    if (completeflag):
        print(lit[i])












