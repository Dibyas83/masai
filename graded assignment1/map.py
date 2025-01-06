def trnsform_arr(arr1):

    max1 = max(arr1)
    result1 = [-1 if x < max1 else x for x in arr1]
    #print(" ".join(result1))
    print(" ".join(map(str , result1)))

d = [3,4,9,6,7]
trnsform_arr(d)