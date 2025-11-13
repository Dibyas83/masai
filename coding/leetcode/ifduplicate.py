
def ifdupli(lista):
    se = set() # hash set
    l = len(lista)
    for i in range(l):
        if lista[i] in se:
            return "dupli"
            break
        else:
            se.add(lista[i])
    return "no dup"


lista = [1,2,3,4,5,6,2]
print(ifdupli(lista))

# by sorting nlogn , then comparing to next


