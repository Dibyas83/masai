
# encode a list of strings to a string .delimiter one word ends and anther word begins

# ["neet","bolp"] -> neet#bolp
# ["neet","bo#lp"] -> neet#bo#lp
# store the length of word,then delimeter - so we read that len after delimeter as word -4#neet5#co#de

class Solute:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, str):
        res, i = [], 0 # i is pos of char

        while i < len(str):
            j = i
            while str[j] != "#":  # if len=245
                j += 1
            length = int(str[i:j])  # 0-3
            res.append(str[j+1:j+1+length])  # j+1 is pos of #
            i = j+1+length
        return res


class Soll:
    def encode(self,strs):
        if len(strs) == 0:
            return chr(258)
        separate = chr(257)
        s = separate.join(strs)
        return s

    def decode(self,s):
        if s == chr(258):
            return []
        separate = chr(257)
        return s.split(separate)

strs = ["ab" , "kl"]

g = Soll()
print(g.encode(strs))
print(g.decode(g.encode(strs)))




