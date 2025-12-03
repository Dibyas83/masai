
# min len of substring which has all asked chars
# using window and hashmap
"""
   a | 1         a | 1
   B | 1    >=   B | 1
   C | 1         C | 1

have =0 ,1, 2, 3(increases when abor c is found)    >=   need -3
 get possible res (have all chars) and their len
 then remove from left and from right to find more possibilities and their len
 and also remove from left() otherthan abc) if it does not affect the having
"""

class Solut:
    def allcharin_sub(self, s: str, t: str) -> str:
        if t == "": return ""
        countT, windsize = {}, {}  # the needed element, currentcount


        for c in t:  # right pointer
            countT[c] = 1 + countT.get(c, 0)  # 1 added to previous count of the char,0 if char does not exist

        have, need= 0, len(countT)
        res, reslen = [-1, -1], float("infinity") # l,r pointr -1,-1. len is initialized to inf
        l = 0
        for r in range(len(s)):
            c = s[r]
            windsize[c] = 1 + windsize.get(c, 0)

            if c in countT and windsize[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l+ 1) < reslen:
                    res = [l,r]  # update res
                    reslen = (r - l + 1)
                windsize[s[l]] -= 1  # count of l pointer ele is decreased
                if s[l] in countT  and windsize[s[l]] < countT[s[l]]:
                    have -= 1
                l +=1

        l, r = res
        return s[l:r+1] if reslen != float("infinity") else ""











