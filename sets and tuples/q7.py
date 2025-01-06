def union(set1,set2,set3):
    new_set = set()
    for ele in set1:
        new_set.add(ele)
    for ele in set2:
        new_set.add(ele)
    for ele in set3:
        new_set.add(ele)

    print(new_set)


set1 = {1,2,3,4,5,6}
set2 = {4,6,7,8,9}
set3 = {6,9,11,12}
union(set1,set2,set3)