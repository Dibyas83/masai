
# ROB no two adjcacent houses and maximize loot, given loot amt of each house -
# using dp
#1,2,2,4,6,2,7,8,9,1,2,6
#a = 0,2  if 3 >(3-2) + (1-0) use b
#b = 1,3
# increment all by 4 places
#---------------------------------------------
#find the max if the 2nd largest is not consecutive add it also

# rob = max((arr[0] + arr[2:n]), rob[1:n])

class Sole:
    def rob(self,nums: list[int]) -> int:
        rob1, rob2 = 0, 0  # need two var tp maintain the last two maxes we could rob from

        for n in nums: # iterate through all houses and  compute the max upto the current index
            temp = max(n + rob1, rob2)
            rob1 = rob2  # move fwd
            rob2 = temp # or n the max of current range
        return rob2 # rob2 will be the max at end






