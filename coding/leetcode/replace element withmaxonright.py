
#[17,18,5,4,6,1] method 1
# new[0] = max(arr[1-5])  have to check from 2nd pos to end
# new[1] = max(arr[2-5])
# new[2] = max(arr[3-5])
# new[3] = max(arr[4-5])
# new[4] = max(arr[5-5])
# new[5] = -1
#method 2
# if we start from end we have to max between the curr(2nd last) and prev(last)
# like this we have to make compare between 2 ele

class Solut:
    def replace_withmax_ofrest(self,nums: list[int]) -> int:
        rightmax = -1
        for i in range(len(nums)-1,-1, -1):
            newmax = max(rightmax,nums[i])
            nums[i] = rightmax
            rightmax = newmax
        return nums









