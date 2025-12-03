

# amandnama,  pal
# amanddnama,  pal
# babad   - bab or aba sub are pall, find the longest sub in a string
# using pointer and window
# consider every ele as center and check left and right, abccba in this case check if left or right is
# same as center check the next char
class Solut:
    def subpal(self, s: str) -> str:
        res = ""
        reslen = 0

        for i in range(len(s)):
            # for odd len
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > reslen: # checking if longest
                    res = s[l:r+1]
                    reslen = r-l + 1
                l -= 1
                r += 1
            # for even len
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > reslen:
                    res = s[l:r + 1]
                    reslen = r - l + 1
                l -= 1
                r += 1




