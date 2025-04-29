class Sol:
    def noof(self, arr: list[int]) -> int:

        cursum = 0
        oddcnt = 0
        evencnt = 0
        res = 0
        MOD = 10 ** 9 + 7
        for no in arr:
            cursum += no
            if cursum % 2:
                res = (res + 1 + evencnt) % MOD
                oddcnt += 1
            else:
                res = (res + oddcnt) % MOD
                evencnt += 1
        return res

h = Sol()
n = int(input())
ar = list(map(int, input().split(" ")))
l = len(ar)
r = []*l
for i in range(l):
    r[i] = float(ar[i])
print(h.noof(r))

"""


def inpt():
    n = int(input())
    ar = list(map(int, input().split(" ")))
    print(noof(ar)

inpt()

class Sol:
    def noof(self, arr: list[int]) -> int:

        cursum = 0
        oddcnt = 0
        evencnt = 1
        res = 0
        MOD = 10**9 + 7
        for no in arr:
            cursum += no
            if cursum % 2 != 0:
                res = (res  + evencnt) % MOD
                oddcnt += 1
            else:
                res = (res + oddcnt) % MOD
                evencnt += 1
        return res

"""






