





def merge_sort(arr1,arr2):
    index1 = 0
    index2 = 0
    merged_arr = []

    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] <arr2[index2]:
            merged_arr.append(arr1[index1])
            index1 += 1
        else:
            merged_arr.append(arr2[index2])
            index2 += 1

    while index1 < len(arr1): # if it has not inceremented full as there still elein arr
        merged_arr.append(arr1[index1])
        index1 += 1

    while index2 < len(arr2): # if it has not inceremented full as there still elein arr
        merged_arr.append(arr2[index2])
        index2 += 1

    return merged_arr
a=[1,5,7]
b = [2,6,9,10]
print(merge_sort(a,b))























