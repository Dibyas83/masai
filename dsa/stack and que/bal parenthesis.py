
def balanced(strin):
    stak = []
    pairs = {")": "(","}": "{","]": "["}
    for char in strin:
        if char in pairs.values():
            stak.append(char)
        elif char in pairs.keys():
            if not stak or stak.pop() != pairs[char]: # pairs[")"] = "(",stak.pop="("
                return False
    return not stak # if not having element

strin = "({{[]}})("
print(balanced(strin))









