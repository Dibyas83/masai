def set_opr(set1,set2):
    unio = set1.union(set2)
    intersec = set1 & set2
    print(unio)
    print(intersec)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set_opr(set1,set2)