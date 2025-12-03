
# a, aa, aba,azza are pal. even or odd length sub
# using pointer and window
# consider every ele as center and check left and right, abccba in this case check if left or right is
# same as center check the next char

#                a b b c   - > consider b  to left is b(b=b) (a sub pal) to right ic c so these three char not  sub
class Solut:
    def noofsubpal(self, s: str) -> int:
        res = 0
        reslen = 0

        for i in range(len(s)):
            l, r = i, i
            res += self.ctpal(s, i, i)
            res += self.ctpal(s, i, i+1)

        return res

    def ctpal(self,s,l,r):
        res = 0
        while l >=0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res


