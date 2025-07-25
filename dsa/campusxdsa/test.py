def inplace_rec_mergesort(arr8,arr9):
    o = p =  0
    k=0
    newarr = [0] * (len(arr8) + len(arr9))
    while o < len(arr8) and p < len(arr9):

        if arr8[o] < arr9[p]:
            newarr[k] = arr8[o]
            o += 1  # but j remains same 0 ,which will be checked in next iteration
            k+=1
        else:
            newarr[k] = arr9[p]
            p += 1  # but i remains same
            k +=1
    while o < len(arr8):
        newarr[k] = arr8[o]
        o += 1
        k+=1
    while p < len(arr9):
        newarr[k] = arr9[p]
        p += 1
        k+=1
    print(k,"k")
    return newarr

d = [2, 4, 6, 7, 11, 22, 44, 82, 223]
b =[1, 2, 4, 7, 8, 20, 20, 23]

print(inplace_rec_mergesort(d,b))
# nlogn ,space comp is n
#it is not adaptive it will always divide
# it is stable





