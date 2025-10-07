
def sortonnames(names,scores):
    n =len(names)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if names[j] > names[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]
                scores[j], scores[j + 1] = scores[j + 1],scores[j]


def sortonscores(names,scores):
    n =len(names)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if scores[j] < scores[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]
                scores[j], scores[j + 1] = scores[j + 1],scores[j]

def lesder(names,scores):
    n = len(names)
    rank = 1
    for i in range(n):
        print(rank,names[i])
        if i!= n-1 and scores[i] > scores[i+1]:
            rank = i + 2

def solve(names,scores):
    sortonnames(names,scores)
    sortonscores(names,scores)
    lesder(names,scores)

def inp():
    n = int(input())
    names = []
    scores = []
    for i in range(n):
        name,score = input().split(" ")
        names.append(name)
        scores.append(int(score))
    solve(names,scores)

inp()

"""
5
a 2
c 6
d 5
r 8
e 4
1 a
1 c
3 d
3 r
5 e
"""





