
# house are in circle ist and last are adjacent
# there are n-1 houses to consider from n houses

class Sole:

    def rob(self,nums: list[int]) -> int:
        return  max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1])) # helperlists in which 1st and last excluded

    def helper(self, nums):
            rob1, rob2 = 0, 0  # need two var to store the max amt we could rob from previous 2 houses

            for n in nums: # iterate through all houses and  compute the max upto the current index
                temp = max(n + rob1, rob2)
                rob1 = rob2  # move fwd
                rob2 = temp # or n the max of current range
            return rob2 # rob2 will be the max at end









