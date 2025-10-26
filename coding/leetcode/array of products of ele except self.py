
"""
using prefix(prod of ele before ele ) and postfix(prod of ele after ele)
time complexity is 3n
nums = [1,2,3,4,5]
pre = [1, 1, 2*1, 3*2, 4*6] from beg to end
post = [120, 3*4*5, 4*5, 5, 1]
ans = [1*2*60, 1*3*20,2*4*5, 6*5, 24*1] from end to begining
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        print(result)

        preFix = 1
        for i in range(len(nums)):
            result[i] = preFix
            preFix *= nums[i]
            # res [1,1,2,6]

        postFix = 1
        for i in range(len(nums) - 1, -1, -1):
            print("result[i]",result[i])
            result[i] *= postFix
            postFix *= nums[i]
            print(nums[i])# p1*6, p4 * 2, p(4*3)*1, p(12*2)*1

        return result

list =[1,2,3,4]
f = Solution()
u = f.productExceptSelf(list)
print(u)









