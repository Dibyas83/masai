
"""
can_construct(abcdef,[ab,abc,cd,def,abcd]) true
can_construct(abcdef,[ab,abc,cd,abcd]) false
can_construct("",[ab,abc,cd,def,abcd]) =  true

                            abcdef

        cdef(ab)         def(abc)        ef(abcd) false

        ef(cd) false       ""  true

skateboard[bo,rd,ate,t,ska,e,sk,boar] =false
                            skateboard

        teboard(ska)                        ateboard(sk)

        eboard(t)                           board(board)

         board(e)                               ard(bo)     d(boar)
board can be stored in memo process
"""

def canconstruct(target,wordbank):

    if target in wordbank:
        return True
    for word in wordbank:
        if target[0] == word[0]:
            suffix = target[len(word):]
            if canconstruct(suffix,wordbank) == True:
                return True

    return False

print(canconstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(canconstruct("abcdef",["ab","abc","cd","de","abcd"]))
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
def mcanconstruct(target,wordbank,memo):
    if target in memo:
        return memo[target]
    if target in wordbank:
        return True
    for word in wordbank:
        if target[0] == word[0]:
            targ = target[len(word):]
            if mcanconstruct(targ,wordbank,memo) == True:
                memo[targ] = True
                return True
    memo[target] = False
    return False
#memo = {} # its storing true or false for other examples, which may return false values

print(mcanconstruct("abcdef",["ab","abc","cd","def","abcd"],memo={}))
print(mcanconstruct("abcdef",["ab","abc","cd","abcd"],memo={}))
# n*m**2











