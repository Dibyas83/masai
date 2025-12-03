
# amandnama,  pal
# amanddnama,  pal
# considering only alphanumeric chars(no space and symbols) and ignoring cases
# create a string after removing those unwanted chars(space and symbols)

class Solut:
    def ispal(self, s: str) -> bool:
        newstr = ""

        for c in s:
            if c.isalnum():
                newstr += c.lower()
        return  newstr == newstr[::-1]
#--------------------------------
# by using two pointer and sliding window and continous comparison only alphanum chars
class Solu2:
    def ispal2(self, s: str) -> bool:
        l, r =  0 , len(s) - 1

        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while r > l and not self.alphanum(s[l]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True

    def alphanum(self,c):
        return (ord('A') <= ord(c) <= ord('Z')  or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))



