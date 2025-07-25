
"""
can_construct(abcdef,[ab,abc,cd,def,abcd]) true
can_construct(abcdef,[ab,abc,cd,abcd]) false
can_construct("",[ab,abc,cd,def,abcd]) =  true

                            abcdef 1

        cdef(ab)         def(abc) 1       ef(abcd) 0

        ef(cd) 0       ""  1

skateboard[bo,rd,ate,t,ska,e,sk,boar] =false
                            skateboard

        teboard(ska)                        ateboard(sk)

        eboard(t)                           board(board)

         board(e)                               ard(bo)     d(boar)
board can be stored in memo process
"""

def ways(target,wordbank,count):

    if target in wordbank:
        return  1

    for word in wordbank:
        if target[0] == word[0]:
            suffix = target[len(word):]
            no_ofways = ways(suffix,wordbank,count)
            count += no_ofways
    return count

print(ways("abcdef",["ab","abc","cdef","def","cd","ef"],0))
print(ways("abcdef",["ab","abc","cd","de","ef"],0))
# m (height)char in word and n or > m words to compare in  wordbank = n**m.space is m**2
"""
t = "dfgdfgfgdfg"
w = ["dfg","fgfg","fgdfg","her"]
print(t[0])
for e in w:
    print(e[0])
    if t[0] == e[0]:
        print("true")
"""
"""
def canconstruct(target,wordbank):
    suffix=[]
    if target in wordbank:
        return True
    for word in wordbank:
        if target[0] == word[0]:
            suffix.append(target[len(word):])
            for words in suffix:
                if words in suffix:
                    return True
                if words[0] == word[0]:  # if words[len(word):] != "":
                    suffix.append(words[len(word):])
                    print(suffix)
                return True
"""
def mways(target,wordbank,count,memo):
    if target in memo:
        return memo[target]
    if target in wordbank:
        return 1
    for word in wordbank:
        if target[0] == word[0]:
            suffix = target[len(word):]
            no_ofways = mways(suffix, wordbank,count,memo)
            count += no_ofways

    memo[target] = count
    return count
#memo = {} # its storing true or false for other examples, which may return false values
# check in tutor
print(mways("abcdef",["ab","abc","cdef","def","cd","ef"],count=0,memo={}))
print(mways("abcdef",["ab","abc","cd","abcd"],0,memo={}))
# n*m**2











