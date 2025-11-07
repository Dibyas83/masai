
# if num be 18 1+64 = 65,65 36+25=61,61 36 + 1 = 37,37 9 + 49 =58,58 25+ 64 = 89,89 64 + 81=145
#19 1+ 81 = 82, 82 64 +4=68,68 36 + 64 = 100,1 will loop infinitly happy no
# or if it sums to a previous no it has summed to before it will be in a loop not reach 1 so unhappy
# use hash set to keep track of prev no visited

class Solution:
    def ishappy(self, n: int) -> bool:
        visit = set() # hash set
        while n not in visit:
            visit.add(n)
            n = self.sumofsquares(n)

            if n==1:
                return True
        return False # if n in visit

    def sumofsquares(self,n: int) -> int:
        output = 0 # 19 % 10 = 9, 19 / 10 = 1,1%10=0 or1/10=0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10  # 1 goes up
        return output
"""
            w = 19

            print(w // 10)
            print(1 % 10)
            print(1 // 10)
"""


# solve using linked list cycle




