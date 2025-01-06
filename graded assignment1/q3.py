for e in range(1,5):
    for r in range(1,5):
        if e == 4:
            print("*",end=" ")
        elif r == 1 or r == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


def test(a=[]):
    a.append(1)
    return a

print(test())
print(test())

list2 =[2,[3,4,[3,[4,5]]],[4,5]]
print(list2[1][0])
print(list2[1][2][1][1])


print("-----------------------")
lis =[4,5,6,4,2,7,6,2]
g = set(lis)
lis = list(g)
print(lis)


s="star wars"
for words in s:
    print(words)
    words[::] = words[-1::-1]








