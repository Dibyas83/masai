

def subset_sum_backtracking(nums,targ):
    result = []
    def back_trak(start,curr_sum,subset):
        if curr_sum == targ: # if target reached
            result.append(list(subset))
            return
        if curr_sum > targ or start >= len(nums): #if sum exceeds target or we are out of nos
            return
        subset.append(nums[start]) # choice 1
        back_trak(start+1,curr_sum + nums[start],subset)

        subset.pop() # remove last choice and choose not to include nums[start]
        back_trak(start + 1, curr_sum, subset)

    back_trak(0,0,[])
    return result

nums = [1,2,3,4,5,6,7,8]
target_val = 10
sol = subset_sum_backtracking(nums,target_val)
print(sol)







