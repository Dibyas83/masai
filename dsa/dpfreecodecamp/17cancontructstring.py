
"""
"abcdef",["ab","abc","cd","def","abcd"]
length of arr is len(arr) + 1

a|b|c|d|e|f| |  - at index info of empty string

if target string is empty it is always true  - seeded
               t  f  f  f  f  f  f
               a  b  c  d  e  f
ab             ------t
abc            --------t
abcd           -----------t
               t  f  t  t  t  f  f

cd                   ------t
def                     ---------t

                t  f  t  t  t  f  t  - 6th index is true means  substring upto 6 without including index6
n = len(arr)
tc = m*n*(n for matching beg char in target to given char in arr ) space m
"""
def canconstruct(m,arr):
    table = [False] * (len(m) + 1)
    table[0] = True

    for i in range(len(m) + 1):
        if table[i] == True:
            for num in arr:
                if m[i:i + len(num)] == num:
                    if i + len(num) <= len(m)+1:
                        table[i + len(num)] = True

    return table[len(m)]

print(canconstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(canconstruct("skateboard",["bo","rd","ate","t","sk","boar"]))
print(canconstruct("eeeeeeeeeee",["e"]))













