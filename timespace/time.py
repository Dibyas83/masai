for i in range(300):
    istr = str(i)
    if len(istr) == 1:
        istr = "00" + istr
    elif len(istr) == 2:
        istr = "0" + istr
    print(istr)

hlst = [22,33,4,6,7,81]
strh = " hello world,by"
print(hlst.index(4))
print(strh.split(" "))



























