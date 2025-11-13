
# there are n = 5 steps total,we can take 1 or 3 steps at a time
# use decision  tree             0
#                    1                        2    taking 1 or 2 steps
#             2           3              3         4    taking 1 or 2 steps will cover these much steps
#         3     4      4     5        4     5     5    6
#      4   5  5   6   5   6          5   6    excess
#    5  6
# 2 leads to 3,4   3 leads to 4,5 these repeating steps which can be stored in dp
# so there 8 leaves of 5, starting with 1 steps there are 5 ways  ,starting from 2 there are 3 ways
# under 1 there is (2  which gives 3 ways) or (3 which gives 2 ways)

# using bottom up approach , memozition  O(n)-   start from base case or bottom
# it will have 1 way from 5 to 5
# it will have 1 way from 4 to 5
# it will have 2 way from 3 to 5 (1+1)- doesnt take into consideration (3 to 4)4 to 5 which is already considered
# it will have 3 way from 2 to 5 (2+1)  # it has only 2 positions(1 , 2)
# it will have 5 way from 1 to 5 (3+2)
# it will have 8 way from 0 to 5 (5+3)

class Solut:
    def climbstair(self, n: int) -> int:
        one, two = 1, 1 # initialised

        for i in range(n-1):
            temp = one # stores prev val for future sum
            one = one + two # var getting updated(stored)
            two = temp
            print(two)
        return one

h= Solut()
print(h.climbstair(5))





