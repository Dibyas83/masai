
# [[1,2,2,4,6,2,7,8,9,1,2,6]] longest consecutive number array that can be created
# 6,7,8,9

# we can check if the no found has its pree no in list if not it itself becomes the 1st no of seq,search if its next no present if not then pop it
# if next no present add lastly find their length ,if any seq again formed has greater length pop prev or pop curr small seq

class Solut:
    def longest_consi_seq(self,nums: list[int]) -> int:
        numsset = set(nums)
        end = 0
        start = 0
        longest = 0
        for n in nums:
            if n-1 not in numsset:
                leng = 0
                while (n+ leng) in numsset:
                    leng += 1
                longest = max(longest ,leng)
                start = n
                end = n + leng
        return longest, start, end

o = [1,2,2,4,6,2,7,8,9,1,2,6]
u = Solut()
print(u.longest_consi_seq(o))





