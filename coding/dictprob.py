
e =[[2,3,4,5],[4,4,5,6],[4,5,63,3]]
e[0].extend([3,4,5,6])
e[1].reverse()
print(e)
M =2
N = 3
sum= 0
matrix = [[1,2],[3,4],[5,6]]
for i in range(N):
    for j in range(M):
        sum += matrix[i][j]
print(sum)


s1 = "tawetetwetwtwet"
s2 = lambda func:func.upper()
print(s2(s1))

def highest_freq(string):
    N = len(string)
    dicto = {}
    for i in string:
        if i in dicto:
            dicto[i] += 1
        else:
            dicto[i] = 1
    val = max(dicto.values())
    for key in dicto:

        if dicto[key] == val:
            print(key)


string = input()
N=len(string)
highest_freq(string)



 # initializing dictionary
test_dict = {'Gfg': 2, 'for': 1, 'CS': 2}


# printing original dictionary
print("The original dictionary is: " + str(test_dict))

# using filter() to find keys with maximum value
max_val = max(test_dict.values())
res = list(filter(lambda x: test_dict[x] == max_val, test_dict))

# printing result
print("Keys with maximum values are: " + str(res))
# This code is contributed by Vinay Pinjala.

arrA =set(list(map(str,input().split(" "))))
arrB =set(list[input().split(" ")])
print(arrA|arrB)