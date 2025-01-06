def difference(set1,set2,set3):
    new_set = []
    for ele in set1:
        if ele not in set3 and ele not in set2:
            new_set.append(ele)
    print(set(new_set))


set1 = {1,2,3,4,5,6}
set2 = {4,6,7,8,9}
set3 = {6,9,11,12}
difference(set1,set2,set3)