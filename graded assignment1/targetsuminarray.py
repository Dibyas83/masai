target_sum = 12
arr1 =[1,2,3,4,5,6,7,8,6,9]
arr2 =[1,2,3,4,5,6,7,8,6,9]
N = len(arr1)

for i in range(N):
    tar = target_sum - arr2[i]
    for j in range(N):
        if tar == arr2[j] and j>i:

            print(arr2[i],arr2[j])