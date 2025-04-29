
"""
if __name__ == "__main__":
    n = int(input())
    arr = list(map(str,input().split(" ")))  # Extract the hour part and convert to integer
    for i in range(len(arr)):

        time_str = arr[i]
        hours, minutes = map(int, time_str.split(":"))
        arr[i] = hours + minutes / 60.0
    dep = list(map(str, input().split(" ")))
    for i in range(len(dep)):
        time_str = dep[i]
        hours, minutes = map(int,time_str.split(":"))
        dep[i] = hours + minutes / 60.0

    # arr = [900, 940, 950, 1100, 1500, 1800]
    # dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(minPlatform(arr, dep))

----------------------------------
if __name__ == "__main__":
    n = int(input())

    arr1 = map(int, input().split(" "))
    arr = list(arr1)
    dep1 = map(int, input().split(" "))
    dep =list(dep1)
    # arr = [900, 940, 950, 1100, 1500, 1800]
    # dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(minPlatform(arr, dep))

--------------------
if __name__ == "__main__":
    n,m = map(int, input().split(" "))
    mat = []
    # taking 2x2 matrix from the user
    for i in range(n):
        # taking row input from the user
        row = list(map(str, input().split(" ")))
        # appending the 'row' to the 'matrix'
        mat.append(row)
    word = input()
    print("YES" if isWordExist(mat, word) else "NO")

---------------------

matrix = []
# taking 2x2 matrix from the user
for i in range(2):
   # taking row input from the user
   row = list(map(int, input().split()))
   # appending the 'row' to the 'matrix'
   matrix.append(row)
----------------

num = input ("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)








"""


















