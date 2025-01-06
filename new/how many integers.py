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
print(count2[-1])

print("----------------------------======================")

inplist1 = "abcdefgijkabc"
newval2 = ""
newval3 = ""
count1 = []
for val in inplist1:
    if val not in newval2:
        newval2 +=val
        count1.append(1)
        print(" not in list",newval2,count1)

    else:
        #newval3.append(val)
        newval3 += val
        count1.append(1)
        # print("in list", newval2, count1)
        count1[-1] += 1
        print(" in list",val)
print(newval3,newval2,count1)
print()
print(count2[-1])















