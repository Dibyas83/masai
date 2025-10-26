



def encode(strs):
    if len(strs) == 0:
        return chr(258)
    separate = chr(257)
    s = separate.join(strs)
    return s

def decode(s):
    if s == chr(258):
        return []
    separate = chr(257)
    return s.split(separate)

strs = ["ab" , "kl"]

g = encode(strs)
print(g)
print(decode(g))






