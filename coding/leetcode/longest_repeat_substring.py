
# you have string s and can change chars to anyother upper char k times. we need no of repeating chars
# we have to dhoose which char to be replaced to, if in a window if there is max A we change other k no of char to A
# if in one win there are are 4 A and k=2 we can have win as 6  if in anather win ther is 5 A win becomes 7
# using max valid window from start and count map
# res is updated with max frequency


class Solut:
    def length_repeat_sub(self, s: str, k: int) -> int:
        count = {}
        l = 0  # left pointer
        res = 0
        maxfreq = 0
        for r in range(len(s)):  # right pointer
            count[s[r]] = 1 + count.get(s[r], 0)  # 1 added to previous count of the char
            maxfreq = max(maxfreq, count[s[r]])

            while (r-l +1) - maxfreq > k:  # checking no of replacement, max(count.values()) gives maxfreq of a char
                count[s[l]] -= 1 # decrementin count of char at l in map
                l += 1

            res = max(res,r-l +1)
        return res







