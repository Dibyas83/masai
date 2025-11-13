
# array of non neg nos. start from ist index. each nos tells max jump len
# [2,3,1,1,4] can we reach the last index- 2 t0 1, 1 to 1, 1 to 4
# or 2 to 3, 3 to 4
# brute force n^n
# [3, 2, 1, 0, 4] - not possible . index 3 is dead end
"""
from val 3 there are 3 paths                3
 to index                       1(2)       2(1)      3(0)
from val 2 there is 2 path   2(1)  3(0)
from val 1 there is 1 path   3(0)          3(0)
"""
# [3, 2, 1, 0, 4] starting from end , we can tell index 3 and 2 dont have sol which dont need to be calculated again

# greedy
# [2,3,1,1,4] starting from end , we can tell index 3 and 2  reach goal which dont need to be calculated again,move goal left

class Sole:
    def jump(self,nums: list[int]) -> int:
        goal = len(nums) - 1 # index

        for i in range(len(nums) -1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return  True if goal == 0 else False

