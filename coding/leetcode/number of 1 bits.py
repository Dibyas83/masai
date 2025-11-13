

# count the number of bits in binary representation. 8 = 1000
# by shifting right and % 2. 1%2 = 1 ,0 % 2= 0

class Solut:
    def noofbit(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1 # right shift
        return res

# time complexity is O(32)

# n= n & n-1
    def maxandbit(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1

        return res



