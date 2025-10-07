
exp = list(map(int,input().split(" ")))
salary = int(input())
if sum(exp)> salary:
    print("debt")

if sum(exp) < salary:
    print("sav")

else:
    print("o bal")






