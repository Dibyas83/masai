
# 4 = 100, rev = 001= 1
# 32 bit 00000100 = 8 , rev = 00100000= 32
# 0&1=0 , 1&1 = 1       0 or 1=1, 0 or 0 = 1
# 00001011 shift left gives 00010110
# 00001011 shift right gives 0000101

# bit  = 00001011
#  00000000 res
#  10000000
# or -------------
#  10000000 res
# bit  = 00000101
#  10000000
#  01000000
# or -------------
#  11000000 res
# bit  = 00000010
#  11000000
#  00000000
# or -------------
#  11000000 res

#  11000000
#  00010000
# or -------------
#  11010000  rev

class Solut:
    def maxbit(self, n: int) -> int:
        res = 0 # all 32 bits are 0

        for i in range(32): # input n=00000010 10000000 11111110 00000101-32bit
            bit = (n >> i) & 1 # moving to right by i make every bit being compared
            res = res | (bit << (31-i)) # that 1 or bit was moved by (31 -0) places to right
        return res



