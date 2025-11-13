
# 0-n has n+1 nos , we picked n distinct no  , find the missing no  between 0-n
# using xor 2^3 = 10 ^ 11 = 01 - if different 1 ,if same 0
# 0^3 = 3, 00 ^ 11=11,   if 0^ 10 = 10
# 5^3^5= 3 , AS 5 CANCELLS
# when [nos] ^ [picked nos] = missing nos
# O(2n)

class Solut:
    def missing(self, nums: list[int]) -> int:  # nums is the list picked, suppose from 0-9 ,8 missing
        res = len(nums) # n=9

        for i in range(len(nums)):
            res += (i-nums[i]) # on 8th index 8-9=-1, 9 + -1 = 8

        return res


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2  # Integer division
        actual_sum = sum(nums)
        return expected_sum - actual_sum


class Solution2:
    def missingNumber(self, nums: list[int]) -> int:
        missing = 0
        n = len(nums)

        # XOR all numbers from 0 to n
        for i in range(n + 1):
            missing ^= i

        # XOR with all numbers in the array
        for num in nums:
            missing ^= num

        return missing

class Solution3:
    def missingNumber(self, nums: list[int]) -> int:
        num_set = set(nums)
        n = len(nums)
        for i in range(n + 1):
            if i not in num_set:
                return i
        return -1 # Should not be reached if a number is always missing