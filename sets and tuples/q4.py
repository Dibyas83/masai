def if_present(ele,tup1):
    x = [i for i in tup1 if i == ele]
    print("yes" if x else "no")
    if ele in tup1:
        print("yes")
    else:
        print("no")

ele = 7
tup1 = (1,2,4,6,7,9)
if_present(ele,tup1)