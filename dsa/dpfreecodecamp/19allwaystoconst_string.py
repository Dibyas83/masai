
"""
"abcdef",["ab","abc","cd","def","abcd",ef,c]
length of arr is len(arr) + 1

a|b|c|d|e|f| |  - at index info of empty string

if target string is empty it is always true or 1 or[[]] a 2d empty array=(' ',[ cat,xyz])=[[]]  outer is collection
array and inner is empty array  - seeded

if ("birds",[cat,dog]) = []  collection array is empty

               []  0   0   0   0   0   0  only index 0 has one empty combination others have no combination

               a   b   c   d   e   f
ab             ------[ab]
abc            ----------[abc]
abcd           -------------[abcd]
               1   0   1   1   1   0   0
c                      --d[abc][ab,c]
cd                     ----e[abcd][ab,cd]
def                        ----------6[abc,def][ab,c,def]
ef                             ------6[abcd,ef][ab,cd,ef]

               1   0   1   2   2   0   4  - 6th index is true means  substring upto 6 without including index6

count = table[len[m]]   and there is two ways to make abcd
n = len(arr)
tc = n**m (extra n for matching beg char in target to given char in arr ) space n**m
"""
def allconst(target, nums):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target) + 1):
        for num in nums:
            if target[i:i + len(num)] == num: # finds words right starting char
                new_combinations = [sub_array + [num] for sub_array in table[i]]  # adds num(curr) to (old)all sub arrays or combi in table[i]
                table[i + len(num)].extend(new_combinations) # new combs added at the culmination points of those words

    return table[len(target)]

print(allconst("purple", ["purp", "p", "le", "ur", "purpl"]))

print(allconst("abcdef",["ab","abc","cd","def","abcd","ef","c"]))
print(allconst("skateboard",["bo","rd","ate","t","sk","boar"]))
print(allconst("eeeeeeeeeee",["e"]))
# this is a good example of overlapping subproblems













