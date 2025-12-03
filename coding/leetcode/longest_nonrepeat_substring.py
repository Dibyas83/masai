
# using shrinking sliding window when duplicates comes if that is in leftmost and set

class Solut:
    def length_nonrepeat_sub(self, s: str) -> int:
        charset = set()
        l = 0  # left pointer
        res = 0

        for r in range(len(s)):  # right pointer
            while s[r] in charset: # and s[l] == s[r]
                charset.remove(s[l])
                l += 1
            charset.add(s[r]) # when not duplicate
            res = max(res,r-l +1)
        return res







