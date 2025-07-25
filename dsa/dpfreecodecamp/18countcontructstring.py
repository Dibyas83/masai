
"""
"abcdef",["ab","abc","cd","def","abcd"]
length of arr is len(arr) + 1

a|b|c|d|e|f| |  - at index info of empty string

if target string is empty it is always true or 1 =(' ',[ xyz])=1 - seeded
               1  0  0  0  0  0
               a  b  c  d  e  f
ab             ------t
abc            --------t
abcd           -----------t
               1  0  1  1  1  0  0

cd                   ------t
def                     ---------t

               1  0  1  1  2  0  1  - 6th index is true means  substring upto 6 without including index6

count = table[len[m]]   and there is two ways to make abcd
n = len(arr)
tc = m*n**2  (extra n for matching beg char in target to given char in arr ) space m
"""
def countconstruct(m,arr):
    table = [0] * (len(m) + 1)
    table[0] = 1

    for i in range(len(m) + 1):
        for num in arr:
            if m[i:i + len(num)] == num:
                if i + len(num) <= len(m)+1:
                    table[i + len(num)] += table[i]

    return table[len(m)]

print(countconstruct("abcdef",["ab","abc","cd","def","abcd","ef"]))
print(countconstruct("skateboard",["bo","rd","ate","t","sk","boar"]))
print(countconstruct("eeeeeeeeeee",["e"]))
print(countconstruct("purple",["purp","p","le","ur","purpl"]))













