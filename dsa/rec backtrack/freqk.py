
def freq(arr):
    if not arr:
        return {}
    elif len(arr) == 1:# base case
        return {arr[0]:1} # single key value pair
    else:
        mid = len(arr) //2
        left = freq(arr[:mid]) # divided into single key value pair
        right = freq(arr[mid:])
        combined = left.copy() # copy created for original not changed
        print(combined,"left")
        print(right,"right")
        for key in right:
            if key in combined:
                combined[key] += right[key] # summation
                print(combined,"found")
            else:
                combined[key] = right[key] # added new key
                print(combined,"not found")
            print("-----------loop")
            print(left,"left loop")
            print(right,"right loop")
        print(combined,"out")
        return combined
n = int(input())
arr = list(map(int,input().split(" ")))
k = int(input())
frequenc =freq(arr)
if any(count >= k for count in frequenc.values()):
    print("True")
else:
    print("False")












